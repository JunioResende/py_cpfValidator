while True:
    cpf = input('Digite um CPF: ')
    newCPF = cpf[:-2]                
    reverse = 10                        
    total = 0

    for index in range(19):
        if index > 8:                   
            index -= 9                  

        total += int(newCPF[index]) * reverse  

        reverse -= 1                    
        if reverse < 2:
            reverse = 11
            d = 11 - (total % 11)

            if d > 9:                   
                d = 0
            total = 0                   
            newCPF += str(d)          

   
    sequence = newCPF == str(newCPF[0]) * len(cpf)

  
    if cpf == newCPF and not sequence:
        print('Válido')
    else:
        print('Inválido')
