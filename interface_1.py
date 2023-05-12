import requests
from tkinter import *


def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacao['text'] = texto

janela = Tk()
janela.title('Cotações')
janela.geometry('300x350')

textop = Label (janela, text='')
textop.grid(column=0, row=0)

textop = Label (janela, text='')
textop.grid(column=1, row=1)

textop = Label (janela, text='veja a cotacao atual do dólar, euro e BTC!')
textop.grid(column=2, row=2, padx=5, pady=10)

botao = Button(janela, text=('buscar'), command=pegar_cotacoes)
botao.grid(column=2, row=3, padx=5, pady=10)

textop = Label ( janela, text='')
textop.grid(column=2, row=4, padx=5, pady=10)

texto_cotacao = Label(janela, text='Clique acima!')
texto_cotacao.grid(column=2, row=5, padx=5, pady=5)


janela.mainloop()
