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
            print("Horário inválido. Use o formato 24h (ex: 14:30)")
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
        print(f"Medicamento '{nome}' adicionado com sucesso!")
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
                print(f"\n Informações de '{nome}':")
                print(f"Horário: {med['horario']}")
                print(f"Frequência: {med['frequencia']}")
                print(f"Dose: {med['dose']}")
                print(f"Status: {med['status']}")
                encontrado = True
                break
        if not encontrado:
            print(" Medicamento não encontrado.")

    pendentes = input("Deseja ver quais remédios faltam tomar? (s/n): ").strip().lower()
    if pendentes == 's':
        print("\n⏳ Medicamentos pendentes:")
        for med in medicamentos:
            if med['status'] == "pendente":
                print(f"- {med['nome']}")

    tomados = input("Deseja ver quais remédios já foram tomados? (s/n): ").strip().lower()
    if tomados == 's':
        print("\nMedicamentos já tomados:")
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
                print("Medicamento excluído com sucesso!")
            else:
                print("Exclusão cancelada.")
            return
    print("Medicamento não encontrado.")

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




