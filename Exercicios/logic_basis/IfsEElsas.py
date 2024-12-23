nome = input("Escreve o teu nome: ")
tamanho_do_teu_nome = len(nome)

if tamanho_do_teu_nome > 4:
    print("O teu nome tem 5 ou mais carateres")
elif tamanho_do_teu_nome < 10:
    print("O teu nome tem menos de 10 carateres")
else:
    print("O teu nome é mta comprido")

print("-----------------------------------")

if tamanho_do_teu_nome > 4:
    print("O teu nome tem 5 ou mais carateres")
if tamanho_do_teu_nome < 10:
    print("O teu nome tem menos de 10 carateres")

#Descobrir o que está mal com este código