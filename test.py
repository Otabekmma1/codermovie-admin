import psycopg2
import logging

logging.basicConfig(level=logging.DEBUG)

try:
    conn = psycopg2.connect(
        dbname='coderdata',
        user='coderuser',
        password='Otabek2007',
        host='coder.railway.internal',
        port='5432'
    )
    print("Connection successful")
except psycopg2.Error as e:
    print(f"Error: {e}")
finally:
    if 'conn' in locals() and conn:
        conn.close()

with conn.cursor() as cursor:
    cursor.execute("SELECT pg_encoding_to_char(encoding) FROM pg_database WHERE datname = 'coderdata'")
    encoding = cursor.fetchone()
    print(f"Encoding: {encoding[0]}")

conn.close()
