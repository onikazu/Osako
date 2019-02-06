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
