# Question 1

temp1 = [4 , 5 , 6 , 7]
temp2 = [4 , 5]
def check_list(x, y):
    for i in x:
        if i not in y:
            print(i)
check_list(temp1, temp2)

# Question 2

ls = [ 'a','b','c','d',]


def reverse1(x):
    y = x[::-1]
    print(y)
reverse1(ls)

def reverse2(x):
    x.reverse()
    print(x)

reverse2(ls)

# Question 3


def add_two():
    x = 0
    y = 1
    while y > 0:
        print(y)
        x,y = y,x+y

add_two()

# Question 4

Strings = ['Guido van Rossum born 31 January 1956 is a Dutch programmer best known as the creatorof the Python programming language' ]


