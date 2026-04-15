#deep copy
#1
import copy
original_list=[10,20,[1,2,3,4]]
deep_copy_list=copy.deepcopy(original_list)
deep_copy_list[2][3]=90
print(original_list)
print()
print(deep_copy_list)