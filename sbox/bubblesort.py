import sys

def bubble(bad_list):
    length = len(bad_list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if bad_list[i] > bad_list[i+1]:
                sorted = False
                bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]

    return bad_list

def main():
    
    # input is injected by the sandbox caller
    # Array copy to avoid the usage of a readonly object
    i = []
    for row in inpt:
        i.append(row)

    print bubble(i)

if __name__ == "__main__":
    main()

main()