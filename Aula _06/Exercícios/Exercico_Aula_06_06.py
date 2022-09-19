#Seja criativo ao desenvolver este programa:
#a. Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.
#b. Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome personalizado.
#c. Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos convites. Imprima o nome das pessoas que não poderão comparecer.
#d. Modifique sua lista, substitua os desistentes por novos convidados.
#e. Exiba um novo convite para cada pessoa que continua presente em sua lista.

convidados = ['Ewan McGregor','Ian McKellen','Mark Hamill','Meryl Streep','Bruce Dickinson'] 

for nome in convidados:
    print(f"Caro(a) {nome}, venho por meio deste lhe convidar para um jantar em minha residência às 20:00 horas do dia 1 de outubro.")  

print("Meryl Streep não poderão ir ao jantar") 

convidados_nova = ['Ewan McGregor','Ian McKellen','Mark Hamill','Kaley Cuoco','Bruce Dickinson'] 

for nome in convidados_nova:
    print(f"Caro(a){nome}, venho por meio deste lhe convidar para um jantar em minha residência às 20:00 horas do dia 1 de outubro.")