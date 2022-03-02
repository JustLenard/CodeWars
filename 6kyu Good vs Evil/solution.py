def good_vs_evil(good, evil):
    gw = [1, 2, 3, 3, 4, 10]
    ew = [1, 2, 2, 2, 3, 5, 10]
    good = [int(x) for x in good.split()]
    evil = [int(x) for x in evil.split()]
    good = sum(good[x] * gw[x] for x in range(6))
    evil = sum(evil[x] * ew[x] for x in range(7))
    if good > evil: return "Battle Result: Good triumphs over Evil"
    elif good < evil: return "Battle Result: Evil eradicates all trace of Good"
    else: return "Battle Result: No victor on this battle field"