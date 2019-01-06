import datetime
from os import system, name
import re

def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def escreve_tela(texto=str()):
    if not isinstance(texto, str):
        return

    print(texto, flush=True)

def valida_data(data=str()):
    if not isinstance(data, str):
        return False

    try:
        padrao = re.compile(r"(\d{2})(/)(\d{2})(/)(\d{4})( )(\d{2})(:)(\d{2})(:)(\d{2})")
        validacao = padrao.fullmatch(data)
        return True if validacao else False
    except re.error:
        return False

def formata_data_americana(data=str()):
    if not isinstance(data, str):
        return False

    data_brasileira = datetime.datetime.strptime(data, "%d/%m/%Y %H:%M:%S")

    return data_brasileira.strftime("%Y-%m-%d %H:%M:%S")

def formata_data_brasileira(data=datetime.datetime.now()):
    if not isinstance(data, datetime.datetime):
        return False

    return data.strftime("%d/%m/%Y %H:%M:%S")
