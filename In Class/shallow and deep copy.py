' shallow copy'

import copy
list1 = [1,2,3,4]
list2 = [5,6,7,8]
# 2D list
my_list =[list1,list2]
#creates a shallow copy of the new list
new_list = copy.copy(my_list)

'deep copy'
#deep includes imutables like strings, ints and floats
import copy
list1 = [1,2,3,4]
list2 = [5,6,7,8]
# 2D list
my_list =[list1,list2]
new_list = copy.deepcopy(my_list)
