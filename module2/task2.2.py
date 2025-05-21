
#positive number or not 
#task 2.2
n=int(input("enter a number :"))
if n<0:
    print("please enter a positive number")
sum=0
for i in range(1,n):
    sum=sum+i
print("sum of first ",n," numbers is : ", sum)
print('end')  