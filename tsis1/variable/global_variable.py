x = "awesome"

def myfunc():      #otkryli function
  global x
  x = "fantastic"

myfunc()            # zakryli function

print("Python is " + x)

"""
global  inside  function sdelali
potomu otvet budet fantastic
"""
