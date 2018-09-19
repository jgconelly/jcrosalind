#Rabbits and Recurrence Relations

def rabbits(n, k):

    fertile_adults = 0
    new_adults = 0
    baby_rabbits = 1 #please note this is all pairs.
    month = 1 #starting in month 1, not month 0. 

    while month < n:
        new_adults = fertile_adults + baby_rabbits 
        baby_rabbits = fertile_adults * k
        fertile_adults = new_adults
        total_rabbits = fertile_adults + baby_rabbits
        month += 1

    print (total_rabbits)

rabbits(36, 3)