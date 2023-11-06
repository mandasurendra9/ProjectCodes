#initialize list
lst = [20, 49, 1, 99]

#initialize largest with first element
largest = lst[0]

#traverse the array
for i in lst:
    if i>largest:
        largest = i

print(largest)