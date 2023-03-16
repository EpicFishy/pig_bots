def choice(round_score, my_score, opponent_score):
    if round_score < 25:
        return TRUE
    if my_score - opponent_score < 10:
        return TRUE
    else:
        return FALSE
