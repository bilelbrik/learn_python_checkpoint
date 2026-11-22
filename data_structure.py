#question 1
def multiply_list(items):
    
    result = 1
    for num in items:
        result *= num
    return result


sample_list = [2, 3, 6]
print(multiply_list(sample_list))  

#question 2
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sample_list.sort(key=lambda item: item[-1])
print(sample_list)  
#question 3
d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}

combined = d1.copy()
for key, value in d2.items():
    combined[key] = combined.get(key, 0) + value

print(combined)
#question 4
n = int(input("Enter a number: "))
squares_dict = {i: i * i for i in range(1, n + 1)}

print(squares_dict)
#question 5
items = [("item1", "12.20"), ("item2", "15.10"), ("item3", "24.5")]
sorted_items = sorted(items, key=lambda item: float(item[1]), reverse=True)

print(sorted_items)
#question 6
# 1. Create a set
my_set = {0, 1, 2, 3, 4}
print("Initial set:", my_set)

# 2. Iterate over a set
print("Iterating over set:")
for element in my_set:
    print(element)

# 3. Add members to a set
my_set.add(5)  # Add a single element
my_set.update([6, 7])  # Add multiple elements
print("After adding elements:", my_set)

# 4. Remove items from a set
my_set.remove(2)  # Raises KeyError if element is missing
my_set.discard(99)  # Safe removal: does nothing if element is missing
print("After removing elements:", my_set)

