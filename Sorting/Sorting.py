list1 = [99, 5,4,7,98,34,76, 101, 64, 3, 17, 1, 33, 22]

#### Selection Sort
# for i in range(len(list1)):
#     for j in range(i+1, len(list1)):
#         if list1[i] > list1[j]:
#             list1[i], list1[j] = list1[j], list1[i]
# print(list1)

#### Bubble Sort
# count = 0
# for i in range(len(list1)):
#     for j in range(len(list1) - i - 1):
#         if list1[j] > list1[j+1]:
#             list1[j], list1[j+1] = list1[j+1], list1[j]
#         count += 1
# print(list1)
# print(count)

#### Bubble Sort - Optimized
count = 0
for i in range(len(list1)):
    for j in range(len(list1) - 1):
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]
        count += 1
print(list1)
print(count)
