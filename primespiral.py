import turtle

def mult(a):
    return a*10

#enter input------------------------------------------------------------------------
n = int(input("enter no."))
co = 0

#calculations-----------------------------------------------------------------------
for i in range(n):
    co=co+(i*10)
n = n*10

#turtle initialization--------------------------------------------------------------
td = turtle.Turtle()
counter1 = 0
counter2 = 0
td.speed(0)

#finding primes---------------------------------------------------------------------

rawprime = []
for i in range(1,co):
    temp = []
    for j in range(1,i):
        if(i%j == 0):
            temp.append(j)
    if(len(temp)<2):
        rawprime.append(i)
prime = list(map(mult,rawprime))

#spiral------------------------------------------------------------------------------

for i in range(10,n,10):
    td.forward(i)
    td.left(90)
td.penup()
td.home()


#plotting-----------------------------------------------------------------------------
for k in range(10,n,10):
    td.forward(k)
    counter1 = counter2
    counter2 = counter2 + k
    for j in range(len(prime)):
        if(counter1 <= prime[j] <= counter2):
            td.left(180)
            td.forward(counter2 - prime[j])
            td.dot()
            td.left(180)
            td.forward(counter2 - prime[j])
    td.left(90)
td.home()

#end---------------------------------------------------------------------------------

turtle.done()