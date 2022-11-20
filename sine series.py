x=int(input("enter value of x"))
n= int(input("enter the value of n"))
sin=-1
fct=i=1
sum=0
while i<=n:
    p=1
    fct=1
    for j in range(1,i+1):
        p=p*x
        fct=fct*j
        sin=-1*sin
        sum=sum+sin*p/fct
        i=i+2
        print("sin(",x,")=",sum)
