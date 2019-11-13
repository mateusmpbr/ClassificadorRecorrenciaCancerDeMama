with open('bd_dedutivo_inteiro_python.txt','r') as f:
    valor_total = [
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0],
                    [0,0,0],
                    [0,0],
                    [0,0,0,0,0],
                    [0,0]
                ]
    
    valor_nao_recorrencia = [
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0],
                    [0,0,0],
                    [0,0],
                    [0,0,0,0,0],
                    [0,0]
                ]

    for index_line, line in enumerate(f):
        atributos = line.strip().split(',')
        for index_atributo, atributo in enumerate(atributos):
            atributo_aux = int(atributo) - 1
            # print("INDEX: " + str(index) + " ATRIBUTO: " + str(atributo_aux))
            valor_total[index_atributo][atributo_aux]+=1

            if(index_line <= 196):
                valor_nao_recorrencia[index_atributo][atributo_aux]+=1

    print("VALOR TOTAL:",valor_total)
    print("VALOR NAO RECORRENCIA",valor_nao_recorrencia)