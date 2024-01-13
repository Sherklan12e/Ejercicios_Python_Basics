# 2-
def maximo_3(num1,num2,num3):
    if(num1>num2 and num1>num3):
        return num1
    elif(num2>num1 and num2> num3):
        return num2
    else:
        return num3
print(maximo_3(300,200,1000))