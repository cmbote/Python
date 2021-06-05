# Biggie Size
def biggie_size(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list
print(biggie_size([-1, 3, 5, -5]))

# Count Positives
def count_positive(list):
    count = 0
    for i in range(len(list)):
        if list[i] > 0:
            count = count + 1 
    list[len(list)-1] = count
    return list
print(count_positive([1,6,-1,-21,-1]))

# Sum Total
def sum_total(list):
    count = 0
    for i in range(len(list)):
        count = count + list[i]
    return count
print(sum_total([1, 2, 3, 4]))

# Average
def average(list):
    count = 0
    for i in range(len(list)):
        count = count + list[i]
    return count/len(list)
print(average([1, 2, 3, 4]))

# Length
def length(list):
    if len(list)==0:
        return 0
    else:
        return len(list)        
print(length([37,2,12,1,-9]))

# Minimum
def min(list):
    count = list[0]
    for i in range(len(list)):
        if list[i] < count:
            count = list[i]
    return count
print(min([37,2,12,1,9]))

# Minimum
def min(list):
    count = list[0]
    for i in range(len(list)):
        if list[i] < count:
            count = list[i]
    return count
print(min([37,2,12,1,9]))

# Maximum
def max(list):
    count = list[0]
    for i in range(len(list)):
        if list[i] > count:
            count = list[i]
    return count
print(max([7,2,12,1,9]))