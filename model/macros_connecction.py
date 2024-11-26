import psycopg

class MacrosConnecction: 
    def __init__(self):
        self.conn = None
        try:
            self.conn = psycopg.connect("dbname=Multi user=Moi password=12345678 host=localhost port=5432")
            # self.conn = psycopg.connect("dbname=Multi user=miusuario password=miclave host=98.85.116.206 port=5432")
        except psycopg.OperationalError as err:
            print("Connection failed:", err)
            self.conn = None
            
    def read_all(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM mydb.macros;")
            return cur.fetchall()
        
    def read_one(self, id):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM mydb.macros WHERE id_usuario = %s;", (id,))
            return cur.fetchone()
        
    def write(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO mydb.macros(calorias,proteina,carbohidratos,grasas,id_usuario)
	            VALUES ( %(calorias)s, %(proteina)s, %(carbohidratos)s, %(grasas)s, %(id_usuario)s);
            """, data)
        self.conn.commit()
        
    def update(self,data):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE mydb.macros
                SET calorias=%(calorias)s, proteina=%(proteina)s, carbohidratos=%(carbohidratos)s, grasas=%(grasas)s
                WHERE id_usuario=%(id_usuario)s
            """,data)
        self.conn.commit()
        
    def delete(self, id):
        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM mydb.macros WHERE id_usuario = %s;", (id,))
        self.conn.commit()

    def __del__(self):
        if self.conn:
            self.conn.close()