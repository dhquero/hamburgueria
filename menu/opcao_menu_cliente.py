from banco.bancodado import BancoDado
from funcao.funcao import escreve_tela, limpa_tela, valida_data, formata_data_americana, formata_data_brasileira
from pedido.pedido import Pedido

def entra_opcao(banco_dado=None, opcao=str(), codigo_cliente=str()):
    if not isinstance(opcao, str):
        return

    limpa_tela()

    if opcao == str("1"):
        inserir_pedido(banco_dado=banco_dado, codigo_cliente=codigo_cliente)
    elif opcao == str("2"):
        alterar_pedido(banco_dado=banco_dado, codigo_cliente=codigo_cliente)
    elif opcao == str("3"):
        consultar_pedido(banco_dado=banco_dado, codigo_cliente=codigo_cliente)
    else:
        escreve_tela("Opcao invalida")

    input()

def inserir_pedido(banco_dado=None, codigo_cliente=str()):
    escreve_tela("INSERIR PEDIDO")
    escreve_tela("")

    observacao = input("OBSERVACAO DO PEDIDO: ")

    if isinstance(observacao, str) and observacao == "":
        observacao = None

    listaHamburguer = []
    while True:
        codigo_hamburguer = input("CODIGO DO HAMBURGUER: ")

        i_codigo_hamburguer = None
        try:
            i_codigo_hamburguer = int(codigo_hamburguer)
        except Exception as e:
            escreve_tela("Erro ao ler codigo do hamburguer. Tente novamente.")
            continue

        quantidade = input("QUANTIDADE: ")

        i_quantidade = None
        try:
            i_quantidade = int(quantidade)
        except Exception as e:
            escreve_tela("Erro ao ler quantidade. Tente novamente.")
            continue

        observacao_item = input("OBSERVACAO DO ITEM: ")

        if isinstance(observacao_item, str) and observacao_item == "":
            observacao_item = None

        listaHamburguer.append({
            "id_hamburguer": i_codigo_hamburguer,
            "quantidade": i_quantidade,
            "observacao": observacao_item
        })

        inserir_mais_hamburguer = None
        while inserir_mais_hamburguer is None or (inserir_mais_hamburguer != "S" and inserir_mais_hamburguer != "N"):
            inserir_mais_hamburguer = input("Adicionar mais hamburguer? (S/N) ")

        if inserir_mais_hamburguer == "N":
            break

    pedido = Pedido(banco_dado=banco_dado)
    id_pedido = pedido.insere_pedido(
        codigo_colaborador=0,
        codigo_cliente=codigo_cliente,
        observacao=observacao,
        status="aberto",
        listaItem=listaHamburguer
    )

    escreve_tela(texto="")
    escreve_tela(texto="Pedido {id_pedido} inserido.".format(id_pedido=id_pedido))

def alterar_pedido(banco_dado=None, codigo_cliente=str()):
    escreve_tela("ALTERAR PEDIDO")
    escreve_tela("")

    codigo_pedido = input("CODIGO DO PEDIDO: ")

    i_codigo_pedido = None
    try:
        i_codigo_pedido = int(codigo_pedido)
    except ValueError as e:
        escreve_tela("Erro ao ler codigo do pedido.")
        return

    pedido = Pedido(banco_dado=banco_dado)

    listaPedido = pedido.busca_dado_pedido(
        codigo_cliente=codigo_cliente,
        codigo_pedido=codigo_pedido
    )

    if (
        listaPedido is None or
        (
            isinstance(listaPedido, list) and
            not len(listaPedido)
        )
    ):
        escreve_tela("Pedido nao encontrado.")
        return

    for item in listaPedido:
        if item.get("status") is not None and isinstance(item.get("status"), str) and item.get("status") != "aberto":
            escreve_tela("O pedido nao pode ser alterado. Status: {status_pedido}".format(status_pedido=item.get("status")))
            return

        escreve_tela(texto="")

        escreve_tela(
            texto=(
                "CODIGO PEDIDO: {codigo_pedido}\n"
                "COLABORADOR: {id_colaborador} - {nome_colaborador}\n"
                "CLIENTE: {id_cliente} - {nome_cliente}\n"
                "DATA: {data_pedido}\n"
                "STATUS: {status}\n"
                "OBSERVACAO: {observacao}\n"
                "ITENS:".format(
                    codigo_pedido=item.get("id"),
                    id_colaborador=item.get("id_colaborador"),
                    nome_colaborador=item.get("cb_nome"),
                    id_cliente=item.get("id_cliente"),
                    nome_cliente=item.get("cl_nome"),
                    data_pedido=formata_data_brasileira(data=item.get("data")),
                    status=item.get("status"),
                    observacao="..." if item.get("observacao") is None else item.get("observacao")
                )
            )
        )

        item_pedido = item.get("item")

        if (
                item_pedido is None or
                (
                        isinstance(item_pedido, list) and
                        not len(item_pedido)
                )
        ):
            escreve_tela(texto="O pedido nao contem itens\n")

        escreve_tela("    CODIGO - HAMBURGUER - QUANTIDADE - OBSERVACAO")
        for itemPedido in item_pedido:
            escreve_tela(
                "    {id_hamburguer} - {nome_hamburguer} - {quantidade} - {observacao}".format(
                    id_hamburguer=itemPedido.get("id_hamburguer"),
                    nome_hamburguer=itemPedido.get("h_nome"),
                    quantidade=itemPedido.get("quantidade"),
                    observacao="..." if itemPedido.get("observacao") is None else itemPedido.get("observacao")
                )
            )

    escreve_tela(texto="")

    escreve_tela(texto="ENTRE COM OS NOVOS DADOS DO PEDIDO")

    observacao = input("OBSERVACAO DO PEDIDO: ")

    if isinstance(observacao, str) and observacao == "":
        observacao = None

    listaHamburguer = []
    while True:
        codigo_hamburguer = input("CODIGO DO HAMBURGUER: ")

        i_codigo_hamburguer = None
        try:
            i_codigo_hamburguer = int(codigo_hamburguer)
        except Exception as e:
            escreve_tela("Erro ao ler codigo do hamburguer. Tente novamente.")
            continue

        quantidade = input("QUANTIDADE: ")

        i_quantidade = None
        try:
            i_quantidade = int(quantidade)
        except Exception as e:
            escreve_tela("Erro ao ler quantidade. Tente novamente.")
            continue

        observacao_item = input("OBSERVACAO DO ITEM: ")

        if isinstance(observacao_item, str) and observacao_item == "":
            observacao_item = None

        listaHamburguer.append({
            "id_hamburguer": i_codigo_hamburguer,
            "quantidade": i_quantidade,
            "observacao": observacao_item
        })

        inserir_mais_hamburguer = None
        while inserir_mais_hamburguer is None or (inserir_mais_hamburguer != "S" and inserir_mais_hamburguer != "N"):
            inserir_mais_hamburguer = input("Adicionar mais hamburguer? (S/N) ")

        if inserir_mais_hamburguer == "N":
            break

    pedido = Pedido(banco_dado=banco_dado)
    pedido.atualiza_pedido(
        codigo_pedido=codigo_pedido,
        codigo_colaborador=0,
        observacao=observacao,
        listaItem=listaHamburguer
    )

    escreve_tela(texto="")
    escreve_tela(texto="Pedido {id_pedido} atualizado.".format(id_pedido=codigo_pedido))

