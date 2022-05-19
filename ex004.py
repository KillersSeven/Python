t1 = input('Digite algo: ')
print(f'O tipo primitivo desse valor é{type(t1)}')
print(f'Só tem espaços?{t1.isspace()}')
print(f'É alfanumérico?{t1.isalnum()}')
print(f'Só tem números?{t1.isnumeric()}')
print(f'É alfabético?{t1.isalpha()}')
print(f'Está em maiúculas?{t1.isupper()}')
print(f'Está em minúsculas?{t1.islower()}')
print(f'Está captalizada?{t1.istitle()}')


