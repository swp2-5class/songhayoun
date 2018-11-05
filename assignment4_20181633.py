import time

f1=1;
f2=1;

fnumber_start=2;

sum=2;

fnumber_limit=int(input("Enter a number:"))

ts = time.time()

while(fnumber_start<fnumber_limit):
    temp=f1+f2;
    print(temp,end="");
    sum+=temp;
    f1=f2;
    f2=temp;
    fnumber_start+=1;
print();

print("합은",sum);