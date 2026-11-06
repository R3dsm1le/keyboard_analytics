import os
import dotenv
import polars as pl
import sqlite3

dotenv.load_dotenv()

storage_options = {
    "aws_access_key_id": os.getenv("R2_ACCESS_KEY_ID"),
    "aws_secret_access_key": os.getenv("R2_SECRET_ACCESS_KEY"),
    "aws_endpoint_url": os.getenv("R2_ENDPOINT_URL"),
    "aws_region": "auto", 
}

# 1. Leer el archivo CSV desde R2
df = pl.read_csv(
    os.getenv("RUTA_CSV"),
    storage_options=storage_options,
)

# 2. Exportar a SQLite usando sqlite3 y pandas
db_path = "/data/analytics.db"
pdf = df.to_pandas()

conn = sqlite3.connect(db_path)
pdf.to_sql("analytics", conn, if_exists="replace", index=False)
conn.close()

# 3. Ajustar permisos para que el contenedor de Superset pueda leerlo/escribirlo
os.chmod(db_path, 0o666)
print("Base de datos SQLite generada correctamente.")