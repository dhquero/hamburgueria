from funcao.funcao import formata_data_americana

from banco.bancodado import BancoDado
from cliente.cliente import Cliente
from funcao.funcao import escreve_tela, limpa_tela
from menu.opcao_menu_cliente import entra_opcao

banco_dado = BancoDado()

#entra_opcao(banco_dado=banco_dado, opcao="3", codigo_cliente="1")

#exit()

limpa_tela()

codigo_cliente = input("Digite seu codigo de cliente: ")

i_codigo_cliente = None

try:
    i_codigo_cliente = int(codigo_cliente)
except ValueError:
    escreve_tela("Erro ao entrar com o codigo do cliente.")
    exit(0)

cliente = Cliente(banco_dado=banco_dado)
lista_cliente = cliente.dado_cliente(codigo=i_codigo_cliente)

if lista_cliente is None or (isinstance(lista_cliente, list) and not len(lista_cliente)):
    escreve_tela("Codigo do cliente inexistente.")
    exit(0)

dado_cliente = lista_cliente[0] if (isinstance(lista_cliente, list) and len(lista_cliente)) else {}

if dado_cliente is None or not isinstance(dado_cliente, dict):
    escreve_tela("Codigo do cliente invalido.")
    exit(0)

limpa_tela()

opcao_menu = str()

while True:
    escreve_tela("Cliente: {codigo} - {nome}".format(codigo=dado_cliente.get("id"), nome=dado_cliente.get("nome")))
    escreve_tela("")
    escreve_tela("Selecione a opcao:")
    escreve_tela("1 - Inserir pedido")
    escreve_tela("2 - Alterar pedido")
    escreve_tela("3 - Consultar pedido")
    escreve_tela("S - Sair")
    escreve_tela("")

    opcao_menu = input("Entre com a opcao do menu: ")

    if isinstance(opcao_menu, str) and opcao_menu == str("S"):
        break

    entra_opcao(banco_dado=banco_dado, opcao=opcao_menu, codigo_cliente=codigo_cliente)

    limpa_tela()

limpa_tela()
