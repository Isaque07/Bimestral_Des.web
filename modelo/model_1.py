import sqlite3
from model.model_1 import *
# Classe RacaPasto

class RacaPasto(Tabela):
    def __init__(self) -> None:
        super().__init__
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS RacaPasto(
            id_raca INTEGER,
            id_pasto INTEGER,
            PRIMARY KEY (id_raca, id_pasto),
            FOREIGN KEY (id_raca) REFERENCES Racas(id_raca) ON DELETE CASCADE,
            FOREIGN KEY (id_pasto) REFERENCES Pastos(id_pasto) ON DELETE CASCADE
            );
        """)
        conn.close()

    def add_Raca_Pasto(self, id_raca: int, id_pasto: int) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
                INSERT INTO RacaPasto(id_raca, id_pasto)
                VALUES({id_raca}, {id_pasto});
                """)
        self.conn.commit()
        self.conn.close()

    def select_associacoesRP(self) -> list:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM RacaPasto;")
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                'id_raca': registro[0],
                'id_pasto': registro[1]
            })
        self.conn.close()
        return registros

    def select_registrosRP(self) -> list:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
        SELECT r.*, p.*
        FROM Racas AS r
        INNER JOIN RacaPasto AS rp ON r.id_raca = rp.id_raca
        INNER JOIN Pastos AS p ON p.id_pasto = rp.id_pasto;
        """)
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                "id_raca": registro[0],
                "nome_raca": registro[1],
                "id_pasto": registro[2],
                "nome_pasto": registro[3],
                "tamanho": registro[4],
                "tipo_vegetacao": registro[5]
            })
        self.conn.close()
        return registros

# Classe ProprietarioPasto

class ProprietarioPasto(Tabela):
    def __init__(self) -> None:
        super().__init__()
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS ProprietarioPasto(
            id_proprietario INTEGER,
            id_pasto INTEGER,
            PRIMARY KEY (id_proprietario, id_pasto),
            FOREIGN KEY (id_proprietario) REFERENCES Proprietarios(id_proprietario) ON DELETE CASCADE,
            FOREIGN KEY (id_pasto) REFERENCES Pastos(id_pasto) ON DELETE CASCADE
            );
        """)
        conn.close()

    def add_Proprietario_Pasto(self, id_proprietario: int, id_pasto: int) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
                INSERT INTO ProprietarioPasto(id_proprietario, id_pasto)
                VALUES({id_proprietario}, {id_pasto});
                """)
        self.conn.commit()
        self.conn.close()

    def select_associacoesPP(self) -> list:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM ProprietarioPasto;")
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                'id_proprietario': registro[0],
                'id_pasto': registro[1]
            })
        self.conn.close()
        return registros

    def select_registrosPP(self) -> list:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
        SELECT p.*, pt.*
        FROM Proprietarios AS p
        INNER JOIN ProprietarioPasto AS pp ON p.id_proprietario = pp.id_proprietario
        INNER JOIN Pastos AS pt ON pt.id_pasto = pp.id_pasto;
        """)
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                "id_proprietario": registro[0],
                "nome_proprietario": registro[1],
                "contato": registro[2],
                "id_pasto": registro[3],
                "nome_pasto": registro[4],
                "tamanho": registro[5],
                "tipo_vegetacao": registro[6]
            })
        self.conn.close()
        return registros

# Classe AnimalP

# Objetos de cada tabela:

Obj_RP = RacaPasto()
Obj_PP = ProprietarioPasto()
