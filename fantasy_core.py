from enum import Enum


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
    [
        T.MATTY,
        T.JON,
        T.HUNYAR,
        T.JAMES,
        T.NICK,
        T.DUC,
        T.STEVE,
        T.MCCLURE,
        T.BRYCE,
        T.LOGAN,
        T.JOE,
        T.HUNYAR,
        T.MATTY,
    ],
    [
        T.NICK,
        T.STD_BUSH,
        T.JAMES,
        T.MATTY,
        T.HUNYAR,
        T.MCCLURE,
        T.BRYCE,
        T.LOGAN,
        T.JOE,
        T.DUC,
        T.STEVE,
        T.MATTY,
        T.JAMES,
    ],
    [
        T.MCCLURE,
        T.LOGAN,
        T.STEVE,
        T.BRYCE,
        T.DUC,
        T.NICK,
        T.JAMES,
        T.HUNYAR,
        T.JON,
        T.MATTY,
        T.STD_BUSH,
        T.DUC,
        T.STEVE,
    ],
    [
        T.JON,
        T.JAMES,
        T.MATTY,
        T.HUNYAR,
        T.STD_BUSH,
        T.JOE,
        T.DUC,
        T.STEVE,
        T.MCCLURE,
        T.BRYCE,
        T.LOGAN,
        T.JAMES,
        T.HUNYAR,
    ],
    [
        T.STD_BUSH,
        T.HUNYAR,
        T.NICK,
        T.JON,
        T.JAMES,
        T.STEVE,
        T.MCCLURE,
        T.BRYCE,
        T.LOGAN,
        T.JOE,
        T.DUC,
        T.JON,
        T.STD_BUSH,
    ],
    [
        T.JOE,
        T.DUC,
        T.LOGAN,
        T.STEVE,
        T.BRYCE,
        T.JON,
        T.MATTY,
        T.STD_BUSH,
        T.NICK,
        T.JAMES,
        T.HUNYAR,
        T.STEVE,
        T.BRYCE,
    ],
    [
        T.BRYCE,
        T.JOE,
        T.MCCLURE,
        T.DUC,
        T.STEVE,
        T.JAMES,
        T.HUNYAR,
        T.JON,
        T.MATTY,
        T.STD_BUSH,
        T.NICK,
        T.BRYCE,
        T.DUC,
    ],
    [
        T.DUC,
        T.BRYCE,
        T.JOE,
        T.MCCLURE,
        T.LOGAN,
        T.MATTY,
        T.STD_BUSH,
        T.NICK,
        T.JAMES,
        T.HUNYAR,
        T.JON,
        T.MCCLURE,
        T.JOE,
    ],
    [
        T.HUNYAR,
        T.NICK,
        T.JON,
        T.STD_BUSH,
        T.MATTY,
        T.LOGAN,
        T.JOE,
        T.DUC,
        T.STEVE,
        T.MCCLURE,
        T.BRYCE,
        T.NICK,
        T.JON,
    ],
    [
        T.LOGAN,
        T.STEVE,
        T.DUC,
        T.JOE,
        T.MCCLURE,
        T.HUNYAR,
        T.JON,
        T.MATTY,
        T.STD_BUSH,
        T.NICK,
        T.JAMES,
        T.LOGAN,
        T.MCCLURE,
    ],
    [
        T.JAMES,
        T.MATTY,
        T.STD_BUSH,
        T.NICK,
        T.JON,
        T.BRYCE,
        T.LOGAN,
        T.JOE,
        T.DUC,
        T.STEVE,
        T.MCCLURE,
        T.STD_BUSH,
        T.NICK,
    ],
    [
        T.STEVE,
        T.MCCLURE,
        T.BRYCE,
        T.LOGAN,
        T.JOE,
        T.STD_BUSH,
        T.NICK,
        T.JAMES,
        T.HUNYAR,
        T.JON,
        T.MATTY,
        T.JOE,
        T.LOGAN,
    ],
]

f = open("scores.csv", "r")
lines = f.readlines()
SCORES = []
for line in lines:
    lineSplit = line.rstrip("\n").split(",")[1:]
    SCORES.append([float(data) for data in lineSplit])
f.close()

WEEKS_COMPLETE = len(SCORES[0])
