import math
def sandglass(n_max,n,m,symbol):
    if n == 0:
        return
    else:
        string = " "*m+symbol*(2*n-1)
        print(string)
        sandglass(n_max,n-1,m+1,symbol)
        if n > 1:
            string = " "*m+symbol*(2*n-1)
            print(string)
    
if __name__ == "__main__":
    string = input().split(" ")
    N = int(string[0])
    symbol = string[1]
    n_max = int(math.sqrt((N+1)/2))
    sandglass(n_max,n_max,0,symbol)
    print(N-2*(n_max**2)+1)
