#!/usr/bin/env python3
"""
Análisis de dominancia: detecta modelos dominados por otro de su familia.
Un modelo está dominado si otro de su familia tiene Q >= y costo <= por examen.
"""
import json
import re
import sys
from pathlib import Path
from collections import defaultdict

# Constantes
TOKEN_IN = 300  # Tokens promedio de input por examen
TOKEN_OUT = 1500  # Tokens promedio de output por examen

def calcular_familia(nombre):
    """Extrae la familia del nombre del modelo.
    
    Familia = mismo proveedor y misma línea base (Qwen, GPT, Claude, etc.)
    sin importar la generación.
    """
    # Normalizar
    nombre = nombre.replace('GPT-', 'GPT').replace('Claude ', 'Claude')
    
    # Extraer primera(s) palabra(s) antes de números
    match = re.match(r'^([A-Za-z]+(?:\s+[A-Za-z]+)?)', nombre)
    if match:
        familia = match.group(1).strip()
        # Casos especiales
        if familia.startswith('Claude'):
            # Claude Opus, Claude Sonnet, Claude Haiku -> subfamilias
            if 'Opus' in nombre:
                return 'ClaudeOpus'
            elif 'Sonnet' in nombre:
                return 'ClaudeSonnet'
            elif 'Haiku' in nombre:
                return 'ClaudeHaiku'
            elif 'Fable' in nombre:
                return 'ClaudeFable'
        return familia.split()[0]  # Primera palabra
    return nombre.split()[0] if nombre else 'Unknown'

def main():
    # Cargar datos
    data = json.load(open('docs/data/models.json'))
    models = {m['key']: m for m in data['models']}
    
    # Excluir ya jubilados por criterios 1-3
    excluidos = set()
    for k, m in models.items():
        if m.get('retired') or m.get('provider_variant') or m.get('runs', 0) == 0:
            excluidos.add(k)
    
    candidatos = {k: m for k, m in models.items() if k not in excluidos}
    print(f"Candidatos después de criterios 1-3: {len(candidatos)}\n")
    
    # Agrupar por familia
    familias = defaultdict(list)
    for key, m in candidatos.items():
        familia = calcular_familia(m['name'])
        familias[familia].append((key, m))
    
    # Calcular dominancia
    dominados = []
    dominancias = {}
    
    for familia, members in sorted(familias.items()):
        if len(members) <= 1:
            continue
        
        for k1, m1 in members:
            if k1 in dominancias:
                continue
            
            q1 = m1.get('quality_avg') or m1.get('score_global', 0)
            c1_in = m1.get('cost_input_per_M', 999)
            c1_out = m1.get('cost_output_per_M', 999)
            c1 = (TOKEN_IN / 1_000_000) * c1_in + (TOKEN_OUT / 1_000_000) * c1_out
            
            for k2, m2 in members:
                if k1 == k2 or k2 in dominancias:
                    continue
                
                q2 = m2.get('quality_avg') or m2.get('score_global', 0)
                c2_in = m2.get('cost_input_per_M', 999)
                c2_out = m2.get('cost_output_per_M', 999)
                c2 = (TOKEN_IN / 1_000_000) * c2_in + (TOKEN_OUT / 1_000_000) * c2_out
                
                # Dominancia: Q2 >= Q1 Y C2 <= C1
                if q2 >= q1 and c2 <= c1:
                    if not (abs(q2 - q1) < 0.001 and abs(c2 - c1) < 0.0001):
                        dominados.append({
                            'key': k1,
                            'name': m1['name'],
                            'familia': familia,
                            'quality': q1,
                            'cost_examen': c1,
                            'dominador_key': k2,
                            'dominador_name': m2['name'],
                            'dominador_quality': q2,
                            'dominador_cost': c2
                        })
                        dominancias[k1] = (k2, m2, c2)
                        break
    
    print(f"Total modelos dominados: {len(dominados)}\n")
    
    # Calcular score de dominancia para rankear
    for d in dominados:
        diff_q = d['dominador_quality'] - d['quality']
        ratio_c = d['cost_examen'] / d['dominador_cost'] if d['dominador_cost'] > 0 else 1
        d['dominancia_score'] = diff_q * 10 + (ratio_c - 1)
    
    # Ordenar por dominancia_score
    dominados.sort(key=lambda x: -x['dominancia_score'])
    
    # Guardar
    resultado = {
        'total_candidatos': len(candidatos),
        'total_dominados': len(dominados),
        'necesitamos_jubilar': len(candidatos) - 90,
        'lista_dominados': dominados
    }
    
    with open('benchmarks/dominancia_resultado.json', 'w', encoding='utf-8') as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Guardado en benchmarks/dominancia_resultado.json")
    
    # Mostrar top 10
    print(f"\nTop 10 más dominados:")
    for i, d in enumerate(dominados[:10], 1):
        print(f"{i:2}. {d['name']:<35} Q={d['quality']:.2f} ${d['cost_examen']:.4f}")
        print(f"    ← {d['dominador_name']:<30} Q={d['dominador_quality']:.2f} ${d['dominador_cost']:.4f}")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
