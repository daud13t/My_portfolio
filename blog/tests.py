from django.test import TestCase
# Create your tests here.
# class parent:
#       def bark(self):
#             print(self.name+' says woof!')

# class puppy(parent):
#       name = 'bitch'

# aclass = puppy()
# aclass.bark()                 
# print(aclass.name)

class parent:
      name = 'no 1 bitch'
      def bark(self):
            print( self.name+' says woof!')
            
class puppy(parent):
      name = 'bitch'

aclass = puppy()
aclass.bark()                 
print(aclass.name)

