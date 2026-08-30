def self_power_sum(n):
    
    mod = pow(10,10)
    sum = 0
    
    for i in range(1,n+1):
        sum += pow(i,i,mod)
        
    return sum % mod

print(self_power_sum(1000))
