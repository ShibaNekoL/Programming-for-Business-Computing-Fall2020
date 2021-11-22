# define 四捨五入function
def chop(avg):
    avg = int(avg*100) / 100
    return avg if avg > 0 else 0


# define player_avg
def player_avg(seasons, records, player_number):

    hit = int()
    at_bats = int()

    # run each row of records
    for i in range(len(records)):
        if records[i][1] == player_number:
            # run each season
            for j in seasons:
                if records[i][2] == j:
                    # 累加安打數
                    hit += records[i][4]
                    # 累加打數
                    at_bats += records[i][3]
    # 打擊率
    player_hitrate = hit / at_bats
    # 四捨五入到小數點第二位
    player_hitrate = chop(player_hitrate)
    return player_hitrate


# define team_avg
def team_avg(seasons, records, teamname):

    hit = int()
    at_bats = int()

    # run each row of records
    for i in range(len(records)):
        # team
        if records[i][0] == teamname:
            for j in seasons:
                if records[i][2] == j:
                    # 累加安打數
                    hit += records[i][4]
                    # 累加打數
                    at_bats += records[i][3]
    # 打擊率
    team_hitrate = hit / at_bats
    team_hitrate = chop(team_hitrate)
    return team_hitrate


# define best_player
def best_player(seasons, records):

    season_player_hitrate = list()
    # run each row of records
    for i in range(len(records)):
        # run each season
        for j in seasons:
            if records[i][2] == j:
                # 安打數
                hit = records[i][4]
                # 打數
                at_bats = records[i][3]
                # 打擊率
                hitrate = hit / at_bats
                # 將season, 球員編號, 打數, 打擊率 合成二維list
                season_player_hitrate.append([j, records[i][1], records[i][3], hitrate])

    list_player = list()

    # 計算單一季節誰是最佳球員
    for j in seasons:

        hitrate_of_one_season = list()
        list_bestplayer = list()
        list_bestplayerbat = list()
        # 把單一季節每個球員打擊率加進一個新list
        for i in range(len(season_player_hitrate)):
            if season_player_hitrate[i][0] == j:
                hitrate_of_one_season.append(season_player_hitrate[i][3])
        # 最大打擊率
        maxhitrate = max(hitrate_of_one_season)

        # 找出哪些球員和打數擁有最大打擊率
        for k in range(len(season_player_hitrate)):
            if season_player_hitrate[k][3] == maxhitrate:
                # 最大打擊率球員list
                list_bestplayer.append(season_player_hitrate[k][1])
                # 最大打擊率打數list
                list_bestplayerbat.append(season_player_hitrate[k][2])

        # 找出打數較少的球員
        if list_bestplayerbat.count(min(list_bestplayerbat)) == 1:
            player = list_bestplayer[list_bestplayerbat.index(min(list_bestplayerbat))]
            list_player.append(player)
        # 若打數相同，則找號碼數字較小的球員
        else:
            # 找出打數相同球員
            samebat = list()
            for m in range(len(list_bestplayerbat)):
                if list_bestplayerbat[m] == min(list_bestplayerbat):
                    samebat.append(list_bestplayer[m])
            # 找號碼小的球員
            player = min(samebat)
            list_player.append(player)

    return list_player


# define best_team
def best_team(seasons, records):
    season_team_hitrate = list()
    teamlist = list()
    hit = int()
    at_bats = int()
    for i in range(len(records)):
        if teamlist.count(records[i][0]) < 1:
            teamlist.append(records[i][0])
    # run each season
    for j in seasons:
        # run each team
        for k in teamlist:
            # run each row of records
            for i in range(len(records)):
                if records[i][2] == j and records[i][0] == k:
                    # 安打數
                    hit += records[i][4]
                    # 打數
                    at_bats += records[i][3]
            # 團隊打擊率
            if at_bats != 0:
                hitrate = hit / at_bats
            else:
                hitrate = 0
            # 將season, 球隊編號, 打數, 打擊率 合成二維list
            season_team_hitrate.append([j, k, at_bats, hitrate])

    list_team = list()

    # 計算單一季節誰是最佳球隊
    for j in seasons:

        hitrate_of_one_season = list()
        list_bestteam = list()
        list_bestteambat = list()
        # 把單一季節每個球隊打擊率加進一個新list
        for i in range(len(season_team_hitrate)):
            if season_team_hitrate[i][0] == j:
                hitrate_of_one_season.append(season_team_hitrate[i][3])
        # 最大打擊率
        maxhitrate = max(hitrate_of_one_season)

        # 找出哪些球隊和打數擁有最大打擊率
        for k in range(len(season_team_hitrate)):
            if season_team_hitrate[k][3] == maxhitrate:
                # 最大打擊率球隊list
                list_bestteam.append(season_team_hitrate[k][1])
                # 最大打擊率打數list
                list_bestteambat.append(season_team_hitrate[k][2])

        # 找出打數較少的球隊
        if list_bestteambat.count(min(list_bestteambat)) == 1:
            team = list_bestteam[list_bestteambat.index(min(list_bestteambat))]
            list_team.append(team)
        # 若打數相同，則找號碼數字較小的球隊
        else:
            # 找出打數相同球隊
            samebat = list()
            for m in range(len(list_bestteambat)):
                if list_bestteambat[m] == min(list_bestteambat):
                    samebat.append(list_bestteam[m])
            # 找號碼小的球隊
            team = min(samebat)
            list_team.append(team)
    return list_team


# input records
list_records = list()

while True:
    line = input()
    # stop input if input LINESTOP
    if line == "RECORDSTOP":
        break
    else:
        linesplit = line.split(",")
        # str to int
        for i in range(1, len(linesplit)):
            linesplit[i] = int(linesplit[i])
        list_records.append(linesplit)


# input function
print_list = list()

while True:
    player_avg_hit = list()
    team_avg_hit = list()
    bestplayer = list()
    bestteam = list()

    list_seasons = list()
    line = input()
    # stop input if input LINESTOP
    if line == "FUNCTIONSTOP":
        break
    else:
        # data cleaning
        # split each part
        linesplit = line.split(" ")

        # part 1 str to int
        functiontype = int(linesplit[0])

        # split part 2
        linesplit[1] = linesplit[1].split(",")
        # part 2 str to int
        for i in range(len(linesplit[1])):
            list_seasons.append(int(linesplit[1][i]))

        # calculate
        # 計算球員打擊率
        if functiontype == 1:
            number = int(linesplit[2])
            player_avg_hit = player_avg(seasons=list_seasons, records=list_records, player_number=number)
            print_list.append([player_avg_hit])
        # 計算球隊打擊率
        if functiontype == 2:
            team = linesplit[2]
            team_avg_hit = team_avg(seasons=list_seasons, records=list_records, teamname=team)
            print_list.append([team_avg_hit])
        # 找出表現最佳球員
        if functiontype == 3:
            bestplayer = best_player(seasons=list_seasons, records=list_records)
            print_list.append(bestplayer)
        # 找出表現最佳球隊
        if functiontype == 4:
            bestteam = best_team(seasons=list_seasons, records=list_records)
            print_list.append(bestteam)

# output
for i in range(len(print_list)):
    for j in range(len(print_list[i])):
        if j == 0:
            output = str(print_list[i][0])
        else:
            output = output + "," + str(print_list[i][j])
    print(output)
    # print(*print_list[i], sep=",")
