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
