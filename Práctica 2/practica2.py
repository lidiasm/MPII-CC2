from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import requests
import pandas

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2), # Comienza inmediatamente.
    'email': ['lidiasm96@correo.ugr.es'], # Email al que enviar el informe si hay error.
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5), # Cada cuanto se reintenta la ejecución.
}

############################ FUNCIONES DE PYTHON ############################

def get_datos():
    # Leemos los dos ficheros csv
    df_humedad = pandas.read_csv('/tmp/workflow/humidity.csv')
    df_temperatura = pandas.read_csv('/tmp/workflow/temperature.csv')
    # Extraemos la columna de la ciudad de San Francisco de humedad y temperatura
    humedad_sf = df_humedad['San Francisco']
    temperatura_sf = df_temperatura['San Francisco']
    # Obtenemos la columna de las fechas porque es la misma en ambos datasets
    datetime = df_humedad['datetime']
    # Formamos el nuevo dataframe unificado
    d = {'DATE':df_humedad['datetime'], 'TEMP':temperatura_sf, 'HUM':humedad_sf}
    dataframe = pandas.DataFrame(data=d)
    # Escribimos el nuevo dataframe en un fichero csv
    ## Con index=False le decimos que no escriba el número de las filas
    dataframe.to_csv('/tmp/workflow/dataframe.csv', index=False)

############################ FUNCIONES DE PYTHON ############################

# Inicializamos el grafo de tareas.
dag = DAG(
    'practica2',
    default_args=default_args,
    description='Grafo de tareas de la practica 2',
    schedule_interval=timedelta(days=1),
)
# PrepararEntorno es una tarea encargada de crear el direcotorio donde almacenar
# los ficheros de datos que se descargarán a continuación.
PrepararEntorno = BashOperator(
                    task_id='preparar_entorno',
                    depends_on_past=False,
                    bash_command='mkdir -p /tmp/workflow/', # Con la opción "-p" intentará crear el directorio si no existe. Si existe no lanza error.
                    dag=dag
                    )
# CapturaDatosHumedad: se encarga de descargar el fichero de datos que contiene la humedad.
CapturaDatosHumedad = BashOperator(
                        task_id='captura_datos_hum',
                        depends_on_past=False,
                        bash_command='wget --output-document /tmp/workflow/humidity.csv.zip https://raw.githubusercontent.com/manuparra/MaterialCC2020/master/humidity.csv.zip',
                        dag=dag
                        )
# CapturaDatosTemperatura: tarea encargada de descargar el otro fichero de datos con las temperaturas.
CapturaDatosTemperatura = BashOperator(
                            task_id='captura_datos_temp',
                            depends_on_past=False,
                            bash_command='wget --output-document /tmp/workflow/temperature.csv.zip https://raw.githubusercontent.com/manuparra/MaterialCC2020/master/temperature.csv.zip',
                            dag=dag
                            )
# DescomprimirDatos: tarea encargada de descomprimir ambos ficheros.
## Con la opción "-d" especificamos la ruta donde queremos que descomprima los ficheros.
## Con la opción "-o" le indicamos que sobreescriba los ficheros sin preguntar.
DescomprimirDatos = BashOperator(
                        task_id='descomprimir_datos',
                        depends_on_past=False,
                        bash_command='unzip -o /tmp/workflow/temperature.csv.zip -d /tmp/workflow ; unzip -o /tmp/workflow/humidity.csv.zip -d /tmp/workflow',
                        dag=dag
                        )
# UnificarDatos: tarea encargada de extraer la humedad y temperatura de San Francisco así como la hora a la que se ha medido.
UnificarDatos = PythonOperator(
                    task_id='unificar_datos',
                    python_callable=get_datos,
                    op_kwargs={},
                    dag=dag
                    )

## ORDEN DE EJECUCIÓN DE TAREAS
PrepararEntorno >> [CapturaDatosHumedad, CapturaDatosTemperatura] >> DescomprimirDatos >> UnificarDatos