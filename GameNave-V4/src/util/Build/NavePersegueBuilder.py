from GameNave4.src.util.Build import NaveBuilder
from GameNave4.src.util.FabricaNaves import FabricaNavePersegue
from GameNave4.src.cgd import Path


class NavePersegueBuilder(NaveBuilder.NaveBuilder):
    def __init__(self):
        super(NavePersegueBuilder, self).__init__()
        self.build_dano()
        self.build_imagem_nave()
        self.build_imagem_explosao()
        self.build_som()
        self.build_nave()

    def build_dano(self):
        self.nave_product.set_dano(0)

    def build_imagem_nave(self):
        self.nave_product.imagem_nave = Path.get_path() + "/Imagem/Nave/Persegue.png"

    def build_imagem_explosao(self):
        self.nave_product.imagem_explosao = Path.get_path() + "/Imagem/Nave/Boss.png"

    def build_som(self):
        self.nave_product.som = Path.get_path() + "/Som/MusicNave.wav"

    def build_nave(self):
        self.nave_product.nave_fabrica = FabricaNavePersegue.FabricaNavePersegue(self.nave_product.imagem_nave,
                                                                                 self.nave_product.imagem_explosao,
                                                                                 self.nave_product.som)