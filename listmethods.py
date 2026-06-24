'''my_list=[12,'java','python','string',30]
my_list.append(40)#to add value 
print(my_list)'''

'''my_list=[12,'java','python','string',30]
my_list.extend(["orange",12])
print(my_list)'''#to extend value

'''name="EBIN"
name.lower()
print(name.lower())'''

'''name="ebin"
name.upper()
print(name.upper())'''
data=[]
def a():

    name=(input("enter name"))
    age=(input("enter age"))
    people={'name':name,'age':age}
    data.append(people)
    print(data)
   

while True:
    
    a()
    more=(input("do you want to add more (Y/N)"))
    if more.lower() != 'Y'.lower():
       break



print("final list",data)
    

