from Modelos.avaliacao import Avaliacao

class Restaurante :
    restaurantes = []

    def __init__(self, nome, categoria):
        # __init__ -> Construtor 
        # Todo objeto é automaticamente direcionado a ele
         
        self.nome = nome.title()
        self.categoria = categoria.title() # upper()
        self._ativo = False # _ativo -> Imutavel | Não deve mexer
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        # __str__ -> Construtor
        # Muda a saída de um Objeto para uma string     

        return f'{self.nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status".ljust(25)}')
        print("-" * 63)
        for restaurante in cls.restaurantes:
            print(f"{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo.ljust(25)}")
    
    @property # Transforma um metodo em atributo
    def ativo(self) :
        return "✅" if self._ativo else "❎"
    
    def alternar_estado(self):
        self._ativo = not self._ativo
    
    def receber_avaliacao(self, cliente, nota): 
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacao :
            return 'Não há avaliações'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
#add
