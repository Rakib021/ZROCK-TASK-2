def vowelCount(name):
  name = name.lower()
  
  vowels = {'a','e','i','o','u'}
  
  counter =0
  
  for char in name:
    if char in vowels:
      counter+=1
  return counter


name =input("Enter string :")
print("number of vowels :",vowelCount(name))