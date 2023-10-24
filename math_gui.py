# interface gráfica

from lib import gera_fatorial
import PySimpleGUI as psg

layou_frame = [
    [psg.Radio('Tabuada: ', 'grupoRadio1', default=True)],
    [psg.Radio('Fatorial: ', 'grupoRadio1')],

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
        num = gera_fatorial(int(valor['numero']))
        window['resultado'].update(f'{valor["numero"]}! = {num}')

window.close()