if __name__ == '__main__':
    N,M = [int(tmp) for tmp in input().split(" ")]
    
    item_list = []
    unsafe_tabel = []
    
    for i in range(N):
        item1,item2 = [tmp for tmp in input().split(" ")]
        if not item1 in item_list:
            item_list.append(item1)
            unsafe_tabel.append({item2})
        else:
            index = item_list.index(item1)
            unsafe_tabel[index].add(item2)
        if not item2 in item_list:
            item_list.append(item2)
            unsafe_tabel.append({item1})
        else:
            index = item_list.index(item2)
            unsafe_tabel[index].add(item1)
                
    #print(item_list)
    #print(unsafe_tabel)

    for i in range(M):
        package = [tmp for tmp in input().split(" ")]
        flag = True
        # 对每一行输入
        for j in range(1,int(package[0])+1):
            # item表中有package[j]，检查
            if package[j] in item_list:
                index = item_list.index(package[j])
                # 检查package[j]后有没有元素冲突
                tmp = set(package[j+1:]).intersection(unsafe_tabel[index])
                if len(tmp) != 0:
                    flag = False
                    break
        if flag:
            print('Yes')
        else:
            print('No')
