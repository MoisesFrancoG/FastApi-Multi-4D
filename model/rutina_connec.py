import psycopg

class RutinaConnection: 
    def __init__(self):
        self.conn = None
        try:
            self.conn = psycopg.connect("dbname=Multi user=miusuario password=miclave host=98.85.116.206 port=5432")
        except psycopg.OperationalError as err:
            print("Connection failed:", err)
            self.conn = None
            
    def read_all(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM mydb.rutina;")
            return cur.fetchall()
        
    def read_one(self, id):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM mydb.rutina WHERE idrutina = %s;", (id,))
            return cur.fetchone()
        
    def write(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO mydb.rutina(progresion, tiempo, nombre)
	            VALUES ( %(progresion)s, %(tiempo)s, %(nombre)s);
            """, data)
        self.conn.commit()
        
    def update(self,data):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE mydb.rutina
                SET progresion=%(progresion)s, tiempo=%(tiempo)s, nombre=%(nombre)s
                WHERE idrutina=%(idrutina)s
            """,data)
        self.conn.commit()
    
    def delete(self, id):
        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM mydb.rutina WHERE idrutina = %s;", (id,))
        self.conn.commit()

    def __del__(self):
        if self.conn:
            self.conn.close()