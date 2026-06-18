'''for r in range(8):
    for st in range(r+1):
        print(" * ",end=(""))
    print("")    '''

'''for r in range(5):
    for st in range(r):
        print("    *",end=(''))
    print('')    '''

'''for i in range (4,-1,-1):
    print(' '*i,'*'*(5-i))'''

"""for r in range (1,5):
    n=1
    for j in range (1,r+1):
     print(r*n,end=" ")
     n+=1
    print(" ")"""


"""#prime number 
n=int(input("enter number: "))
x=0
if n<1:
    print(f"(i) is not a prime number")
    for i in range (2,(n//2)+1):
      if n%i==0:
          x=1
        if x==1:
          print(f"n")
    else:
         print(f"(i) is a prime number")
"""

def greet(name,age,place="kochi",course="none"):
          print(f"hello {name} you are {age} years old")
          if place:
           print ("you are from", place)
greet(name="aswin",age="19",place="kottayam")              