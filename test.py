import os

ARQUIVO = "medicamentos.txt"
medicamentos = []

# Carregar medicamentos do arquivo
def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        for linha in f:
            dados = linha.strip().split("|")
            if len(dados) == 5:
                medicamento = {
                    "nome": dados[0],
                    "horario": dados[1],
                    "frequencia": dados[2],
                    "dose": dados[3],
                    "status": dados[4]
                }
                medicamentos.append(medicamento)

# Salvar medicamentos no arquivo
def salvar_dados():
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for med in medicamentos:
            linha = f"{med['nome']}|{med['horario']}|{med['frequencia']}|{med['dose']}|{med['status']}\n"
            f.write(linha)

def validar_horario(horario):
    try:
        h, m = map(int, horario.split(":"))
        return 0 <= h < 24 and 0 <= m < 60
    except:
        return False

def adicionar_medicamento():
    while True:
        nome = input("Nome do medicamento: ").strip()
        horario = input("Horário a ser tomado (HH:MM): ").strip()
        while not validar_horario(horario):
            print("⛔ Horário inválido. Use o formato 24h (ex: 14:30)")
            horario = input("Horário a ser tomado (HH:MM): ").strip()

        frequencia = input("Frequência (ex: 1x ao dia, de 8 em 8h): ").strip()
        dose = input("Dose a ser tomada: ").strip()

        medicamentos.append({
            "nome": nome,
            "horario": horario,
            "frequencia": frequencia,
            "dose": dose,
            "status": "pendente"
        })

        salvar_dados()
        print(f"✅ Medicamento '{nome}' adicionado com sucesso!")
        mais = input("Deseja adicionar outro medicamento? (s/n): ").strip().lower()
        if mais != 's':
            break

def listar_medicamentos():
    if not medicamentos:
        print("📭 Nenhum medicamento cadastrado.")
        return

    print("\n📋 Lista de medicamentos:")
    for i, med in enumerate(medicamentos, 1):
        print(f"{i}. {med['nome']} - {med['horario']} - {med['frequencia']} - Dose: {med['dose']} - Status: {med['status']}")

    escolha = input("\nDeseja visualizar um medicamento específico? (s/n): ").strip().lower()
    if escolha == 's':
        nome = input("Digite o nome do medicamento: ").strip()
        encontrado = False
        for med in medicamentos:
            if med['nome'].lower() == nome.lower():
                print(f"\n🔍 Informações de '{nome}':")
                print(f"Horário: {med['horario']}")
                print(f"Frequência: {med['frequencia']}")
                print(f"Dose: {med['dose']}")
                print(f"Status: {med['status']}")
                encontrado = True
                break
        if not encontrado:
            print("⛔ Medicamento não encontrado.")

    pendentes = input("Deseja ver quais remédios faltam tomar? (s/n): ").strip().lower()
    if pendentes == 's':
        print("\n⏳ Medicamentos pendentes:")
        for med in medicamentos:
            if med['status'] == "pendente":
                print(f"- {med['nome']}")

    tomados = input("Deseja ver quais remédios já foram tomados? (s/n): ").strip().lower()
    if tomados == 's':
        print("\n✅ Medicamentos já tomados:")
        for med in medicamentos:
            if med['status'] == "tomado":
                print(f"- {med['nome']}")

def excluir_medicamento():
    nome = input("Digite o nome do medicamento que deseja excluir: ").strip()
    for med in medicamentos:
        if med['nome'].lower() == nome.lower():
            certeza = input(f"Tem certeza que deseja excluir '{nome}'? (s/n): ").strip().lower()
            if certeza == 's':
                medicamentos.remove(med)
                salvar_dados()
                print("🗑️ Medicamento excluído com sucesso!")
            else:
                print("❌ Exclusão cancelada.")
            return
    print("⛔ Medicamento não encontrado.")

def menu():
    while True:
        print("\n==== MENU PRINCIPAL ====")
        print("1 - Adicionar novo medicamento")
        print("2 - Ver lista de medicamentos")
        print("3 - Excluir medicamento")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_medicamento()
        elif opcao == "2":
            listar_medicamentos()
        elif opcao == "3":
            excluir_medicamento()
        elif opcao == "4":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida.")

# Início do programa
carregar_dados()
menu()











import time

medicamentos = []

def menu():
    while True:
        print("\n==== MENU PRINCIPAL ====")
        print("1 - Adicionar novo medicamento")
        print("2 - Ver lista de medicamentos")
        print("3 - Excluir medicamento")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_medicamento()
        elif opcao == "2":
            listar_medicamentos()
        elif opcao == "3":
            excluir_medicamento()
        elif opcao == "4":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida.")

