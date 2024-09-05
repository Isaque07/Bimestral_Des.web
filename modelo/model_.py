import sqlite3

# Classe Tabela (superclasse):
class Tabela:
    def __init__(self) -> None:
        self.module = sqlite3
        self.conn = self.module.connect("fazendaDB.db")
        self.cursor = self.conn.cursor()

# Classe Animais:
class Animais(Tabela):
    def __init__(self) -> None:
        super().__init__()
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Animais(
            id_animal INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome_animal VARCHAR(60) NOT NULL,
            idade INTEGER NOT NULL,
            peso REAL NOT NULL,
            genero VARCHAR(10) NOT NULL
            );
        """)
        self.conn.close()

    def add_animal(self, nome: str, idade: int, peso: float, genero: str) -> None:
        self.conn = self.module.connect("fazendaDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
        INSERT INTO Animais(nome_animal, idade, peso, genero)
        VALUES('{nome}', {idade}, {peso}, '{genero}');
        """)
        self.conn.commit()
        self.conn.close()

    def select_animais(self) -> list:
        self.conn = self.module.connect("fazendaDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM Animais;")
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                'id': registro[0],
                'nome_animal': registro[1],
                'idade': registro[2],
                'peso': registro[3],
                'genero': registro[4]
            })
        self.conn.close()
        return registros

    def del_animal(self, id: int) -> None:
        self.conn = self.module.connect("fazendaDB.db")
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"DELETE FROM Animais WHERE id_animal = {id};")
        self.conn.commit()
        self.conn.close()

    def update_animal(self, id: int, nome: str, idade: int, peso: float, genero: str) -> None:
        self.conn = self.module.connect("fazendaDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            UPDATE Animais SET nome_animal = '{nome}', idade = {idade}, peso = {peso}, genero = '{genero}'
            WHERE id_animal = {id};
            """)
        self.conn.commit()
        self.conn.close()

# Classe Raças:
class Racas(Tabela):
    def __init__(self) -> None:
        super().__init__()
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Racas(
            id_raca INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome_raca VARCHAR(30) NOT NULL
            );
        """)
        self.conn.close()

    def add_raca(self, nome: str) -> None:
        self.conn = self.module.connect("fazendaDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
        INSERT INTO Racas(nome_raca)
        VALUES('{nome}');
        """)
        self.conn.commit()
        self.conn.close()

    def select_racas(self) -> list:
        self.conn = self.module.connect("fazendaDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM Racas;")
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                'id': registro[0],
                'nome_raca': registro[1]
            })
        self.conn.close()
        return registros

    def del_raca(self, id: int) -> None:
        self.conn = self.module.connect("fazendaDB.db")
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"DELETE FROM Racas WHERE id_raca = {id};")
        self.conn.commit()
        self.conn.close()

    def update_raca(self, id: int, nome: str) -> None:
        self.conn = self.module.connect("fazendaDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            UPDATE Racas SET nome_raca = '{nome}'
            WHERE id_raca = {id};
            """)
        self.conn.commit()
        self.conn.close()

# Classe Pastos:
class Pastos(Tabela):
    def __init__(self) -> None:
        super().__init__()
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Pastos(
            id_pasto INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome_pasto VARCHAR(30) NOT NULL,
            tamanho_hectares REAL NOT NULL
            );
        """)
        self.conn.close()

    def add_pasto(self, nome: str, tamanho: float) -> None:
        self.conn = self.module.connect("fazendaDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
        INSERT INTO Pastos(nome_pasto, tamanho_hectares)
        VALUES('{nome}', {tamanho});
        """)
        self.conn.commit()
        self.conn.close()

    def select_pastos(self) -> list:
        self.conn = self.module.connect("fazendaDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM Pastos;")
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                'id': registro[0],
                'nome_pasto': registro[1],
                'tamanho_hectares': registro[2]
            })
        self.conn.close()
        return registros

    def del_pasto(self, id: int) -> None:
        self.conn = self.module.connect("fazendaDB.db")
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"DELETE FROM Pastos WHERE id_pasto = {id};")
        self.conn.commit()
        self.conn.close()

    def update_pasto(self, id: int, nome: str, tamanho: float) -> None:
        self.conn = self.module.connect("fazendaDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            UPDATE Pastos SET nome_pasto = '{nome}', tamanho_hectares = {tamanho}
            WHERE id_pasto = {id};
            """)
        self.conn.commit()
        self.conn.close()

# Classe Proprietários:
class Proprietarios(Tabela):
    def __init__(self) -> None:
        super().__init__()
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Proprietarios(
            id_prop INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome_prop VARCHAR(30) NOT NULL
            );
        """)
        self.conn.close()

    def add_prop(self, nome: str) -> None:
        self.conn = self.module.connect("fazendaDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
        INSERT INTO Proprietarios(nome_prop)
        VALUES('{nome}');
        """)
        self.conn.commit()
        self.conn.close()

    def select_props(self) -> list:
        self.conn = self.module.connect("fazendaDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM Proprietarios;")
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                'id': registro[0],
                'nome_prop': registro[1]
            })
        self.conn.close()
        return registros

    def del_prop(self, id: int) -> None:
        self.conn = self.module.connect("fazendaDB.db")
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"DELETE FROM Proprietarios WHERE id_prop = {id};")
        self.conn.commit()
        self.conn.close()

    def update_prop(self, id: int, nome: str) -> None:
        self.conn = self.module.connect("fazendaDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            UPDATE Proprietarios SET nome_prop = '{nome}'
            WHERE id_prop = {id};
            """)
        self.conn.commit()
        self.conn.close()

# Objetos de cada tabela:

Obj_Animal = Animais()
Obj_Prop = Proprietarios()
Obj_Raca = Racas()
Obj_Pasto = Pastos()
