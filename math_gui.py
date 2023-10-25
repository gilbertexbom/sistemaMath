# interface gráfica

from lib import *
import PySimpleGUI as psg

layou_frame = [
    [psg.Radio('Tabuada', 'btnRadio1', key='tabuada')],
    [psg.Radio('Fatorial', 'btnRadio1', key='fatorial', default=True)],
]

layout = [
    [psg.Text('Informe um número: '), psg.InputText(key='numero'), psg.Frame('Opções: ', layou_frame)],
    [psg.Text("", key='resultado')],
    [psg.Output(size=(12,6), key='resultado2')],
    [psg.Button('Calcular'), psg.Button('Limpar')],
]

window = psg.Window('Sistema Matemático do Senai', layout)

while True:
    evento, valor = window.read()

    if evento == psg.WIN_CLOSED:
        break
    elif evento == 'Limpar':
        # psg.popup('Limpar a tela!')
        window['fatorial'].update(True) # Radio
        window['resultado'].update('') # Text
        window['numero'].update('') # InputText
        window['resultado2'].update('') # Output
    else:
        if valor['fatorial']:
            num = gera_fatorial(int(valor['numero']))
            window['resultado'].update(f'{valor["numero"]}! = {num}')
        else:
            window['resultado2'].update(gerar_tabuada(int(valor['numero'])))



window.close()