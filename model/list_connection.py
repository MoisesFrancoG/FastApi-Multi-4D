import psycopg

class ListaConnection: 
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
            cur.execute("SELECT * FROM mydb.lista_alimentos;")
            return cur.fetchall()
        
    def read_one(self, id):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM mydb.lista_alimentos WHERE idcomida = %s;", (id,))
            return cur.fetchall()
        
    def write(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO mydb.lista_alimentos(idcomida, idalimento, nombre,marca,calorias,proteina,carbohidratos,grasa,porcion,tipomedida,categoriacomida)
	            VALUES ( %(idcomida)s,%(idalimento)s,%(nombre)s,%(marca)s,%(calorias)s, %(proteina)s, %(carbohidratos)s, %(grasa)s,%(porcion)s,%(tipomedida)s,%(categoriacomida)s);
            """, data)
        self.conn.commit()
        
    def update(self, data):
        with self.conn.cursor() as cur:
            # Obtener los datos del alimento relacionado
            cur.execute("SELECT calorias, proteina, carbohidratos, grasa, porcion FROM mydb.alimentos WHERE idalimentos = %s;", (data['idalimento'],))
            alimento = cur.fetchone()

            if not alimento:
                raise ValueError(f"Alimento con id {data['idalimento']} no encontrado.")

            # Calcular los valores ajustados a la nueva porción
            base_porcion = alimento[4]  # Porción base del alimento
            porcion_factor = data['porcion'] / base_porcion

            data['calorias'] = alimento[0] * porcion_factor
            data['proteina'] = alimento[1] * porcion_factor
            data['carbohidratos'] = alimento[2] * porcion_factor
            data['grasa'] = alimento[3] * porcion_factor    

            # Actualizar la lista de alimentos
            cur.execute("""
                UPDATE mydb.lista_alimentos
                SET porcion = %(porcion)s, 
                    categoriacomida = %(categoriacomida)s, 
                    calorias = %(calorias)s, 
                    proteina = %(proteina)s,
                    carbohidratos = %(carbohidratos)s, 
                    grasa = %(grasa)s
                WHERE idlistaalimentos = %(idlistaalimentos)s;
            """, data)

            # Confirmar los cambios
            self.conn.commit()


        
    def delete(self, id):
        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM mydb.lista_alimentos WHERE idlistaalimentos = %s;", (id,))
        self.conn.commit()

    def __del__(self):
        if self.conn:
            self.conn.close()