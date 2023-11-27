edad = int(input('Ingrese su edad: '))
sexo = str(input('Ingrese su sexo (F/M): '))



if (sexo == 'M') and (edad >= 60):
    print('Ya puede jubilarse')
elif (sexo == 'F') and (edad >= 54):
    print('Ya puede jubilarse')    
if (sexo == 'M') and (edad < 60):
    print('No tiene la edad necesaria para jubilarse')
elif (sexo == 'F') and (edad < 54):
    print('No tiene la edad necesaria para jubilarse')

