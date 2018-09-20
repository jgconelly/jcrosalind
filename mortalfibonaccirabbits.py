#Mortal Fibonacci Rabbits

def mortal_rabbits(n, m):
    rabbits = [1] + [0]*(m - 1)
    for i in range(n - 1):
        rabbits = [sum(rabbits[1:])] + rabbits[:-1]
    print(sum(rabbits))

mortal_rabbits(98, 17)