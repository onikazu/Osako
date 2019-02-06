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
