#Criação de tela baseado no PySimpleGUI
import PySimpleGUI as sg
from cotacao import pegar_cotacao
'''
Atributos que tem na tela
para pegar valores de um inputText precisa colocar o key e o nome de referencia para manipular o valor
'''
layout = [
    [sg.Text("Pegar cotação da moeda")],
    [sg.InputText(key="nome_cotacao")],
    [sg.Button("Pegar cotação"),sg.Button("Limpar"),sg.Button("Cancelar")],
    [sg.Text("", key="texto_cotacao")],
]
#Criação da janela
Janela = sg.Window("Sistema de cotação",layout)

#Repetição enquanto for verdadeiro sistema ficará repetindo a ação da tela
while True:
    #Crar as variavel para pegar os eventos e valores de ação na tela
    evento, valores = Janela.read()
    #Evento para encerrar a janela
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        break
    #Evento de limpar campo informa o nome da tela e entre conchetes colocar a chave que foi criada e atualizar 
    if evento == "Limpar":
        Janela["nome_cotacao"].update("")
    if evento == "Pegar cotação":
        codigo_cotacao = valores["nome_cotacao"]
        #Chamar outra class com a busca de cotação e retornar o valor da cotação da moeda desejada
        cotacao = pegar_cotacao(codigo_cotacao)
        Janela["texto_cotacao"].update(f"A cotação do {codigo_cotacao} é de R$ {cotacao}")
    
Janela.close()