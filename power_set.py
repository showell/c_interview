def power_set(big_lst):
    n = len(big_lst)
    power_set = []
    for i in range(1 << n):
        lst = []
        for j in range(n):
            if i&(1<<j):
                lst.append(big_lst[j])
        power_set.append(lst)
    return power_set
    
lst = [10, 20, 30]
print power_set(lst)
