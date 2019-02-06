import analyze.robo_tools

def analyzePhysicalMessage(message, result):
    i_time = int(analyze.robo_tools.getParam(message, "sense_body", 1))
    # スタミナ情報の解析
    d_stamina = 0.0
    st = message.split(" ")
    for i in range(len(st)):
        if st[i] == "(stamina":
            d_stamina = float(st[i+1])

    result["time"] = i_time
    result["stamina"] = d_stamina
    return result
