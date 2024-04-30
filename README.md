<h1 align="center"> ETL orquestado con Apache Airflow en contenedores Docker </h1>

## Índice

- [Resumen del proyecto](#Resumen-del-proyecto)
- [Arquitectura empleada](#Arquitectura-empleada)
- [Conexión desde PostgreSQL a Power BI](#Conexión-desde-PostgreSQL-a-Power-BI)
- [Vista Dashboard en Power BI](#Vista-Dashboard-en-Power-BI)
- [Instalaciones adicionales](#Instalaciones-adicionales)

## Resumen del proyecto
Este proyecto de ETL extrae información desde archivos CSV, ejecuta con Docker-Compose contenedores Docker para: Scheduler y Web Server de Apache Airflow, además de bases de datos en PostgreSQL, con el fin de orquestar y automatizar procesos ETL que inserten información nueva y actualicen registros modificados en base de datos creada, lo cual se ejecuta cada un minuto y se puede monitorear desde el Web Server de Airflow, para finalmente conectarse y visualizar dicha informacion en Power BI.

## Arquitectura empleada
El esquema general del modo en que se relacionan las partes del sistema es el siguiente:
<br/><br/>

![etl_airflow_docker](https://github.com/Cris-Neumann/ETL-with-Airflow-and-Docker/assets/99703152/328c1609-6d52-4550-9ff0-75b5ce4c9858)

## Conexión desde PostgreSQL a Power BI
Para la conexión desde PostgreSQL a Power BI se utiliza una conexión ODBC, utilizando el string conector a Power BI vía ANSIx64:
```
Driver={PostgreSQL ANSI(x64)};Server=SERVIDOR_SELECCIONADO;Port=PUERTO_SELECCIONADO;Database=BASE_DE_DATOS_SELECCIONADA
```

## Vista Dashboard en Power BI
A continuación una vista diseñada en Power BI, alojada en directorio 'views', con los ingresos, gastos y ahorro de clientes.
<br/><br/>

![dashboard](https://github.com/Cris-Neumann/ETL-with-Airflow-and-Docker/assets/99703152/ec4680ba-ab6b-43d6-9ee0-32433ae07d5f)

## Instalaciones adicionales
Adicional al conector ODBC, se debe instalar Docker y Docker Compose.
