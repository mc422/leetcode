# 380. Insert Delete GetRandom O(1)
#
# first, to find value with O(1), you need a hashtable
# second, to randomly select an element with O(1), you need a list so you can randomly choose index
#  and get the element
# So the solution is a hashtabe and a array
# when we remove one element, we copy the last one into it.