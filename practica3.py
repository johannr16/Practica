num = input ('Porfavor ingresa un numero:')
num= float(num)

msg = f'El numero {num} es '
if num % 2 ==0:
    msg += 'par y'
else:
   msg += 'par y'

if num >= 0 :
   msg += ' positivo'
else:
   msg += ' negativo'

print(msg)