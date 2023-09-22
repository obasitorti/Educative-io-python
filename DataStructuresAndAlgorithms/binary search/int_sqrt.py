def integer_square_root(k):
    if k == 0 or k == 1:
        return k
    
    low = 0
    high = k

    while low <= high:
        mid = (low + high) // 2
        square = mid * mid
        if square <= k:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result

print(integer_square_root(625))