import customtkinter as ctk
expressao = ""
def Criar_janela():
    janela = ctk.CTk()
    janela.title("Calculadora")
    janela.geometry("600x400")
    global entrada
    entrada = ctk.CTkEntry(janela,width=300,height=40)
    entrada.grid(row=0,column=0,columnspan=4,padx=10,pady=10)



    botoes = [
            ("7",1,0),("8",1,1),("9",1,2),("/",1,3),
              ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
              ("1",3,0),("2",3,1),("3",3,2),("-",3,3),
              ("0",4,0),(".",4,1),("=",4,2),("+",4,3),
              ("c",5,0)
    ]
    def inserir_valor(valor): #insere o valor na entrada
        global expressao
        expressao += valor
        entrada.delete(0,"end")#limpa todo o campo
        entrada.insert(0,expressao)#insere o valor de EXPRESSAO do caractere 0
    def calcular(): # função que calcula
        global expressao
        try:
            resultado= eval(expressao)
            entrada.delete(0,"end")
            entrada.insert(0,str(resultado))
            expressao = str(resultado)
            return expressao

        except Exception:
            return "error"
    def limpar(): # defino a função de limpar a entrada
        global expressao
        expressao = ""
        entrada.delete(0,"end")

    for texto, row, col in botoes:

        if texto == "=":
            botao = ctk.CTkButton(janela,
                                  text="=",
                                  command=calcular)
            
        elif texto == "c":
            botao = ctk.CTkButton(janela,
                                  text="c",
                                  command=limpar)
        
        else:    
            botao = ctk.CTkButton(janela,
                                text=texto,#text= texto, se refere ao primeiro objeto em cada tupla na lista
                                command=lambda valor=texto:inserir_valor(valor))#chamo lambda para a função nao ser executada antes da acão, valor= cria um valor para cada botao
        botao.grid(row=row,
                   column=col,
                   pady=10,
                   padx=5,
                   sticky="nsew")
    janela.mainloop()


Criar_janela()