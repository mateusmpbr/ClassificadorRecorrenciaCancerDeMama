with open('bd_dedutivo/padrao/bd_dedutivo_inteiro_python.txt','r') as f:
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
                
    valor_nao_recorrencia_teste = [
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

            valor_total[index_atributo][atributo_aux]+=1

            if(index_line <= 195):
                valor_nao_recorrencia[index_atributo][atributo_aux]+=1

            if(int(atributos[0]) > 5 or int(atributos[2]) < 5):
                valor_nao_recorrencia_teste[index_atributo][atributo_aux]+=1

    nome_atributos = ['idade','menopausa','tamanho do tumor','inv-nodes','node-caps','deg-malig','mama','breast-quad','irradiada']

    for i in range(9):
        print('-----',nome_atributos[i],'-----')
        print("VALOR TOTAL:",valor_total[i])
        print("VALOR NAO RECORRENCIA",valor_nao_recorrencia[i])
        print("VALOR NAO RECORRENCIA TESTE",valor_nao_recorrencia_teste[i])