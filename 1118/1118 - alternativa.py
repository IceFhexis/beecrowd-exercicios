ls = []

while(True):
    if len(ls) == 2:
        print('novo calculo (1-sim 2-nao)')
        
        i = int(input()) 
        
        if(i == 1):
            ls = []

        if(i == 2): break
        
        continue

    x = float(input())
    if 0 <= x <= 10:
        ls.append(x)

        if len(ls) == 2:
            print(f'media = {(sum(ls)/2):.2f}')
    else:
        print('nota invalida')
