
# Bahareh Nojan - Assignment 6

def filter_critical_scores(score_list, min_severity=70):
    critical_scores = []

    for score in score_list:
        if score > min_severity:
            if score > 100:
                score = 100
            critical_scores.append(score)

    return critical_scores
