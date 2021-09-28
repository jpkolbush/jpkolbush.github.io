import numpy.random as nr
from enum import Enum

WEEKS_COMPLETE = 3


class T(Enum):
    KOLBUSH = 1
    JON = 2
    JOE = 3
    NICK = 4
    MATTY = 5
    MCCLURE = 6
    LOGAN_DUC = 7
    STEVE = 8
    JAMES = 9
    BRYCE = 10
    HUNYAR = 11
    SCOTT = 12

def getConf(team):
    if team in [T.KOLBUSH, T.JOE, T.MCCLURE, T.LOGAN_DUC, T.STEVE, T.BRYCE]:
        return 0
    else:
        return 1

SCHEDULE = [
    [ T.LOGAN_DUC, T.STEVE, T.JOE, T.MCCLURE, T.MATTY, T.NICK, T.SCOTT, T.HUNYAR, T.JAMES, T.JON, T.LOGAN_DUC, T.JOE, T.BRYCE,],
    [ T.MATTY, T.HUNYAR, T.JAMES, T.NICK, T.JOE, T.LOGAN_DUC, T.STEVE, T.BRYCE, T.MCCLURE, T.KOLBUSH, T.MATTY, T.JAMES, T.SCOTT,],
    [ T.BRYCE, T.LOGAN_DUC, T.KOLBUSH, T.STEVE, T.JON, T.MATTY, T.NICK, T.SCOTT, T.HUNYAR, T.JAMES, T.MCCLURE, T.KOLBUSH, T.LOGAN_DUC,],
    [ T.HUNYAR, T.SCOTT, T.MATTY, T.JON, T.MCCLURE, T.KOLBUSH, T.JOE, T.LOGAN_DUC, T.STEVE, T.BRYCE, T.JAMES, T.SCOTT, T.HUNYAR,],
    [ T.JON, T.JAMES, T.NICK, T.SCOTT, T.KOLBUSH, T.JOE, T.LOGAN_DUC, T.STEVE, T.BRYCE, T.MCCLURE, T.JON, T.HUNYAR, T.JAMES,],
    [ T.STEVE, T.BRYCE, T.LOGAN_DUC, T.KOLBUSH, T.NICK, T.SCOTT, T.HUNYAR, T.JAMES, T.JON, T.MATTY, T.JOE, T.BRYCE, T.STEVE,],
    [ T.KOLBUSH, T.JOE, T.MCCLURE, T.BRYCE, T.JAMES, T.JON, T.MATTY, T.NICK, T.SCOTT, T.HUNYAR, T.KOLBUSH, T.STEVE, T.JOE,],
    [ T.MCCLURE, T.KOLBUSH, T.BRYCE, T.JOE, T.HUNYAR, T.JAMES, T.JON, T.MATTY, T.NICK, T.SCOTT, T.BRYCE, T.LOGAN_DUC, T.MCCLURE,],
    [ T.SCOTT, T.MATTY, T.JON, T.HUNYAR, T.LOGAN_DUC, T.STEVE, T.BRYCE, T.MCCLURE, T.KOLBUSH, T.JOE, T.NICK, T.JON, T.MATTY,],
    [ T.JOE, T.MCCLURE, T.STEVE, T.LOGAN_DUC, T.SCOTT, T.HUNYAR, T.JAMES, T.JON, T.MATTY, T.NICK, T.STEVE, T.MCCLURE, T.KOLBUSH,],
    [ T.NICK, T.JON, T.SCOTT, T.JAMES, T.STEVE, T.BRYCE, T.MCCLURE, T.KOLBUSH, T.JOE, T.LOGAN_DUC, T.SCOTT, T.MATTY, T.NICK,],
    [ T.JAMES, T.NICK, T.HUNYAR, T.MATTY, T.BRYCE, T.MCCLURE, T.KOLBUSH, T.JOE, T.LOGAN_DUC, T.STEVE, T.HUNYAR, T.NICK, T.JON,]
]

# std = 20.77989
std = 23
week1Weight = 0.1
week2Weight = 0.381228202347
weight = 0.465214410626

def sortSeed(teamRes):
    return teamRes["Wins"] *100000 + teamRes["PF"]
def sortTeamEnum(teamRes):
    return teamRes["Team"].value
def sortSeedEnd(teamRes):
    return teamRes["Seed"]

