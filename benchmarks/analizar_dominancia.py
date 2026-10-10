#!/usr/bin/env python3
"""Análisis de dominancia por familia/tier."""
import json
import re
from collections import defaultdict

data = json.load(open('docs/data/models.json'))
models = {m['key']: m for m in data['models']}

# Excluir ya jubilados
candidatos = {
    k: m for k, m in models.items()
    if not m.get('retired') and not m.get('provider_variant') and m.get('runs', 0) > 0
}

# Agrupar por familia
familias = defaultdict(list)
for key, m in candidatos.items():
    name = m['name']
    match = re.match(r'^([A-Za-z\s]+)', name)
    familia = match.group(1).strip().split()[0] if match else name.split()[0]
    familias[familia].append((key, m))

# Detectar dominados
print("Modelos dominados por familia:\n")
dominados = []
for familia, members in sorted(familias.items()):
    if len(members) <= 1:
        continue
    
    print(f"{familia} ({len(members)} miembros):")
    for k1, m1 in members:
        q1 = m1.get('quality_avg') or m1.get('score_global', 0)
        c1 = m1.get('cost_input', 999) + m1.get('cost_output', 999)
        
        for k2, m2 in members:
            if k1 == k2:
                continue
            q2 = m2.get('quality_avg') or m2.get('score_global', 0)
            c2 = m2.get('cost_input', 999) + m2.get('cost_output', 999)
            
            # m1 dominado por m2: m2 >= Q, m2 <= cost
            if q2 >= q1 and c2 <= c1:
                print(f"  ✗ {m1['name']:<30} Q={q1:.2f} ${c1:.2f} dominado por {m2['name']}")
                dominados.append(k1)
                break

print(f"\nTotal dominados: {len(set(dominados))}")
