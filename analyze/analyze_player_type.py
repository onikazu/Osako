import analyze.robo_tools


def analyzePlayerType(message, result):
    # print("m_strPlayerType: ", self.m_strPlayerType)
    # print(message)
    id = int(analyze.robo_tools.getParam(message, "id", 1))
    # print("id: ", id)
    result["id"] = id
    result["player_type"] = message
    return result
