lst = [3,1,4,1,5,9,2,6,5,9]

lst.sort()

for i, idx in enumerate(lst):
    if i < lst[idx + 1]:
        
