import random
with open("draw_base.txt", "r") as f:
    que = f.readlines()
draw_lot_list = []
for i in que:
    i = i.strip()
    draw_lot_list.append(i)

pro_name = input("輸入隊伍1名稱：")
con_name = input("輸入隊伍2名稱：")
c_year = input("輸入第幾屆（輸入中文數字）：")
count = input("輸入比賽場次：")
year = input("輸入比賽日期（年）：")
month = input("輸入比賽日期（月）：")
day = input("輸入比賽日期（日）：")
time = input("輸入比賽時間 （按Enter設定為16:00）：")
room = input("輸入比賽地點：")
if time == "":
    time = "16:00"

name_list = [pro_name, con_name]
pro_num = random.randint(0, 1)
if pro_num == 1:
    con_num = 0
else:
    con_num = 1

draw_num = random.randint(0, len(draw_lot_list) - 1)
print(f"\n校園隨想辯論比賽（第{c_year}屆）賽事資料\n"
      f"比賽場次：{count}\n"
      f"日期：{year}年{month}月{day}日\n"
      f"時間：{time}\n"
      f"地點：{room}室\n"
      f"辯題：{que[draw_num]}"
      f"正方：{name_list[pro_num]}\n"
      f"反方：{name_list[con_num]}\n"
      f"請雙方留意：\n"
      f"1. 兩隊參賽者需於比賽前最少十分鐘到達作賽地點，否則主席有權宣告遲到隊伍失去參賽資格；\n"
      f"2. 是次賽事將會被錄影。若賽事出現任何爭議，聖呂中辯保留翻看及翻聽錄音及錄影的權利。\n"
      f"請兩隊代表收到訊息回覆「ok」，好讓賽務人員確保雙方都收到訊息。🙏🏻")

retry = input("\nInput '1' to redraw, press enter to end the program:")
while retry == '1':
    pro_num = random.randint(0, 1)
    if pro_num == 1:
        con_num = 0
    else:
        con_num = 1
    draw_num = random.randint(0, len(draw_lot_list) - 1)
    print(f"\n校園隨想辯論比賽（第{c_year}屆）賽事資料\n" 
          f"比賽場次：{count}\n"
          f"日期：{year}年{month}月{day}日\n"
          f"時間：{time}\n"
          f"地點：{room}室\n"
          f"辯題：{que[draw_num]}"
          f"正方：{name_list[pro_num]}\n"
          f"反方：{name_list[con_num]}\n"
          f"請雙方留意：\n"
          f"1. 兩隊參賽者需於比賽前最少十分鐘到達作賽地點，否則主席有權宣告遲到隊伍失去參賽資格；\n"
          f"2. 是次賽事將會被錄影。若賽事出現任何爭議，聖呂中辯保留翻看及翻聽錄音及錄影的權利。\n"
          f"請兩隊代表收到訊息回覆「ok」，好讓賽務人員確保雙方都收到訊息。🙏🏻")
    retry = input("\nInput '1' to redraw, press enter to end the program:")
