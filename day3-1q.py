def maxprofit(price,n):
    profit=[0]*n
    print("profit",profit)
    max_price=price[n-1]
    print("max_price",max_price)
    for i in range (n-2,0,-1):
        print(price[i])
        if price[i]>max_price:
             max_price = price[i]
        profit[i] = max(profit[i + 1], max_price - price[i])
        print(profit[i])
    min_price = price[0]
    print("minimum price", min_price)
    for i in range(1, n):
        print(price[i])
        if price[i] < min_price:
            min_price = price[i]
        profit[i] = max(profit[i - 1], profit[i] + (price[i] - min_price))
        print(profit [i])
    result = profit[n - 1]
    print(result)
    return result
price = [2,30,15,10,8,25,80]
print("Maximum profit is", maxprofit(price,len(price)))
        
            
    
