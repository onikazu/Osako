def init_player(team_name, version):
    return "(init {} (version {})".format(team_name, version)


def init_goalie(team_name, version):
    return "(init {} (goalie)(version {}))".format(team_name, version)


def init_coach(team_name, coach_name, version):
    return "(init {) {} {})".format(team_name, coach_name, version)
