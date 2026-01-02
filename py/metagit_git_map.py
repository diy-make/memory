import os
import json
import time

def generate_git_map(repo_root, output_path, agent_name):
    """
    Generates a structural map of the current Git repository,
    focusing on chrono-fractal heartwood nodes.
    """
    mappings = []
    
    # Identify key nodes
    # 1. Root JSON
    root_json = os.path.join(repo_root, "json")
    if os.path.exists(root_json):
        mappings.append({
            "path": "json/",
            "type": "heartwood_root",
            "status": "active",
            "description": "The legislative core of the repository."
        })

    # 2. Chrono-Fractal Scan (Last 2 days)
    for year in ['2025', '2026']:
        y_path = os.path.join(repo_root, year)
        if not os.path.exists(y_path): continue
        
        for q in ['Q1', 'Q2', 'Q3', 'Q4']:
            q_path = os.path.join(y_path, q)
            if not os.path.exists(q_path): continue
            
            # Simple walk to find leaf json dirs
            for root, dirs, files in os.walk(q_path):
                if root.endswith("/json"):
                    rel_path = os.path.relpath(root, repo_root)
                    mappings.append({
                        "path": rel_path + "/",
                        "type": "heartwood_leaf",
                        "status": "active" if "2026" in rel_path else "archived",
                        "contains": files[:5] # Sample first 5 files
                    })

    # 3. Substrate Scan
    substrate_nodes = ["webm", "pdf", "png"]
    for node in substrate_nodes:
        n_path = os.path.join(repo_root, "..", node) # Substrate is often next to public/
        if os.path.exists(n_path):
            mappings.append({
                "path": node + "/",
                "type": "substrate",
                "status": "active",
                "description": "Cloud-synced binary storage."
            })

    output_data = {
        "title": "Git Map: Memory Public",
        "version": "1.0",
        "generated_at": int(time.time()),
        "attribution": f"{agent_name} ({time.strftime('%Y%m%d-%H%M%S')})",
        "description": "Forensic map of the internal repository structure.",
        "mappings": mappings
    }

    with open(output_path, 'w') as f:
        json.dump(output_data, f, indent=2)
    
    print(f"✅ Git map generated at: {output_path}")

if __name__ == "__main__":
    # Internal paths for memory/public/
    repo_root = "/home/bestape/gemini/repos/diy-make/memory/public"
    # Output to today's chrono-fractal json
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    output_dir = os.path.join(repo_root, "2026/Q1/01/01/json")
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"{timestamp}_metagit_git_map.json")
    
    generate_git_map(repo_root, output_file, "Palamedes")
