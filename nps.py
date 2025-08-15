class NPS:
    def __init__(self):
        self.notas = []
    
    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
        else:
            print("A nota precisa ser um valor entre 0 e 10")

    def calculator_nps(self):
        detratores = [n for n in self.notas if n <= 6]
        promotores = [n for n in self.notas if n >= 9]

        percentual_detratores = (len(detratores)) / (len(self.notas)) * 100
        percentual_promotores = (len(promotores)) / (len(self.notas)) * 100

        nps = percentual_detratores - percentual_promotores
        return nps
    
    def avaliar_classificacao(self): 
        nps = self.calculator_nps()

        if nps < 0:
            print("Zona crítica")
        elif nps < 50:
            print("Zona neutra (Razoável)")
        elif nps < 75:
            print("Zona de qualidade (Muito Bom)")
        else: 
            print("Zona de excelência (Excelente)")

if __name__ == '__main__':
    pesquisa_NPS = NPS()

    print("----- Pesquisa de satisfação -----")
    print("Digite 'sair' para encerrar.\n")

    while True:
        nota = input("Em uma escala de 0 a 10, o quanto você recomendaria nossa empresa? ")

        if nota.lower() == 'sair':
            break

        if nota.isdigit():
            pesquisa_NPS.adicionar_nota(int(nota))
        else:
            print("Digite apenas números entre 0 e 10 ou 'sair' para encerrar.")

    print("\nNotas registradas:", pesquisa_NPS.notas)
    pesquisa_NPS.avaliar_classificacao()