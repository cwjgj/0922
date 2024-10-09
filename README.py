import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("时间到！")

def focus_timer(focus_time, break_time):
    while True:
        print(f"开始专注 {focus_time} 分钟...")
        countdown(focus_time * 60)
        print("休息时间！休息一下吧。")
        countdown(break_time * 60)

# 调用函数，设定25分钟专注，5分钟休息
focus_timer(25, 5)
