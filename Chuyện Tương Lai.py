# FORTUNE telling game by Matt Hobbs

import sys

print('''Xin chào, chào mừng bạn đến với trò chơi kể chuyện FORTUNE! Bạn sẽ học
về cách chi tiêu và đầu tư tiền của bạn theo cách tốt nhất để có
cuộc sống thoải mái và không căng thẳng''')
print()
playerName = input('Tên của bạn là gì? : ')
print()
print('xin chào ' + playerName +'!')
print()
print('Bạn bao nhiêu tuổi ' + playerName +'?')

playerAge = 0
# nhập một số
# while 1> playerAge hoặc 128 <playerAge:
while not playerAge in range (5,129):
  try:
     playerAge = int(input("Nhập một số nguyên (5 - 128) : "))
  except ValueError:
      print("Vui lòng chỉ nhập số nguyên...")  
      continue

print()
print((str(playerAge)) + ' là độ tuổi hoàn hảo để bắt đầu lập kế hoạch cho tương lai của bạn!')
print()
print('Khi bạn học xong ' + playerName +' sau đó bạn sẽ bao nhiêu tuổi?')

playerAgeAfterSchool = 0
# nhập một số # trong khi 1> người chơi Age AfterSchool hoặc 30 <playerAge afterSchool:
while not playerAgeAfterSchool in range (16,31):
  try:
     playerAgeAfterSchool = int(input("Nhập một số nguyên (16 - 30) : "))
  except ValueError:
      print("Vui lòng chỉ nhập số nguyên ...")  
      continue

print()
print('Được chứ ' + playerName +' Tôi hiểu rằng bạn sẽ ' + str(playerAgeAfterSchool) + ' Khi bạn học xong')
print()
print('Bạn nghĩ bạn sẽ sống bao nhiêu tuổi ' + playerName +'?')

playerDeathAge = 0
# nhập một số 
# # trong khi 1> người chơi Death Age hoặc 30 <playerDeathAge:
while not playerDeathAge in range (40,129):
  try:
     playerDeathAge = int(input("Nhập một số nguyên (40 - 128) : "))
  except ValueError:
      print("Vui lòng chỉ nhập số nguyên...")  
      continue

print('Và bạn nghĩ bạn sẽ bao nhiêu tuổi khi bạn muốn nghỉ hưu?')

playerRetirementAge = 0
# nhập một số
while not playerRetirementAge in range (30,129):
  try:
     playerRetirementAge = int(input("Nhập một số nguyên (30 - 128) : "))
  except ValueError:
      print("Vui lòng chỉ nhập số nguyên...")  
      continue

if playerRetirementAge == playerDeathAge:
    print('Giáo sư! Tôi đoán công cụ này không hữu ích cho bạn, tạm biệt!')
    sys.exit()

playerWorkingYears = playerRetirementAge - playerAgeAfterSchool
playerRetirementYears = playerDeathAge - playerRetirementAge

print()
print('Điều đó có nghĩa là nó sẽ hoạt động cho ' + str(playerWorkingYears)+' năm')
print()
print('Và nó cũng có nghĩa là bạn muốn tận hưởng thời gian nghỉ hưu của mình '+ str(playerRetirementYears)+' năm')
print()
print('Bạn nghĩ mình sẽ kiếm được bao nhiêu tiền mỗi giờ khi bắt đầu làm việc?')

playerHourlyRate = 0
# nhập một số
while True:
  try:
     playerHourlyRate = int(input("Nhập một số nguyên: "))
     break
  except ValueError:
      print("Vui lòng chỉ nhập số nguyên...")  
      continue

print()
print('Và bạn sẽ làm việc bao nhiêu giờ mỗi tuần? (Toàn thời gian điển hình là 40)')

playerHoursPerWeek = 0
# nhập một số
while not playerHoursPerWeek in range (1,80):
  try:
     playerHoursPerWeek = int(input("Nhập một số nguyên (1 - 80) : "))
  except ValueError:
      print("Vui lòng chỉ nhập số nguyên ...")  
      continue

print('Bạn sẽ có bao nhiêu tuần nghỉ lễ mỗi năm?')

playerHolidays = 0
# nhập một số
while not playerHolidays in range (1,53):
  try:
     playerHolidays = int(input("Nhập một số nguyên (1 - 52) : "))
  except ValueError:
      print("Vui lòng chỉ nhập số nguyên ...")  
      continue

playerSalary = playerHourlyRate * playerHoursPerWeek * (52 - playerHolidays)

print('Điều đó có nghĩa là bạn sẽ làm $' + "{:,}".format(playerSalary) +' mỗi năm.')
print()
print('Bạn sẽ chi bao nhiêu tiền cho tiền thuê nhà mỗi tháng?')

playerRentPerMonth = 0
# nhập một số
while True:
  try:
     playerRentPerMonth = int(input("Enter a whole number : "))
     break
  except ValueError:
      print("Vui lòng chỉ nhập số nguyên ...")  
      continue

print('Bạn sẽ chi bao nhiêu mỗi ngày cho thực phẩm?')

