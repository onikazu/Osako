import robo_tools
import math


OUT_OF_RANGE = 999


def analyze_aural_message(message, result):
    index0 = message.find(" ")
    index1 = message.find(" ", index0+1)
    index2 = message.find(" ", index1+1)
    index3 = message.find(")", index2+1)
    str_speaker = message[index1+1:index2]
    str_content = message[index2+1:index3]
    play_mode = ""
    if str_speaker == "referee":
        play_mode = str_content
    result["speaker"] = str_speaker
    result["content"] = str_content
    result["play_mode"] = play_mode
    return result


def analyze_initial_message(message, result):
    index0 = message.index(" ")
    index1 = message.index(" ", index0 + 1)
    index2 = message.index(" ", index1 + 1)
    index3 = message.index(")", index2 + 1)

    str_side = message[index0+1:index1]
    i_number = int(message[index1+1:index2])
    str_play_mode = message[index2+1:index3]
    result["side"] = str_side
    result["number"] = i_number
    result["play_mode"] = str_play_mode
    return result


def analyze_physical_message(message, result):
    print("result: ", result)
    i_time = int(robo_tools.getParam(message, "sense_body", 1))
    # スタミナ情報の解析
    d_stamina = 0.0
    st = message.split(" ")
    for i in range(len(st)):
        if st[i] == "(stamina":
            d_stamina = float(st[i + 1])

    result["time"] = i_time
    result["stamina"] = d_stamina
    return result


def analyze_player_param(message, result):
    # str_player_param = message
    # result["player_param"] = str_player_param
    return result


def analyze_player_type(message, result):
    # print("m_strPlayerType: ", self.m_strPlayerType)
    # print(message)
    id = int(robo_tools.getParam(message, "id", 1))
    # print("id: ", id)
    # result["id"] = id
    # result["player_type"] = message
    return result


def analyze_visual_message(message, result, kick_off_x, kick_off_y):
    time = int(robo_tools.getParam(message, "see", 1))
    play_mode = result["play_mode"]
    if time < 1:
        return
    result["neck"] = robo_tools.getNeckDir(message)
    if result["neck"] == OUT_OF_RANGE:
        return
    if robo_tools.checkInitialMode(play_mode):
        result["x"] = kick_off_x
        result["y"] = kick_off_y

    pos = robo_tools.estimatePosition(message, result["neck"], result["x"], result["y"])
    result["x"] = pos["x"]
    result["y"] = pos["y"]
    if message.find("(b)") == -1:
        return
    ball_dist = robo_tools.getParam(message, "(b)", 1)
    ball_dir = robo_tools.getParam(message, "(b)", 2)
    rad = math.radians(robo_tools.normalizeAngle(result["neck"] + ball_dir))
    result["ball_x"] = result["x"] + ball_dist * math.cos(rad)
    result["ball_y"] = result["y"] + ball_dist * math.sin(rad)

    return result


def analyze_server_param(message, result):
    # print("serverParam: ", message)
    # str_server_param = message
    # result["server_param"] = str_server_param
    return result
