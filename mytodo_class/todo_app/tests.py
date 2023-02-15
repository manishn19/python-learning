from django.test import TestCase

# Create your tests here.

list1 = ['3', '4', '2']
list2 = [3, 4, 2]
list1.sort()
list2.sort()
if list1 == list2:
    print('Equale')
else:
    print('Not Equal')
