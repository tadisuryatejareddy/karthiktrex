def fun(x):
    repeated=[]
    size=len(x)
    for i in range(size):
        k=i+1;
        for j in range(size,k):
            if (x[i]==x[j] and not in repeated):
                repeated.append(x[i])
    return repeated
                
print("the duplicate elements in the list are")
list=[20,20,10,10]
result=[]
result=fun(list)
print(result)
