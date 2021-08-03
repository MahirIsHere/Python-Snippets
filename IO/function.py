def my_function():
  print("Hello from a function")


my_function()

#If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
  print("The youngest child is " + kids[2])


my_function("Oloka",'Nishat',"Pie")


#If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function(**kid):
  print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")

