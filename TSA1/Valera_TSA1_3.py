#AUTHOR: VALERA, TAMIYAH GALE C.
#DATE: 2025-02-03

#Problem 3: A program that will display the following given output. (for a. use nested for statement and for b. use nested while statement)

#a.            1
#             12
#           123
#         1234
#      12345

print("\na.Using nested for statement")
for i in range(1, 6):
    print(' ' * (5 - i) + ''.join(str(j) for j in range(1, i + 1)))

#b.     1
#        333
#        55555
#        666666
#        7777777

print("\nb.Using nested while statement")
i = 1
while i <= 7:
    if i != 2 and i != 4:
        print(" " , str(i) * i)
    i += 1
    

