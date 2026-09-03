from collections import defaultdict
def aggregate(samples):
    totals=defaultdict(float); counts=defaultdict(int)
    for s in samples: totals[s["name"]]+=float(s["value"]); counts[s["name"]]+=1
    return {n:round(totals[n]/counts[n],3) for n in totals}
