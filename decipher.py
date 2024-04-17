import math
import Crypto.Util.number as cun
from sympy import nextprime

# ref: https://stackoverflow.com/questions/356090/how-to-compute-the-nth-root-of-a-very-big-integer
def find_invpow(x,n):
        """Finds the integer component of the n'th root of x,
        an integer such that y ** n <= x < (y + 1) ** n.
        """
        high = 1
        while high ** n < x:
            high *= 2
        low = high//2
        while low < high:
            mid = (low + high) // 2
            if low < mid and mid**n < x:
                low = mid
            elif high > mid and mid**n > x:
                high = mid
            else:
                return mid
        return mid + 1

while True:
    version = input("version = ")
    n = int(input("n = "))
    e = int(input("e = "))
    c = int(input("c = "))

    if (version == 'A'):
        n_root = find_invpow(n, 2)
        print("n root = ", n_root)
        for i in range(0, 100):
            n_root = nextprime(n_root)
            print("q = ", n_root, end=" ")
            if (n % n_root == 0):
                print("YES")
                break
            print("NO")
        q = n_root
        p = n//q
        print(f"p = {p}")
        tot = (p-1)*(q-1)
        print(f"tot = {tot}")
        d = pow(e, -1, tot)
        print(f"d = {d}")
        dec = pow(c, d, n)
        print( f"m= {dec}")
        print( cun.long_to_bytes(dec).decode())

    elif (version == 'B'):
        p = math.isqrt(n)
        if (n % p == 0):
            print("YES")
        print(f"p = {p}")
        tot = (p)*(p-1)
        print(f"tot = {tot}")
        d = pow(e, -1, tot)
        print(f"d = {d}")
        dec = pow(c, d, n)
        print( f"m= {dec}")
        print( cun.long_to_bytes(dec).decode())
    elif (version == 'C'):
        for i in range(2**15, 2**16+1):
            try:
                
                dec = pow(c, i, n)
                print( cun.long_to_bytes(dec).decode())
                print(f"e = {i}")
                print(f"m = {dec}")
                break
            except:
                print(f"NO {i}")
                continue
    elif (version == 'D'):
        try:
            cube_root = find_invpow(c, 3)
            dec = int(cube_root)
            print( "cube root: ", dec)
            print( cun.long_to_bytes(dec).decode())
        except:
            print("NO")
    elif (version == 'E'):
        try:
            d = pow(e, -1, n-1)
            print(f"d = {d}")
            dec = pow(c, d, n)
            print( f"m= {dec}")
            print( cun.long_to_bytes(dec).decode())
        except:
            print("NO")
    
    print("\n\n")
