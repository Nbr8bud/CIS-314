import random, secrets, timeit
from collections import Counter

#1.1-Fill data structure with 100 random numbers between 1-16 using random
x=[random.randrange(1,16) for i in range (100)]


#1.2-Fill data structure with 100 random numbers between 1-16 using random
y=[secrets.choice(range(1,16)) for i in range (100)]


#1.3-Get a count of the unique numbers in each data structure
unique_num_val_x=Counter(x)
unique_num_val_y=Counter(y)


#1.4-Based on counts, does one method appear better than the other
    #- It seems that secrets is the better choice due to it having more variety of each number but they both almost seem the same


#2-Run #1 again with 1-65535
x1=[random.randrange(1,65535) for i in range (100)]
y1=[secrets.choice(range(1,65535)) for i in range (100)]

unique_num_val_x1=Counter(x1)

unique_num_val_y1=Counter(y1)
    #The values for each number all comes out to be 1 due to there only being 100 different elements for numbers 1-65535


#3- Create a 100 elements list with numbers between 1-16
x2=[random.randrange(1,16) for i in range (100)]


#3.1- Write a function to sort the list and time how long it takes
def insertion_sort(x2):
    for i in range(1, len(x2)):
        key=x2[i]
        j=i-1
        while j>=0 and key<x2[j]:
            x2[j+1]=x2[j]
            j-=1
        x2[j+1]=key

st1=timeit.default_timer()
insertion_sort(x2)
et1=timeit.default_timer()

elapsed_time1=et1-st1

print()
print(x2)
print("Time taken for process: %.9f seconds" %elapsed_time1)


#3.2-Time how long it takes using .sort()
st2=timeit.default_timer()
list.sort(x2)
et2=timeit.default_timer()

elapsed_time2=et2-st2

print()
print(x2)
print("Time taken for process: %.9f seconds" %elapsed_time2)


#4- Do #3 again with a 100 element list between 1-65535
st1=timeit.default_timer()
insertion_sort(x1)
et1=timeit.default_timer()

elapsed_time1=et1-st1

print()
print(x1)
print("Time taken for process: %.9f seconds" %elapsed_time1)


st2=timeit.default_timer()
list.sort(x1)
et2=timeit.default_timer()

elapsed_time2=et2-st2

print()
print(x1)
print("Time taken for process: %.9f seconds" %elapsed_time2)
    #The insertion sort takes a bit longer but the .sort() took less time with more elements


#5- Do #4 again but with a 500 element list
x3=[random.randrange(1,65535) for i in range (500)]

st1=timeit.default_timer()
insertion_sort(x3)
et1=timeit.default_timer()

elapsed_time1=et1-st1

print()
print(x3)
print("Time taken for process: %.9f seconds" %elapsed_time1)


st2=timeit.default_timer()
list.sort(x3)
et2=timeit.default_timer()

elapsed_time2=et2-st2

print()
print(x3)
print("Time taken for process: %.9f seconds" %elapsed_time2)
    #The .sort() method is much faster than the insertion sort with a large amount of elements