import time

def time_dec(func):
    
  def wrapper(*arg):
      t = time.clock()
      res = func(*arg)
      print(func.__name__, time.clock()-t)
      return res

  return wrapper
