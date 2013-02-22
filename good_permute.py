def good_permute(arr, bad_head = None):
    if len(arr) == 1:
        if arr[0] == bad_head:
            return []
        return [arr]
    result = []
    for i in range(len(arr)):
        v = arr[i]
        if v == bad_head: continue
        others = arr[:i] + arr[i+1:]
        for p2 in good_permute(others, v+1):
            result.append([v] + p2)
    return result

print good_permute([1,2,3,4])
    
