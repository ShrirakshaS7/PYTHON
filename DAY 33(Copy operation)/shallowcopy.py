#Shallow copy
#1
import copy
original_list=[10,20,[1,2,3,4]]
shallow_copy_list=copy.copy(original_list)
shallow_copy_list[2][3]=98
print(original_list)
print()
print(shallow_copy_list)