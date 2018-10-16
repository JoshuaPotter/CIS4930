# Joshua Potter, jop13
# RSA.py

import random

class RSA(object):
   # Constructor
   def __init__(self):
      self.list = []
      self.e = 0
      self.d = 0
      self.N = 0

   # Get messages from user
   def inputFunc(self):
      # Get the number of entries
      numberOfMessages = int(input("Enter the number of messages: "))

      # Get the entries and append to object list
      print("Enter the messages: ")
      while numberOfMessages > 0:
         self.list.append(int(input()))
         numberOfMessages = numberOfMessages - 1

   # Print message along with number parameter
   def printFunc(self, number):         
      print("message is", number)

   def encryptDecorator(self, message):
      def wrapper():
         print("The encrypted ", message())
      return wrapper

   def decryptDecorator(self, message):
      def wrapper():
         print("The decrypted ", message())
      return wrapper

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
      self.N = p * q
      phi = (p - 1) * (q - 1)

      # calculate e for 1 < e < phi
      # look for numbers that satisfy GCD(e, phi) == 1
      self.e = random.randint(1, phi)
      while self.gcd(self.e, phi) != 1:
         self.e = random.randint(1, phi)

      # calculate d if e and phi are co-primes
      self.d = self.inverse(self.e, phi)

      print("N is", self.N)
      print("e is", self.e)

   def encrypt(self, messageToEncrypt):
      return pow(messageToEncrypt, self.e, self.N)

   def decrypt(self, messageToDecrypt):
      return pow(messageToDecrypt, self.d, self.N)

   def messages(self):
      self.inputFunc()
      self.keyGen(int(input("Enter the minimum value for the prime numbers: ")))
      encrypted = []
      for i in self.list:
         x = self.encrypt(i)
         encrypted.append(x)
         print("Encrypted: ", x)

      for i in encrypted:
         x = self.decrypt(i)
         print("Decrypted: ", x)

   '''
   Helper Functions
   '''

   # Lowest common multiple
   def lcm(self, first, second):
      return first * second

   # Greatest common divisor 
   def gcd(self, first, second):
      if second == 0:
         return first
      else:
         return self.gcd(second, (first % second))

   # Multiplicative inverse
   # Calculated using euclidian algorithm
   # Source: https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
   def inverse(self, e, phi):
      phiTemp = phi
      p = 0
      x = 1

      if phi == 1:
         return 0

      # step through euclidian algorithm 
      while e > 1:
         q = e // phiTemp
         t = phiTemp
         phiTemp = e % phiTemp
         e = t
         t = p
         p = x - q * p
         x = t

      # if negative, add phi
      if x < 0:
         x = x + phi

      return x

# run program
if __name__ == "__main__":
   algorithm = RSA()
   algorithm.messages()
