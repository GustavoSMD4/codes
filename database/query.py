import csv
import sqlite3

conn = sqlite3.connect("database/database.db", check_same_thread=False)
cursor = conn.cursor()

def createTables():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CODES (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            CODE TEXT NOT NULL UNIQUE,
            QTDE INTEGER
        )               
    """)
    
    conn.commit()

def inserirDados():
    with open('codes.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        
        for row in reader:
            code = row[0].strip().zfill(4)
            qtde = float(row[1].strip())
            
            cursor.execute("INSERT INTO CODES (CODE, QTDE) VALUES (?, ?)", (code, qtde))
            conn.commit()
            print("inserido")

createTables()
inserirDados()
conn.close()




