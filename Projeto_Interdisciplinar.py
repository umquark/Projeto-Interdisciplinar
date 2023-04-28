import os, math
os.system('cls')
cont = 0

while cont == 0:

  nome = input('Digite o nome de usuário: ')
  print(f'Olá {nome}.')

  print(f'Digite 1 para: Conversão da base decimal para as bases binário, hexadecimal e octadecimal.')
  print(f'Digite 2 para: Conversão das bases binário, hexadecimal e octadecimal para a base decimal.')
  print(f'Digite "Esc" durante o menu para sair.')

  menu = input('Insira uma opção: ')

  if menu == '1':
    print('Digite 1 para: Converter da base decimal para a base binário: ')
    print('Digite 2 para: Converter da base decimal para a base hexadecimal: ')
    print('Digite 3 para: Converter da base decimal para a base octadecimal: ')

    opcao1 = input('Insira uma opção: ')

    if opcao1 == '1':
        binario = ""
        dec = int(input('Digite um número para conversão: '))
        while dec > 0:
            r = dec%2
            binario = str(r) + binario
            dec = dec //2
            cont += 1
        print(f'Binário = {binario}')
        
    elif opcao1 == '2':
        dec = int(input('Digite um número para conversão: '))
        hexa = ""
        while dec > 0:
          r = dec%16
          dec = dec // 16
          if r < 10:
            hexa = str(r) + hexa
        else:
            hexa = chr(ord('A') + r - 10) + hexa
            print(f'Hexadecimal = {hexa}')
        
    elif opcao1 == '3':
        dec = int(input('Digite um número para conversão: '))
        octal = ""
        while dec > 0:
          r = dec%8
          dec = dec // 8
          octal = str(r) + octal
          cont =+1
        print(f'Octodecimal = {octal}')
        
    elif opcao1.lower() == 'esc':
      break
  
  elif menu == '2':
    print('Digite 1 para: Converter da base binário para a base decimal: ')
    print('Digite 2 para: Converter da base hexadecimal para a base decimal: ')
    print('Digite 3 para: Converter da base octadecimal para a base decimal: ')
    
    opcao2 = input('Insira uma opcão: ')
    
    if opcao2 == '1':
      binario = ""
      num = float(input('Digite um número para conversão: '))
      while num > 0:
            r = num%2
            binario = str(r) + binario
            num = num //2
            print(binario)
      
    elif opcao2 == '2':
      num = float(input('Digite um número para conversão: '))
      
    elif opcao2 == '3':
      num = float(input('Digite um número para conversão: '))
      
    elif opcao2.lower() == 'esc':
      break
    
  elif menu.lower() == 'esc':
    break