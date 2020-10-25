import math
n = 10000000019
prime = True
for i in range(round(math.sqrt(n)), 2, -1):
    out = divmod(n,i) 
    if out[1] == 0:
        print(f'{n} is not prime')
        prime = False
if prime:
    print(f'{n} is a prime')