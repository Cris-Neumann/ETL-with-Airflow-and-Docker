-- Desde PGAdmin
CREATE TABLE IF NOT EXISTS tb_destino (
    id_usuario SERIAL PRIMARY KEY NOT NULL UNIQUE,
    rut	VARCHAR (100),
    nombre	VARCHAR (100),
    apellido VARCHAR (100),
    edad INT,
    genero VARCHAR (100),
    direccion VARCHAR (200),
    zona VARCHAR (100),
    pais VARCHAR (100),
    segmento VARCHAR (10),
    cod_seguro VARCHAR (10),
    ingreso_medio INT,
    gasto_medio INT);
INSERT INTO tb_destino (id_usuario, rut, nombre, apellido, edad, genero, direccion, zona, pais, segmento, cod_seguro, ingreso_medio, gasto_medio)
VALUES
    (1,'43986759',' Juan','Perez',50,'Masculino','7943 S. Fifth Street','Europa','United Kingdom','A','C0020',1172407,768978),
    (2,'35310078',' Maria','Gonzalez',30,'Femenino','77 Lyme Street','Europa','Malta','E','C002',1867717,635565),
    (3,'47790587',' Jose','Soto',49,'Masculino','9448 Fairfield St.','Australia y Oceanía','Marshall Islands','E','C0015',1753500,383098),
    (4,'44354488',' David','Diaz',62,'Femenino','8143 College St.','África','Iran','E','C007',709477,555944),
    (5,'30769365',' Joel','Gutierrez',28,'Masculino','9893 W. Vale Ave.','Centroamérica y Caribe','Guatemala','D','C003',1823254,234382),
    (6,'44894548',' Felipe','Urrutia',42,'Femenino','8094 Albany Drive','Centroamérica y Caribe','Grenada','E','C005',2083622,910636),
    (7,'49468628','Leandra','Zabala',32,'Masculino','9001 Creek Street','Australia y Oceanía','Fiji','A','C008',905937,434120),
    (8,'42864391','Severo','Alex',59,'Femenino','57 Green Drive','África','Tunisia ','C','C001',769693,983988),
    (9,'36427593','Lucho','Sanmiguel',55,'Masculino','86 Surrey St.','Centroamérica y Caribe','Grenada','B','C003',807591,313046),
    (10,'38993544','Matías','Bartolomé',50,'Femenino','8728 Boston Street','Australia y Oceanía','Australia','E','C008',635705,277354);
