from nps import NPS

pesquisa_NPS = NPS()

print("----- Pesquisa de satisfação-----")
print("Digite 'sair' para encerrar. ")

while True:
    nota = input("Em uma escala de 0 a 10, o quanto você recomendaria nossa empresa?")

    if nota.lower() == 'sair':
        break

    # Validação
    if nota.isdigit():
        nota = int(nota)
        pesquisa_NPS.adicionar_nota(nota)
    else:
        print("Digite apenas números entre 0 e 10 ou 'sair' para encerrar.")


print("\nNotas registradas:", pesquisa_NPS.notas)
print(f"NPS calculado: {pesquisa_NPS.calcular_nps():.2f}")
pesquisa_NPS.avaliar_classificacao()