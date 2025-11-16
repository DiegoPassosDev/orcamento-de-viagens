from tkinter import *
from tkinter import Tk, StringVar, ttk, messagebox
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from views import *

# Definindo cores para o tema
cor00 = "#2e2d2b"  # Preto
cor01 = "#feffff"  # Branco
cor02 = "#4fa882"  # Verde
cor03 = "#38576b"  # Azul escuro
cor04 = "#403d3d"  # Cinza escuro
cor05 = "#e06636"  # Laranja
cor06 = "#038cfc"  # Azul claro
cor07 = "#3fbfb9"  # Verde claro
cor08 = "#263238"  # Cinza azulado
cor09 = "#e9edf5"  # Cinza claro
cor10 = "#6e8faf"  # Azul acinzentado
cor11 = "#f2f4f2"  # Cinza muito claro
cor12 = "#bb5555" # Vermelho


colors = ["#5588bb", "#66bbbb", "#99bb55", "#ee9944", "#444466", "#bb5555"]

# Dados e totalizações globais
total_budget = 0
expenses_data = [
    ["1", "Transporte", "Taxi", 50.00],
    ["2", "Hospedagem", "Hotel", 300.00],
    ["3", "Alimentação", "Restaurante", 100.00],
    ["4", "Lazer", "Cinema", 40.00],
]
window = Tk()
window.title("FluxIT Solutions - Travel Budget")
window.geometry("820x610")
window.configure(background=cor01)
window.resizable(width=FALSE, height=FALSE)

# Centralizar janela na tela
window_width = 820
window_height = 610
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

style = ttk.Style(window)
style.theme_use("clam")
style.configure("Treeview", highlightthickness=0, bd=0, font=("Calibri", 9))


frameUp = Frame(window, width=1043, height=50, bg=cor01)
frameUp.grid(row=0, column=0)

frameCenter = Frame(window, width=1043, height=290, bg=cor01, padx=10)
frameCenter.grid(row=1, column=0)

frameLeft = Frame(frameCenter, width=250, height=290, bg=cor09, pady=0, relief="raised")
frameLeft.place(x=0, y=5)

frameRight = Frame(
    frameCenter, width=630, height=290, bg=cor01, pady=0, relief="raised"
)
frameRight.place(x=250, y=5)

frameDown = Frame(window, width=820, height=300, bg=cor01, relief="flat")
frameDown.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)

title_up = Label(
    frameUp,
    text="Orçamento de Viagens",
    compound=LEFT,
    padx=5,
    anchor=NW,
    font=("Verdana 20 bold"),
    bg=cor01,
    fg=cor04,
)
title_up.place(x=0, y=0)

image_title = Image.open("img/plane.png")
image_title = image_title.resize((45, 45))
image_title = ImageTk.PhotoImage(image_title)
image_title_label = Label(
    frameUp,
    image=image_title,
    width=900,
    compound=LEFT,
    padx=5,
    relief=FLAT,
    anchor=NW,
    bg=cor01,
    fg=cor04,
)
image_title_label.place(x=350, y=0)


