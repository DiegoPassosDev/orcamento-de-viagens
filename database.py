import sqlite3 as sqlite
import os

DB_NAME = "travel_budget.db"


def initialize_database():
    """Cria tabelas se nao existirem."""
    connection = sqlite.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Amount (
            id INTEGER PRIMARY KEY,
            value REAL NOT NULL
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            description TEXT NOT NULL,
            value REAL NOT NULL
        )
        """
    )

    connection.commit()
    connection.close()
    print(f"Banco de dados '{DB_NAME}' inicializado!")
