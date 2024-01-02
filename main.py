class livro():

    def __init__(self, nome, autor, genero):

        self.nome = nome
        self.autor = autor
        self.genero = genero

    def mostrar(self, nome, genero, autor):

        print(f"\nO livro que você escolheu é: {self.nome}, do(a) autor(a) {
              self.autor} e possue o gênero {self.genero}")


class leitor():

    def __init__(self, nome):

        self.nome = nome


biblioteca = {

    1: livro('Harry Potter e a Pedra Filosofal', 'J. K. Rowling', "Fantasia e Aventura"),
    2: livro("Diário de um Banana", 'Jeff Kinney', 'Ficção juvenil'),
    3: livro('A Marca de uma Lágrima', "Pedro Bandeira", 'Infanto-Juvenil'),
    4: livro('Quimica Geral', "Ricardo Feltre", "Educativo"),
    5: livro("Hunter x Hunter  Vol.1", "Yoshiriro Togashi", "Mangá Shounen")
}


nomeUsuario = str(input("Digite o seu nome ao lado: ")).strip().capitalize()


usuario = leitor(nomeUsuario)

escolhaRepeticao = None

listaAlternativas = [0, 1]
listaAlternativasAcaoInicial = [1, 2]

acaoInicial = int(input("Escolha a sua ação:\n\n1 - Acessar livro\n2 - Criar livro\n\nDigite: "))

while acaoInicial not in listaAlternativasAcaoInicial:
    
    acaoInicial = int("Você não digitou algo possível. Escolha a sua ação:\n\n1 - Acessar livro\n2 - Criar livro\n\nDigite: ")
    

if acaoInicial == 1:
    
    while escolhaRepeticao == None or escolhaRepeticao == False:

        numeroDoLivro = int(input(f"Seja bem vindo ao programa {
                        usuario.nome}, Digite o número do seu livro: "))

        while numeroDoLivro > len(biblioteca) or numeroDoLivro < 1:

            numeroDoLivro = int(
            input("Parece que você digitou um valor de livro inexistente. Digite denovo: "))

        escolha = int(input(f"O livro escolhido foi {
                  biblioteca[numeroDoLivro].nome}. Tem certeza? Digite(1 - sim -- 0 - não): "))

        while escolha not in listaAlternativas:

            escolha = int(input(
            "Você digitou uma alternativa errada. Digite denovo(1 - sim -- 0 - não): "))

        if escolha == 0:

            escolhaRepeticao = False
        else:

            escolhaRepeticao = True
            biblioteca[numeroDoLivro].mostrar(
            biblioteca[numeroDoLivro].nome, biblioteca[numeroDoLivro].genero, biblioteca[numeroDoLivro].autor)

            print("\nOk, aqui está o seu livro :)\n")

else:
    
    numeroLivro = int(input("Digite o valor em número(s) inteiro(s) para seu livro ser registrado: "))
    
    while numeroLivro in biblioteca.keys():
        
        numeroLivro = int(input("Parece que esse valor já foi usado. Digite outro valor para seu livro ser registrado: "))
        
    nomeLivro = str(input("Digite o nome do seu livro: "))
    
    autorLivro = str(input("Digite o nome do autor de seu livro: "))
    
    generoLivro = str(input("Digite o gênero textual de seu livro: "))
    
    novoLivro = livro(nomeLivro, autorLivro, generoLivro)
    
    biblioteca[numeroLivro] = novoLivro
    
    print(vars(biblioteca[numeroLivro]))
    
    
    
    
        
        