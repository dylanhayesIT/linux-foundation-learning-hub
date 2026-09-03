def normalize(samples):
    return [{"timestamp":s["timestamp"],"metric":s["metric"],"value":float(s["value"]),"source":s.get("source","unknown")} for s in samples if {"timestamp","metric","value"}<=s.keys()]
