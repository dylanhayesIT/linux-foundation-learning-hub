def validate_workload(spec):
    errors=[]
    for c in spec.get("containers",[]):
        if "resources" not in c: errors.append(c.get("name","unknown")+":missing_resources")
        if c.get("privileged",False): errors.append(c.get("name","unknown")+":privileged_container")
    return errors or ([] if spec.get("containers") else ["no_containers"])
