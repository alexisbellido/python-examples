def merge_sort(numbers):
    
    if len(numbers) > 1:
        print(numbers)
    
        mid_index = len(numbers) // 2
        l_array = numbers[:mid_index]
        r_array = numbers[mid_index:]

        l_array = merge_sort(l_array)
        r_array = merge_sort(r_array)
        
        return combine_arrays(l_array, r_array)
    else:
        return numbers
        

def combine_arrays(l_array, r_array):
    result = []
    
    i = 0
    j = 0
    
    
    while i < len(l_array) and j < len(r_array):
        if l_array[i] < r_array[j]:
            result.append(l_array[i])
            i += 1
        else:
            result.append(r_array[j])
            j += 1
    
    while i < len(l_array):
        result.append(l_array[i])
        i += 1    
        
    while j < len(r_array):
        result.append(r_array[j])
        j += 1
    
    return result
    

if __name__ == '__main__':
    numbers = [1, 4, 3, 2, 5, 12, 11, 10]
    result = merge_sort(numbers)
    print(result)

  
    # l_array = [1, 3, 5, 11] # track it with "i"
    # r_array = [2, 4, 10, 12]  # track it with "j"
    
        
    # result = combine_arrays(l_array, r_array)
    # print(result)
            
        
    
    
    
