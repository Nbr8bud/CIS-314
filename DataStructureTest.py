#Set and List of NFL teams

x={"LAC","DAL","JAX","TB","BAL","NYG","CIN","MIN","MIA","SEA"}
y=["SEA","MIA","MIN","CIN","NYG","BAL","TB","JAX","DAL","LAC"]


#2- Print the 3rd element

#Can't print a certain element from a set due to it being unindexed and unordered
print(y[2])


#3- Print the elements in a random order
print(x)

#Can't print a list in a random order due to it being indexed and ordered without importing a module

#4- An an 11th element to the end of the structure
x.add("PHI")
print(x) #Can't add to "end" since it is unindexed and unordered

y.append("PHI")
print(y)


#5- Remove first element
x.remove("LAC")
print(x)

y.remove("SEA")
print(y)


#6- Remove same element from both lists
x.remove("DAL")
print(x)

y.remove("DAL")
print(y)