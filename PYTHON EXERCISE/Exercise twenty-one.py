#计算日期间隔
import datetime
birthday = "1997-5-20"
birthday_date = datetime.datetime.strptime(birthday, "%Y-%m-%d")
print(birthday_date, type(birthday_date))

curr_datetime = datetime.datetime.now()
print(curr_datetime, type(curr_datetime))
#gpt
import datetime

birthday_date = datetime.datetime(1997, 5, 20)
print(birthday_date, type(birthday_date))

curr_datetime = datetime.datetime.now()
print(curr_datetime, type(curr_datetime))
