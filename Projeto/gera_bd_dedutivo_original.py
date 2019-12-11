with open('base_TP.txt','r') as f1:
    with open('bd_dedutivo.txt','w+') as f2:
        for line in f1:
            
            atributos = line.strip().split(',')
            dados = ''
            first = True

            for atributo in atributos:
                if first:
                    dados+= f'\'{atributo}\''
                    first = False
                else:
                    dados+= f',\'{atributo}\''

            f2.write(f'individuo({dados}).\n')

# with open('bd_dedutivo/padrao/bd_dedutivo_inteiro_python.txt','r') as f1:
#     with open('bd_dedutivo/nova_coluna/bd_dedutivo_inteiro_completo_coluna_numero_linha.txt','w+') as f2:
#         count = 1
#         for line in f1:
            
#             dados =  str(count) + "," + line.strip()

#             count+=1

#             f2.write(f'individuo({dados}).\n')
