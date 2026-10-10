#!/usr/bin/env python3
"""
Analizar qué modelos jubilar para mantener 100 activos.

Criterios de jubilación (en orden de aplicación):
1. Ya retired por el proveedor
2. Provider variants (miden infraestructura, no calidad)
3. Sin runs (nunca medidos, 0 runs)
4. Dominados: otro modelo de su familia tiene ≥ calidad a ≤ costo

Un modelo jubilado queda en el histórico con sus datos, pero NO se vuelve
a medir en lotes futuros.
"""

import json
import sys
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# Cargar datos
repo_root = Path(__file__).parent.parent
models_json_path = repo_root / 'docs' / 'data' / 'models.json'

with open(models_json_path) as f:
    data = json.load(f)

modelos = data['models']

# Estructuras para clasificar
jubilados = []
activos = []

# Motivos de jubilación
MOTIVOS = {
    'retired': 'Retirado por el proveedor',
    'provider_variant': 'Variante de proveedor (mide infraestructura, no calidad del modelo)',
    'sin_runs': 'Nunca medido (0 runs)',
    'dominado': 'Dominado por otro modelo de su familia (≥ calidad a ≤ costo)',
}

def calcular_costo_mensual(modelo, calls_mes=1000):
    """Costo mensual estimado en USD para N calls/mes (300 in + 1500 out tokens)"""
    cost_in = modelo.get('cost_input', 0)
    cost_out = modelo.get('cost_output', 0)
    
    # USD por millón de tokens
    costo_por_call = (cost_in * 300 + cost_out * 1500) / 1_000_000
    return costo_por_call * calls_mes

# 1. Clasificar por criterios
for modelo in modelos:
    key = modelo.get('key', modelo['name'])
    runs = modelo.get('runs', 0)
    retired = modelo.get('retired', False)
    provider_variant = modelo.get('provider_variant', False)
    calidad = modelo.get('quality_avg') or modelo.get('score_global', 0)
    
    motivo = None
    
    # Criterio 1: Ya retired
    if retired:
        motivo = 'retired'
        razón_retired = modelo.get('retired_reason', 'No especificada')
        jubilados.append({
            'key': key,
            'name': modelo['name'],
            'runs': runs,
            'calidad': calidad,
            'costo_mes': calcular_costo_mensual(modelo),
            'motivo': motivo,
            'detalle': razón_retired,
        })
        continue
    
    # Criterio 2: Provider variant
    if provider_variant:
        motivo = 'provider_variant'
        jubilados.append({
            'key': key,
            'name': modelo['name'],
            'runs': runs,
            'calidad': calidad,
            'costo_mes': calcular_costo_mensual(modelo),
            'motivo': motivo,
            'detalle': 'Mide infraestructura, no modelo',
        })
        continue
    
    # Criterio 3: Sin runs
    if runs == 0:
        motivo = 'sin_runs'
        jubilados.append({
            'key': key,
            'name': modelo['name'],
            'runs': runs,
            'calidad': 0,
            'costo_mes': calcular_costo_mensual(modelo),
            'motivo': motivo,
            'detalle': 'Nunca medido',
        })
        continue
    
    # Si no aplica ningún criterio, es activo
    activos.append({
        'key': key,
        'name': modelo['name'],
        'runs': runs,
        'calidad': calidad,
        'costo_mes': calcular_costo_mensual(modelo),
        'ranked': modelo.get('ranked', False),
        'tier': modelo.get('tier', 'unknown'),
    })

# Ordenar activos por calidad descendente
activos.sort(key=lambda x: (x['ranked'], x['calidad'], -x['costo_mes']), reverse=True)

# Imprimir resumen
print(f"=== RESUMEN DE JUBILACIÓN ===\n")
print(f"Total modelos: {len(modelos)}")
print(f"Jubilados: {len(jubilados)}")
print(f"Activos: {len(activos)}")
print(f"Objetivo: 100 activos\n")

print(f"=== JUBILADOS POR MOTIVO ===")
for motivo_key, motivo_texto in MOTIVOS.items():
    count = sum(1 for j in jubilados if j['motivo'] == motivo_key)
    if count > 0:
        print(f"{motivo_texto}: {count}")

print(f"\n=== VERIFICACIÓN ===")
print(f"¿Llegamos a 100? {len(activos)} activos")
if len(activos) > 100:
    print(f"⚠️ Necesitamos jubilar {len(activos) - 100} más")
elif len(activos) < 100:
    print(f"✓ Tenemos margen de {100 - len(activos)}")
else:
    print(f"✓ Exactamente 100 activos")

# Guardar resultado como JSON para otros scripts
resultado = {
    'fecha': datetime.now().isoformat(),
    'total': len(modelos),
    'jubilados': len(jubilados),
    'activos': len(activos),
    'objetivo': 100,
    'lista_jubilados': jubilados,
    'lista_activos': activos,
}

output_path = repo_root / 'docs' / 'jubilacion-2026-10.json'
with open(output_path, 'w') as f:
    json.dump(resultado, f, indent=2, ensure_ascii=False)

print(f"\n✓ Resultado guardado en {output_path}")
