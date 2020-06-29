# Cloud Computing 2

## Máster en Ingeniería Informática 19-20.

### Prácticas

1. Servicio Cloud de almancenamiento con OwnCloud.

Consiste en realizar un despligue de OwnCloud completo utilizando diferentes microservicios encargados de tareas específicas, tales como la administración de las bases de datos, autenticación, balanceado de carga o gestión del almacenamiento. Para ello utilizaremos las siguientes tecnologías:

* Un servicio de almacenamiento en cloud como *OwnCloud*, que convertiremos en un microservicio en contenedores y al cual le añadiremos todos los demás servicios adionales para darle soporte.

* NGINX : trabajará como proxy y balanceador de carga para el microservicio que albergará *OwnCloud*.

* MySQL/MariaDB: microservicio que dotará a *OwnCloud* de acceso y gestión de los datos.

* LDAP: microservicio para conectar la autenticación de *OwnCloud* para los usuarios y el acceso.

La arquitectura debe permitir balancear la carga desde el servicio NGINX hasta los contenedores (al menos 2), de modo que el tráfico se encauce hacía los
contenedores de *OwnCloud*. Los demás microservicios sólo es necesario que tengan una única instancia.

2. Despliegue de un servicio Cloud Native.

Esta práctica consiste en la creación, entrega/despliegue de un servicio Cloud Native completo desde la adquisición del código fuente, acceso a datos hasta la ejecución de contenedores, compuesto por una API de tipo HTTP RESTful que permita entregar un servicio de predicción de temperatura y humedad. Esta API será capaz de obtener la predicción de Humedad y Temperatura para intervalos de 24, 48 y 72 horas. En la primera versión se utilizará *ARIMA* para obtener dichas predicciones mientras que en la segunda versión, en mi caso, he utilizado una API denominada *DarkSky*. 

Para diseñar todo el flujo de trabajo del servicio Cloud Native para predicción, mostramos cuál sería el esquema de operaciones/tareas que debes implementar como un DAG en **AirFlow**.

El código de esta práctica se puede encontrar [aquí](https://github.com/lidiasm/CC2-airflow).

3. Base de datos en Cloud Computing MongoDB y Neo4J 

Utilizando las diferentes órdenes y operaciones de MongoDB, se deben crear las siguientes consultas para la colección, previamente creada, para almacenar el *dataset SacramentoCrimeJanuary2006*.

* Contar el número de delitos/robos.

* Contar el número de delitos por hora.

* Muestra el TOP 5 de los delitos más habituales.

4. Procesamiento y minería de datos en Big Data con Spark sobre plataformas cloud

El objetivo reside en resolver un problema de clasificación aplicado a un conjunto de datos muy voluminoso, que habrá que dividir en entrenamiento y prueba, mediante el uso de diferentes técnicas y algoritmos de aprendizaje automático ubicados en la librería *MLLib*. Para ello habrá que usar hábilmente distintas herramientas de los ecosistemas de **Hadoop y Spark**, desplegadas sobre distintos escenarios. Una vez diseñados e implementados se comparará el rendimiento de los distintos clasificadores para identificar cuál resulta ser el más adecuado para el problema en cuestión realizando un estudio empírico comparativo.

Para el desarrollo de práctica se usará el cluster hadoop.ugr.es, que provee de HDFS y Spark ya preparado y listo para trabajar sobre él, y que proporciona todas las herramientas para el procesamiento. 


### Teoría

* Exposición acerca de la disciplina *Knowledge as a Service* (KaaS).

* Epígrafe elaborado para componer el tema 4 acerca de los *Requisitos específicos para aplicaciones cloud*.