def consultar_pedido(banco_dado=None, codigo_cliente=str()):
    escreve_tela("CONSULTAR PEDIDO(S) POR PERIODO")
    escreve_tela("")

    data_inicial = input("Data inicial (01/01/2019 00:00:00): ")

    if not valida_data(data=data_inicial):
        escreve_tela("Data inicial invalida.")
        return

    data_inicial_americana = formata_data_americana(data_inicial)

    data_final = input("Data final (01/01/2019 23:59:59): ")

    if not valida_data(data=data_final):
        escreve_tela("Data final invalida.")
        return

    data_final_americana = formata_data_americana(data_final)

    pedido = Pedido(banco_dado=banco_dado)

    listaPedido = pedido.consulta_pedido_periodo(
        codigo_cliente=codigo_cliente,
        data_inicial=data_inicial_americana,
        data_final=data_final_americana
    )

    escreve_tela(texto="")

    if (
        listaPedido is None or (
            isinstance(listaPedido, list) and
            not len(listaPedido)
        )
    ):
        escreve_tela("O periodo selecionado nao possui registros")

    for item in listaPedido:
        escreve_tela(
            texto=(
                "CODIGO PEDIDO: {codigo_pedido}\n"
                "COLABORADOR: {id_colaborador} - {nome_colaborador}\n"
                "CLIENTE: {id_cliente} - {nome_cliente}\n"
                "DATA: {data_pedido}\n"
                "STATUS: {status}\n"
                "OBSERVACAO: {observacao}\n"
                "ITENS:".format(
                    codigo_pedido=item.get("id"),
                    id_colaborador=item.get("id_colaborador"),
                    nome_colaborador=item.get("cb_nome"),
                    id_cliente=item.get("id_cliente"),
                    nome_cliente=item.get("cl_nome"),
                    data_pedido=formata_data_brasileira(data=item.get("data")),
                    status=item.get("status"),
                    observacao="..." if item.get("observacao") is None else item.get("observacao")
                )
            )
        )

        item_pedido = item.get("item")

        if (
                item_pedido is None or
            (
                isinstance(item_pedido, list) and
                not len(item_pedido)
            )
        ):
            escreve_tela(texto="O pedido nao contem itens\n")
            continue

        escreve_tela("    CODIGO - HAMBURGUER - QUANTIDADE - OBSERVACAO")
        for itemPedido in item_pedido:
            escreve_tela(
                "    {id_hamburguer} - {nome_hamburguer} - {quantidade} - {observacao}".format(
                    id_hamburguer=itemPedido.get("id_hamburguer"),
                    nome_hamburguer=itemPedido.get("h_nome"),
                    quantidade=itemPedido.get("quantidade"),
                    observacao="..." if itemPedido.get("observacao") is None else itemPedido.get("observacao")
                )
            )

        escreve_tela(texto="")
