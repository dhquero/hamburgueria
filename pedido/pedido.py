import datetime

from banco.bancodado import BancoDado
from pedido.itempedido import ItemPedido

class Pedido:
    banco_dado = None

    def __init__(self, banco_dado=None):
        self.banco_dado = banco_dado

    def insere_pedido(self, codigo_colaborador=0, codigo_cliente=0, observacao=str(), status=str(), listaItem=[]):
        id_pedido = self.banco_dado.insere_dado(
            pesquisa=(
                "INSERT INTO pedido (id_colaborador, id_cliente, observacao, status) "
                "VALUES (%s, %s, %s, %s);"
            ),
            parametro=(codigo_colaborador, codigo_cliente, observacao, status)
        )

        if listaItem is not None and len(listaItem):
            for itemListaPedido in listaItem:
                self.banco_dado.insere_dado(
                    pesquisa=(
                        "INSERT INTO item_pedido (id_pedido, id_hamburguer, quantidade, observacao) "
                        "VALUES (%s, %s, %s, %s);"
                    ),
                    parametro=(
                        id_pedido,
                        itemListaPedido.get("id_hamburguer"),
                        itemListaPedido.get("quantidade"),
                        itemListaPedido.get("observacao")
                    )
                )

        return id_pedido

    def atualiza_pedido(
            self,
            codigo_pedido=0,
            codigo_colaborador=0,
            observacao=str(),
            listaItem=[]
    ):
        self.banco_dado.atualiza_dado(
            pesquisa=(
                "UPDATE pedido SET id_colaborador = %s, observacao = %s WHERE id = %s;"
            ),
            parametro=(codigo_colaborador, observacao, codigo_pedido)
        )

        self.banco_dado.exclui_dado(
            pesquisa=(
                "DELETE FROM item_pedido WHERE id_pedido = %s;"
            ),
            parametro=(codigo_pedido,)
        )

        if listaItem is not None and len(listaItem):
            for itemListaPedido in listaItem:
                self.banco_dado.insere_dado(
                    pesquisa=(
                        "INSERT INTO item_pedido (id_pedido, id_hamburguer, quantidade, observacao) "
                        "VALUES (%s, %s, %s, %s);"
                    ),
                    parametro=(
                        codigo_pedido,
                        itemListaPedido.get("id_hamburguer"),
                        itemListaPedido.get("quantidade"),
                        itemListaPedido.get("observacao")
                    )
                )

    def busca_dado_pedido(self, codigo_cliente=0, codigo_pedido=0):
        lista_pedido = self.banco_dado.busca_dado(
            pesquisa=(
                "SELECT p.id AS id, p.id_colaborador AS id_colaborador, p.id_cliente AS id_cliente, "
                "p.data AS data, p.status AS status, p.observacao AS observacao, cb.nome AS cb_nome, "
                "cl.nome AS cl_nome "
                "FROM pedido p "
                "LEFT JOIN colaborador cb ON (cb.id = p.id_colaborador) "
                "INNER JOIN cliente cl ON (cl.id = p.id_cliente) "
                "WHERE p.id_cliente = %s AND p.id = %s "
                "ORDER BY p.id ASC;"
            ),
            parametro=(codigo_cliente, codigo_pedido,)
        )

        for item in lista_pedido:
            itemPedido = ItemPedido(banco_dado=self.banco_dado)

            listaItem = itemPedido.consulta_item_pedido(codigo_pedido=item.get("id"))

            item.update({"item": listaItem})

        return lista_pedido

    def consulta_pedido_periodo(self, codigo_cliente=0, data_inicial=datetime.datetime.now(), data_final=datetime.datetime.now()):
        lista_pedido = self.banco_dado.busca_dado(
            pesquisa=(
                "SELECT p.id AS id, p.id_colaborador AS id_colaborador, p.id_cliente AS id_cliente, "
                "p.data AS data, p.status AS status, p.observacao AS observacao, cb.nome AS cb_nome, "
                "cl.nome AS cl_nome "
                "FROM pedido p "
                "LEFT JOIN colaborador cb ON (cb.id = p.id_colaborador) "
                "INNER JOIN cliente cl ON (cl.id = p.id_cliente) "
                "WHERE p.id_cliente = %s AND p.data BETWEEN %s AND %s "
                "ORDER BY p.id ASC;"
            ),
            parametro=(codigo_cliente, data_inicial, data_final,)
        )

        for item in lista_pedido:
            itemPedido = ItemPedido(banco_dado=self.banco_dado)

            listaItem = itemPedido.consulta_item_pedido(codigo_pedido=item.get("id"))

            item.update({"item":listaItem})

        return lista_pedido