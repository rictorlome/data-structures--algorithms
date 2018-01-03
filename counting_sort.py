"""
/* Parameters:
 * A - Array of N unsorted positive integers
 * K - Maximum value of all integers to be sorted
 *
 *
*/
"""
import numpy as np

#Example unsorted array to test with.
K = 100
A = np.random.randint(K, size=1000)

def counting_sort(unsorted_array, max_val):
    #Create class Link in order to populate array.
    class Link:
        def __init__(self, key, next=None):
            self.key = key
            self.next = None

    #Create an array of size K.
    myarray = [None] * K

    #Iterate through unsorted_array.
    for num in unsorted_array:
        #Create a link for every number in unsorted_array
        lnk = Link(num)
        if myarray[num] is None:
            myarray[num] = lnk
        else:
            lnk.next = myarray[num]
            myarray[num] = lnk

    #Iterate through myarray
    res = []
    for el in myarray:
        if el is None:
            next
        else:
            res.append(el.key)
            cur = el
            while cur.next is not None:
                cur = cur.next
                res.append(cur.key)
    return res
