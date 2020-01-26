def getdata() :
  list = []
  numberOfItems = int(input("How many items will be in list?\n"))
  for i in range(0, numberOfItems):
    list.append(input("Insert data: "))    
  return list

def listReverse(list) :
  reversedList = []
  for i in range(len(list) -1, -1, -1) :
    reversedList.append(list[i])

  return reversedList

list = getdata()
print(listReverse(list))