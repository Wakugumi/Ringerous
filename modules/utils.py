import json
from modules.ring import Ring

def load_ring_from_input(path):
    with open(path) as f:
        data = json.load(f)
    return Ring(
        elements=data["elements"],
        add_table=data["add_table"],
        mul_table=data["mul_table"]
    )

