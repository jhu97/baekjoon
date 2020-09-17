import sys
input = sys.stdin.readline
now = input()
start = input()
now_list = now.split(':')
start_list = start.split(':')
now_time = (int(now_list[0]) * 3600) + (int(now_list[1]) * 60) + int(now_list[2])
start_time = (int(start_list[0]) * 3600) + (int(start_list[1]) * 60) + int(start_list[2])
rest = start_time - now_time
sec = str(rest % 60)
min = str((rest // 60) % 60)
hours = str((rest // 3600) % 24)
time = '{0}:{1}:{2}'.format(hours.zfill(2), min.zfill(2), sec.zfill(2))
print(time)
