class RSA(object):
   def __init__(self):
      self.list = []
      self.e = 0
      self.d = 0

   def inputFunc(self):
      numberOfMessages = input("Enter the number of messages: ")
      numberOfMessages = int(numberOfMessages)
      print("Enter the messages: ")
      while numberOfMessages > 0:
         self.list.append(input())
         numberOfMessages = numberOfMessages - 1

   def printFunc(self):
      print(self.list)      

   def primeGen(self, min):
      print()

   def keyGen(self, min):
      print()

   def LCM(self):
      print()

   def GCD(self):
      print()

   def encrypt(self, messageToEncrypt):
      print()

   def decrypt(self, messageToDecrypt):
      print()

   def messages(self):
      print()

# run program
if __name__ == "__main__":
   algorithm = RSA()
   algorithm.inputFunc()
   algorithm.printFunc()

