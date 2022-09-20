import numpy.random as nr
from enum import Enum
import copy


class T(Enum):
    STD_BUSH = 1
    JON = 2
    JOE = 3
    NICK = 4
    MATTY = 5
    MCCLURE = 6
    LOGAN = 7
    STEVE = 8
    JAMES = 9
    BRYCE = 10
    HUNYAR = 11
    DUC = 12


def getConf(team):
    if team in [T.DUC, T.JOE, T.MCCLURE, T.LOGAN, T.STEVE, T.BRYCE]:
        return 0
    else:
        return 1

SCHEDULE = [
    [T.MATTY, T.JON, T.HUNYAR, T.JAMES, T.NICK, T.DUC, T.STEVE, T.MCCLURE, T.BRYCE, T.LOGAN, T.JOE, T.HUNYAR, T.MATTY],
    [T.NICK, T.STD_BUSH, T.JAMES, T.MATTY, T.HUNYAR, T.MCCLURE, T.BRYCE, T.LOGAN, T.JOE, T.DUC, T.STEVE, T.MATTY, T.JAMES],
    [T.MCCLURE, T.LOGAN, T.STEVE, T.BRYCE, T.DUC, T.NICK, T.JAMES, T.HUNYAR, T.JON, T.MATTY, T.STD_BUSH, T.DUC, T.STEVE],
    [T.JON, T.JAMES, T.MATTY, T.HUNYAR, T.STD_BUSH, T.JOE, T.DUC, T.STEVE, T.MCCLURE, T.BRYCE, T.LOGAN, T.JAMES, T.HUNYAR],
    [T.STD_BUSH, T.HUNYAR, T.NICK, T.JON, T.JAMES, T.STEVE, T.MCCLURE, T.BRYCE, T.LOGAN, T.JOE, T.DUC, T.JON, T.STD_BUSH],
    [T.JOE, T.DUC, T.LOGAN, T.STEVE, T.BRYCE, T.JON, T.MATTY, T.STD_BUSH, T.NICK, T.JAMES, T.HUNYAR, T.STEVE, T.BRYCE],
    [T.BRYCE, T.JOE, T.MCCLURE, T.DUC, T.STEVE, T.JAMES, T.HUNYAR, T.JON, T.MATTY, T.STD_BUSH, T.NICK, T.BRYCE, T.DUC],
    [T.DUC, T.BRYCE, T.JOE, T.MCCLURE, T.LOGAN, T.MATTY, T.STD_BUSH, T.NICK, T.JAMES, T.HUNYAR, T.JON, T.MCCLURE, T.JOE],
    [T.HUNYAR, T.NICK, T.JON, T.STD_BUSH ,T.MATTY, T.LOGAN, T.JOE, T.DUC, T.STEVE, T.MCCLURE, T.BRYCE, T.NICK, T.JON],
    [T.LOGAN, T.STEVE, T.DUC, T.JOE, T.MCCLURE, T.HUNYAR, T.JON, T.MATTY, T.STD_BUSH, T.NICK, T.JAMES, T.LOGAN, T.MCCLURE],
    [T.JAMES, T.MATTY, T.STD_BUSH, T.NICK, T.JON, T.BRYCE, T.LOGAN, T.JOE, T.DUC, T.STEVE, T.MCCLURE, T.STD_BUSH, T.NICK],
    [T.STEVE, T.MCCLURE, T.BRYCE, T.LOGAN, T.JOE, T.STD_BUSH, T.NICK, T.JAMES, T.HUNYAR, T.JON, T.MATTY, T.JOE, T.LOGAN]
]

f = open("scores.csv", "r")
lines = f.readlines()
SCORES = []
for line in lines:
    lineSplit = line.rstrip("\n").split(",")[1:]
    SCORES.append([float(data) for data in lineSplit])
f.close()

WEEKS_COMPLETE = len(SCORES[0])

# std = 20.77989
std = 23
week1Weight = 0.05
week2Weight = 0.3
weight = 0.465214410626


def sortSeed(teamRes):
    return teamRes["Wins"] * 100000 + teamRes["PF"]


def sortTeamEnum(teamRes):
    return teamRes["Team"].value


def sortSeedEnd(teamRes):
    return teamRes["Seed"]


