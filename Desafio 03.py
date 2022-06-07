herói = int(input('Quantas balas o herói está carregando?'))
dragão = int(input('Quantos dragões existem?'))
if herói < dragão*2:
    print('O herói não sobreviveu')
else:
    resto = herói - 2*dragão
    print('O herói sobreviveu, sobraram {} balas'.format(resto))