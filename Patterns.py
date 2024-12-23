# Pattern 1
print("PATTERN 1:  ")
n = 5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end='')
    print()


# Pattern 2 
print("PATTERN 2 :")
n =5 
for i in range (1 , n+1 ):
    for j in  range( i ):
        print("*", end='')
    print()

# Pattern 3 
print("Pattern 3 : ")
n = 5
for i in range(1 , n+1 ):
    for j in range(1 , i+1 ):
        print(j , end='')
    print()

# Pattern 4 
print("Pattern 4 :  ")
n = 5
for i in range(  n  ):
    for j in range(n):
        print("*", end='')
    print()

# Patter 5 
# If i want the number to occur the near number i have print the j
print("Pattern 5 : ")
n = 5
for i in range(n , 0,-1 ):
    for j in range (1 , i +1 ):
        print(j , end= '')
    print()

# Pattern 6 : 
print("Pattern 6 :")
n = 5 
for i in range (1 , n +1 ):
    for j in range ( i):
        print(i, end='')
    print()