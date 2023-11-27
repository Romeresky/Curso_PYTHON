peso = float(input('Ingrese su peso en Kg: '))
estatura = float(input('Ingrese su estatura en metros: '))

#IMC
IMC = (peso/(estatura**2))
print('Tu IMC es de: ', IMC)
if IMC < 16:
    print('Estas con delgadez severa')
elif IMC >= 16 and IMC <= 16.99:
    print('Estas con delgadez moderada')
elif IMC >= 17 and IMC <= 18.49:
    print('Estas con delgadez aceptable')
elif IMC >= 18.5 and IMC <= 24.99:
    print('Estas con un peso normal, sigue así :P')
elif IMC >= 25 and IMC <= 29.99:
    print('Estas en sobrepeso')
elif IMC >= 30 and IMC <= 34.99:
    print('Estas con obesidad tipo I')
elif IMC >= 35 and IMC <= 39.99:
    print('Estas con obesidad tipo II')
elif IMC >= 40 and IMC <= 49.99:
    print('Estas con obesidad tipo III (obesidad mórbida)')
elif IMC >= 50:
    print('Estas con obesidad tiopo IV o extrema')