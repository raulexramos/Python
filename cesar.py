alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
chave = 3

# Mensagem a ser criptografada
mensagem = "raulex esta mensagem será criptografada."
n = len(alfabeto)

cifrada = ""
for letra in mensagem:
    indice = alfabeto.index(letra)
    nova_letra = alfabeto[(indice + chave)%n]
    
    cifrada = cifrada + nova_letra
    
print(mensagem)
print(cifrada)
