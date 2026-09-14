def decor_func(func):
  def wrapper(a,b):
    print("*"* 30)
    func(a,b)
    print("*"* 30)
  return wrapper

def add(a,b):
  print(f"\t\tsum is: {a+b}")


dec_function = decor_func(add)
dec_function(10, 20)

'''
output:
******************************
		sum is: 30
******************************
'''
