<h1 align="center"> ETL orquestado con Apache Airflow en contenedores Docker </h1>

## Índice

- [Resumen del proyecto](#Resumen-del-proyecto)
- [¿Qué es Docker?](#qué-es-docker)
- [¿Qué es Apache Airflow?](#qué-es-apache-airflow)
- [Arquitectura empleada](#Arquitectura-empleada)
- [Conexión desde PostgreSQL a Power BI](#Conexión-desde-PostgreSQL-a-Power-BI)
- [Vista Dashboard en Power BI](#Vista-Dashboard-en-Power-BI)
- [Instalaciones adicionales y ejecución](#Instalaciones-adicionales-y-ejecución)

## Resumen del proyecto
Este proyecto de ETL extrae información desde archivos CSV, ejecuta con Docker-Compose contenedores Docker para: Scheduler y Web Server de Apache Airflow, además de bases de datos en PostgreSQL, con el fin de orquestar y automatizar procesos ETL que inserten información nueva y actualicen registros modificados en base de datos creada, lo cual se ejecuta cada un minuto y se puede monitorear desde el Web Server de Airflow, para finalmente conectarse y visualizar dicha informacion en Power BI.

## ¿Qué es Docker?
Docker es una plataforma que facilita la creación, el despliegue y la ejecución de aplicaciones en contenedores. Un contenedor es una unidad de software que empaqueta el código de una aplicación y todas sus dependencias para que la aplicación pueda ejecutarse de manera consistente en cualquier entorno. Documentación oficial: https://docs.docker.com/

## ¿Qué es Apache Airflow?
Apache Airflow es una herramienta de código abierto para crear, programar y monitorear flujos de trabajo o procesos de datos. Un flujo de trabajo es una serie de tareas que se ejecutan en un orden específico. Documentación oficial: https://airflow.apache.org/docs/

## Arquitectura empleada
El esquema general del modo en que se relacionan las partes del sistema es el siguiente:
<br/><br/>

![etl_airflow_docker](https://github.com/Cris-Neumann/ETL-with-Airflow-and-Docker/assets/99703152/328c1609-6d52-4550-9ff0-75b5ce4c9858)

## Conexión desde PostgreSQL a Power BI
Para la conexión desde PostgreSQL a Power BI, se utiliza una conexión ODBC (Open Database Connectivity) para PostgreSQL: https://acortar.link/O3tS7e.
Y se utiliza el siguiente string conector a Power BI vía ANSIx64:
```
Driver={PostgreSQL ANSI(x64)};Server=SERVIDOR_SELECCIONADO;Port=PUERTO_SELECCIONADO;Database=BASE_DE_DATOS_SELECCIONADA
```

## Vista Dashboard en Power BI
A continuación una vista diseñada en Power BI, alojada en directorio 'views', con los ingresos, gastos y ahorro de clientes.
<br/><br/>

![dashboard](https://github.com/Cris-Neumann/ETL-with-Airflow-and-Docker/assets/99703152/ec4680ba-ab6b-43d6-9ee0-32433ae07d5f)

## Instalaciones adicionales y ejecución
Para ejecutar los contenedores con Docker Compose, debe previamente instalar Docker Engine and Docker CLI:
https://docs.docker.com/engine/install/ubuntu/, y luego instalar Docker Compose: https://docs.docker.com/compose/install/linux/.
Una vez instalados, puede probar los servicios ejecutando los siguientes comandos en la terminal:
```
sudo service docker start
sudo docker --version
```
Luego de verificar que aparezcan las versiones del cliente y del servidor, puede ejecutar los servicios con el siguiente comando:
```
docker-compose up -d
```
