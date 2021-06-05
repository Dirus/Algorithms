def main():
    A = []
    l = int(input("Enter the No. of elements: "))
    print("Enter the array elements ")
    for i in range(0,l):
        A.append(int(input()))
    print("Array after sorting : ",insertionSort(A))
    

# Best case --> Already sorted array -> O(n)
#  Worst case --> Reversed sorted array -> O(n^2)
#  Average case --> O(n^2)
def insertionSort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A
    
if __name__=="__main__":
    main()