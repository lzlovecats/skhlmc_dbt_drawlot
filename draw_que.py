import random
import time

with open("draw_base.txt", "r") as f:
    que = f.readlines()
draw_lot_list = []
for i in que:
    i = i.strip()
    draw_lot_list.append(i)

draw_num = random.randint(0, len(draw_lot_list) - 1)

print("")
for i in range(0, 3):
    print("Loading...")
    time.sleep(1)
print(f"辯題：{que[draw_num]}")