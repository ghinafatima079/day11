# Write a Python program to add member(s) in a set
set1={"apple","banana","cherry"}
print(set1)
set1.add("mango")   # to add single element, use 'add'
print(set1)
set1.update(["kiwi","strawberry"])   # to add multiple elements, use 'update'
print(set1)

# Write a Python program to remove item(s) from a given set
set2={4,3,5.7,'pqr'}
set2.remove(4)
print(set2)
#set2.remove(10)    #will throw an error
set2.discard(10)
print(set2)
set2.pop()   #will remove any random element
print(set2)


# You are given two sets of integers, **`set_a`** and **`set_b`**. Implement a Python program that performs the following operations and prints the results:
a={1,4,7.9,'abcd'}
b={4,3,7.9,"abcd"}
# 1. Union: Find and print the union of **`set_a`** and **`set_b`**.
print("a union b: ",a|b)
print("a union c: ",a.union(b))
# 2. Intersection: Find and print the intersection of **`set_a`** and **`set_b`**.
print("a intersection b: ",a&b)
print("a intersection b: ",a.intersection(b))
# 3. Difference: Find and print the elements that are present in **`set_a`** but not in **`set_b`**.
print("difference of a and b",a-b)
print("difference of b and a",b.difference(a))
# 4. Symmetric Difference: Find and print the elements that are present in either of the sets, but not in both.
print("symmetric difference: ",a.symmetric_difference(b))
print("symmetric difference: ",b.symmetric_difference(a))
