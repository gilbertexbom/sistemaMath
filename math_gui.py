# interface gráfica

from lib import *
import PySimpleGUI as psg

layou_frame = [
    [psg.Radio('Tabuada: ', 'btnRadio1', key='tabuada')],
    [psg.Radio('Fatorial: ', 'grupoRadio1', key='fatorial', default=True)],

]

layout = [
    [psg.Text('Informe um número: '), psg.InputText(key='numero'), psg.Frame('Opções: ', layou_frame)],
    [psg.Text("", key='resultado')],
    [psg.Button('Calcular'), psg.Button('Limpar')],
]

window = psg.Window('Sistema Matemático do Senai', layout)

while True:
    evento, valor = window.read()

    if evento == psg.WIN_CLOSED:
        break
    else:
        if valor['fatorial']:
            num = gera_fatorial(int(valor['numero']))
            window['resultado'].update(f'{valor["numero"]}! = {num}')
        else:
            num = gerar_tabuada(int(valor['numero']))
            window['resultado'].update(f'{valor["numero"]}! = {num}')



window.close()