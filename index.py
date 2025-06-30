class Grafo():
    def __init__(self):
        self.cidades = []
        self.conexoes = {}

    def cadastra_cidade(self):
        c = input("Digite o nome da cidade: ").lower()
        if not c:
            print("Nome da cidade não pode ser vazio.")
            return False
        for cidade in self.cidades:
            if c.lower() == cidade.nome.lower():
                print("Cidade já cadastrada.")
                return False
        self.cidades.append(Cidade(c))
        self.conexoes[c] = {}
        print(f"Cidade {c} cadastrada com sucesso.")
        return True
    
    def lista_cidade(self):
        if not self.cidades:
            print("Nenhuma cidade cadastrada.")
            return
        else:
            print("Cidades cadastradas:")
            for cidade in sorted(self.cidades, key=lambda c: c.nome.lower()):
                print(cidade.nome)
    
    def cadastra_conexao(self):
        c1 = input("Digite o nome da primeira cidade: ").lower()
        c2 = input("Digite o nome da segunda cidade: ").lower()
        
        if c1 not in self.conexoes or c2 not in self.conexoes:
            print("Uma ou ambas as cidades não estão cadastradas.")
            return False
        
        if c2 in self.conexoes[c1]:
            print(f"Conexão entre {c1} e {c2} já existe.")
            return False

        try:
            distancia = float(input(f"Digite a distância entre {c1} e {c2} (em km): "))
        except ValueError:
            print("Distância inválida.")
            return

        self.conexoes[c1][c2] = distancia
        self.conexoes[c1][c2] = distancia
        print(f"Conexão entre {c1} e {c2} cadastrada com sucesso com distância de {distancia} km.")

    def lista_conexoes(self):
        if not self.conexoes:
            print("Nenhuma conexão cadastrada.")
            return
        print("Conexões cadastradas:")
        for cidade, vizinhos in self.conexoes.items():
            if vizinhos:
                for vizinho, distancia in vizinhos.items():
                    print(f"{cidade} --> {vizinho} (distância: {distancia} km)")
            else:
                print(f"{cidade} não possui conexões.")
    
    def lista_vizinhos(self):
        c = input("Digite o nome da cidade para listar os vizinhos: ").lower()
        if c not in self.conexoes:
            print(f"Cidade {c} não está cadastrada.")
            return
        vizinhos = self.conexoes[c]
        if not vizinhos:
            print(f"Cidade {c} não possui vizinhos.")
        else:
            print(f"Vizinhos de {c}:")
            for vizinho, distancia in vizinhos.items():
                print(f"{vizinho} (distância: {distancia} km)")
    
    
class Cidade():
    def __init__(self, nome):
        self.nome = nome
    

    
if __name__ == "__main__":
    grafo = Grafo()
    n = 1

    while n != 0:
        print("\nMenu:")
        print("1. Cadastrar cidade")
        print("2. Listar cidades")
        print("3. Cadastrar conexão")
        print("4. Listar conexões")
        print("5. Listar vizinhos de uma cidade")
        print("0. Sair")
        
        n = int(input("Escolha uma opção: "))
        
        
        if n == 1:
            grafo.cadastra_cidade()
        elif n == 2:
            grafo.lista_cidade()
        elif n == 3:
            grafo.cadastra_conexao()
        elif n == 4:
            grafo.lista_conexoes()
        elif n == 5:
            grafo.lista_vizinhos()
        elif n == 0:
            print("Saindo do programa.")
            break
        validar = input("Deseja continuar? [s/n]: ")
        if validar == "n":
            print("Programa encerrado!")
            break