import sqlite3 as sqlite

connection = sqlite.connect("travel_budget.db")


# Inserir valor na tabela Amount
def insert_value(value):
    connection.execute("INSERT INTO Amount (value) VALUES (?)", (value,))
    connection.commit()


# Atualizar valor na tabela Amount sempre no id 1
def update_value(value):
    # Garante que haverá um registro com id=1: usa INSERT OR REPLACE
    connection.execute(
        "INSERT OR REPLACE INTO Amount (id, value) VALUES (1, ?)", (value,)
    )
    connection.commit()
    # NÃO fechar a conexão global aqui — outras funções usam `connection`


# Selecionar valor na tabela Amount
def select_value():
    cursor = connection.execute("SELECT value FROM Amount WHERE id = 1")
    row = cursor.fetchone()
    if row is None:
        return None
    return row[0]


# Selecionar os dados na tabela Expenses e retornar em uma lista
def select_expenses():
    cursor = connection.execute("SELECT * FROM Expenses")
    return cursor.fetchall()


# Selecionar dos os valores de Expenses e retornar a soma deles
def sum_expenses():
    cursor = connection.execute("SELECT SUM(value) FROM Expenses")
    return cursor.fetchone()[0]


# Adicionar uma nova despesa na tabela Expenses
def insert_expense(category, description, value):
    connection = sqlite.connect("travel_budget.db")
    connection.execute(
        "INSERT INTO Expenses (category, description, value) VALUES (?, ?, ?)",
        (category, description, value),
    )
    connection.commit()
    connection.close()


def delete_expense(id):
    connection = sqlite.connect("travel_budget.db")
    connection.execute("DELETE FROM Expenses WHERE id = ?", (id,))
    connection.commit()
    connection.close()


def delete_all_expenses():
    connection = sqlite.connect("travel_budget.db")
    connection.execute("DELETE FROM Expenses")
    connection.commit()
    connection.close()


def delete_amount():
    """Remove o registro(s) da tabela Amount (apaga o valor do orçamento)."""
    connection = sqlite.connect("travel_budget.db")
    connection.execute("DELETE FROM Amount")
    connection.commit()
    connection.close()


def update_expense(expense_id, category, description, value):
    """Atualiza uma despesa pelo id."""
    connection = sqlite.connect("travel_budget.db")
    connection.execute(
        "UPDATE Expenses SET category = ?, description = ?, value = ? WHERE id = ?",
        (category, description, value, expense_id),
    )
    connection.commit()
    connection.close()
