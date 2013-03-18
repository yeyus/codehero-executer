import sys

def mergeSort(toSort):
    if len(toSort) <= 1:
        return toSort
 
    mIndex = len(toSort) / 2
    left = mergeSort(toSort[:mIndex])
    right = mergeSort(toSort[mIndex:])
 
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:   
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
 
    if len(left) > 0:
        result.extend(mergeSort(left))
    else:
        result.extend(mergeSort(right))
     
    return result

def main():
    input = [9,8,7,6,5,4,3,2,0,1]
    print mergeSort(input)

if __name__ == "__main__":
    main()

main()