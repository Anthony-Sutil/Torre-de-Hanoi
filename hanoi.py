def torre_hanoi(n, origem, destino, auxiliar):  # Função para resolver o problema da Torre de Hanoi com 'n' discos da 'origem' para o 'destino' usando 'auxiliar'.
    if n == 1:  # Caso base: se houver apenas um disco para mover, imprime o movimento e retorna 1 movimento.
        print(f"Mova o disco 1 de {origem} para {destino}")  # Imprime o movimento do enésimo disco da 'origem' para o 'destino'.
        return 1 
    else:  # Caso recursivo
        movimentos = 0  # Inicializa o número total de movimentos.
        movimentos += torre_hanoi(n-1, origem, auxiliar, destino)  # Move n-1 discos da 'origem' para 'auxiliar' usando 'destino'.
        print(f"Mova o disco {n} de {origem} para {destino}")  # Imprime o movimento do enésimo disco da 'origem' para o 'destino'.
        movimentos += 1  # Incrementa o total de movimentos em 1 para este movimento.
        movimentos += torre_hanoi(n-1, auxiliar, destino, origem)  # Move os n-1 discos da 'auxiliar' para o 'destino' usando 'origem'.
        return movimentos  # Retorna o número total de movimentos feitos.
n =7 # Quantidade de discos
total_movimentos = torre_hanoi(n, 'A', 'C', 'B') # Chama a função para resolver o problema da Torre de Hanoi
print(f"Total de movimentos realizados: {total_movimentos}") # Imprime o número total de movimentos