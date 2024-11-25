import psycopg

class UserConnection:
    def __init__(self):
        self.conn = None
        try:
            self.conn = psycopg.connect("dbname=Multi user=Moi password=12345678 host=localhost port=5432")
            #self.conn = psycopg.connect("dbname=Multi user=miusuario password=miclave host=98.85.116.206 port=5432")
        except psycopg.OperationalError as err:
            print("Connection failed:", err)
            self.conn = None


    def read_all(self):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                SELECT *
	FROM mydb.usuario;
        """)
            return data.fetchall()


    def write(self,data):
        with self.conn.cursor() as cur:
            cur.execute("""
                 INSERT INTO mydb.usuario(
	nombre, userpassword, email, edad, peso, estatura, sexo, indiceactividad)
	VALUES (%(nombre)s, %(userpassword)s, %(email)s, %(edad)s, %(peso)s, %(estatura)s, %(sexo)s, %(indiceactividad)s);       
            """,data)
        self.conn.commit()
    def __del__(self):
        if self.conn:
            self.conn.close()
            
    def read_one(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
             SELECT * FROM mydb.usuario WHERE idusuario = %s
            """, (id,))
            data = cur.fetchone()
            return data

    def delete(self,id):
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM mydb.usuario
	            WHERE idusuario = %s;
            """,(id,))
        self.conn.commit()
    
    
    def update(self,data):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE mydb.usuario
	            SET nombre= %(nombre)s, userpassword=%(userpassword)s, email= %(email)s, edad=%(edad)s, peso=%(peso)s, estatura=%(estatura)s, sexo=%(sexo)s, indiceactividad=%(indiceactividad)s
	            WHERE idusuario = %(idusuario)s; 
        """,data)
        self.conn.commit()

    
    def get_by_email(self, email):
        with self.conn.cursor() as cur:
            cur.execute("""
            SELECT * FROM mydb.usuario WHERE email = %s
            """, (email,))
            return cur.fetchone()


