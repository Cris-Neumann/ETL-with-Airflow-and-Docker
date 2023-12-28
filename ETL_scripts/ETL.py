import os
import traceback
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from aux_functions import update_to_sql, insert_to_sql, credentials

# Fechas y ruta prinicpal
path = os.path.dirname(os.path.realpath(__file__))
now = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
today = datetime.today().strftime("%d-%m-%Y")
cred = credentials(path)

# Origen: Archivo CSV.
source = pd.read_csv(path + '/data_origen.csv', sep = ';')
source['rut'] = source['rut'].astype('int64')

# Destino: Conexion a BBDD PostgreSQL.
user = cred['destino']['user']
passw = cred['destino']['passw']
host = cred['destino']['host']
port = cred['destino']['port']
db = cred['destino']['db']
engine = create_engine('postgresql://' + user + ':' + passw + '@' + host + ':' + port + '/' + db)
target = pd.read_sql('SELECT * FROM public."tb_destino"', engine)

# Filas de 'source' que no estan en 'target', es decir, cambios o nuevos registros.
changes = source[~source.apply(tuple,1).isin(target.apply(tuple,1))]
modified = changes[changes.id_usuario.isin(target.id_usuario)]
inserts = changes[~changes.id_usuario.isin(target.id_usuario)]

def main():
    try:
        update_len = update_to_sql(modified, 'tb_destino', 'id_usuario', engine)
        insert_len = insert_to_sql(inserts, 'tb_destino', engine)
        engine.dispose()
        with open(path + r'/ETL_log/log.txt', 'a+') as f:
                    f.write("\n" + str(now) +': Actualizacion BBDD PostgreSQL con exito, ' + 
                    update_len + ' registros actualizados y ' + insert_len + ' registros ' +
                    'insertados.')
    except Exception as e:
        with open(path + r'/ETL_log/log.txt', 'a+') as f:
                    f.write("\n" + str(now) +': ERROR: Load funcion main(), ' 
                    'Traceback: ' + str(traceback.format_exc()))
        engine.dispose()
        raise e

if __name__ == '__main__':
    main()