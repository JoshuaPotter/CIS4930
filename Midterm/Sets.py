def decorator(func):
   def func_wrapper(x):
      return "<h1>" + x + "</h1>"
   return func_wrapper

def func(name):
   # Sets
   s1 = set("ABCDEF")
   s2 = set("ABCD")
   print(s1)
   print(s2)
   print("Union: " + str(s1.union(s2)))
   print("Intersection: " + str(s1.intersection(s2)))
   print("Difference: " + str(s1.difference(s2)))

   # Decorator
   html = decorator(print)
   print("Welcome, " + name)
   print(html("Welcome, " + name))

if __name__ == "__main__":
   func("Josh")