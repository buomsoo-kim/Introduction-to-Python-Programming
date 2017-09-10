def insertion_sort(seq):
    for i in range(1,len(seq)):    
        j = i                    
        while j > 0 and seq[j] < seq[j-1]: 
            seq[j], seq[j-1] = seq[j-1], seq[j] 
            j=j-1 
    return seq

insertion_sort([9, 4, 8, 2, 3, 5, 1])