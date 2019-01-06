from banco.bancodado import BancoDado

class Cliente:
    banco_dado = None

    def __init__(self, banco_dado=None):
        self.banco_dado = banco_dado

    def dado_cliente(self, codigo=0):
        if not isinstance(codigo, int):
            return None

        lista = self.banco_dado.busca_dado(
            pesquisa=(
                "SELECT id, nome "
                "FROM cliente c "
                "WHERE id = %s;"
            ),
            parametro=(codigo,)
        )

        return lista