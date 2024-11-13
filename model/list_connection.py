import psycopg

class ListaConnection: 
    def __init__(self):
        self.conn = None
        try:
            self.conn = psycopg.connect("dbname=Multi user=Moi password=12345678 host=localhost port=5432")
        except psycopg.OperationalError as err:
            print("Connection failed:", err)
            self.conn = None
            
    def read_all(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM mydb.lista_alimentos;")
            return cur.fetchall()
        
    def read_one(self, id):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM mydb.lista_alimentos WHERE idlistaalimentos = %s;", (id,))
            return cur.fetchall()
        
    def write(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO mydb.lista_alimentos(idcomida, idalimento, nombre,marca,calorias,proteina,carbohidratos,grasa,"tamañoporcion",tipomedida,categoriacomida)
	            VALUES ( %(idcomida)s,%(idalimento)s,%(nombre)s,%(marca)s,%(calorias)s, %(proteina)s, %(carbohidratos)s, %(grasa)s,%(tamañoporcion)s,%(tipomedida)s,%(categoriacomida)s);
            """, data)
        self.conn.commit()
        
    def update(self,data):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE mydb.lista_alimentos
                SET idcomida=%(idcomida)s, idalimento=%(idalimento)s, nombre=%(nombre)s,
                marca=%(marca)s,calorias=%(calorias)s,proteina=%(proteina)s,
                carbohidratos=%(carbohidratos)s,grasa=%(grasa)s, "tamañoporcion"=%(tamañoporcion)s, tipomedida=%(tipomedida)s, categoriacomida=%(categoriacomida)s   
                WHERE idlistaalimentos=%(idlistaalimentos)s
            """,data)
        self.conn.commit()
        
    def delete(self, id):
        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM mydb.lista_alimentos WHERE idlistaalimentos = %s;", (id,))
        self.conn.commit()

    def __del__(self):
        if self.conn:
            self.conn.close()