def validar_horario(horario):
    try:
        h, m = map(int, horario.split(":"))
        return 0 <= h < 24 and 0 <= m < 60
    except:
        return False

def adicionar_medicamento():
    while True:
        nome = input("Nome do medicamento: ").strip()
        horario = input("Horário a ser tomado (HH:MM): ").strip()
        while not validar_horario(horario):
            print("⛔ Horário inválido. Insira um horário dentro de 24h (ex: 14:30)")
            horario = input("Horário a ser tomado (HH:MM): ").strip()

        frequencia = input("Frequência (ex: 1x ao dia, de 8 em 8h): ").strip()
        dose = input("Dose a ser tomada: ").strip()

        medicamentos.append({
            "nome": nome,
            "horario": horario,
            "frequencia": frequencia,
            "dose": dose,
            "status": "pendente"
        })

        print(f"✅ Medicamento '{nome}' adicionado com sucesso!")
        mais = input("Deseja adicionar outro medicamento? (s/n): ").strip().lower()
        if mais != 's':
            break

def listar_medicamentos():
    if not medicamentos:
        print("📭 Nenhum medicamento cadastrado.")
        return

    print("\n📋 Lista de medicamentos:")
    for i, med in enumerate(medicamentos, 1):
        print(f"{i}. {med['nome']} - {med['horario']} - {med['frequencia']} - Dose: {med['dose']} - Status: {med['status']}")

    escolha = input("\nDeseja visualizar um medicamento específico? (s/n): ").strip().lower()
    if escolha == 's':
        nome = input("Digite o nome do medicamento: ").strip()
        encontrado = False
        for med in medicamentos:
            if med['nome'].lower() == nome.lower():
                print(f"\n🔍 Informações de '{nome}':")
                print(f"Horário: {med['horario']}")
                print(f"Frequência: {med['frequencia']}")
                print(f"Dose: {med['dose']}")
                print(f"Status: {med['status']}")
                encontrado = True
                break
        if not encontrado:
            print("⛔ Medicamento não encontrado.")

    pendentes = input("Deseja ver quais remédios faltam tomar? (s/n): ").strip().lower()
    if pendentes == 's':
        print("\n⏳ Medicamentos pendentes:")
        for med in medicamentos:
            if med['status'] == "pendente":
                print(f"- {med['nome']}")

    tomados = input("Deseja ver quais remédios já foram tomados? (s/n): ").strip().lower()
    if tomados == 's':
        print("\n✅ Medicamentos já tomados:")
        for med in medicamentos:
            if med['status'] == "tomado":
                print(f"- {med['nome']}")

def excluir_medicamento():
    nome = input("Digite o nome do medicamento que deseja excluir: ").strip()
    for med in medicamentos:
        if med['nome'].lower() == nome.lower():
            certeza = input(f"Tem certeza que deseja excluir '{nome}'? (s/n): ").strip().lower()
            if certeza == 's':
                medicamentos.remove(med)
                print("🗑️ Medicamento excluído com sucesso!")
            else:
                print("❌ Exclusão cancelada.")
            return
    print("⛔ Medicamento não encontrado.")

# Iniciar o programa
menu()


Após esses dados, o medicamento é adicionado com sucesso.
O sistema então pergunta se o usuário deseja adicionar outro medicamento.
	•	Se sim, o processo se repete.
	•	Se não, o sistema retorna ao menu principal.

⸻

🔹 Opção 2: Ver lista de medicamentos

Aqui, o sistema exibe todos os medicamentos já adicionados e pergunta:

“Deseja visualizar algum medicamento específico?”

	•	Se o usuário desejar:
	1.	Ele digita o nome do medicamento.
	2.	O sistema verifica se ele está na lista.
	•	Se sim, as informações do medicamento são exibidas.
	•	Se não, o sistema informa que o medicamento não foi encontrado e pede para inserir um nome válido.

Além disso, o sistema permite:
	•	Verificar quais medicamentos ainda precisam ser tomados.
	•	Verificar quais medicamentos já foram tomados.

⸻

🔹 Opção 3: Excluir medicamento

Ao fluxo em um programa real em Python com interface gráfica (usando customtkinter), ou em uma versão simples de terminal. Deseja isso?


import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Minhas Leituras")
app.geometry("500x500")

