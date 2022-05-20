def getSum(n):
    for range in(1,100): 
        sum = 0
        for digit in str(n): 
            sum += int(digit)      
        return sum

n = 36
print(n/(getSum(n)))
        
   
