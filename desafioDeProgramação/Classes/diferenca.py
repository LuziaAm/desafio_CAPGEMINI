class Diferenca:
    # Dado um vetor de inteiros n e um inteiro qualquer x. Construa um algoritmo que determine o número de elementos pares do vetor que tem uma diferença igual ao valor de x.

    def diferenca(lista, x):
        # Ordena de forma reversa
        lista.sort(reverse=True)
        # Contador para saber quantos vetrores tem a diferença = x.
        cont = 0
        vet2 = []
        for i in range(len(lista)):
            for j in range(len(lista)):
                # Váriavel para saber a diferença entre os dois valores do vetor
                diferenca = lista[i] - lista[j]
                # Caso  a diferença seja igual a x
                if diferenca == x:
                    vet2.append([lista[i], lista[j]])
                    cont += 1
        #return vet2
        return cont




