import time

def focus_timer(minutes):
    total_seconds = minutes * 60
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
    print("时间到！休息一下吧！")

# 调用函数，设定25分钟的专注时间
focus_timer(25)