faixas = {
    "Criança": {"min": 0, "max": 11, "livros": ["O Pequeno Príncipe", "Chapeuzinho Vermelho", "Diário de um Banana"]},
    "Adolescente": {"min": 12, "max": 17, "livros": ["Harry Potter", "Crepúsculo", "Jogos Vorazes"]},
    "Jovem": {"min": 18, "max": 25, "livros": ["1984", "O sol é para todos", "Quarto de Despejo"]},
    "Adulto": {"min": 26, "max": 1000, "livros": ["Café com Deus Pai"]}
}

def recomendar_livros():
    try:
        idade = int(entry_idade.get())
        nome = entry_nome.get()
        cidade = entry_cidade.get()

        if not nome or not cidade:
            messagebox.showwarning("Campos vazios", "Preencha todos os campos!")
            return

        resposta = switch_recomendar.get()

        faixa_encontrada = None
        for faixa, info in faixas.items():
            if info["min"] <= idade <= info["max"]:
                faixa_encontrada = faixa
                livros = info["livros"]
                break

        resultado_text = f"Olá, {nome}!\nCidade/Estado: {cidade}\n"

        if resposta == "on":
            if faixa_encontrada:
                resultado_text += f"\n📘 Faixa Etária: {faixa_encontrada}\n📚 Livros recomendados:\n"
                for livro in livros:
                    resultado_text += f" - {livro}\n"
            else:
                resultado_text += "Idade fora do intervalo permitido."
        else:
            resultado_text += "\nVocê escolheu não receber recomendações agora."

        textbox_resultado.configure(state="normal")
        textbox_resultado.delete("1.0", "end")
        textbox_resultado.insert("1.0", resultado_text)
        textbox_resultado.configure(state="disabled")

    except ValueError:
        messagebox.showerror("Erro", "Digite uma idade válida (número).")

# --- Elementos da Interface ---

label_titulo = ctk.CTkLabel(app, text="📖 Minhas Leituras", font=("Arial", 24, "bold"))
label_titulo.pack(pady=20)

entry_nome = ctk.CTkEntry(app, placeholder_text="Digite seu nome")
entry_nome.pack(pady=10)

entry_idade = ctk.CTkEntry(app, placeholder_text="Digite sua idade")
entry_idade.pack(pady=10)

entry_cidade = ctk.CTkEntry(app, placeholder_text="Informe sua Cidade/Estado")
entry_cidade.pack(pady=10)

switch_recomendar = ctk.CTkSwitch(app, text="Deseja recomendações de livros?")
switch_recomendar.pack(pady=10)

btn_enviar = ctk.CTkButton(app, text="Ver Recomendação", command=recomendar_livros)
btn_enviar.pack(pady=15)

textbox_resultado = ctk.CTkTextbox(app, height=150, state="disabled")
textbox_resultado.pack(pady=10, padx=20, fill="both", expand=True)

app.mainloop()

print("\033[1;34;40m--------- Minhas Leituras ---------\033[m")
nome = input("Nome do Usuário: ")
print("\033[1;34;40mBem vindo(a)",str(nome),"ao programa Minhas Leituras,bom te ter aqui!\033[m")



faixas ={"Criança":{"min":0, "max":11,"livros":["O Pequeno Príncipe, Chapeuzinho Vermelho,Diário de um Banana"]},
    "Adolescente":{"min":12,"max":17,"livros":["Harry Potter,Crepúsculo,Jogos Vorazes",]},
    "Jovem":{"min":18,"max":25,"livros":["1984,O sol é para todos,Quarto de Despejo"]},
    "Adulto":{"min":26,"max":1000,"livros":["Café com Deus Pai"]}}


def rec_livros(idade):
    faixa_encontrada = None
    for faixa, info in faixas.items():
        if info["min"]<= idade <= info["max"]:
            faixa_encontrada = faixa
            livros = info["livros"]
            break
    if faixa_encontrada:
        print(f"\n\033[1;34;40mFaixa etária\033[m:{faixa_encontrada.capitalize()}")
        print("📚Livros recomendados:")
        for livro in livros:
             print(f"\033[1;34;40m{livro}\033[m")
        return
    print("Idade fora do intervalo permitido.")

try:
    idade = int(input("Quantos anos você tem? "))
    resposta = input("\033[1;34;40mGostaria que eu recomendasse livros para sua faixa etária?\033[m ").strip().lower()
    if resposta in ["sim","ss"]:
        rec_livros(idade)
    elif resposta in ["não",'nao','nn']:
        print("tudo bem, vamos prosseguir")
    else:
        print("Resposta não reconhecida. Por Favor, digite 'sim' ou 'não'")
except ValueError:
    print("Digite um número válido")

print("               ")

cidadeestado = input("Informe sua Cidade/Estado? ")
print("\033[1;34;40mAposto que deve ser um lugar muito bonito...\033[m")
