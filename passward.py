print('you have 3 chances to enter the code, be carefule!!!')
passward = 'a123456'
x = 3
while x > 0:
	code = input('please enter the passward: ')
	if code == passward:
		print('Log in success!!')
		break
	else:
		if x > 1:
			print('wrong passward, you have', x - 1, 'chance left')
		else:
			print('wrong passward, you have', x - 1, 'chance left, \nlog in failed')
			break
	x = x - 1
