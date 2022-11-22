# Progressão geométrica agora!

print("="*50)
print("            PROGRESSÃO GEOMÉTRICA!!!\n")
razao = int(input("Digite a razão da progressão geométrica: "))
primeiro = int(input("Digite o primeiro termo para iniciar a progressão: "))
print("\n")
print(f"Razão = {razao}\nPrimeiro termo = {primeiro}")
n = 1
proximo = primeiro
for contador in range (primeiro, primeiro + 10):
    print(f"{n}) {proximo}")
    proximo *= razao
    n += 1
print("Estes são os 10 primeiros termos desta progressão geométrica!")
