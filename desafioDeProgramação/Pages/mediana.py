class CalMediana:
    def mediana(lista):
        # Ordena a lista
        arr_sort = sorted(lista)

        # Tamanho da lista
        qtd = len(lista)

        # Se número ímpar
        if qtd % 2 == 1:
            vlr_para_mediana = qtd - 1
            div_para_mediana = int(vlr_para_mediana / 2)
            mediana = div_para_mediana
            # print('Mediana = ',arr_sort[mediana])
            return arr_sort[mediana]
        # Se número par
        elif qtd % 2 == 0:
            vlr_para_mediana = qtd - 2
            div_para_mediana = int(vlr_para_mediana / 2)
            mediana_central1 = arr_sort[div_para_mediana]
            mediana_central2 = arr_sort[div_para_mediana + 1]
            media_aritmetica = (mediana_central1 + mediana_central2) / 2
            #print('Mediana = ',media_aritmetica)
            return media_aritmetica