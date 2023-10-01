from tkinter import PhotoImage, messagebox  
import customtkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#configuração de janela 1 
janela =customtkinter.CTk()
janela.geometry("600x400")
janela.title("Sistema de Cadastro")

#configuração de janela 2
def abrir_janela2():
    janela.iconify()
    messagebox.showinfo("Login","Seja Bem-Vindo ao Sistema")
    janela2=customtkinter.CTkToplevel(janela)
    janela2.geometry("700x400")
    janela2.title("Login")
    texto=customtkinter.CTkLabel(janela2,text="ESCOLHA UMA OPÇÃO PARA CONTINUAR ! ")
    texto.pack()
    botao1=customtkinter.CTkButton(janela2,text="EXCLUIR",command=abrir_janela2)
    botao1.place(x=340,y=44)
    botao1=customtkinter.CTkButton(janela2,text="ALTERAR",command=abrir_janela2)
    botao1.place(x=500,y=44)
    botao1=customtkinter.CTkButton(janela2,text="CADASTRAR",command=abrir_janela2)
    botao1.place(x=15,y=44)
    botao1=customtkinter.CTkButton(janela2,text="INCLUIR",command=abrir_janela2)
    botao1.place(x=180,y=44)
    #---------------------------------------------------------------------------------
    texto=customtkinter.CTkLabel(janela2,text="Nome completo*")
    texto.place(x=57,y=100)
    formularionome=customtkinter.CTkEntry(janela2,placeholder_text="Digite o nome de usuario",width=200)
    formularionome.place(x=180,y=100)
    formularioemail=customtkinter.CTkLabel(janela2,text="E-mail*")
    formularioemail.place(x=415,y=100)
    formularioemail=customtkinter.CTkEntry(janela2,placeholder_text="Digite o e-mail",width=200)
    formularioemail.place(x=480,y=100)
    formularicpf=customtkinter.CTkLabel(janela2,text="CPF*")
    formularicpf.place(x=365,y=150)
    formularicpf=customtkinter.CTkEntry(janela2,placeholder_text="Digite o CPF ",width=200)
    formularicpf.place(x=404,y=150)
    formulariotelefone=customtkinter.CTkLabel(janela2,text="TEL*")
    formulariotelefone.place(x=115,y=150)
    formulariotelefone=customtkinter.CTkEntry(janela2,placeholder_text="Digite o telefone ",width=200)
    formulariotelefone.place(x=150,y=150)
    

#Fechar janela sem uso 
def fecha_janela():
    fecha=customtkinter.CTkFrame(janela,text="",command=janela.destroy)
    fecha.pack()

#titulo janela
texto=customtkinter.CTkLabel(janela,text="FAZER LOGIN", font=("arial bold",20))
texto.pack(padx=10,pady=10)
textoemail=customtkinter.CTkLabel(janela,text="admin", font=("arial bold",20))
textoemail.place(x=80,y=57)
textosenha=customtkinter.CTkLabel(janela,text="senha", font=("arial bold",20,))
textosenha.place(x=80,y=104)
#imput usuario 
email=customtkinter.CTkEntry(janela,placeholder_text="digite seu e-mail",width=300)
email.pack(padx=10,pady=10)

#imput senha
senha=customtkinter.CTkEntry(janela,placeholder_text="digite a senha",width=300,show="*")
senha.pack(padx=10,pady=10)
checkbox=customtkinter.CTkCheckBox(janela,text="ENTRAR",command=abrir_janela2)
checkbox.pack(padx=10,pady=10)

#botao entrar
botao=customtkinter.CTkButton(janela,text="ENTRAR",command=abrir_janela2)
botao.place(x=150,y=200)

#botao sair
botao=customtkinter.CTkButton(janela,text="SAIR >",command=janela.destroy)
botao.place(x=310,y=200)

    
janela.mainloop()