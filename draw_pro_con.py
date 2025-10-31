import random
import time

t_list = []
name1 = input("輸入隊伍1名稱：")
name2 = input("輸入隊伍2名稱：")
draw_num = random.randint(0, 1)
if draw_num == 0:
    sec_num = 1
else:
    sec_num = 0
t_list.append[name1]
t_list.append[name2]



print("")
print(f"正方： {t_list[draw_num]}")
print(f"反方： {t_list[sec_num]}")

