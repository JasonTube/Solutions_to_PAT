if __name__ == '__main__':
    N,M = [int(tmp) for tmp in input().split(" ")]
    dangerous_dic = {}
    
    for i in range(N):
        item1,item2 = input().split(" ")
        if item1 in dangerous_dic:
            dangerous_dic[item1].add(item2)
        else:
            temp = set()
            temp.add(item2)
            dangerous_dic[item1] = temp
    #print(dangerous_dic)
    
    for i in range(M):
        package = [tmp for tmp in input().split(" ")]
        package = set(package[1:])
        for j in package:
            if j in dangerous_dic :
                if package & dangerous_dic[j]:
                # including same elements
                    print("No")
                    break
        else:
            print("Yes")


'''
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
                
    #print(item_list)
    #print(unsafe_tabel)

    for i in range(M):
        package = [tmp for tmp in input().split(" ")]
        package = set(package[1:])
        # 对每一行输入
        for item in package:
            # item表中有item，检查
            try:
                index = item_list.index(item)
                if package & unsafe_tabel[index]:
                    print('No')
                    break
            except ValueError:
                continue
        else:
            print('Yes')
'''
