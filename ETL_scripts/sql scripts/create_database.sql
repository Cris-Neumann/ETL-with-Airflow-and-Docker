''' Pasos para usar psql (postgre desde consola):
1) Entrar al contenedor docker de postgres:
    docker exec -it <container_id> /bin/bas
2) Conectarse a postgre:
    psql -d postgres -U airflow
3) Salir del contenedor sin detenerlo:
    Ctrl+P + Ctrl+Q   '''

-- Desde psql crear db:
CREATE DATABASE db_destino;
\c db_destino;
