count = 0
for i in range(2,100+1):
    for j in range(1,i):
        if i % j == 0:
            count +=1
            
            
    if count > 1:
        
        count = 0
    else:
        print(i)
        count = 0