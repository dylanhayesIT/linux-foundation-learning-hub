def health_score(load1,memory_used_pct,disk_used_pct):
    if min(load1,memory_used_pct,disk_used_pct)<0: raise ValueError("metrics cannot be negative")
    return round(max(0,min(100,100-min(load1*10,40)-memory_used_pct*.3-disk_used_pct*.3)),2)
