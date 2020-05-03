 
def fib_even(n_max):
    out = []
    
    n_last0 = 1
    n_last1 = 1
    
    while(True):
        n = n_last0 + n_last1
        if n > n_max:
            break
        
        n_last1 = n_last0
        n_last0 = n
        if not n % 2:
            out.append(n)
        
    return out


if __name__ == "__main__":
    a = fib_even(4000000)
    print(sum(a))
