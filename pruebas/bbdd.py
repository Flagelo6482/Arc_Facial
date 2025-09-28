# database.py
import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "database": "demo",
    "user": "postgres",
    "password": "1234",
    "port": "5432"
}

def get_connection():
    """Retorna una conexión a la base de datos"""
    try:
        return psycopg2.connect(**DB_CONFIG)
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return None