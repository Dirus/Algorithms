def main():
    A = []
    l = int(input("Enter the No. of elements: "))
    print("Enter the array elements ")
    for i in range(0,l):
        A.append(int(input()))
    heapSort(A)
    print("Array after Sorting: ",A)

def Left(i):
    return 2*i
def Right(i):
    return 2*i+1


# T(n) = T(2n/3) + O(1) = O(Logn)
def Heapify(A,n,i):
    largest = i
    l = Left(i)
    r = Right(i)
    # See if left child of root exists and is greater than root
    if l < n and A[l] > A[largest]:
        largest = l
    # See if right child of root exists and is greater than root
    if r < n and A[r] > A[largest]:
        largest = r
    # Change root, if needed 
    if largest !=i :
        A[i],A[largest] = A[largest], A[i] #swap
        # Heapify the root
        Heapify(A,n,largest)

# time complexity = O(n)
def buildMaxHeap(A):
    for i in range(len(A)//2 - 1,-1,-1):
        Heapify(A,len(A),i)

# time complexity = O(nLogn)
def heapSort(A):
    buildMaxHeap(A)
    for i in range(len(A)-1,0,-1):
        A[i],A[0] = A[0],A[i]
        Heapify(A,i,0)



if __name__=="__main__":
    main()