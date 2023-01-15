file = open('books.txt', 'r+')
lista = file.readlines()
lista = [i.replace('\n','') for i in lista]
print(lista)
for line in lista:
    print(f'{line[0]}{len(line)}')
file.close()