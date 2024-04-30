nombre = input ('ingrese su nombre')
edad = float(input('ingrese su edad'))
precio =[]
if edad <= 4:
    precio = 'gratis'
elif edad >4 and edad <= 18:
    precio = '$1.50'
elif edad > 60:
    precio = '$1'
else :
    precio = '$2'

print (f'su edad es {edad} es y el precio de su entrada es {precio}') 