def dec_to_bin(num):
    resto = []
    q = num
    while q!=0:
        q,r = divmod(q,2)
        resto.append(int(r))
    to_str = list(map(str,resto))[::-1]

    if num%1!=0: #Caso seja fracionário
        resto_frac = []
        r = num%1
        for repeats in range(10):
            print(f'{r:.3f}*2 = {r*2:.3f}')
            r*=2
            q,r = divmod(r,1)
            resto_frac.append(int(q))
            print(f'resto {r:.3f}, inteiro {q:.3f}')
            if r ==0:
                break

    return to_str + [','] + resto_frac

print(dec_to_bin(8.357))
