def top_n(items, n):
    """return the top n items in an array in desc order
    
    Args:
        items (array) list or array-like object
        n (int): number of items to return
        
    Return:
        array: top n items, in desc order
        
    Egs:
        >>> top_n([8,3,2,7,4], 3)
        [8,7,3]
    """
    for i in range(n): #keep sorting until we have the top n items
        for j in range(len(items)-1-i):
            
            if items[j] > items[j+1]: #if the items is bigger than the next item
                items[j], items[j+1] = items[j+1], items[j] #swap the two
                
    top_n = items[-n:] #get the last two items
    return top_n[::-1] #return the descending order