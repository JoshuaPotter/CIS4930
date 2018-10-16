import random

class RSA(object):
   # Constructor
   def __init__(self):
      self.list = []
      self.e = 0
      self.d = 0

   # Get messages from user
   def inputFunc(self):
      # Get the number of entries
      numberOfMessages = input("Enter the number of messages: ")
      numberOfMessages = int(numberOfMessages)

      # Get the entries and append to object list
      print("Enter the messages: ")
      while numberOfMessages > 0:
         self.list.append(input())
         numberOfMessages = numberOfMessages - 1

   # Print message along with number parameter
   def printFunc(self, number):
      print("The message is", number)

   # Generate the next prime number after min parameter
   def primeGen(self, min):
      isPrime = False
      if min == 1:
         prime = 2
      else:
         # Iterate past "min" number until we find a prime
         iterator = min + 1
         while isPrime == False:
            index = 2
            while index < iterator:
               if iterator % index == 0:
                  isPrime = False
                  index = iterator
               else:
                  isPrime = True
               index = index + 1
            iterator = iterator + 1
         prime = iterator - 1
      return prime

   # Generate RSA keys from prime numbers
   def keyGen(self, min):
      p = self.primeGen(min)
      q = self.primeGen(p)
      N = p * q
      self.e = random.randint(1, self.totient(p, q))

   def encrypt(self, messageToEncrypt):
      print()

   def decrypt(self, messageToDecrypt):
      print()

   def messages(self):
      print()

   '''
   Helper Functions
   '''

   # Lowest common multiple
   def LCM(self):
      print()

   # Greatest common denominator 
   def GCD(self):
      print()
   
   # Calculates phi of N
   def totient(self, p, q):
      return ((p-1)*(q-1))


# run program
if __name__ == "__main__":
   algorithm = RSA()
   #  algorithm.inputFunc()
   #  algorithm.printFunc(5)
   x = 205
   print("The next prime number to", x, "is", algorithm.primeGen(x))
