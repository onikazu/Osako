def analyzeAuralMessage(message, result):
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


def analyzeInitialMessage(message, result):
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



def analyzePhysicalMessage(message, result):
    i_time = int(analyze.robo_tools.getParam(message, "sense_body", 1))
    # スタミナ情報の解析
    d_stamina = 0.0
    st = message.split(" ")
    for i in range(len(st)):
        if st[i] == "(stamina":
            d_stamina = float(st[i + 1])

    result["time"] = i_time
    result["stamina"] = d_stamina
    return result


def analyzePlayerParam(message, result):
    str_player_param = message
    result["player_param"] = str_player_param
    return result


def analyzePlayerType(message, result):
    # print("m_strPlayerType: ", self.m_strPlayerType)
    # print(message)
    id = int(analyze.robo_tools.getParam(message, "id", 1))
    # print("id: ", id)
    result["id"] = id
    result["player_type"] = message
    return result