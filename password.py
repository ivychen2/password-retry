i = 0
print('請輸入密碼，有3次輸入機會')

while i < 3:
	pw = input('請輸入密碼：')
	i = i + 1

	if pw != 'a123456':
		print('密碼錯誤還有', 3-i,'次機會')

	else:	
		print('登入成功')
		break




