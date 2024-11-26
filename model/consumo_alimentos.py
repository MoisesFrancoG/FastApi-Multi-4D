import psycopg
from datetime import date
class ConsumoConnec:
    def __init__(self):
        self.conn = None
        try:
            self.conn = psycopg.connect("dbname=midatabase user=miusuario password=miclave host=35.174.29.231 port=5432")
            #self.conn = psycopg.connect("dbname=Multi user=Moi password=12345678 host=localhost port=5432")
            #self.conn = psycopg.connect("dbname=Multi user=miusuario password=miclave host=98.85.116.206 port=5432")
        except psycopg.OperationalError as err:
            print("Connection failed:", err)
            self.conn = None
            
    # Añadir este método
    def get_all_by_user(self, id_usuario):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM mydb.consumo_alimentos 
                WHERE id_usuario = %s 
                ORDER BY fecha DESC;
            """, (id_usuario,))
            return cur.fetchall()
    
    # Mantener los métodos existentes y añadir este nuevo método
    def get_or_create_daily_consumo(self, id_usuario):
        fecha_hoy = date.today().isoformat()  # Fecha actual en formato YYYY-MM-DD
        with self.conn.cursor() as cur:
            # Verificar si ya existe un consumo para este usuario y la fecha actual
            cur.execute("""
                SELECT idconsumo FROM mydb.consumo_alimentos 
                WHERE id_usuario = %s AND fecha = %s;
            """, (id_usuario, fecha_hoy))
            result = cur.fetchone()
            if result:
                # Si ya existe, devolver el idconsumo
                return result[0]
            else:
                # Si no existe, crearlo
                cur.execute("""
                    INSERT INTO mydb.consumo_alimentos (id_usuario, fecha) 
                    VALUES (%s, %s)
                    RETURNING idconsumo;
                """, (id_usuario, fecha_hoy))
                idconsumo = cur.fetchone()[0]
                self.conn.commit()
                return idconsumo        
    
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
                VALUES (%(id_usuario)s, %(fecha)s)
                RETURNING idconsumo;
            """, data)
            idconsumo = cur.fetchone()[0]
        self.conn.commit()
        return idconsumo
    
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