import numpy as numpy

arr_1d = numpy.arange(11)
print("Original array:\n",arr_1d)

# slicing in 1D array
print("sliced array:\n",arr_1d[3:8])
# with step
print("sliced array:\n",arr_1d[3:8:2]) # start < stop ==> move forward
# backwards
print("sliced array:\n",arr_1d[8:2:-1]) # start > stop  <== move backward


# slicing in 2D array
arr_2d = numpy.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]]) 
print("original matrix:\n",arr_2d)
print("specific element:\n",arr_2d[1,1]) # [row,col]
print("Entire row:\n",arr_2d[2]) # row_indx
print("Entire column:\n",arr_2d[:, 2]) # all rows of 2nd column (:) all
