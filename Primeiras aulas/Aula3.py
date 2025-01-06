#Dicionário (Dicts)

alvo = {
    'ip': '192.168.1.1',
    'so': "windows",
    'ativo': True,
    'portas': [80, 22, 21],
}

print(alvo["so"])
print(alvo["ativo"])

#Adicionar ou atualizar uma chave e valor
print(alvo)
alvo["so"] = "linux"
print(alvo)

#deletar
del alvo["so"]
print(alvo)

#ler
print(alvo.values())
print(alvo.keys()) # Somente as chaves