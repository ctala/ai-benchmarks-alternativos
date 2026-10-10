#!/usr/bin/env python3
"""
Análisis de jubilación v2 - con dominancia correcta.

Aplica criterios en orden:
1. Retired por proveedor
2. Provider variants
3. Sin runs
4. Dominados (mismo tier/familia, peor o igual Q, mayor o igual costo)
5. Más caros para misma nota (si no alcanza con dominancia)
"""
import json
from collections import defaultdict
from pathlib import Path

# Load models.json
data = json.load(open('docs/data/models.json'))
models = {m['key']: m for m in data['models']}

# Categorías de jubilación
jubilados = {
    'retired': [],
    'provider_variant': [],
    'sin_runs': [],
    'dominados': [],
    'mas_caros': [],
}

activos = []

# Paso 1: Retired
for key, m in models.items():
    if m.get('retired'):
        jubilados['retired'].append((key, m))

# Paso 2: Provider variants
for key, m in models.items():
    if m.get('provider_variant') and key not in [k for k, _ in jubilados['retired']]:
        jubilados['provider_variant'].append((key, m))

# Paso 3: Sin runs
for key, m in models.items():
    if m.get('runs', 0) == 0 and key not in [k for cat in jubilados.values() for k, _ in cat]:
        jubilados['sin_runs'].append((key, m))

# Paso 4: Dominancia por familia/tier
# Primero agrupar candidatos restantes por familia y tier
candidatos = []
for key, m in models.items():
    if key in [k for cat in jubilados.values() for k, _ in cat]:
        continue
    candidatos.append((key, m))

# Agrupar por familia (simplificado: primer token del nombre)
familias = defaultdict(list)
for key, m in candidatos:
    name = m['name']
    # Familia = primeras palabras antes del primer número
    import re
    match = re.match(r'^([A-Za-z\s]+)', name)
    if match:
        familia = match.group(1).strip().split()[0]  # Primera palabra
    else:
        familia = name.split()[0] if name else key
    
    familias[familia].append((key, m))

# Detectar dominados dentro de cada familia
for familia, members in familias.items():
    if len(members) <= 1:
        continue
    
    for i, (k1, m1) in enumerate(members):
        q1 = m1.get('quality_avg') or m1.get('score_global', 0)
        c1 = (m1.get('cost_input', 999) + m1.get('cost_output', 999))
        
        for k2, m2 in members:
            if k1 == k2:
                continue
            
            q2 = m2.get('quality_avg') or m2.get('score_global', 0)
            c2 = (m2.get('cost_input', 999) + m2.get('cost_output', 999))
            
            # m1 dominado por m2: m2 tiene igual o mejor calidad Y menor o igual costo
            if q2 >= q1 and c2 <= c1 and (k1, m1) not in jubilados['dominados']:
                jubilados['dominados'].append((k1, m1))
                break

# Contar lo que llevamos
total_jubilados = sum(len(v) for v in jubilados.values())
candidatos_activos = [
    (k, m) for k, m in models.items()
    if k not in [key for cat in jubilados.values() for key, _ in cat]
]

print(f"Después de aplicar retired/variants/sin_runs/dominados:")
print(f"  Jubilados: {total_jubilados}")
print(f"  Candidatos activos: {len(candidatos_activos)}")

# Paso 5: Si candidatos > 100, aplicar "más caros para misma nota"
if len(candidatos_activos) > 100:
    faltan = len(candidatos_activos) - 100
    print(f"\nNecesitamos jubilar {faltan} más para llegar a 100.")
    
    # Ordenar por prioridad (ranked, calidad, runs)
    candidatos_activos.sort(key=lambda x: (
        -x[1].get('ranked', False),
        -(x[1].get('quality_avg') or x[1].get('score_global', 0)),
        -x[1].get('runs', 0)
    ))
    
    # Los últimos faltan son los de menor prioridad
    for k, m in candidatos_activos[-faltan:]:
        jubilados['mas_caros'].append((k, m))
    
    activos = candidatos_activos[:-faltan]
else:
    activos = candidatos_activos

# Resumen
print(f"\n{'='*60}")
print(f"RESUMEN FINAL")
print(f"{'='*60}")
print(f"Total modelos: {len(models)}")
print(f"Jubilados: {sum(len(v) for v in jubilados.values())}")
for cat, items in jubilados.items():
    print(f"  - {cat}: {len(items)}")
print(f"Activos: {len(activos)}")

# Guardar resultado
resultado = {
    "fecha": "2026-10-10",
    "total": len(models),
    "jubilados": sum(len(v) for v in jubilados.values()),
    "activos": len(activos),
    "desglose_jubilados": {k: len(v) for k, v in jubilados.items()},
    "lista_jubilados": [
        {
            "key": k,
            "name": m['name'],
            "motivo": cat,
            "quality": m.get('quality_avg') or m.get('score_global', 0),
            "cost_input": m.get('cost_input', 0),
            "cost_output": m.get('cost_output', 0),
            "runs": m.get('runs', 0),
            "ranked": m.get('ranked', False)
        }
        for cat, items in jubilados.items()
        for k, m in items
    ],
    "lista_activos": [
        {
            "key": k,
            "name": m['name'],
            "quality": m.get('quality_avg') or m.get('score_global', 0),
            "cost_input": m.get('cost_input', 0),
            "cost_output": m.get('cost_output', 0),
            "runs": m.get('runs', 0),
            "ranked": m.get('ranked', False)
        }
        for k, m in activos
    ]
}

with open('docs/jubilacion-2026-10-v2.json', 'w', encoding='utf-8') as f:
    json.dump(resultado, f, indent=2, ensure_ascii=False)

print(f"\n✓ Guardado en docs/jubilacion-2026-10-v2.json")
