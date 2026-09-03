def choose_node(nodes,cpu,memory_gb,accelerator=False):
    c=[n for n in nodes if n["cpu_free"]>=cpu and n["memory_free_gb"]>=memory_gb and (not accelerator or n.get("accelerator",False))]
    return max(c,key=lambda n:(n["cpu_free"],n["memory_free_gb"]))["name"] if c else None
