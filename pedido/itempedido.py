from banco.bancodado import BancoDado

class ItemPedido:
    banco_dado = None

    def __init__(self, banco_dado=None):
        self.banco_dado = banco_dado

    def consulta_item_pedido(self, codigo_pedido=0):
        if not isinstance(codigo_pedido, int):
            return None

        lista = self.banco_dado.busca_dado(
            pesquisa=(
                "SELECT ip.id_hamburguer AS id_hamburguer, h.nome AS h_nome, ip.quantidade AS quantidade, "
                "observacao AS observacao "
                "FROM item_pedido ip "
                "INNER JOIN hamburguer h ON (h.id = ip.id_hamburguer) "
                "WHERE id_pedido = %s;"
            ),
            parametro=(codigo_pedido,)
        )

        return lista
