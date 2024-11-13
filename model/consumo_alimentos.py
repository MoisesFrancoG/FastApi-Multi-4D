import psycopg

class ConsumoConnec:
    def __init__(self):
        self.conn = None
        try:
            self.conn = psycopg.connect("dbname=Multi user=Moi password=12345678 host=localhost port=5432")
        except psycopg.OperationalError as err:
            print("Connection failed:", err)
            self.conn = None
            
    def read_all(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM mydb.consumo_alimentos;")
            return cur.fetchall()
    
    def read_one(self, id):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM mydb.consumo_alimentos WHERE idconsumo = %s;", (id,))
            return cur.fetchone()
        
    def write(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO mydb.consumo_alimentos (id_usuario, fecha)
                VALUES (%(id_usuario)s, %(fecha)s);
            """, data)
        self.conn.commit()
    
    def update(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE mydb.consumo_alimentos
                SET id_usuario=%(id_usuario)s, fecha=%(fecha)s 
                WHERE idconsumo=%(idconsumo)s;
            """, data)
        self.conn.commit()
        
    def delete(self, id):
        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM mydb.consumo_alimentos WHERE idconsumo = %s;", (id,))
        self.conn.commit()

    def __del__(self):
        if self.conn:
            self.conn.close()