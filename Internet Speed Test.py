import speedtest
from PySimpleGUI import PySimpleGUI as sg
import sys
import pyttsx3
import webbrowser


def iafala(comando):
    engine = pyttsx3.init()
    engine.say(comando)
    engine.runAndWait()


teste = speedtest.Speedtest()




with open('Download.dll', "w") as bla:
    blabla = bla.write('')

with open('upload.dll', "w") as blablabla:
    blablablabla = blablabla.write('')



while True:
    with open('download.dll', "r") as sla:
        velocidade_download = sla.read()

    with open('upload.dll', "r") as slaa:
        velocidade_upload = slaa.read()




    sg.theme('Reddit')

    layout = [
        [sg.Text('Bem-vindo ao teste de velocidade de internet.')],
        [sg.Button('--- Iniciar Teste ---', border_width= 0), sg.Button('Fechar Teste', border_width= 0), sg.Button('Créditos', border_width= 0) ],
        [sg.Text(f'resultado do download: {velocidade_download} MB (MegaBytes)')],
        [sg.Text(f'resultado do upload: {velocidade_upload} MB (MegaBytes)')],
        [sg.Text(f'resultado do ping: {teste.results.ping} ms (Milissegundos)')],

    ]

    janela = sg.Window('Internet Speed Test', layout, font='Sans', use_custom_titlebar= True, titlebar_icon= 'Wi-Fi Icon.png',  )

    while True:
        eventos, valores = janela.read()

        if eventos == '--- Iniciar Teste ---':

            iafala('Testando Velocidade De Download...')
            velo_download = teste.download()
            with open('download.dll', "w") as download:
                dodownload = download.write(f'{velo_download / 10**6:.2f}')

            # Upload
            iafala('testando velocidade de upload...')
            velo_upload = teste.upload()
            with open('upload.dll', "w") as upload:
                upupload = upload.write(f'{velo_upload / 10**6:.2f}')
            
            
            janela.close()
            janela.read()

        if eventos == sg.WINDOW_CLOSED:
            break

        if eventos == 'Fechar Teste':
            sys.exit()
        
        if eventos == 'Créditos':
            webbrowser.open('https://www.youtube.com/channel/UCCDHZbCirMnOeAyWcaUan6Q')
            webbrowser.open('https://github.com/Lumazini')
