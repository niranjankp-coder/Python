def decor_func(func):
  def inner(name):
    if name == "Ravi":
      print("*" * 30)
      print(f"\t\tHi {name}")
      print("\t\tHow are you")
      print("\t\tvery Good morning")
      print("*" * 30)
    else:
      func(name)
  return inner
      
@decor_func
def greet(name):
  print("Good morning")

greet("Ravi")
greet("Raju")

'''output:
******************************
		Hi Ravi
		How are you
		very Good morning
******************************
Good morning
'''
