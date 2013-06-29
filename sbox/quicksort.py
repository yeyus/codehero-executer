# Copyright (c) 2013 the authors listed at the following URL, and/or
# the authors of referenced articles or incorporated external code:
# http://en.literateprograms.org/Quicksort_(Python,_arrays)?action=history&offset=20120413011615
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# 
# Retrieved from: http://en.literateprograms.org/Quicksort_(Python,_arrays)?oldid=18499

from random import *

def partition(a, start, end, pivotIndex):
    low = start
    high = end - 1  # After we remove pivot it will be one smaller
    pivotValue = a[pivotIndex]
    a[pivotIndex] = a[end]

    while True:
        while low <= high and a[low] < pivotValue:
            low = low + 1
        while low <= high and a[high] >= pivotValue:
            high = high - 1
        if low > high:
            break
        a[low], a[high] = a[high], a[low]
    a[end] = a[low]
    a[low] = pivotValue
    return low


def insertionSort(a, start, end):
    for i in xrange(start, end + 1):
        # Insert a[i] into the sorted sublist
        v = a[i]
        for j in reversed(xrange(0, i)):
            if a[j] <= v:
                a[j + 1] = v
                break
            a[j + 1] = a[j]
        else:
            a[0] = v
    return a

def qsortRange(a, start, end):
    if end - start + 1 < 32:
        insertionSort(a, start, end)
    else:
        pivotIndex = partition(a, start, end, randint(start, end))
        qsortRange(a, start, pivotIndex - 1)
        qsortRange(a, pivotIndex + 1, end)
    return a

def qsort(a):
    return qsortRange(a, 0, len(a) - 1)

def main():
    
    # input is injected by the sandbox caller
    # Array copy to avoid the usage of a readonly object
    i = []
    for row in inpt:
        i.append(row)

    print qsort(i)

if __name__ == "__main__":
    main()

main()    