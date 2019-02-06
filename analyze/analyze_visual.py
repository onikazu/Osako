import analyze.robo_tools
import math

def analyzeVisualMessage(message, result, dKickOffX, dKickOffY):
    OUT_OF_RANGE = 999
    time = int(analyze.robo_tools.getParam(message, "see", 1))
    if time < 1:
        return
    result["neck"] = analyze.robo_tools.getNeckDir(message)
    if result["neck"] == OUT_OF_RANGE:
        return
    if analyze.robo_tools.checkInitialMode(play_mode):
        result["x"] = dKickOffX
        result["y"] = dKickOffY

    pos = analyze.robo_tools.estimatePosition(message, result["neck"], result["x"], result["y"])
    result["x"] = pos["x"]
    result["y"] = pos["y"]
    if message.find("(b)") == -1:
        return
    ball_dist = analyze.robo_tools.getParam(message, "(b)", 1)
    ball_dir = analyze.robo_tools.getParam(message, "(b)", 2)
    rad = math.radians(analyze.robo_tools.normalizeAngle(result["neck"] + ball_dir))
    result["ball_x"] = result["x"] + ball_dist * math.cos(rad)
    result["ball_y"] = result["y"] + ball_dist * math.sin(rad)

    return result
