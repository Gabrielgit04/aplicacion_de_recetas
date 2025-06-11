import sqlite3

def conexion_database():
    try:
        conex = sqlite3.connect('recetas.db')
        cursor = conex.cursor()
        
        print("Conexion completada.")
        conex.commit()
                
    except sqlite3.Error as error:
        print(f"Error de conexion{error}")
        
    finally:
        if conex:
            conex.close()
    
conexion_database()    
