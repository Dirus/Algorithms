def main():
    A = []
    # l = int(input("Enter the No. of elements: "))
    # print("Enter the array elements ")
    # for i in range(0,l):
    #     A.append(int(input()))
    A = [5,2,4,7,1,3,2,6]
    mergeSort(A)
    print("Array after sorting: ",A)


# T(n) =    O(1) if n=1
#           2T(n/2)+O(n) if n>1 = O(nlgn)
def mergeSort(A):
    l = len(A)
    if l > 1:
        # Find mid of array
        mid = l//2
        # divide array into two halves
        L = A[:mid]
        R = A[mid:]
        # sorting first half
        mergeSort(L)
        # sorting second half
        mergeSort(R)
        n1 = len(L)
        n2 = len(R)
        i=j=k=0
        while i< n1 and j < n2:
            if L[i] < R[j]:
                A[k] = L[i]
                i = i+1
            else:
                A[k] = R[j]
                j = j+1
            k = k+1
        # Checking if any element was left    
        while i< n1:
            A[k] = L[i]
            k = k+1
            i = i+1
        while j< n2:
            A[k] = R[j]
            k = k+1
            j = j+1


if __name__=="__main__":
    main()