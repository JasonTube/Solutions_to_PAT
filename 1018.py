# 运行超时
if __name__ == "__main__":
    n = int(input())
    dic = {'B':0,'C':1,'J':2}
    cid = {0:'B',1:'C',2:'J'}
    judge_table = [[0,1,-1],[-1,0,1],[1,-1,0]]

    count = [0]*3
    jia_list = [0]*3
    yi_list = [0]*3
    
    for i in range(n):
        jia,yi = input().split(" ")
        result = judge_table[dic[jia]][dic[yi]]
        if result == 1:        # 甲胜
            count[0] += 1
            jia_list[dic[jia]] += 1
        elif result == 0:      # 平
            count[1] += 1
        else:               # 乙胜
            count[2] += 1
            yi_list[dic[yi]] += 1
            
    print(" ".join(str(tmp) for tmp in count))
    print(" ".join(str(tmp) for tmp in count[::-1]))
    
    max_jia = cid[jia_list.index(max(jia_list))]
    max_yi = cid[yi_list.index(max(yi_list))]

    print(f'{max_jia} {max_yi}')
