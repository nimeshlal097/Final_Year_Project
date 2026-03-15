import json

with open('S.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

new_cell_source = [
    "import numpy as np\n",
    "\n",
    "def check_peak_location(V1, V2, L, beta, h):\n",
    "    \"\"\"\n",
    "    Validates if the voltage peak is at a busbar or along the line.\n",
    "    Based on equations (3), (4), and (5) from the paper.\n",
    "    \"\"\"\n",
    "    # Calculate alpha (Eq. 5)\n",
    "    num = V2 * np.sin(np.radians(beta * h))\n",
    "    den = V1 - V2 * np.cos(np.radians(beta * h))\n",
    "    alpha = np.arctan2(num, den) # Use arctan2 for quadrant safety\n",
    "    \n",
    "    # Calculate Max Voltage Location (Eq. 3)\n",
    "    L_max_v = (np.pi/2 - alpha) * (L / (np.radians(beta) * h))\n",
    "    \n",
    "    # Validation Logic\n",
    "    if L_max_v < 0 or L_max_v > L:\n",
    "        return f\"Peak is at a Busbar (L_max: {L_max_v:.2f}m)\"\n",
    "    else:\n",
    "        return f\"Peak is ALONG the line at {L_max_v:.2f}m\"\n",
    "\n",
    "# If you have your Admittance Matrix (Y_h) or Impedance Matrix (Z_h)\n",
    "def calculate_propagation_ratio(Z_matrix, source_node, target_node):\n",
    "    \"\"\"\n",
    "    Calculates voltage relation between two buses (Eq. 9).\n",
    "    \"\"\"\n",
    "    # V_target / V_source = Z_target_source / Z_source_source\n",
    "    prop_ratio = np.abs(Z_matrix[target_node, source_node] / Z_matrix[source_node, source_node])\n",
    "    return prop_ratio\n",
    "\n",
    "def get_conversion_factor(V_hv, V_lv):\n",
    "    return (V_hv**2) / (V_lv**2)\n"
]

new_cell = {
    "cell_type": "code",
    "execution_count": None,
    "id": "validation_funcs_123",
    "metadata": {},
    "outputs": [],
    "source": new_cell_source
}

nb['cells'].append(new_cell)

with open('S.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
print("Successfully appended new cell to notebook.")
