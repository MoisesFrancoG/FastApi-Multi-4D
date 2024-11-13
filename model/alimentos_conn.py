import psycopg

class AlimentosConnection:
    def __init__(self):
        self.conn = None
        try:
            self.conn = psycopg.connect("dbname=Multi user=Moi password=12345678 host=localhost port=5432")
        except psycopg.OperationalError as err:
            print("Connection failed:", err)
            self.conn = None

    def read_all(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM mydb.alimentos;")
            return cur.fetchall()

    def read_one(self, id):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM mydb.alimentos WHERE idalimentos = %s;", (id,))
            return cur.fetchone()

    def write(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO mydb.alimentos (id_usuario, nombre, marca, calorias, proteina, carbohidratos, grasa, "tamañoporcion", tipomedida)
                VALUES (%(id_usuario)s, %(nombre)s, %(marca)s, %(calorias)s, %(proteina)s, %(carbohidratos)s, %(grasa)s, %(tamañoporcion)s, %(tipomedida)s);
            """, data)
        self.conn.commit()

    def update(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE mydb.alimentos
                SET id_usuario=%(id_usuario)s, nombre=%(nombre)s, marca=%(marca)s, calorias=%(calorias)s, proteina=%(proteina)s,
                    carbohidratos=%(carbohidratos)s, grasa=%(grasa)s, "tamañoporcion"=%(tamañoporcion)s, tipomedida=%(tipomedida)s
                WHERE idalimentos=%(idalimentos)s;
            """, data)
        self.conn.commit()

    def delete(self, id):
        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM mydb.alimentos WHERE idalimentos = %s;", (id,))
        self.conn.commit()

    def __del__(self):
        if self.conn:
            self.conn.close()
