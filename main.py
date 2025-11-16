"""
Entry point da aplicacao de Orcamento de Viagens.
Inicializa o banco de dados e abre a interface grafica.
"""

# Inicializa o banco de dados ANTES de importar screen
from database import initialize_database

initialize_database()

import screen

if __name__ == "__main__":
    # Inicia a interface grafica
    screen.window.mainloop()
