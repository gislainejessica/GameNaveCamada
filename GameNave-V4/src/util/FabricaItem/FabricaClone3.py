from GameNave4.src.util.FabricaItem import FabricaClone
from GameNave4.src.cgd import Path


class FabricaClone3(FabricaClone):
    def __init__(self):
        super(FabricaClone3, self).__init__(Path.get_path() + "Imagem/Item/Clone3.png")
