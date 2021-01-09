## Pseudo Code

            ALGORITHM Mergesort(arr)
                DECLARE n <-- arr.length
                    
                if n > 1
                DECLARE mid <-- n/2
                DECLARE left <-- arr[0...mid]
                DECLARE right <-- arr[mid...n]
                // sort the left side
                Mergesort(left)
                // sort the right side
                Mergesort(right)
                // merge the sorted left and right sides together
                Merge(left, right, arr)

            ALGORITHM Merge(left, right, arr)
                DECLARE i <-- 0
                DECLARE j <-- 0
                DECLARE k <-- 0

                while i < left.length && j < right.length
                    if left[i] <= right[j]
                        arr[k] <-- left[i]
                        i <-- i + 1
                    else
                        arr[k] <-- right[j]
                        j <-- j + 1
                        
                    k <-- k + 1

## Trace
            Array: [6,2,4,3]
* pass1:
  * left =[6,2] , right = [4,3]

* pass2 :
  * array = [6,2] , left =[6] , right =[2]

* pass3 :
  * array = [2,6]

* pass4 :
  * array = [4,3] , left =[4] , right =[3]

* pass5 :
  * array = [3,4]

* pass6:
  * array = [2,3,4,6]