n=int(input('enter n value:'))

sum1=0

sum2=0

for i in range (1,n+1):

    if i%2==0:

      sum1=sum1+i

      print(sum1)

    else:

      sum2=sum2+i

      print(sum2)

      

print('sum of even numbers:',sum1)

print('sum of odd numbers:',sum2)
