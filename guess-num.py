import random

print('猜數字')
f_num = input('請輸入起始數字: ')
f_num = int(f_num)
s_num = input('請輸入最大數字')
s_num =int(s_num)

num = random.randint(f_num, s_num)
times = 0

print('---------------------')

while True:
	gus = input('請猜並輸入數字: ')
	gus = int(gus)
	times = times + 1

	if gus == num:
		print('---------------------')
		print('猜測次數: ', times, '次')
		print('恭喜猜對了！')
		break
	elif gus > num:
		print('---------------------')
		print('猜測次數: ', times, '次')
		print('猜錯了，答案還要再小一點！再猜一次吧！')
	else:
		print('---------------------')
		print('猜測次數: ', times, '次')
		print('猜錯了，數字還要再大一點！再猜一次吧！')