playerFoodCost = 0
# nhập một số
while True:
  try:
     playerFoodCost = int(input("Nhập một số nguyên: "))
     break
  except ValueError:
      print("Vui lòng chỉ nhập số nguyên...")  
      continue

playerTotalExpenses = playerRentPerMonth * 12 + playerFoodCost * 365 

print('Tổng chi phí của bạn là $'+ "{:,}".format(playerTotalExpenses)+ ' mỗi năm')
print()
print('Điều này có nghĩa là bạn sẽ có $' + "{:,}".format(playerSalary - playerTotalExpenses) +' còn lại mỗi năm')
print()
print('''Bạn muốn đầu tư bao nhiêu trong số tiền này mỗi năm cho
nghỉ hưu trong tương lai của bạn?''')

playerAnnualInvestment = 0
# nhập một số
while True:
  try:
     playerAnnualInvestment = int(input("Nhập một số nguyên: "))
     break
  except ValueError:
      print("Vui lòng chỉ nhập số nguyên ...")  
      continue

playerRetirementSum = playerWorkingYears * playerAnnualInvestment

print('Đáng kinh ngạc! Điều đó có nghĩa là bạn sẽ đầu tư tổng cộng $' +"{:,}".format(playerRetirementSum))
print('trong những năm làm việc của bạn')
print()
print('Do đó, bạn sẽ có $' +"{:,}".format(int(playerRetirementSum/playerRetirementYears)) +' mỗi năm cho kỳ nghỉ hưu của bạn')
print()
print('So với chi tiêu của bạn, điều này có nghĩa là bạn sẽ có $' +"{:,}".format((int(playerRetirementSum/playerRetirementYears) - playerTotalExpenses)) +' còn lại mỗi năm')
print()

if ((playerRetirementSum/playerRetirementYears) - playerTotalExpenses) > 0:
    print('Tuyệt vời, có vẻ như bạn sẽ có đủ tiền để kéo dài thời gian nghỉ hưu của mình!')
else:
    print("Rất tiếc, có vẻ như bạn sẽ không có đủ tiền để sống qua ngày nghỉ hưu")

#print ('Bạn có nghĩ đây là số tiền đủ để bạn tồn tại?')
#playerSurvive = input ()
print()
input('Nhấn Enter để tiếp tục...')
print()
print('''Nhưng điều này chỉ xảy ra nếu bạn để số tiền đầu tư đó vào ngân hàng
tài khoản kiếm được rất ít tiền lãi .... thay vào đó nếu bạn đầu tư đúng cách,
tự nó có thể phát triển ồ ạt. Đây được gọi là "lãi kép"''')
print()
print('''Tính trung bình, thị trường chứng khoán Mỹ đã tăng trưởng trở lại khoảng 9% mỗi năm
trong 100 năm qua. Hãy xem điều gì sẽ xảy ra khi chúng tôi thêm một số phát triển vào
tiền đầu tư $''' + "{:,}".format(playerAnnualInvestment) + ' mỗi năm.''')
print()
print('Bạn mong đợi mức tăng trưởng bao nhiêu phần trăm mỗi năm?')

playerGrowthExpect = 0
# nhập một số
while not playerGrowthExpect in range (1,101):
  try:
     playerGrowthExpect = int(input("Nhập một số nguyên (9 là số điển hình): "))
  except ValueError:
      print("Vui lòng chỉ nhập số nguyên ...")  
      continue

#playerGrowthExpect = input ()
#playerGrowthExpect = int (playerGrowthExpect)

print('Được rồi bạn đang mong đợi ' + str(playerGrowthExpect)+'% mỗi năm')
print()
playerGrowthExpect = playerGrowthExpect/100

# PMT × {[(1 + r / n) ^ (nt) - 1] / (r / n)} × (1 + r / n)
# Tổng = PMT × p {[(1 + r / n) ^ (nt) - 1] / (r / n)}

# A = giá trị tương lai của khoản đầu tư / khoản vay, bao gồm cả lãi suất
# P = số tiền đầu tư chính (số tiền gửi ban đầu hoặc số tiền cho vay)
# PMT = khoản thanh toán hàng tháng
# r = lãi suất hàng năm (số thập phân)
# n = số lần tiền lãi được cộng lại trên một đơn vị t
# t = thời gian (tháng, năm, v.v.) số tiền được đầu tư hoặc vay để

playerCompoundedTotal = playerAnnualInvestment*((((1+playerGrowthExpect/1)**(1*playerWorkingYears))-1)/(playerGrowthExpect/1))
playerCompoundedTotal = int(playerCompoundedTotal)

print('Ồ! Bây giờ bạn sẽ có $' + "{:,}".format(playerCompoundedTotal) +' thay vì $' + "{:,}".format(playerRetirementSum))
print()
print('Điều này có nghĩa là bây giờ bạn sẽ có $' +"{:,}".format(int(playerCompoundedTotal/playerRetirementYears)) + ' mỗi năm')
print('và chi phí của bạn sẽ là $' +"{:,}".format(playerTotalExpenses) +'.')
print()
print('Cái này có tốt hơn cho bạn không?:')

playerSurvive2 = input()
