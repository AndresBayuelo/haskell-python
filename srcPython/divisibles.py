import divisible as d

def divisibles(num):
    count=0
    for i in range(num):
        if(i!=0):
            if(d.divisible(num,i)):
                count = count + 1
    return count

#print(divisibles(4))