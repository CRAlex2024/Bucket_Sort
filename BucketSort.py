def bucket_sort(arr):
    # Create n empty buckets
    bucket = []
    n = len(arr)
    for i in range(n):
        bucket.append([])

    # Put array elements in different buckets
    for j in arr:
        index_b = int(n * j)
        bucket[index_b].append(j)

    # Sort individual buckets
    for i in range(n):
        bucket[i] = sorted(bucket[i])

    # Concatenate all buckets into arr
    k = 0
    for i in range(n):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
    return arr

# Example usage
arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
print("Before sorting array elements are:")
print(arr)

sorted_arr = bucket_sort(arr)
print("After sorting array elements are:")
print(sorted_arr)

