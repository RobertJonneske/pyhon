print("Enter Marks Obtained in 5 Subjects: ")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

tot = markOne+markTwo+markThree+markFour+markFive
avg = tot/5
if avg>70 <100:
  print("grade A")
elif avg>60 <69:
  print("grade B")
elif avg>50 <59:
  print("grade C")
elif avg>40 <49:
  print("grade D")
elif avg>o <39:
  print("grade fail")
else:
  print("invalid input")