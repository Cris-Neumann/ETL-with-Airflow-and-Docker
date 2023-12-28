<h1 align="center"> ETL orquestado con Apache Airflow en contenedores Docker </h1>

## Índice

- [Resumen del proyecto](#Resumen-del-proyecto)
- [Arquitectura empleada](#Arquitectura-empleada)
- [Conexión desde PostgreSQL a Power BI](#Conexión-desde-PostgreSQL-a-Power-BI)
- [Vista Dashboard en Power BI](#Vista-Dashboard-en-Power-BI)

## Resumen del proyecto
Este proyecto de ETL extrae información desde archivos CSV, ejecuta con Docker-Compose contenedores Docker para: Scheduler y Web Server de Apache Airflow, además de bases de datos en PostgreSQL, con el fin de orquestar y automatizar procesos ETL que inserten información nueva y actualicen registros modificados en base de datos creada, lo cual se ejecuta cada un minuto y se puede monitorear desde el Web Server de Airflow, para finalmente conectarse y visualizar dicha informacion en Power BI.

## Arquitectura empleada
El esquema general del modo en que se relacionan las partes del sistema es el siguiente:
![etl_airflow_docker](https://github.com/Cris-Neumann/Codigo_abierto/assets/99703152/b3704d19-69b4-4fa5-9b36-19aefb65691c)

## Conexión desde PostgreSQL a Power BI
Para la conexión desde PostgreSQL a Power BI se utiliza una conexión ODBC, utilizando el string conector a Power BI vía ANSIx64: Driver={PostgreSQL ANSI(x64)};Server=SERVIDOR_SELECCIONADO;Port=PUERTO_SELECCIONADO;Database=BASE_DE_DATOS_SELECCIONADA

## Vista Dashboard en Power BI
A continuación una vista diseñada en Power BI, alojada en directorio 'views', con los ingresos, gastos y ahorro de clientes.
<br/><br/>

![dashboard](https://github.com/Cris-Neumann/Codigo_abierto/assets/99703152/c7fc134b-a430-437d-854a-6350267c4245)
