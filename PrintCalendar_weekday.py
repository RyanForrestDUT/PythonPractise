'''
# Author: ryan
# Date: Oct. 7 14:00
# Note: print calendar
# Description:
	1800年1月1日为星期三，判断2020年10月1日为星期几？
'''

# 判断是否为闰年
def is_leap_year(year):
	if (year %4 == 0 and year %100 != 0) or (year % 400 == 0):
		return True
	else:
		return False

# 获取指定年份指定月的天数
def get_num_of_days_in_month(year, month):
	if month in (1,3,5,7,8,10,12):
		return 31
	elif month in (4,6,9,11):
		return 30
	elif is_leap_year(year):
		return 29
	else:
		return 28

# 获取自1800年1月1日至指定年月日之间的总天数		
def get_total_num_of_days(year,month,day):
	days = 0
	# 计算截止当年总共多少天
	for y in range(1800,year):
		if is_leap_year(y):
			days += 366
		else:
			days += 365
			
	# 计算截止当年的当月多少天	
	for m in range(1,month):
		days += get_num_of_days_in_month(year,m)
	
	# 计算截止当天
	days += day

	return days

# 题设1800年1月1日为星期三，根据流逝的总天数推算指定年月日为星期几	
def get_week_day(year, month, day):
	 weekday = (3 + (get_total_num_of_days(year, month, day) - 1)% 7 ) % 7
	 return weekday
	
weeks =['星期一','星期二','星期三', '星期四', '星期五', '星期六', '星期日']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	
# 打印日历
def print_calendar(year, month, days):
	print ("\t\t\t ", months[month-1], "\t\t",  year)
	print ('---------------------------------------------------------------------------------------')
	print ("\tSunday \tMonday \tTuesday \tWednesday \tThursday \tFriday \tSaturday")
	
	weekday = get_week_day(year, month, 1)
	if weekday % 7 != 0:
		for i in range(1, weekday+1):
				print("\t", end='')

	ncount = 1			
	for m in range(1, days+1):
		if ((weekday + ncount) % 7 == 0):
			print ('\t', m, "\n")
		else:
			print ('\t', m,end='')
		ncount += 1
	
	print()
	
			
# 测试代码
while True:
	# 读取年月日
	try:
		year = (int)(input("please input a year:"))	
		
		month = (int)(input("please input a month: "))
		if month > 12 or month < 1:
			raise Exception("input param invalid.")
			
		day = (int)(input("please input a day: "))
		# 获取当年当月最大天数
		days = get_num_of_days_in_month(year, month)
		if day > days or day < 1:
			raise Exception("input param invalid.")
	except:
		print ("input param error!!")
		continue
	
	# 测试输出
	weekday = get_week_day(year, month, day)
	print (year, '年', month, '月', day, '日: ', weeks[weekday - 1])

	# 打印日历
	print_calendar(year, month, days)
	
	
