from GameNave4.src.util.FabricaItem import FabricaMunicao
from GameNave4.src.cgd import Path


class FabricaMunicao3(FabricaMunicao):
    def __init__(self):
        super(FabricaMunicao3, self).__init__(Path.get_path() + "Imagem/Item/Municao3.png", 200, 10)
