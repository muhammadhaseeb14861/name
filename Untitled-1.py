for i in range(1, len(arr)): 
        key = arr[i] 
        j = i - 1 
        # Move elements that are less than key to one position ahead 
        while j >= 0 and arr[j] < key: 
            arr[j + 1] = arr[j] 
            j -= 1 
        arr[j + 1] = key 
