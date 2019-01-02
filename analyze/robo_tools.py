"""
robo_tools.py
サッカーエージェントで使用している数値・テキスト処理
"""

import math

OUT_OF_RANGE = 999
strFlagName = []
dFlagX = []
dFlagY = []
strFlagName.append("g r");
dFlagX.append(52.5);
dFlagY.append(0.0)
strFlagName.append("g l");
dFlagX.append(-52.5);
dFlagY.append(0.0)
strFlagName.append("f c t");
dFlagX.append(0.0);
dFlagY.append(-34.0)
strFlagName.append("f c b");
dFlagX.append(0.0);
dFlagY.append(+34.0)
strFlagName.append("f c");
dFlagX.append(0.0);
dFlagY.append(0.0)
strFlagName.append("f p l t");
dFlagX.append(-36.0);
dFlagY.append(-20.16)
strFlagName.append("f p l b");
dFlagX.append(-36.0);
dFlagY.append(20.16)
strFlagName.append("f p l c");
dFlagX.append(-36.0);
dFlagY.append(0.0)
strFlagName.append("f p r t");
dFlagX.append(36.0);
dFlagY.append(-20.16)
strFlagName.append("f p r b");
dFlagX.append(36.0);
dFlagY.append(20.16)
strFlagName.append("f p r c");
dFlagX.append(36.0);
dFlagY.append(0.0)
strFlagName.append("f g l t");
dFlagX.append(-52.5);
dFlagY.append(-7.01)
strFlagName.append("f g l b");
dFlagX.append(-52.5);
dFlagY.append(7.01)
strFlagName.append("f g r t");
dFlagX.append(52.5);
dFlagY.append(-7.01)
strFlagName.append("f g r b");
dFlagX.append(52.5);
dFlagY.append(7.01)
strFlagName.append("f t l 50");
dFlagX.append(-50.0);
dFlagY.append(-39.0)
strFlagName.append("f t l 40");
dFlagX.append(-40.0);
dFlagY.append(-39.0)
strFlagName.append("f t l 30");
dFlagX.append(-30.0);
dFlagY.append(-39.0)
strFlagName.append("f t l 20");
dFlagX.append(-20.0);
dFlagY.append(-39.0)
strFlagName.append("f t l 10");
dFlagX.append(-10.0);
dFlagY.append(-39.0)
strFlagName.append("f t 0");
dFlagX.append(0.0);
dFlagY.append(-39.0)
strFlagName.append("f t r 10");
dFlagX.append(10.0);
dFlagY.append(-39.0)
strFlagName.append("f t r 20");
dFlagX.append(20.0);
dFlagY.append(-39.0)
strFlagName.append("f t r 30");
dFlagX.append(30.0);
dFlagY.append(-39.0)
strFlagName.append("f t r 40");
dFlagX.append(40.0);
dFlagY.append(-39.0)
strFlagName.append("f t r 50");
dFlagX.append(50.0);
dFlagY.append(-39.0)
strFlagName.append("f b l 50");
dFlagX.append(-50.0);
dFlagY.append(39.0)
strFlagName.append("f b l 40");
dFlagX.append(-40.0);
dFlagY.append(39.0)
strFlagName.append("f b l 30");
dFlagX.append(-30.0);
dFlagY.append(39.0)
strFlagName.append("f b l 20");
dFlagX.append(-20.0);
dFlagY.append(39.0)
strFlagName.append("f b l 10");
dFlagX.append(-10.0);
dFlagY.append(39.0)
strFlagName.append("f b 0");
dFlagX.append(0.0);
dFlagY.append(39.0)
strFlagName.append("f b r 10");
dFlagX.append(10.0);
dFlagY.append(39.0)
strFlagName.append("f b r 20");
dFlagX.append(20.0);
dFlagY.append(39.0)
strFlagName.append("f b r 30");
dFlagX.append(30.0);
dFlagY.append(39.0)
strFlagName.append("f b r 40");
dFlagX.append(40.0);
dFlagY.append(39.0)
strFlagName.append("f b r 50");
dFlagX.append(50.0);
dFlagY.append(39.0)
strFlagName.append("f l t 30");
dFlagX.append(-57.5);
dFlagY.append(-30.0)
strFlagName.append("f l t 20");
dFlagX.append(-57.5);
dFlagY.append(-20.0)
strFlagName.append("f l t 10");
dFlagX.append(-57.5);
dFlagY.append(-10.0)
strFlagName.append("f l 0");
dFlagX.append(-57.5);
dFlagY.append(0.0)
strFlagName.append("f l b 10");
dFlagX.append(-57.5);
dFlagY.append(10.0)
strFlagName.append("f l b 20");
dFlagX.append(-57.5);
dFlagY.append(20.0)
strFlagName.append("f l b 30");
dFlagX.append(-57.5);
dFlagY.append(30.0)
strFlagName.append("f r t 30");
dFlagX.append(57.5);
dFlagY.append(-30.0)
strFlagName.append("f r t 20");
dFlagX.append(57.5);
dFlagY.append(-20.0)
strFlagName.append("f r t 10");
dFlagX.append(57.5);
dFlagY.append(-10.0)
strFlagName.append("f r 0");
dFlagX.append(57.5);
dFlagY.append(0.0)
strFlagName.append("f r b 10");
dFlagX.append(57.5);
dFlagY.append(10.0)
strFlagName.append("f r b 20");
dFlagX.append(57.5);
dFlagY.append(20.0)
strFlagName.append("f r b 30");
dFlagX.append(57.5);
dFlagY.append(30.0)
strFlagName.append("f l t");
dFlagX.append(-52.5);
dFlagY.append(-34.0)
strFlagName.append("f l b");
dFlagX.append(-52.5);
dFlagY.append(34.0)
strFlagName.append("f r t");
dFlagX.append(52.5);
dFlagY.append(-34.0)
strFlagName.append("f r b");
dFlagX.append(52.5);
dFlagY.append(34.0)

