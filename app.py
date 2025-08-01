from Modelos.restaurante import Restaurante

restaurante_praca = Restaurante("praça", "Gourmet")
restaurante_mexicano = Restaurante("Mexican Food", "Mexicana")
restaurante_freddy = Restaurante("Freddy`s Pizza", "Pizzaria")
restaurante_freddy.receber_avaliacao('Chris', 7)
restaurante_freddy.receber_avaliacao('Rafa', 10)
restaurante_freddy.receber_avaliacao('Rodrigo', 8)



def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__': 
    main()