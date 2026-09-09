"""
MCP Server for Rubinstein Alternating-Offers Bargaining Skill
"""

import json
import sys
from client import RubinsteinBargaining

def handle_call(name: str, args: dict) -> dict:
    if name == "compute_rubinstein_split":
        d1 = args.get("delta1", 0.9)
        d2 = args.get("delta2", 0.8)
        s = args.get("surplus", 100.0)
        rb = RubinsteinBargaining(d1, d2, s)
        return rb.compute_equilibrium_split()
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_call(req.get("method"), req.get("params", {}))
        sys.stdout.write(json.dumps(res) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
