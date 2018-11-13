def p_decorator(func):
   def func_wrapper(param):
      return "<p>" + func(param) + "</p>"
   return func_wrapper

@p_decorator
def welcome(name):
   return "Welcome, " + name

if __name__ == "__main__":
   print(welcome("Josh"))