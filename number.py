import random

r = random.randint(1, 100)

while True:
	num = input('請從1-100中猜一數字:')
	num = int(num)
	if num == r:
		print('終於猜對了!')
		break

	elif num > r:
		print('比正確答案大')
	elif num < r:
		print('比正確答案小')	