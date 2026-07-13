print ("Seja bem-vindo ao MultiApp")
nome = input ("Digite seu nome: ")
genero = input ("Gênero: " )

idade = int(input("Idade: "))

if idade < 12:
    categoria = "criança"
elif idade < 18:
    categoria = "adolescente"
elif idade < 60:
    categoria = "adulto"
else:
    categoria = "idoso"

print(f"Olá, {nome}! Pelo visto temos um(a) {categoria} de {idade} anos do gênero {genero}.")