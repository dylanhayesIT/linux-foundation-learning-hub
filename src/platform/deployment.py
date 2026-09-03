def readiness(*checks):
    return round(sum(bool(x) for x in checks)/len(checks)*100,1) if checks else 0
