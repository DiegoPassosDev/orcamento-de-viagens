# 🌍 Orçamento de Viagens

Uma aplicação desktop robusta e intuitiva para gerenciamento de orçamento de viagens, desenvolvida em Python com interface gráfica moderna usando Tkinter.

**Versão:** 1.0.0  
**Status:** ✅ Completo e funcional

---

## 📋 Tabela de Conteúdos

- [Características](#características)
- [Screenshots](#screenshots)
- [Requisitos do Sistema](#requisitos-do-sistema)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Funcionalidades Detalhadas](#funcionalidades-detalhadas)
- [Banco de Dados](#banco-de-dados)
- [Arquitetura](#arquitetura)
- [Troubleshooting](#troubleshooting)
- [Contribuições](#contribuições)
- [Licença](#licença)

---

## ✨ Características

- ✅ **Gerenciamento de Orçamento:** Defina e acompanhe seu orçamento total de viagem
- ✅ **Adição de Despesas:** Registre despesas por categoria com descrição e valor
- ✅ **Edição de Despesas:** Modifique despesas existentes via modal intuitivo
- ✅ **Exclusão de Despesas:** Delete despesas individuais ou todas de uma vez
- ✅ **Visualização em Gráfico:** Veja a distribuição das despesas por categoria em gráfico pizza
- ✅ **Cálculos Automáticos:** Acompanhe totais de despesas e saldo restante em tempo real
- ✅ **Banco de Dados SQLite:** Persistência de dados confiável
- ✅ **Interface Responsiva:** Design limpo e organizado em painéis
- ✅ **Validação de Entrada:** Campos numéricos com validação automática
- ✅ **Modal Centralizado:** Janela de edição centralizada no monitor

---

## 📸 Screenshots

### Tela Principal
A interface é dividida em três seções principais:

1. **Painel Esquerdo:** Exibe orçamento total, despesas totais e saldo restante
2. **Painel Direito:** Gráfico pizza com distribuição das despesas por categoria
3. **Painel Inferior:** Tabela de despesas com ações CRUD e controles de saldo

---

## 🔧 Requisitos do Sistema

### Software
- **Python:** 3.8 ou superior
- **Sistema Operacional:** Windows, macOS ou Linux

### Dependências Python
- `tkinter` - Interface gráfica (incluso no Python padrão)
- `Pillow` - Processamento de imagens
- `matplotlib` - Geração de gráficos

---

## 📦 Instalação

### 1. Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/orcamento-de-viagens.git
cd orcamento-de-viagens
```

### 2. Criar Ambiente Virtual (Recomendado)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

**Ou instale manualmente:**
```bash
pip install Pillow matplotlib
```

### 4. Executar a Aplicação
```bash
python main.py
```

A aplicação será iniciada e:
1. Verificará se o banco de dados existe
2. Criará as tabelas necessárias (se não existirem)
3. Abrirá a interface gráfica

---

## 🚀 Como Usar

### Iniciar a Aplicação
```bash
python main.py
```

### Operações Básicas

#### 1. **Definir Orçamento**
- Vá ao painel "Ajustar Saldo" (inferior direito)
- Digite o valor que deseja adicionar ao orçamento
- Clique em "Atualizar"
- O orçamento total será atualizado automaticamente

#### 2. **Adicionar Despesa**
- Vá ao painel "Insira Novas Despesas" (inferior central)
- Selecione uma categoria no dropdown:
  - Transporte
  - Aluguel
  - Alimentação
  - Entreterimento
  - Outros
- Digite uma descrição
- Informe o valor
- Clique em "Adicionar"
- A despesa será inserida na tabela e os totais serão atualizados

#### 3. **Editar Despesa**
- Selecione uma despesa na tabela (linha)
- Clique no botão "Editar"
- A janela de edição abrirá centralizada
- Modifique os campos desejados
- Clique em "Salvar" para confirmar ou "Cancelar"
- Totais e gráfico são atualizados automaticamente

#### 4. **Excluir Despesa Individual**
- Selecione uma despesa na tabela
- Clique em "Excluir" (seção "Excluir Despesa")
- Confirme a exclusão
- A despesa será removida e os totais atualizados

#### 5. **Excluir Todas as Despesas**
- Clique em "Excluir" (seção "Excluir Tudo")
- Confirme a ação (irreversível)
- Todas as despesas **e o orçamento** serão removidos
- A tabela e gráfico serão zerados

#### 6. **Visualizar Gráfico**
- O gráfico pizza atualiza em tempo real
- Mostra a proporção de despesas por categoria
- Exibe porcentagem de cada categoria
- Atualiza automaticamente ao adicionar/editar/excluir despesas

---

## 📁 Estrutura do Projeto

```
orcamento-de-viagens/
│
├── main.py                 # Entry point da aplicação
├── database.py             # Inicialização e gerenciamento do BD
├── views.py                # Camada de acesso aos dados (CRUD)
├── screen.py               # Interface gráfica (GUI)
│
├── img/                    # Pasta com ícones
│   ├── plane.png           # Ícone do avião (título)
│   ├── new.png             # Ícone "Adicionar"
│   ├── edit.png            # Ícone "Editar"
│   ├── update.png          # Ícone "Atualizar"
│   └── delete.png          # Ícone "Excluir"
│
├── travel_budget.db        # Banco de dados SQLite (auto-gerado)
├── requirements.txt        # Dependências do projeto
├── README.md               # Este arquivo
└── .gitignore              # Arquivos ignorados no Git
```

---

## 🏗️ Funcionalidades Detalhadas

### Painel de Orçamentos e Despesas (Esquerda)
Exibe em tempo real:
- **Orçamento Total:** Valor total destinado à viagem
- **Despesas Totais:** Soma de todas as despesas registradas
- **Saldo Restante:** Diferença entre orçamento e despesas (Orçamento - Despesas)

### Distribuição das Despesas (Direita)
- Gráfico pizza com segmentação por categoria
- Mostra porcentagem de cada categoria
- Legendas com nomes das categorias
- Atualização automática em tempo real

### Detalhes das Despesas (Inferior)

#### Tabela de Despesas
- Lista todas as despesas registradas
- Colunas: Tipo, Descrição, Total
- ID interno oculto (usado para operações)
- Suporta seleção de itens
- Scrollbar vertical e horizontal

#### Painel de Adição
- **Categoria:** Dropdown com 5 opções
- **Descrição:** Campo de texto livre
- **Valor:** Campo numérico com validação
- **Botão Adicionar:** Insere nova despesa
- Campo de categoria é limpo após adição

#### Painel de Edição
- **Botão Editar:** Abre modal para editar item selecionado
- Modal centralizado no monitor
- Pré-preenchido com dados atuais
- Validação de entrada
- Botões Salvar/Cancelar

#### Painel de Ajuste de Saldo
- **Campo Adicionar Saldo:** Valor a somar ao orçamento
- **Validação:** Apenas números (suporta ponto e vírgula)
- **Botão Atualizar:** Confirma adição

#### Painéis de Exclusão
- **Excluir Despesa:** Remove despesa selecionada (com confirmação)
- **Excluir Tudo:** Remove todas as despesas e o orçamento (com confirmação de segurança)

---

## 🗄️ Banco de Dados

### Arquivo: `travel_budget.db`

Banco de dados SQLite com 2 tabelas:

#### Tabela: `Amount`
Armazena o orçamento total da viagem.

```sql
CREATE TABLE Amount (
    id INTEGER PRIMARY KEY,
    value REAL NOT NULL
)
```

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `id` | INTEGER | Chave primária (sempre 1) |
| `value` | REAL | Valor do orçamento |

#### Tabela: `Expenses`
Armazena todas as despesas registradas.

```sql
CREATE TABLE Expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    description TEXT NOT NULL,
    value REAL NOT NULL
)
```

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `id` | INTEGER | Chave primária (auto-incremento) |
| `category` | TEXT | Categoria da despesa |
| `description` | TEXT | Descrição da despesa |
| `value` | REAL | Valor da despesa |

### Inicialização Automática

Ao executar `python main.py`:
1. O arquivo `database.py` verifica se o BD existe
2. Se não existir, cria o BD e as tabelas
3. Se existir, usa o BD existente
4. Mensagem de status é exibida no console

---

## 🏛️ Arquitetura

### Padrão de Arquitetura: MVC (Model-View-Controller)

```
┌─────────────────────────────────────────┐
│         main.py (Entry Point)           │
│  ├─ Inicializa BD (database.py)         │
│  └─ Carrega GUI (screen.py)             │
└──────────────┬──────────────────────────┘
               │
       ┌───────┴────────┐
       │                │
┌──────▼──────┐  ┌──────▼────────┐
│  screen.py  │  │  database.py   │
│  (View)     │  │  (Database)    │
└──────┬──────┘  └───────────────┘
       │
       └──────────┬──────────────┐
                  │              │
          ┌───────▼──────┐  ┌───▼─────────┐
          │  views.py    │  │ travel_     │
          │  (CRUD Ops)  │  │ budget.db   │
          └──────────────┘  └─────────────┘
```

### Fluxo de Dados

1. **main.py:** Entry point que inicializa BD e abre GUI
2. **database.py:** Cria BD e tabelas (IF NOT EXISTS)
3. **screen.py:** Interface gráfica que chama funções de CRUD
4. **views.py:** Funções CRUD que acessam o banco
5. **travel_budget.db:** Persiste os dados

### Fluxo Típico de uma Operação (Exemplo: Adicionar Despesa)

```
1. Usuário clica "Adicionar"
   ↓
2. screen.add_expenses() lê valores do formulário
   ↓
3. Valida entrada (campos preenchidos, valor numérico)
   ↓
4. Chama views.insert_expense(category, description, value)
   ↓
5. views.insert_expense() executa INSERT no BD
   ↓
6. BD registra nova linha em Expenses
   ↓
7. screen.py recalcula totais via views.sum_expenses()
   ↓
8. Atualiza labels (orçamento, despesas, saldo)
   ↓
9. Chama refresh_graphic() para atualizar pie chart
   ↓
10. Exibe mensagem de sucesso ao usuário
```

---

## 📚 Referência de Funções

### database.py
```python
initialize_database()
# Cria BD e tabelas se não existirem
```

### views.py
```python
insert_value(value)           # Insere orçamento
update_value(value)           # Atualiza orçamento (INSERT OR REPLACE)
select_value()                # Retorna orçamento atual

insert_expense(category, description, value)  # Adiciona despesa
select_expenses()             # Retorna lista de todas as despesas
sum_expenses()                # Retorna soma de todas as despesas
update_expense(id, category, description, value)  # Edita despesa
delete_expense(id)            # Deleta despesa específica
delete_all_expenses()         # Deleta todas as despesas
delete_amount()               # Deleta registro do orçamento
```

### screen.py
```python
values_panel()                # Cria painel de totalizações
graphic_panel()               # Cria painel de gráfico
expenses_panel()              # Cria painel de operações CRUD
refresh_graphic()             # Atualiza gráfico pizza
setup_table()                 # Popula tabela com despesas
add_expenses()                # Handler do botão Adicionar
edit_selected_expense()       # Handler do botão Editar
delete_selected_expense()     # Handler do botão Excluir
delete_all_expenses_ui()      # Handler do botão Excluir Tudo
update_total_budget()         # Handler do botão Atualizar (saldo)
```

---

## 🎨 Esquema de Cores

| Variável | Cor | Uso |
|----------|-----|-----|
| `cor00` | #2e2d2b (Preto) | Texto em botões |
| `cor01` | #feffff (Branco) | Fundo geral |
| `cor02` | #4fa882 (Verde) | Destaque |
| `cor03` | #38576b (Azul Escuro) | Títulos de seções |
| `cor04` | #403d3d (Cinza Escuro) | Texto principal |
| `cor09` | #e9edf5 (Cinza Claro) | Fundo de painéis |
| `cor10` | #6e8faf (Azul Acinzentado) | Subtítulos |

---

## 🖼️ Ícones

Todos os ícones utilizados nesta aplicação foram obtidos do site **[Icons8](https://icons8.com.br/)** e respeitam os termos de uso da plataforma.

### Ícones Utilizados
- ✈️ **plane.png** - Ícone do avião (título da aplicação)
- ➕ **new.png** - Ícone "Adicionar despesa"
- ✏️ **edit.png** - Ícone "Editar despesa"
- 🔄 **update.png** - Ícone "Atualizar saldo"
- 🗑️ **delete.png** - Ícone "Excluir despesa(s)"

---

## 🐛 Troubleshooting

### Problema: "ModuleNotFoundError: No module named 'PIL'"
**Solução:**
```bash
pip install Pillow
```

### Problema: "ModuleNotFoundError: No module named 'matplotlib'"
**Solução:**
```bash
pip install matplotlib
```

### Problema: "sqlite3.OperationalError: no such table"
**Solução:** Execute novamente `python main.py` para reinicializar o BD.

### Problema: Imagens não aparecem nos botões
**Solução:** Verifique se a pasta `img/` existe no mesmo diretório que `main.py` e contém os arquivos PNG.

### Problema: Janela modal não abre centralizada
**Solução:** Verifique as dimensões do seu monitor; o cálculo de centralização leva em conta a resolução atual.

### Problema: Despesa não é atualizada no gráfico após edição
**Solução:** O gráfico é atualizado automaticamente. Se não aparecer, tente fechar e reabrir a aplicação.

### Problema: Caracteres especiais (ç, ã, etc) aparecem errados
**Solução:** Certifique-se de que o arquivo está salvo em UTF-8. Recarregue a aplicação.

---

## 💾 Backup do Banco de Dados

Para fazer backup do seu banco de dados:

```bash
# Copie o arquivo travel_budget.db para local seguro
cp travel_budget.db travel_budget_backup.db
```

Para restaurar:
```bash
# Substitua o arquivo atual pelo backup
cp travel_budget_backup.db travel_budget.db
```

---

## 📝 Validações de Entrada

### Campo "Valor" (Despesas)
- ✅ Aceita números inteiros e decimais
- ✅ Suporta ponto como separador (ex: 100.50)
- ❌ Rejeita automaticamente letras e caracteres especiais
- ❌ Campo não permite digitação inválida

### Campo "Adicionar Saldo"
- ✅ Aceita números inteiros e decimais
- ✅ Suporta ponto ou vírgula como separador (ex: 100.50 ou 100,50)
- ❌ Rejeita automaticamente letras e caracteres especiais
- ❌ Campo obrigatório (com validação de preenchimento)

### Campo "Descrição"
- ✅ Aceita qualquer texto
- ✅ Converte automaticamente para MAIÚSCULAS
- ❌ Campo obrigatório

### Dropdown "Categoria"
- ✅ 5 categorias pré-definidas
- ✅ Seleção obrigatória
- ❌ Não permite categorias customizadas (v1.0)

---

## 🔐 Segurança e Boas Práticas

- ✅ SQL Injection Prevention: Uso de prepared statements (?)
- ✅ Data Validation: Validação de entrada em campos numéricos
- ✅ Confirmation Dialogs: Confirmação antes de exclusões permanentes
- ✅ Error Handling: Try/except em operações críticas com fallback
- ✅ Database Initialization: Verificação IF NOT EXISTS antes de criar tabelas
- ✅ Image References: Mantém referências a imagens para evitar garbage collection

---

## 🚀 Melhorias Futuras (v2.0)

- [ ] Exportar relatório em PDF/Excel
- [ ] Filtro de despesas por data
- [ ] Múltiplas moedas
- [ ] Categorias customizáveis
- [ ] Sugestões baseadas em padrões de gastos
- [ ] Sincronização em nuvem
- [ ] Modo escuro
- [ ] Suporte a backup automático
- [ ] Relatórios por período
- [ ] Integração com APIs de câmbio

---

## 📞 Suporte e Contribuições

### Reportar Bugs
1. Abra uma issue no repositório
2. Descreva o problema detalhadamente
3. Inclua prints/logs de erro
4. Especifique seu SO e versão do Python

### Contribuir com Código
1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 👤 Autor

Desenvolvido por **[FluixIT-Solutions]**

- GitHub: [@DiegoPassosDev](https://github.com/DiegoPassosDev)
- LinkedIn: [Diego Passos](https://www.linkedin.com/in/diegopassosaju/)

---

## 🙏 Agradecimentos

- **Icons8** - Pelos ícones disponibilizados (https://icons8.com.br/)
- **Python Community** - Pelo excelente framework e bibliotecas
- **Tkinter Developers** - Pela biblioteca GUI robusta
- **Todos os contribuidores e usuários** 

---

## 📌 Changelog

### v1.0.0 (15 de Novembro de 2025)
- ✅ Versão inicial completa
- ✅ Funcionalidades CRUD (Create, Read, Update, Delete)
- ✅ Gráfico de distribuição de despesas
- ✅ Banco de dados SQLite
- ✅ Interface gráfica com Tkinter
- ✅ Validação de entrada
- ✅ Modal centralizado para edição
- ✅ Documentação completa

---

**Desenvolvido com ❤️ em Python**

