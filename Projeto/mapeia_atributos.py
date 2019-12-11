with open('bd_dedutivo/nova_coluna/bd_dedutivo_inteiro_python_coluna_r_nr.txt','r') as f:
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

    recorrencias_classificadas_corretamente = 0
    recorrencias_classificadas_como_nao_recorrencias = 0
    nao_recorrencias_classificadas_corretamente = 0
    nao_recorrencias_classificadas_como_recorrencias = 0

    for index_line, line in enumerate(f):
        atributos = line.strip().split(',')
        for index_atributo, atributo in enumerate(atributos):
            if (index_atributo == len(atributos) - 1):
                break

            atributo_aux = int(atributo) - 1

            valor_total[index_atributo][atributo_aux] += 1
            # atributos[-1] == 0 -> nao_recorrente
            if(atributos[-1] == '0'):
                valor_nao_recorrencia[index_atributo][atributo_aux] += 1
            else:
                valor_recorrencia[index_atributo][atributo_aux] += 1

        # atributos[-2] == 2 -> irradiada == no
        # atributos[-5] != 3 -> deg-malig != 3
        if(atributos[5] != '3' and atributos[8] == '2'):
            if(atributos[-1] == '0'):
                nao_recorrencias_classificadas_corretamente+=1
            else:
                recorrencias_classificadas_como_nao_recorrencias+=1
        else:
            if(atributos[-1] == '1'):
                recorrencias_classificadas_corretamente+=1
            else:
                nao_recorrencias_classificadas_como_recorrencias+=1

    nome_atributos = ['idade', 'menopausa', 'tamanho do tumor', 'inv-nodes',
                      'node-caps', 'deg-malig', 'mama', 'breast-quad', 'irradiada']

    for i in range(9):
        print('-----', nome_atributos[i], '-----')
        print("VALOR TOTAL:", valor_total[i])
        print("VALOR RECORRENCIA:", valor_recorrencia[i])
        print("VALOR NAO RECORRENCIA:", valor_nao_recorrencia[i])
    
    print('------------------------------')
    print("RECORRENCIAS CLASSIFICADAS CORRETAMENTE:", recorrencias_classificadas_corretamente)
    print("RECORRENCIAS CLASSIFICADAS COMO NAO RECORRENCIAS:", recorrencias_classificadas_como_nao_recorrencias)
    print("PORCENTAGEM DE RECORRENCIAS CLASSIFICADAS CORRETAMENTE:", recorrencias_classificadas_corretamente/(recorrencias_classificadas_corretamente + recorrencias_classificadas_como_nao_recorrencias))
    print("NAO RECORRENCIAS CLASSIFICADAS CORRETAMENTE:", nao_recorrencias_classificadas_corretamente)
    print("NAO RECORRENCIAS CLASSIFICADAS COMO RECORRENCIAS:", nao_recorrencias_classificadas_como_recorrencias)
    print("PORCENTAGEM DE NAO RECORRENCIAS CLASSIFICADAS CORRETAMENTE:", nao_recorrencias_classificadas_corretamente/(nao_recorrencias_classificadas_corretamente + nao_recorrencias_classificadas_como_recorrencias))
