print ('*-* Cálculo de Media *-*')

nota1= float(input('Nota 1:'))
nota2 = float(input('Nota 2:'))
n_faltas = int(input ('Faltas:'))

media = (nota1 + nota2) /2

print('Média: {}'.format(media))

if media >= 6 and n_faltas <=18:
    print('Apravado!')
elif media>=6 and n_faltas > 18:
    print('reprovado por faltas')
elif media < 6 and n_faltas <18:
    print ('*-* Exame Final *-*')
    exame = float(input('Nota do exame:' ))
    media_final = (media + exame) / 2
    if media_final >= 6:
        print ('Aprovado no exame final')
else: 
    print('Reprovado')
