n=int(input("enter the upper limit"))
for i in range(0,n+1):
    if(i==1):
        print(i)
    elif(i%15==0):
        print("fizz-buzz")
    elif (i%3==0):
        print("fizz")
    elif(i%5==0):
        print("buzz")
    else:
        print(i)