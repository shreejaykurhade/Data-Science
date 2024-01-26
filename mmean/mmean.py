import random 
total_sum = 0; p = 0; 
while p!=1000:
    
    i = 0; j = 0; sum = 0;  list1 = []; 
   
    while i!=100:
        random_int = random.randint(1,100)
        list1.append(random_int)
        i+=1
    print(list1)
   
    while j!=100:
        num = int(list1[j])
        sum=sum + num
        j+=1
    print(f"The sum is {sum}")
    
    mean=sum/100
    print("The mean is ",mean)
    
    #Now we take such mean of 1000 different means to check the mean of random 100 integer's mean
    total_sum= total_sum + mean 
    p+=1
mmean=total_sum/1000

print("The Average Mean produced by random generation of 100 numbers is : ",mmean)