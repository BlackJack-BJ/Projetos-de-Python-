password = input()
strong = False
lista_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lista_char = ['!', '@', '#', '$', '%', '&', '*']
cont_num = 0
cont_char = 0

for caracter in password:
    for num in lista_num:
        if num == caracter:
            cont_num += 1
            
    for char in lista_char:
        if char == caracter:
            cont_char += 1
            
if cont_num >= 2 and cont_char >= 2 and len(password) >= 7:
    strong  = True
    
if strong:
    print('Strong')
    
else:
    print('Weak')