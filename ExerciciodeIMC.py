print ('*-* Cálculo de IMC *-*')

peso= float(input('Peso:'))
altura = float(input('Altura:'))


Imc = (peso/altura**2)

print('Imc: {}'.format(Imc))

if Imc < 18.5:
    print('Abaixo do peso')
elif Imc >18.5 and Imc <24.9:   
    print('Peso Normal')
elif Imc >25 and Imc <29.9:
    print ('Sobrepeso')
elif Imc >30 and Imc <34.9:
    print ('Obesidade de Grau 1')  
elif Imc >35 and Imc <39.9:
    print ('Obesidade grau 2')
elif Imc >40:
    print ('Obesidade mórbida')
else: 
    print ('Vá em uma nutricionista porque não funciona esta calculadora')

