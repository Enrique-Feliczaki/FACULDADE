def fibo(num):
    if num==1 or num==2:
        return 1
    else:
        return fibo(num-1)+fibo(num-2)

numero_sequencia = 10
interador = 1
while interador <= numero_sequencia:
    result = fibo(interador)
    print(result)
    
    interador+=1
        