def generateSeason():
    scores = copy.deepcopy(SCORES)
    # List of results for each team
    ret = []
    for team in T:
        ret.append(
            {
                "Team": team,
                "Wins": 0,
                "Losses": 0,
                "PF": 0,
                "Seed": 0,
                "Rd1": 0,
                "Rd2": 0,
                "Playoffs": 0,
                "Champion": 0,
                "Bottom 4": 0,
                "Bolan": 0,
            }
        )

    # Get averages
    league_tot = 0
    team_tots = [0] * 12
    for team_idx in range(12):
        for week_idx in range(WEEKS_COMPLETE):
            team_tots[team_idx] += scores[team_idx][week_idx]
            league_tot += scores[team_idx][week_idx]
    league_avg = league_tot / (12.0 * WEEKS_COMPLETE)
    team_avgs = [team_tots[i] / WEEKS_COMPLETE for i in range(12)]

    # Simulate scores for the rest of the season
    for team_idx in range(12):
        if WEEKS_COMPLETE == 1:
            sim_avg = week1Weight * team_avgs[team_idx] + (1 - week1Weight) * league_avg
        elif WEEKS_COMPLETE == 2:
            sim_avg = week2Weight * team_avgs[team_idx] + (1 - week2Weight) * league_avg
        else:
            sim_avg = weight * team_avgs[team_idx] + (1 - weight) * league_avg
        scores[team_idx][WEEKS_COMPLETE:] = nr.normal(
            sim_avg, std, (17 - WEEKS_COMPLETE)
        )
        ret[team_idx]["PF"] = sum(scores[team_idx][:13])

    # Determine Record for regular season & two week tots for playoffs
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

    # Detrimine Seeding, Playoffs, & Bottom 4
    ret.sort(key=sortSeed, reverse=True)

    second_seed_idx = 1
    while getConf(ret[second_seed_idx]["Team"]) == getConf(ret[0]["Team"]):
        second_seed_idx += 1
    ret.insert(1, ret.pop(second_seed_idx))

    for seed in range(1, 13):
        ret[seed - 1]["Seed"] = seed
        if seed < 5:
            ret[seed - 1]["Playoffs"] = True
        elif seed > 8:
            ret[seed - 1]["Bottom 4"] = True

    # Determine champ and bolun
    champA = 0 if ret[0]["Rd1"] > ret[3]["Rd1"] else 3
    champB = 1 if ret[1]["Rd1"] > ret[2]["Rd1"] else 2
    champ = champA if ret[champA]["Rd2"] > ret[champB]["Rd2"] else champB
    ret[champ]["Champion"] = True

    bolanA = 8 if ret[8]["Rd1"] < ret[11]["Rd1"] else 11
    bolanB = 9 if ret[9]["Rd1"] < ret[10]["Rd1"] else 10
    bolan = bolanA if ret[bolanA]["Rd2"] < ret[bolanB]["Rd2"] else bolanB
    ret[bolan]["Bolan"] = True

    # Sort it back in team order
    ret.sort(key=sortTeamEnum)
    return ret


def Bambitron(n):
    retAgr = []
    for team in T:
        retAgr.append(
            {
                "Team": team,
                "Wins": 0,
                "Losses": 0,
                "PF": 0,
                "Seed": 0,
                "Rd1": 0,
                "Rd2": 0,
                "Playoffs": 0,
                "Champion": 0,
                "Bottom 4": 0,
                "Bolan": 0,
                "Seeds": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            }
        )
    keys = retAgr[0].keys()

    worst_playoffs = [0] * 14
    best_sacko = [0] * 14
    # Sum up results
    for i in range(n):
        ret = generateSeason()
        for team_idx in range(12):
            for key in keys:
                if key != "Team" and key != "Seeds":
                    retAgr[team_idx][key] += ret[team_idx][key]
                elif key == "Seeds":
                    seed_idx = ret[team_idx]["Seed"] - 1
                    retAgr[team_idx]["Seeds"][seed_idx] += 1
                    if seed_idx == 3:
                        worst_playoffs[ret[team_idx]["Wins"]] += 1
                    elif seed_idx == 8:
                        best_sacko[ret[team_idx]["Wins"]] += 1

    # Average out results
    for team_idx in range(12):
        for key in keys:
            if key != "Team" and key != "Seeds":
                retAgr[team_idx][key] /= n
            elif key == "Seeds":
                for seed_i in range(12):
                    retAgr[team_idx]["Seeds"][seed_i] /= n

    for wins in range(14):
        worst_playoffs[wins] /= n
        best_sacko[wins] /= n

    print(worst_playoffs)
    print(best_sacko)

    retAgr.sort(key=sortSeedEnd)

    # write results
    f = open("BambitronResults.csv", "w")
    f.write("Team,Wins,Losses,Seed,PF, Playoffs,Haley,Bottom 4,Bolan\n")
    for team in retAgr:
        f.write(
            "{},{},{},{},{},{},{},{},{}\n".format(
                team["Team"].name,
                round(team["Wins"], 1),
                round(team["Losses"], 1),
                round(team["Seed"], 1),
                round(team["PF"], 1),
                round(team["Playoffs"] * 100, 2),
                round(team["Champion"] * 100, 2),
                round(team["Bottom 4"] * 100, 2),
                round(team["Bolan"] * 100, 2),
            )
        )
    f.close()

    f = open("BambitronSeeding.csv", "w")
    f.write("Team,1,2,3,4,5,6,7,8,9,10,11,12\n")
    for team in retAgr:
        team["Seeds"] = [str(round(seed_p * 100, 2)) for seed_p in team["Seeds"]]
        f.write("{},{}\n".format(team["Team"].name, ",".join(team["Seeds"])))
    f.close()


def testSchedule():
    testDict = {}
    for team in T:
        testDict[team] = 0
    i = 1
    for sched in SCHEDULE:
        if len(sched) != 13:
            print("A schedule {} has wrong number of weeks".format(i))
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