def getParam(message, keyword, number):
    key = "(" + keyword
    index0 = message.find(key)
    if index0 < 0:
        return OUT_OF_RANGE

    index1 = message.find(" ", index0 + len(key))
    if number == 4:
        index1 = message.find(" ", index1 + 1)
        index1 = message.find(" ", index1 + 1)
        index1 = message.find(" ", index1 + 1)
    elif number == 3:
        index1 = message.find(" ", index1 + 1)
        index1 = message.find(" ", index1 + 1)
    elif number == 2:
        index1 = message.find(" ", index1 + 1)
    else:
        pass
    index2 = message.find(" ", index1 + 1)
    index3 = message.find(")", index1 + 1)
    if index3 < index2 and index3 != -1 or index2 == -1:
        index2 = index3
    result = 0.0
    try:
        result = float(message[index1:index2])
    except Exception:
        # print("player4[getParam]:文字データによるエラー")
        # print("error 時のgetparamの引数{} ,{}, {}".format(message, keyword, number))
        result = OUT_OF_RANGE
    return result


def getObjectMessage(message, keyword):
    result = ""
    index0 = message.find(keyword)
    while -1 < index0:
        index1 = message.find(")", index0+2)
        index2 = message.find(")", index1+1)
        result += message[index0:index2+1]
        result += ")"
        index0 = message.find(keyword, index2)
    return result


def getNeckDir(message):
    index0 = message.find("((l")
    lineName = ""
    line = ""
    lineDist = -1 * OUT_OF_RANGE
    lineDir = -1 * OUT_OF_RANGE
    while index0 > -1:
        index1 = message.find(")", index0+3)
        lineName = message[index0+1:index1+1]
        line = "(" + lineName
        index2 = message.find(")", index1+1)
        line += message[index1+1:index2+1]
        dist = getParam(line, lineName, 1)
        dir = getParam(line, lineName, 2)
        if dist > lineDist:
            lineDist = dist
            lineDir = dir
        index0 = message.find("((l", index0+3)
    if lineDist == OUT_OF_RANGE:
        return OUT_OF_RANGE

    playerNeck = OUT_OF_RANGE
    if lineName.startswith("(l b)"):
        if 0 < lineDir and lineDir <= 90:
            playerNeck = 180 - lineDir
        else:
            playerNeck = -lineDir
    elif lineName.startswith("(l t)"):
        if 0 < lineDir and lineDir <= 90:
            playerNeck = -lineDir
        else:
            playerNeck = -180 - lineDir
    elif lineName.startswith("(l l)"):
        if 0 < lineDir and lineDir <= 90:
            playerNeck = -90 - lineDir
        else:
            playerNeck = 90 - lineDir
    elif lineName.startswith("(l r)"):
        if 0 < lineDir and lineDir <= 90:
            playerNeck = 90 - lineDir
        else:
            playerNeck = -90 - lineDir
    return playerNeck


def getDistance(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    return math.sqrt(dx * dx + dy * dy)


def normalizeAngle(angle):
    # if abs(angle) > 720.0:
    #     print("angle error")
    while angle > 180.0:
        angle -= 360.0
    while angle < -180:
        angle += 360.0
    return angle

def checkInitialMode(play_mode):
    if play_mode.startswith("before_kick_off") or play_mode.startswith("goal_l") or \
            play_mode.startswith("goal_r"):
        return True
    else:
        return False

def getLandMarker(message, playerX, playerY):
        # Bの解決
        message = message.replace("B", "b", 1)
        # Fの解決
        if message.find("(F)") > -1:
            name = "(F)"
            min_dist = OUT_OF_RANGE
            for i in range(2, 55):
                dist = getDistance(playerX, playerY, dFlagX[i], dFlagY[i])
                if min_dist > dist:
                    min_dist = dist
                    name = strFlagName[i]
            message = message.replace("F", name, 1)

        if message.find("(G)") > -1:
            name = "(G)"
            min_dist = OUT_OF_RANGE
            for i in range(2):
                dist = getDistance(playerX, playerY, dFlagX[i], dFlagY[i])
                if min_dist > dist:
                    min_dist = dist
                    name = strFlagName[i]
            message = message.replace("G", name, 1)

def estimatePosition(self, message, neckDir, playerX, playerY):
        result = {"x": 999, "y": 999}
        message = getLandMarker(message, playerX, playerY)

        flag = getObjectMessage(message, "((g") + \
               getObjectMessage(message, "((f")
        index0 = flag.find("((")
        X = Y = W = S = 0.0
        flags = 0
        while index0 > -1:
            index1 = flag.find(")", index0 + 2)
            index2 = flag.find(")", index1 + 1)
            name = flag[index0 + 2:index1]
            # print("name", name)
            j = 0
            while strFlagName[j].endswith(name) is False:
                j += 1
                # if j >= 50:
                #     print("j", j, "name", name)
            dist = getParam(flag, name, 1)
            dir = getParam(flag, name, 2)
            rad = math.radians(normalizeAngle(dir + neckDir))
            W = 1 / dist
            X += W * (dFlagX[j] - dist * math.cos(rad))
            Y += W * (dFlagY[j] - dist * math.sin(rad))
            S += W
            flags += 1
            index0 = flag.find("((", index0 + 2)

        if flags > 0:
            result["x"] = X / S
            result["y"] = Y / S
        return result
