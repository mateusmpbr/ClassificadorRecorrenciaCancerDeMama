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
