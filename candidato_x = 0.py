candidato_x = 0 
candidato_y = 0
candidato_z = 0
branco = 0 

while True:
    print('Escolha sua opção de voto: ')
    print('1= Candidato_X'), print('2= Candidato_Y'), print('3= Candidato_X'), print('4-branco.')
    try:
        voto = int(input('Digite seu voto: '))
        if voto == 1:
            candidato_x += 1
        elif voto == 2:
            candidato_y += 1
        elif voto == 3:
            candidato_z += 1
        elif voto == 4:
            branco += 1
        else:
            print('Digite uma opção válida')
            continue
         sair = int(input('1) Fim da votação' ' 2) Continuar a votar:'))
        if sair == 1:
            print(f'Votos Candidato_X foi de: {candidato_x}')
            print(f'Votos Candidato_Y foi de: {candidato_y}')
            print(f'Votos Candidato_Z foi de: {candidato_z}')
            print(f'Votos em branco foi de: {branco}')
            if candidato_x > candidato_y and candidato_x > candidato_z:
                print('Candidato_X ganhou as eleições')
            elif candidato_y > candidato_x and candidato_y > z:
                print('Candidato_Y ganhou as eleições')
            elif candidato_z > candidato_x and candidato_z > y:
                print('Candidato_Z ganhou as eleições')
            elif branco > candidato_x and branco > candidato_y and branco > z:
                print('Branco conseguiu mais votos')
            break
        elif sair == 2:
            continue
    except Exception:
        print('ERROR')