#The difference between del and clear in List methods

a=[1,2,3,4,5,6]
del a[0]
print(a)
#result of print(a) [2,3,4,5,6]


a=[1,2,3,4,5,6]
a.clear()
print(a) 
# result is [] empty braket


 # in  "del" operation only that patricalur index of element will be delete 
 # in "clear" operation total elements will be delete or clear       


#i think 2 methods to use reverse a list that is
#1.using nagitive  indexing 
a=[1,2,3,4,5,6,7]
b=a[::-1]
print(b)

#2.in list methods "reverse()"
a=[1,2,3,4,5,6,7]
a.reverse()
print(a)

#difference between copy and direct assignment
#1 "copy"
a=[1,2,3,4]
b=a.copy()
a.append(6)
print(b)
# result is [1,2,3,4] 

# direct assignment
a=[1,2,3,4]
b=a
a.append(6)
print(a)
#result is [1,2,3,4,6]

#finally the result is ... 1.in "copy" operation that "append" operation is not appleid
#                           not only "append operation" any operation should not change

#                          2.in "direct assignment" that "append" operation is applied
#                            direct assignment take changes


