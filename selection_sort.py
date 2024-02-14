dirString = ""

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0 #stores index of arrays smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def findGreatest(arr):
    greatest = arr[0]
    greatest_index = 0 #stores index of arrays greatest value
    for i in range(1, len(arr)):
        if arr[i] > greatest:
            greatest = arr[i]
            greatest_index = i
    return greatest_index

def selectionSort(arr, dirString):
    sortedArr = []
    for i in range(len(arr)):
        if dirString == "s":
            smallest = findSmallest(arr)
            sortedArr.append(arr.pop(smallest))
        elif dirString == "g":
            greatest = findGreatest(arr)
            sortedArr.append(arr.pop(greatest))
        else:
            print("Invalid argument, call selectionSort with array and either 's' for smallest or 'g' for greatest to smallest")
            break
        
    return sortedArr

if __name__ == "__main__":
    print(selectionSort([5, 3, 4, 1, 2], 's'))
    print(selectionSort([5, 3, 4, 1, 2], 'g'))
    print(selectionSort([5, 3, 4, 1, 2], 'k'))
