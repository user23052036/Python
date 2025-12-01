import numpy as np 
import time

# we use numpy because list in python are very slow and can take multiple datatypes
# whereas numpy is highly optimized c++ library which performs fast operations over array() and takes 
# similar datas as input


lists = [1,2,3,4,5]
print("tupil multiplication: ",lists*2) # duplicate created

array = np.array(lists)
print("array multiplication: ",array*array) # element wise multiplication


#----------------------------------------------------------------------------------------------

arr_id = np.array([1,2,3,4,5,6]) # array in numpy takes tupil from python as input []
print("\n\n1D array: ",arr_id)

arr_2d = np.array([[1,2,3],[4,5,6]])
print("2D array:\n",arr_2d)

#-----------------------------------------------------------------------------------------------

start1 = time.time()

new_list = [i*2 for i in range(1000220)]
print("Time taken for list calc: ",time.time()-start1)

start2 = time.time()
numpy_array = np.arange(1000220)*2
print("Time taken for array calc: ",time.time()-start2)

#-------------------------------------------------------------------------------------------------

zeros1 = np.zeros(10,int)
zeros2 = np.zeros((3,4),int)
print("zero array:\n ",zeros1)
print("zero array:\n ",zeros2)


ones1 = np.ones(10,int)
ones2 = np.ones((3,4),int)
print("ones array:\n ",ones1)
print("ones array:\n ",ones2)

full = np.full((3,4),7,int)
print("full array:\n ",full)

#-------------------------------------------------------------------------------------------------

random = np.random.random((4,5))
print("Radom array:\n ",random)

sequence = np.arange(1,20,2)
print("sequence array:\n ",sequence)

#-------------------------------------------------------------------------------------------------

# Vector Matrix and Tensor
