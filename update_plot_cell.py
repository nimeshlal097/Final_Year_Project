import json
import re

with open('S.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# The plotting cell is at index 23
cell_content = nb['cells'][23]['source']

new_content = []
for line in cell_content:
    if '        # Cleanly skip naming "Line X" intermediate nodes so it\'s not messy\n' in line:
        new_content.append("        # Apply checking logic for line components\n")
        new_content.append("        if str(node).startswith(\"Line \"):\n")
        new_content.append("            # For a proper check, V1, V2, L, beta, and h are needed. \n")
        new_content.append("            # Assuming these need to be plugged in based on the node's properties\n")
        new_content.append("            # Example logic if you wanted to highlight the peak via checking:\n")
        new_content.append("            # peak_info = check_peak_location(V1, V2, L, beta, h)\n")
        new_content.append("            # print(f\"{node}: {peak_info}\")\n")
        new_content.append("            continue\n")
    elif '        if str(node).startswith(\"Line \"):\n' in line:
        pass # Already handled above
    elif '            continue\n' in line and new_content[-1] == "            continue\n":
        pass # Already handled
    else:
        new_content.append(line)


nb['cells'][23]['source'] = new_content

with open('S.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Updated mapping logic")
