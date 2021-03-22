#CALCULATING TABLE OF ANY DESIRED NUMBAER UPTO ANY DESIRED LIMIT USING ONLY RANGE METHOD AND FOR LOOP
n=int(float(input("Enter no. to be calculated: ")))
m=int(float(input("Enter last limit")))
for m in range(n,n*(m+1),n):
    print (m)