'''s=input("enter your string:")
a={}
for b in s:
    if b in a:
        a[b]=a[b]+1
    else:
        a[b]=1
for n in a:
    print(f"{n}={a[n]}")
'''

'''numbers=[19,2,1,23,8]
n=len(numbers)#to find length of list
for k in range (n-1):
    for v in range (n-k-1):
        if numbers[v]>numbers[v+1]:
           numbers[v],numbers[v+1]=numbers[v+1],numbers[v]
print(numbers)'''

