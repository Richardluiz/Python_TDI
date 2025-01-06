## Lists e Tuples ##

alvos = ["192.168.1.10",
"192.168.1.20", "192.168.1.30", "192.168.1.40"]

print(alvos[3])
print(alvos[0:2])

#Ler uma lista (acessar)

a = alvos[0]
print(a)

#Adicionar um elemento a lista

alvos.append("tdi")
alvos.append(10)
print(alvos)

alvos.insert(0, "Inicio") # Inserir no começo da lista

#Remover
alvos.remove("192.168.1.10")
print(alvos)

#Remove o último elemento da lista
ultimo = alvos.pop()
print(alvos)
print(ultimo)

#Consultar uma lista

print(len(alvos))

print("#########")
print("192,168.1.20" in alvos)

#Tuple
portas = (80 , 22, 21)  # Nunca vai poder adicionar e deletar um elemento na lista
