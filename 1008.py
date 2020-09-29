if __name__=='__main__':
    N, M = [int(tmp) for tmp in input().split()]
    A = [int(tmp) for tmp in input().split()]
    
    # 按移动的规则将数组转化成有向图，图中有多少个闭合回路就需要进行几个循环，每个循环存一次tmp
    M = M % N
    if M != 0: # 防止除零错误
        for k in range(1,M+1):
            if (k*N) % M == 0: # 除尽代表可以从任意点出发循环回到该点
                for i in range(int(M/k)): # (k*N)/M个点在同一个回路上，故共有M/k个回路
                    tmp = A[i]
                    for j in range(int(N*k/M)-1):
                        A[(i-j*M) % N] = A[(i+(-j-1)*M) % N]
                    A[(i+(-N+1)*M) % N] = tmp
                break
            
    print(" ".join(str(tmp) for tmp in A))
