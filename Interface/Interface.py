# Criação de tela no TKINTER primeiros teste de criação

from tkinter import *
import requests

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/BTC-BRL,EUR-BRL,USD-BRL")

    requisicao_dic = requisicao.json()
    
    cotacao_dollar = requisicao_dic['USDBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    
    print(f"A cotação do Dólar é ",cotacao_dollar)
    print(f"A cotação do Bitcon é ",cotacao_btc)       
    print(f"A cotação do Euro é ",cotacao_euro)  
janela = Tk()

janela.title("Minha primeira jenala")

texto_orientacao =  Label(janela,text="Clicar no botão para ver a cotação das moedas")
texto_orientacao.grid(column=0, row=0)

botao = Button(janela,text="Buscar cotação",command=pegar_cotacoes)

botao.grid(column=0,row=1)
janela.mainloop()