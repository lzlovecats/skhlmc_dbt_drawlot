import random
with open("teams_base.txt", "r") as f:
    que = f.readlines()
draw_team_list = []
for i in que:
    i = i.strip()
    draw_team_list.append(i)

team = []
draw_num = []
if len(draw_team_list) % 2 == 0:
    for i in range(len(draw_team_list)):
        draw = random.randint(0, len(draw_team_list) - 1)
        while draw in draw_num:
            draw = random.randint(0, len(draw_team_list) - 1)
        draw_num.append(draw)
        team.append(draw_team_list[draw])
    print("")
    for i in range(len(draw_team_list)):
        print(f"Team {i + 1}: {team[i]}")
else:
    skip_team = []
    spec = random.randint(0, len(draw_team_list) - 1)
    draw_num.append(spec)
    for i in range(len(draw_team_list)):
        if i == spec:
            continue
        skip_team.append(draw_team_list[i])
    spec_num = []
    for i in range(len(skip_team)):
        draw = random.randint(0, len(skip_team) - 1)
        while draw in spec_num:
            draw = random.randint(0, len(skip_team) - 1)
        spec_num.append(draw)
        team.append(skip_team[draw])
    print("")
    for i in range(len(skip_team)):
        print(f"Team {i + 1}: {team[i]}")
    print(f"Team {len(skip_team) + 1}: {draw_team_list[spec]}")
