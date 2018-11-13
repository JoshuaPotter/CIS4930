# Write a program to read in 10 strings from the user. Combine them into one string. Then replace all occurrences of the letter ‘e’ with the letter ‘i’ and print the string

if __name__ == "__main__":
   i = 10
   list = []
   str = ""

   print("Enter ten strings: ")
   while i > 0:
      list.append(input())
      i -= 1

   print(list)

   for x in list:
      str += x

   print(str)

   print(str.replace("e", "i"))