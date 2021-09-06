import random, math

# Generate an array of elements

array = [21, 22, 49, 1, 4, 12, 43, 6,87 ,234 ,32]

# for i in range(1000):
#     number = random.randint(1, 200000)
#     array.append(number)

array.sort()

def search(array, number):
    lenght = len(array)
    middle = math.ceil(lenght/2)

   
    search = True

    while(search):
        middle_el = array[middle]

        if(number > middle_el):
            middle = math.ceil((lenght + middle + 1)/2)
            print(middle)
        
        elif(number < middle_el):
            middle = math.ceil((lenght-middle-1)/2)
            print(middle)

        else:
            search = False
            
    return middle 

index = search(array, 234)
print(array, "\n",index)