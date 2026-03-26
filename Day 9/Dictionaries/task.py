programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

# print(programming_dictionary["Bug"])

# Add values
programming_dictionary["Loop"] = "The action..."
# print(programming_dictionary)

empty_dictionary = {}
# ele tambem limpa um dicionario que ja existe se executar

# editar
programming_dictionary["Bug"] = "Bla"

# loop
for key in programming_dictionary:
    print(key) #ele retorna aqui apenas a chave
    print(programming_dictionary[key]) # retona apenas o valor dos valores das chaves