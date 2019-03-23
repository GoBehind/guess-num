import random
num = random.randint(1, 100)

print('猜數字, 請猜一個介於1~100(包含)之間的數字')

while True:
	gus = input('請輸入數字: ')
	gus = int(gus)

	if gus == num:
		print('恭喜猜對了！')
		break
	elif gus > num:
		print('猜錯了，答案還要再小一點！再猜一次吧！')
	else:
		print('猜錯了，數字還要再大一點！再猜一次吧！')
