import psycopg

class EjercicioConnection: 
    def __init__(self):
        self.conn = None
        try:
            #self.conn = psycopg.connect("dbname=Multi user=Moi password=12345678 host=localhost port=5432")
            self.conn = psycopg.connect("dbname=midatabase user=miusuario password=miclave host=35.174.29.231 port=5432")
        except psycopg.OperationalError as err:
            print("Connection failed:", err)
            self.conn = None
            
    def read_all(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM mydb.ejercicios;")
            return cur.fetchall()
        
    def read_one(self, id):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM mydb.ejercicios WHERE idrutina = %s;", (id,))
            return cur.fetchall()
        
    def write(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO mydb.ejercicios(idrutina, nombre, descripcion,dificultad,musculotrabajado,imagen)
	            VALUES ( %(idrutina)s, %(nombre)s, %(descripcion)s, %(dificultad)s,%(musculotrabajado)s,%(imagen)s);
            """, data)
        self.conn.commit()
        
    def update(self,data):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE mydb.ejercicios
                SET idrutina=%(idrutina)s, nombre=%(nombre)s, descripcion=%(descripcion)s, dificultad=%(dificultad)s,musculotrabajado=%(musculotrabajado)s
                WHERE idejercicios=%(idejercicios)s
            """,data)
        self.conn.commit()
        
    def delete(self, id):
        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM mydb.ejercicios WHERE idejercicios = %s;", (id,))
        self.conn.commit()

    def __del__(self):
        if self.conn:
            self.conn.close()