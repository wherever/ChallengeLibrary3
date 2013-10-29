#class gains attributes of another class
# call Book from within Shelf
class Library(object):
   def __init__ (self,name):
      self.name='X'
   def printName(self):
      print self.name
   
class Shelf(Library):
   def __init__(self,name,bookName):
      super(Shelf,self).__init__ (name)
      self.book=Book(bookName)
      
class Book:
   def __init__ (self,bookName):
      self.name=bookName
      
sh=Shelf('A','Huck Finn')
sh.printName()
print sh.book.name
# Shelf X contains Huck Finn
X
Huck Finn