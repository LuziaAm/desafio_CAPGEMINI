class Criptografia:

    def criptografia(string):
        import math

        string_concat = string.replace(" ","")
        len_str = len(string_concat)
        col = math.ceil((math.sqrt(len_str)))

        # Vetor para receber as linhas
        mat = []
        # Variável para percorrer o vetor
        pos = 0

        for l in range(col):
            linha = []
            for c in range(col):
                if pos < len_str:
                    linha.append(string_concat[pos])
                else:
                    linha.append('')
                pos += 1
            mat.append(linha)

        cript = ''
        cont_col = 0
        for l in range(col):
            for c in range(col):
                if mat[c][l] != '':
                    cript += mat[c][l]
                    cont_col+=1
                elif mat[c][l] == '' and cont_col == len_str:
                    return cript
                    break
            cript += ' '

        return cript
