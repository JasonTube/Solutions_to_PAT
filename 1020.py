if __name__ == "__main__":
    kind, demand = [int(tmp) for tmp in input().split(" ")]
    stocks = [eval(tmp) for tmp in input().split(" ")]
    total_prices = [eval(tmp) for tmp in input().split(" ")]
    
    infos = [[total_price/stock,stock] for total_price,stock in zip(total_prices,stocks)]
    infos.sort(key = (lambda x:x[0]),reverse = True)

    total_cost = 0
    for price,stock in infos:
        if demand <= stock:
            total_cost += price*demand
            break
        else:
            total_cost += price*stock
            demand -= stock
    print("%.2f" % total_cost)
