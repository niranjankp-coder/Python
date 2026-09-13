def decorator_func(func):
  def inner(a,b):
    print("*"* 10)
    func(a,b)
    print("*"* 10)
  return inner

@decorator_func
def add(a,b):
  print(f"sum is: {a+b}")

add(20, 30)
