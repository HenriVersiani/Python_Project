arquivo = "frutas.txt"
frutas_precos = []
somaPrecos = 0
passouMedia = []

with open(arquivo, "r") as file:
    for linha in file:
        fruta, preco = linha.strip().split(",")
        frutas_precos.append({"fruta": fruta, "preco": float(preco)})
    print(frutas_precos)

for item in frutas_precos:
    somaPrecos += item["preco"]

def mediaPreco(somaPrecos):   
    return somaPrecos / len(frutas_precos)  

def verificarPassouMedia():
    for item in frutas_precos:
        media = mediaPreco(somaPrecos)
        if item["preco"] > media:
            passouMedia.append({"fruta": item["fruta"], "preco": item["preco"]})
          
        if item["preco"] < media:
            print("Esse não passou!")       


verificarPassouMedia()

print("Frutas acima da média:",passouMedia)

with open("frutas_vazio.txt", "w") as file:
    for item in passouMedia:
        file.write(f"{item['fruta']}, {item['preco']}\n")