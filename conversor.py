inde  = int(input("Digite '1' para binário ou '2' para hexadecimal: "))
num   = int(input("Digite o valor que vc deseja converter: "))
vetor = []


if inde == 1: #conversão para binário
    
    while num >1  :
        
        vetor.append(int(num%2))
        num = num/2
elif inde == 2 :
    while num > 1:
        vetor.append(int(num%16))
        num = num/16
else:
    while num > 1:
        vetor.append(int(num%8))
        num = num/8
            
        
print(vetor)
print("".join(map(str, vetor[::-1])))
        
    
    
    
    
   
    