def values_panel():
    lbl_title_values = Label(
        frameLeft,
        text="Orçamentos e Despesas",
        width=23,
        anchor=CENTER,
        font=("Verdana 12 bold"),
        bg=cor03,
        fg=cor01,
    )
    lbl_title_values.place(x=0, y=0)

    lbl_total_budget = Label(
        frameLeft,
        text="Orçamento Total:",
        width=20,
        anchor=W,
        font=("Verdana 10 bold"),
        bg=cor09,
        fg=cor04,
    )
    lbl_total_budget.place(x=10, y=50)

    global lbl_total_budget_value, lbl_total_expenses_value, lbl_balance_value

    # tenta obter o orçamento atual da base (se disponível), caso contrário usa o valor padrão
    try:
        tb = select_value()
        if tb is None:
            tb = total_budget
    except Exception:
        tb = total_budget

    lbl_total_budget_value = Label(
        frameLeft,
        text=f"R$ {tb:.2f}",
        width=20,
        anchor=NW,
        font=("Verdana 11"),
        bg=cor01,
        fg=cor04,
    )
    lbl_total_budget_value.place(x=10, y=80)

    lbl_total_expenses = Label(
        frameLeft,
        text="Despesas Totais:",
        width=20,
        anchor=W,
        font=("Verdana 10 bold"),
        bg=cor09,
        fg=cor04,
    )
    lbl_total_expenses.place(x=10, y=120)

    # tenta somar as despesas pela função da view (se disponível)
    try:
        total_expenses = sum_expenses() or 0
    except Exception:
        try:
            rows = select_expenses()
            total_expenses = sum(r[3] for r in rows) if rows else 0
        except Exception:
            total_expenses = sum(item[3] for item in expenses_data)

    lbl_total_expenses_value = Label(
        frameLeft,
        text=f"R$ {total_expenses:.2f}",
        width=20,
        anchor=NW,
        font=("Verdana 11"),
        bg=cor01,
        fg=cor04,
    )
    lbl_total_expenses_value.place(x=10, y=150)

    lbl_balance = Label(
        frameLeft,
        text="Saldo Restante:",
        width=20,
        anchor=W,
        font=("Verdana 10 bold"),
        bg=cor09,
        fg=cor04,
    )
    lbl_balance.place(x=10, y=190)
    balance = tb - total_expenses
    lbl_balance_value = Label(
        frameLeft,
        text=f"R$ {balance:.2f}",
        width=20,
        anchor=NW,
        font=("Verdana 11"),
        bg=cor01,
        fg=cor04,
    )
    lbl_balance_value.place(x=10, y=220)


frame_center_pie = None
category_canvas = None


def refresh_graphic():
    global frame_center_pie, category_canvas

    # Limpa o gráfico anterior se existir
    if category_canvas is not None:
        category_canvas.get_tk_widget().destroy()
    if frame_center_pie is not None:
        frame_center_pie.destroy()

    figure_graph = Figure(figsize=(7, 4), dpi=87)
    ax = figure_graph.add_subplot(111)

    # Busca despesas do banco de dados
    try:
        expenses = select_expenses()
    except Exception:
        expenses = []

    # Agrupa despesas por categoria e calcula a soma
    category_totals = {}
    for expense in expenses:
        # expense é uma tupla: (id, category, description, value)
        category = expense[1]
        value = float(expense[3])
        if category not in category_totals:
            category_totals[category] = 0
        category_totals[category] += value

    # Prepara listas para o gráfico
    if category_totals:
        categorys_list = list(category_totals.keys())
        values_list = list(category_totals.values())
    else:
        # Se não houver despesas, exibe um gráfico vazio com placeholder
        categorys_list = ["Sem dados"]
        values_list = [1]

    explode = [0.05 for _ in values_list]

    ax.pie(
        values_list,
        explode=explode,
        wedgeprops=dict(width=0.2),
        autopct="%1.1f%%",
        colors=colors,
        shadow=True,
        startangle=90,
    )

    ax.legend(categorys_list, loc="center right", bbox_to_anchor=(1.55, 0.5))

    frame_center_pie = Frame(
        frameRight, width=600, height=290, bg=cor11, pady=0, relief="raised"
    )
    frame_center_pie.place(x=-140, y=-25)

    lbl_title_graphic = Label(
        frameRight,
        text="Distribuição das Despesas",
        width=52,
        anchor=CENTER,
        padx=2,
        font=("Verdana 12 bold"),
        bg=cor10,
        fg=cor01,
    )
    lbl_title_graphic.place(x=0, y=0)

    category_canvas = FigureCanvasTkAgg(figure_graph, frame_center_pie)
    category_canvas.get_tk_widget().grid(row=0, column=0, padx=0)


def graphic_panel():
    refresh_graphic()


