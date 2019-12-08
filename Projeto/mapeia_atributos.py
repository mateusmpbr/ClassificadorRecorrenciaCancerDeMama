with open('bd_dedutivo/nova_coluna/bd_dedutivo_inteiro_python_novaColuna.txt','r') as f:
    valor_total = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0],
        [0, 0, 0],
        [0, 0],
        [0, 0, 0, 0, 0],
        [0, 0]
    ]

    valor_nao_recorrencia = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0],
        [0, 0, 0],
        [0, 0],
        [0, 0, 0, 0, 0],
        [0, 0]
    ]

    valor_recorrencia = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0],
        [0, 0, 0],
        [0, 0],
        [0, 0, 0, 0, 0],
        [0, 0]
    ]

    teste_recorrencia_certo = 0
    teste_recorrencia_errado = 0
    teste_nao_recorrencia_certo = 0
    teste_nao_recorrencia_errado = 0

    for index_line, line in enumerate(f):
        atributos = line.strip().split(',')
        for index_atributo, atributo in enumerate(atributos):
            if (index_atributo == len(atributos) - 1):
                break

            atributo_aux = int(atributo) - 1

            valor_total[index_atributo][atributo_aux] += 1
            # print("recorrente?",atributos[-1])
            if(atributos[-1] == '0'):
                valor_nao_recorrencia[index_atributo][atributo_aux] += 1
            else:
                valor_recorrencia[index_atributo][atributo_aux] += 1

        if(atributos[-2] == '2' or atributos[-5] == '1'):
            if(atributos[-1] == '0'):
                teste_nao_recorrencia_certo+=1
            else:
                teste_recorrencia_errado+=1
        else:
            if(atributos[-1] == '1'):
                teste_recorrencia_certo+=1
            else:
                teste_nao_recorrencia_errado+=1

    nome_atributos = ['idade', 'menopausa', 'tamanho do tumor', 'inv-nodes',
                      'node-caps', 'deg-malig', 'mama', 'breast-quad', 'irradiada']

    for i in range(9):
        print('-----', nome_atributos[i], '-----')
        print("VALOR TOTAL:", valor_total[i])
        print("VALOR RECORRENCIA", valor_recorrencia[i])
        print("VALOR NAO RECORRENCIA", valor_nao_recorrencia[i])
    
    print('------------------------------')
    print("TESTE RECORRENCIA CERTO", teste_recorrencia_certo)
    print("TESTE RECORRENCIA ERRADO", teste_recorrencia_errado)
    print("TESTE NAO RECORRENCIA CERTO", teste_nao_recorrencia_certo)
    print("TESTE NAO RECORRENCIA ERRADO", teste_nao_recorrencia_errado)
