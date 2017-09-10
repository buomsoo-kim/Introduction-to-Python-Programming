def bubble_sort(seq):
    length = len(seq)        
    for a in range(length):
        for b in range(length-1):
            if (seq[a] < seq[b]):
                seq[a], seq[b] = seq[b], seq[a]
    return seq 

bubble_sort([9, 4, 8, 2, 3, 5, 1])