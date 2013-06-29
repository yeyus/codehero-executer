import sys

def insertionSort(a, start, end):
    for i in xrange(start, end + 1):
        # Insert a[i] into the sorted sublist
        v = a[i]
        for j in xrange(i-1, -1, -1):
            if a[j] <= v:
                a[j + 1] = v
                break
            a[j + 1] = a[j]
        else:
            a[0] = v
    return a

def main():
    
    # input is injected by the sandbox caller
    # Array copy to avoid the usage of a readonly object
    i = []
    for row in inpt:
        i.append(row)

    print insertionSort(i,0,len(i)-1)

if __name__ == "__main__":
    main()

main()