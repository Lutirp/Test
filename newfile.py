print("Seja bem-vindo ao MultiApp")

nome = input("Digite seu nome: ")
genero = input("Gênero: ").lower()
idade = input("Idade: ")

# Nome
if nome == "":
    nome = "não informado"
elif not nome.replace(" ", "").isalpha():
    nome = "inválido"

# Gênero
if genero == "":
    genero = "não informado"
elif not genero.replace(" ", "").isalpha():
    genero = "inválido"

# Idade
if idade.isdigit():
    idade = int(idade)

    if idade < 12:
        categoria = "criança"
    elif idade < 18:
        categoria = "adolescente"
    elif idade < 60:
        categoria = "adulto"
    else:
        categoria = "idoso"
else:
    categoria = "desconhecida"
    idade = "não informada"

print(f"Olá, {nome}! Pelo visto temos um(a) {categoria} de {idade} anos do gênero {genero}.")