def expenses_panel():
    lbl_title_expenses = Label(
        frameDown,
        text="Detalhes das Despesas",
        width=87,
        anchor=NW,
        padx=6,
        font=("Verdana 12 bold"),
        bg=cor03,
        fg=cor01,
    )
    lbl_title_expenses.grid(row=0, column=0, columnspan=6, pady=0)

    frameTable = Frame(frameDown, width=220, height=250, bg=cor01)
    frameTable.grid(row=1, column=0, pady=0, padx=(0, 2), sticky=NSEW)

    frameAction = Frame(frameDown, width=180, height=250, bg=cor01)
    frameAction.grid(row=1, column=1, padx=(2, 2), sticky=NSEW)

    frameConfig = Frame(frameDown, width=290, height=250, bg=cor01)
    frameConfig.grid(row=1, column=2, padx=(2, 0), sticky=NSEW)

    def setup_table():
        table_head = ["id", "Tipo", "Descrição", "Total (R$)"]

        list_itens = select_expenses()
        global tree

        # Mantém o 'id' nas colunas (necessário para operações), mas oculta visualmente
        display_cols = ("Tipo", "Descrição", "Total (R$)")
        tree = ttk.Treeview(
            frameTable,
            selectmode="extended",
            columns=table_head,
            show="headings",
            displaycolumns=display_cols,
        )
        vsb = ttk.Scrollbar(frameTable, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(frameTable, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree.grid(row=0, column=0, sticky=NSEW)
        vsb.grid(row=0, column=1, sticky=NS)
        hsb.grid(row=1, column=0, sticky=EW)

        # Define cabeçalhos e larguras (id ficará oculto via displaycolumns)
        hd = ["center", "w", "center", "e"]
        h = [0, 120, 120, 80]

        for idx, col in enumerate(table_head):
            tree.heading(col, text=(col.title() if col != "id" else ""), anchor=CENTER)
            tree.column(
                col, width=h[idx], anchor=hd[idx], minwidth=(0 if col == "id" else 20)
            )

        # Insere os itens retornados pelo banco (mantendo o id nos valores)
        for item in list_itens:
            tree.insert("", "end", values=item)

    setup_table()

    lbl_expense_data = Label(
        frameAction,
        text="Insira Novas Despesas",
        anchor=CENTER,
        width=24,
        relief=FLAT,
        font=("Verdana 10 bold"),
        bg=cor01,
        fg=cor04,
    )
    lbl_expense_data.place(x=4, y=10)
    lbl_category = Label(
        frameAction,
        text="Categoria",
        anchor=CENTER,
        font=("Verdana 10"),
        bg=cor01,
        fg=cor04,
    )
    lbl_category.place(x=4, y=40)

    category = ["Transporte", "Aluguel", "Alimentação", "Entreterimento", "Outros"]

    cmb_category_expenses = ttk.Combobox(frameAction, width=13, font=("Verdana 10"))
    cmb_category_expenses["values"] = category
    cmb_category_expenses.place(x=80, y=41)

    lbl_description = Label(
        frameAction,
        text="Descrição",
        anchor=CENTER,
        font=("Verdana 10"),
        bg=cor01,
        fg=cor04,
    )
    lbl_description.place(x=4, y=80)
    input_description = Entry(frameAction, width=20, justify=LEFT, relief="solid")
    input_description.place(x=80, y=81)

    lbl_amount = Label(
        frameAction, text="Valor", anchor=NW, font=("Verdana 10"), bg=cor01, fg=cor04
    )
    lbl_amount.place(x=4, y=120)
    input_amount = Entry(frameAction, width=20, justify=LEFT, relief=SOLID)
    input_amount.place(x=80, y=121)

    # Criar função para que o campo input_amount não deixe o usuário digitar letras
    def validate_amount(value):
        if value == "" or value.replace(".", "", 1).isdigit():
            return True
        else:
            return False

    input_amount.config(
        validate="key", validatecommand=(input_amount.register(validate_amount), "%P")
    )

    # Adicionando os valores na tabela Expenses
    def add_expenses():
        category = cmb_category_expenses.get().upper()
        description = input_description.get().upper()
        amount = input_amount.get()

        print(category, description, amount)

        if not all([category, description, amount]):
            messagebox.showwarning("Atenção", "Por favor, preencha todos os campos.")
            return
        insert_expense(category, description, amount)
        messagebox.showinfo("Sucesso", "Despesa adicionada com sucesso!")
        setup_table()
        input_description.delete(0, END)
        input_amount.delete(0, END)
        # limpa campo de categoria após adicionar
        try:
            cmb_category_expenses.set("")
        except Exception:
            try:
                cmb_category_expenses.current(-1)
            except Exception:
                pass
        input_description.focus_set()

        # Atualiza os totais exibidos (tenta pela view, com fallback)
        try:
            total_expenses = sum_expenses() or 0
        except Exception:
            try:
                rows = select_expenses()
                total_expenses = sum(r[3] for r in rows) if rows else 0
            except Exception:
                total_expenses = sum(item[3] for item in expenses_data)

        try:
            tb = select_value()
            if tb is None:
                tb = total_budget
        except Exception:
            tb = total_budget

        # Atualiza labels
        try:
            # Atualiza também o Orçamento Total (tb pode ser 0 quando apagado)
            lbl_total_budget_value.config(text=f"R$ {tb:.2f}")
            lbl_total_expenses_value.config(text=f"R$ {total_expenses:.2f}")
            lbl_balance_value.config(text=f"R$ {tb - total_expenses:.2f}")
        except Exception:
            pass

        # Atualiza o gráfico
        try:
            refresh_graphic()
        except Exception:
            pass

    # Carrega ícones com fallback caso não exista ou haja erro
    try:
        img_edit = Image.open("img/edit.png")
        img_edit = img_edit.resize((17, 17))
        img_edit = ImageTk.PhotoImage(img_edit)
    except Exception:
        img_edit = None

    try:
        img_add_action = Image.open("img/new.png")
        img_add_action = img_add_action.resize((17, 17))
        img_add_action = ImageTk.PhotoImage(img_add_action)
    except Exception:
        img_add_action = None
    btn_add_action = Button(
        frameAction,
        image=img_add_action,
        compound=LEFT,
        anchor=CENTER,
        text="Adicionar",
        width=116,
        overrelief=RIDGE,
        font=("Verdana 7 bold"),
        bg=cor01,
        fg=cor00,
        cursor="hand2",
        command=add_expenses,
    )
    btn_add_action.image = img_add_action
    btn_add_action.place(x=80, y=160)

    # Botão Editar - abre modal para editar despesa selecionada
    def edit_selected_expense():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning(
                "Atenção", "Por favor, selecione uma despesa para editar."
            )
            return

        item_id = selected[0]
        values = tree.item(item_id, "values")
        if not values:
            messagebox.showwarning("Atenção", "Item selecionado inválido.")
            return

        expense_id = values[0]
        current_category = values[1]
        current_description = values[2]
        current_value = values[3]

        # Janela modal de edição (centralizada e modal em relação à janela principal)
        modal = Toplevel(window)
        modal.title("Editar Despesa")
        w_modal = 320
        h_modal = 180
        modal.resizable(False, False)
        modal.transient(window)
        modal.grab_set()
        modal.update_idletasks()
        try:
            win_x = window.winfo_rootx()
            win_y = window.winfo_rooty()
            win_w = window.winfo_width()
            win_h = window.winfo_height()
            x = win_x + (win_w // 2) - (w_modal // 2)
            y = win_y + (win_h // 2) - (h_modal // 2)
            modal.geometry(f"{w_modal}x{h_modal}+{x}+{y}")
        except Exception:
            modal.geometry(f"{w_modal}x{h_modal}")

        lbl_cat = Label(modal, text="Categoria", font=("Verdana 9"))
        lbl_cat.place(x=10, y=10)
        cmb_cat = ttk.Combobox(modal, width=20, font=("Verdana 9"))
        cmb_cat["values"] = [
            "Transporte",
            "Aluguel",
            "Alimentação",
            "Entreterimento",
            "Outros",
        ]
        try:
            cmb_cat.set(current_category)
        except Exception:
            cmb_cat.set("")
        cmb_cat.place(x=110, y=10)

        lbl_desc = Label(modal, text="Descrição", font=("Verdana 9"))
        lbl_desc.place(x=10, y=45)
        entry_desc = Entry(modal, width=25, font=("Verdana 9"))
        entry_desc.insert(0, current_description)
        entry_desc.place(x=110, y=45)

        lbl_val = Label(modal, text="Valor", font=("Verdana 9"))
        lbl_val.place(x=10, y=80)
        entry_val = Entry(modal, width=15, font=("Verdana 9"))
        entry_val.insert(0, current_value)
        entry_val.place(x=110, y=80)

        # Validação do valor (apenas números)
        def validate_modal_amount(value):
            if value == "" or value.replace(".", "", 1).isdigit():
                return True
            return False

        entry_val.config(
            validate="key",
            validatecommand=(entry_val.register(validate_modal_amount), "%P"),
        )

        def save_edit():
            new_cat = cmb_cat.get().upper()
            new_desc = entry_desc.get().upper()
            raw = entry_val.get().strip()
            if not all([new_cat, new_desc, raw]):
                messagebox.showwarning("Atenção", "Preencha todos os campos.")
                return
            try:
                new_value = float(raw.replace(",", "."))
            except Exception:
                messagebox.showwarning("Atenção", "Valor inválido.")
                return

            try:
                update_expense(expense_id, new_cat, new_desc, new_value)
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível atualizar: {e}")
                return

            messagebox.showinfo("Sucesso", "Despesa atualizada com sucesso!")
            # Atualiza a tabela, labels e gráfico
            try:
                setup_table()
            except Exception:
                pass

            try:
                total_expenses = sum_expenses() or 0
            except Exception:
                try:
                    rows = select_expenses()
                    total_expenses = sum(r[3] for r in rows) if rows else 0
                except Exception:
                    total_expenses = sum(item[3] for item in expenses_data)

            try:
                tb = select_value()
                if tb is None:
                    tb = total_budget
            except Exception:
                tb = total_budget

            try:
                lbl_total_budget_value.config(text=f"R$ {tb:.2f}")
                lbl_total_expenses_value.config(text=f"R$ {total_expenses:.2f}")
                lbl_balance_value.config(text=f"R$ {tb - total_expenses:.2f}")
            except Exception:
                pass

            try:
                refresh_graphic()
            except Exception:
                pass

            modal.destroy()

        btn_save = Button(modal, text="Salvar", width=10, command=save_edit, bg=cor02, fg=cor01, font=("Verdana 10 bold"))
        btn_save.place(x=55, y=120)
        btn_cancel = Button(modal, text="Cancelar", width=10, command=modal.destroy, bg=cor12, fg=cor01, font=("Verdana 10 bold"))
        btn_cancel.place(x=175, y=120)
        # coloca foco no modal e no campo descrição
        try:
            modal.focus_force()
            entry_desc.focus_set()
        except Exception:
            pass

    # Usa a mesma imagem do botão adicionar para evitar erro se não houver imagem de editar

    # Cria o botão Editar — usa imagem se disponível
    if img_edit is not None:
        btn_edit_action = Button(
            frameAction,
            image=img_edit,
            compound=LEFT,
            anchor=CENTER,
            text="Editar",
            width=116,
            overrelief=RIDGE,
            font=("Verdana 7 bold"),
            bg=cor01,
            fg=cor00,
            cursor="hand2",
            command=edit_selected_expense,
        )
        btn_edit_action.image = img_edit
    else:
        btn_edit_action = Button(
            frameAction,
            text="Editar",
            width=116,
            overrelief=RIDGE,
            font=("Verdana 7 bold"),
            bg=cor01,
            fg=cor00,
            cursor="hand2",
            command=edit_selected_expense,
        )
    btn_edit_action.place(x=80, y=200)

    lbl_title_balace = Label(
        frameConfig,
        text="Ajustar Saldo",
        anchor=CENTER,
        width=23,
        relief=FLAT,
        font=("Verdana 10 bold"),
        bg=cor01,
        fg=cor04,
    )
    lbl_title_balace.place(x=10, y=10)

    lbl_value_balance = Label(
        frameConfig,
        text="Adicionar Saldo",
        anchor=NW,
        font=("Verdana 10"),
        bg=cor01,
        fg=cor04,
    )
    lbl_value_balance.place(x=10, y=40)

    input_balance = Entry(frameConfig, width=16, justify=LEFT, relief=SOLID)
    input_balance.place(x=120, y=41)

    # validação para aceitar apenas números (inclui ponto ou vírgula)
    def validate_balance(value):
        if value == "":
            return True
        try:
            # permite vírgula ou ponto
            v = value.replace(",", ".")
            float(v)
            return True
        except Exception:
            return False

    input_balance.config(
        validate="key", validatecommand=(input_balance.register(validate_balance), "%P")
    )

    # Função para adicionar valor ao saldo total
    def update_total_budget():
        raw = input_balance.get().strip()
        if not raw:
            messagebox.showwarning(
                "Atenção", "Por favor, insira um valor para adicionar ao saldo."
            )
            return
        try:
            value = float(raw.replace(",", "."))
        except Exception:
            messagebox.showwarning("Atenção", "Valor inválido. Use apenas números.")
            return

        # obtém o total atual
        try:
            current = select_value()
            if current is None:
                current = total_budget
        except Exception:
            current = total_budget

        new_total = float(current) + value

        # tenta atualizar, se não existir insere
        try:
            update_value(new_total)
        except Exception:
            try:
                insert_value(new_total)
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível atualizar o saldo: {e}")
                return

        messagebox.showinfo("Sucesso", f"Saldo atualizado: R$ {new_total:.2f}")

        # Atualiza labels e gráfico
        try:
            lbl_total_budget_value.config(text=f"R$ {new_total:.2f}")
        except Exception:
            pass

        try:
            total_expenses = sum_expenses() or 0
        except Exception:
            try:
                rows = select_expenses()
                total_expenses = sum(r[3] for r in rows) if rows else 0
            except Exception:
                total_expenses = sum(item[3] for item in expenses_data)

        try:
            lbl_total_expenses_value.config(text=f"R$ {total_expenses:.2f}")
            lbl_balance_value.config(text=f"R$ {new_total - total_expenses:.2f}")
        except Exception:
            pass

        try:
            refresh_graphic()
        except Exception:
            pass

        input_balance.delete(0, END)

    img_add_config = Image.open("img/update.png")
    img_add_config = img_add_config.resize((17, 17))
    img_add_config = ImageTk.PhotoImage(img_add_config)
    btn_add_config = Button(
        frameConfig,
        image=img_add_config,
        compound=LEFT,
        anchor=CENTER,
        text="Atualizar",
        width=94,
        overrelief=RIDGE,
        font=("Verdana 7 bold"),
        bg=cor01,
        fg=cor00,
        cursor="hand2",
        command=update_total_budget,
    )
    btn_add_config.image = img_add_config
    btn_add_config.place(x=120, y=76)

    lbl_delete = Label(
        frameConfig,
        text="Excluir Despesa",
        anchor=N,
        width=12,
        relief=FLAT,
        font=("Verdana 8 bold"),
        bg=cor01,
        fg=cor04,
        cursor="hand2",
    )
    lbl_delete.place(x=10, y=120)
    img_delete = Image.open("img/delete.png")
    img_delete = img_delete.resize((17, 17))
    img_delete = ImageTk.PhotoImage(img_delete)

    # Função para excluir a despesa selecionada na tabela
    def delete_selected_expense():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning(
                "Atenção", "Por favor, selecione uma despesa na tabela."
            )
            return

        # pega apenas o primeiro selecionado
        item_id = selected[0]
        values = tree.item(item_id, "values")
        if not values:
            messagebox.showwarning("Atenção", "Item selecionado inválido.")
            return

        expense_id = values[0]
        confirm = messagebox.askyesno(
            "Confirmação", "Deseja excluir a despesa selecionada?"
        )
        if not confirm:
            return

        try:
            delete_expense(expense_id)
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível excluir a despesa: {e}")
            return

        messagebox.showinfo("Sucesso", "Despesa excluída com sucesso!")
        setup_table()

        # Recalcula os totais e atualiza os labels
        try:
            total_expenses = sum_expenses() or 0
        except Exception:
            try:
                rows = select_expenses()
                total_expenses = sum(r[3] for r in rows) if rows else 0
            except Exception:
                total_expenses = sum(item[3] for item in expenses_data)

        try:
            tb = select_value()
            if tb is None:
                tb = total_budget
        except Exception:
            tb = total_budget

        try:
            # atualiza também o orçamento total exibido
            try:
                lbl_total_budget_value.config(text=f"R$ {tb:.2f}")
            except Exception:
                pass
            lbl_total_expenses_value.config(text=f"R$ {total_expenses:.2f}")
            lbl_balance_value.config(text=f"R$ {tb - total_expenses:.2f}")
        except Exception:
            pass

        # Atualiza o gráfico
        try:
            refresh_graphic()
        except Exception:
            pass

    btn_delete = Button(
        frameConfig,
        image=img_delete,
        compound=LEFT,
        anchor=CENTER,
        text="Excluir",
        width=94,
        overrelief=RIDGE,
        font=("Verdana 7 bold"),
        bg=cor01,
        fg=cor00,
        command=delete_selected_expense,
        cursor="hand2",
    )
    btn_delete.image = img_delete
    btn_delete.place(x=120, y=116)

    lbl_delete_all = Label(
        frameConfig,
        text="Excluir Tudo",
        anchor=NW,
        width=12,
        relief=FLAT,
        font=("Verdana 8 bold"),
        bg=cor01,
        fg=cor04,
        cursor="hand2",
    )
    lbl_delete_all.place(x=7, y=162)

    # Função para excluir todas as despesas
    def delete_all_expenses_ui():
        confirm = messagebox.askyesno(
            "Confirmação",
            "Deseja excluir todas as despesas? Esta ação não pode ser desfeita.",
        )
        if not confirm:
            return

        try:
            delete_all_expenses()
            # também remove o valor do orçamento (Amount)
            try:
                delete_amount()
            except Exception:
                pass
        except Exception as e:
            messagebox.showerror(
                "Erro", f"Não foi possível excluir todas as despesas: {e}"
            )
            return

        messagebox.showinfo(
            "Sucesso", "Todas as despesas e o orçamento foram excluídos."
        )
        setup_table()

        # Recalcula e atualiza totais
        try:
            tb = select_value()
            if tb is None:
                tb = 0
        except Exception:
            # se o registro foi removido, zera o orçamento
            tb = 0

        try:
            total_expenses = sum_expenses() or 0
        except Exception:
            try:
                rows = select_expenses()
                total_expenses = sum(r[3] for r in rows) if rows else 0
            except Exception:
                total_expenses = sum(item[3] for item in expenses_data)

        try:
            # garante que o Orçamento Total também seja mostrado como zero
            try:
                lbl_total_budget_value.config(text=f"R$ {tb:.2f}")
            except Exception:
                pass
            lbl_total_expenses_value.config(text=f"R$ {total_expenses:.2f}")
            lbl_balance_value.config(text=f"R$ {tb - total_expenses:.2f}")
        except Exception:
            pass

        try:
            refresh_graphic()
        except Exception:
            pass

    btn_delete_all = Button(
        frameConfig,
        image=img_delete,
        compound=LEFT,
        anchor=CENTER,
        text="Excluir",
        width=94,
        overrelief=RIDGE,
        font=("Verdana 7 bold"),
        bg=cor01,
        fg=cor00,
        command=delete_all_expenses_ui,
    )
    btn_delete_all.image = img_delete
    btn_delete_all.place(x=120, y=160)


values_panel()
graphic_panel()
expenses_panel()
window.mainloop()
