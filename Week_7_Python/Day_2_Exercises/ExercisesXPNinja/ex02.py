"""
Analyse this code before executing it. What is the purpose of this code?

ANSWER:
It's a sorting algorithm, it checks if the value from the preceeding index is larger than the value of index being
iterated over. If so, it swaps the values.
"""


def insertion_sort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)