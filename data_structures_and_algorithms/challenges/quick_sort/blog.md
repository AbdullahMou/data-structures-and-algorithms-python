## Pseudo Code
            ALGORITHM QuickSort(arr, left, right)
                if left < right
                    // Partition the array by setting the position of the pivot value 
                    DEFINE position <-- Partition(arr, left, right)
                    // Sort the left
                    QuickSort(arr, left, position - 1)
                    // Sort the right
                    QuickSort(arr, position + 1, right)

            ALGORITHM Partition(arr, left, right)
                // set a pivot value as a point of reference
                DEFINE pivot <-- arr[right]
                // create a variable to track the largest index of numbers lower than the defined pivot
                DEFINE low <-- left - 1
                for i <- left to right do
                    if arr[i] <= pivot
                        low++
                        Swap(arr, i, low)

                // place the value of the pivot location in the middle.
                // all numbers smaller than the pivot are on the left, larger on the right. 
                Swap(arr, right, low + 1)
                // return the pivot index point
                return low + 1

            ALGORITHM Swap(arr, i, low)
                DEFINE temp;
                temp <-- arr[i]
                arr[i] <-- arr[low]
                arr[low] <-- temp



## Trace
            Array: [9,7,8,3,2,1]
* pass1: [0:5]
  *             Array: [7,9,8,3,2,1]

* pass2 :
  * array = [1,3,2] [7] [8,9]

* pass3 :
  * array = [2,3,1] [7] [8,9]

* pass4 :
  * array = [1,2,3]  [7] [8] [9]

* pass5 :
  * array = [1] [2] [3] [7] [8] [9]