def generateSeason():
    scores = [
        [122.46,65.7,62.64,    0,0,0,0,0,0,0,0,0,0,0,0,0,0],#    KOLBUSH = 1
        [121.48,99.32,105.34,    0,0,0,0,0,0,0,0,0,0,0,0,0,0],#    JON = 2
        [135.56,125.7,112.14,    0,0,0,0,0,0,0,0,0,0,0,0,0,0],#    JOE = 3
        [103.62,98.48,86.72,    0,0,0,0,0,0,0,0,0,0,0,0,0,0],#    NICK = 4
        [109.9,126.74,136.98,     0,0,0,0,0,0,0,0,0,0,0,0,0,0],#    MATTY = 5
        [107.88,129.48,95.32,    0,0,0,0,0,0,0,0,0,0,0,0,0,0],#    MCCLURE = 6
        [123.8,110.16,124.12,     0,0,0,0,0,0,0,0,0,0,0,0,0,0],#    LOGAN_DUC = 7
        [110.94,83.14,96.84,    0,0,0,0,0,0,0,0,0,0,0,0,0,0],#    STEVE = 8
        [82.02,116.1,83.74,     0,0,0,0,0,0,0,0,0,0,0,0,0,0],#    JAMES = 9
        [113.98,137.92,91,    0,0,0,0,0,0,0,0,0,0,0,0,0,0],#    BRYCE = 10
        [133.86,127.52,143.22,    0,0,0,0,0,0,0,0,0,0,0,0,0,0],#    HUNYAR = 11
        [99,95.76,76.98,        0,0,0,0,0,0,0,0,0,0,0,0,0,0] #   SCOTT = 12
    ]
    #List of results for each team
    ret = []
    for team in T:
        ret.append({"Team": team, "Wins": 0, "Losses": 0, "PF": 0, "Seed": 0, "Rd1": 0, "Rd2": 0,
                            "Playoffs": 0, "Champion": 0, "Bottom 4": 0, "Bolan": 0})

    #Get averages
    league_tot = 0
    team_tots = [0] * 12
    for team_idx in range(12):
        for week_idx in range(WEEKS_COMPLETE):
            team_tots[team_idx] += scores[team_idx][week_idx]
            league_tot += scores[team_idx][week_idx]
    league_avg = league_tot/(12.0 * WEEKS_COMPLETE)
    team_avgs = [team_tots[i]/WEEKS_COMPLETE for i in range(12)]
    

    #Simulate scores for the rest of the season
    for team_idx in range(12):
        if WEEKS_COMPLETE == 1:
            sim_avg = week1Weight * team_avgs[team_idx] + (1- week1Weight)*league_avg
        elif WEEKS_COMPLETE == 2:
            sim_avg = week2Weight * team_avgs[team_idx] + (1- week2Weight)*league_avg
        else:
            sim_avg = weight * team_avgs[team_idx] + (1- weight)*league_avg
        scores[team_idx][WEEKS_COMPLETE:] = nr.normal(sim_avg, std, (17- WEEKS_COMPLETE)) 
        ret[team_idx]["PF"] = sum(scores[team_idx][:13])
    
    #Determine Record for regular season & two week tots for playoffs
    for team_idx in range(12):
        for week in range(13):
            opponent = SCHEDULE[team_idx][week]
            this_score = scores[team_idx][week]
            opp_score = scores[opponent.value - 1][week]
            if this_score > opp_score:
                ret[team_idx]["Wins"] += 1
            elif this_score < opp_score:
                ret[team_idx]["Losses"] += 1
            else:
                ret[team_idx]["Wins"] += 0.5
                ret[team_idx]["Losses"] += 0.5
        ret[team_idx]["Rd1"] = scores[team_idx][13] + scores[team_idx][14]
        ret[team_idx]["Rd2"] = scores[team_idx][15] + scores[team_idx][16]

    #Detrimine Seeding, Playoffs, & Bottom 4
    ret.sort(key=sortSeed, reverse=True)

    second_seed_idx = 1
    while getConf(ret[second_seed_idx]["Team"]) == getConf(ret[0]["Team"]):
        second_seed_idx += 1
    ret.insert(1, ret.pop(second_seed_idx))

    for seed in range(1,13):
        ret[seed - 1]["Seed"] = seed
        if seed < 5:
            ret[seed - 1]["Playoffs"] = True
        elif seed > 8:
            ret[seed - 1]["Bottom 4"] = True
    
    #Determine champ and bolun
    champA = 0 if ret[0]["Rd1"] > ret[3]["Rd1"] else 3
    champB = 1 if ret[1]["Rd1"] > ret[2]["Rd1"] else 2
    champ = champA if ret[champA]["Rd2"] > ret[champB]["Rd2"] else champB
    ret[champ]["Champion"] = True

    bolanA = 8 if ret[8]["Rd1"] < ret[11]["Rd1"] else 11
    bolanB = 9 if ret[9]["Rd1"] < ret[10]["Rd1"] else 10
    bolan = bolanA if ret[bolanA]["Rd2"] < ret[bolanB]["Rd2"] else bolanB
    ret[bolan]["Bolan"] = True

    #Sort it back in team order
    ret.sort(key=sortTeamEnum)
    return ret
        
def Bambitron(n):
    retAgr = []
    for team in T:
        retAgr.append({"Team": team, "Wins": 0, "Losses": 0, "PF": 0, "Seed": 0, "Rd1": 0, "Rd2": 0,
                            "Playoffs": 0, "Champion": 0, "Bottom 4": 0, "Bolan": 0})
    keys = retAgr[0].keys()
    
    #Sum up results
    for i in range(n):
        ret = generateSeason()
        for team_idx in range(12):
            for key in keys:
                if key != "Team":
                    retAgr[team_idx][key] += ret[team_idx][key]
    
    #Average out results
    for team_idx in range(12):
        for key in keys:
            if key != "Team":
                retAgr[team_idx][key] /= n
    
    retAgr.sort(key=sortSeedEnd)

    #write results
    f = open("BambitronResults.csv", "w")
    f.write("Team,Wins,Losses,Seed,PF, Playoffs,Haley,Bottom 4,Bolan\n")
    for team in retAgr:
        f.write("{},{},{},{},{},{},{},{},{}\n".format(team["Team"].name, round(team["Wins"], 1), round(team["Losses"],1),
                                round(team["Seed"], 1), round(team["PF"], 1), round(team["Playoffs"]*100, 2), round(team["Champion"]*100, 2),
                                 round(team["Bottom 4"]*100, 2), round(team["Bolan"]*100, 2)))
    f.close()


def testSchedule():
    testDict = {}
    for team in T:
        testDict[team] = 0
    i = 1
    for sched in SCHEDULE:
        if len(sched) != 13:
            print("A schedule has wrong number of weeks")
            return
        week = 0
        for opp in sched:
            testDict[opp] = testDict[opp] + 1
            if SCHEDULE[opp.value - 1][week] != T(i):
                print("Error: Mismatch playors")
                return
            week += 1
        i += 1
    print(testDict)

Bambitron(50000)