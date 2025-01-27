color = "Green"
try:
  length = len(color)
except NameError:
  print("Check the variable name")
else:
    print("Total Length ",length)
