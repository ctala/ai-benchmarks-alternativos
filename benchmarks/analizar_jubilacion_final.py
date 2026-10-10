#!/usr/bin/env python3
"""
Análisis final de jubilación con orden de prioridad y límite de dominados.
Meta: 90 activos + 10 cupos = 100 total
"""
import json
import sys
from pathlib import Path

META_ACTIVOS = 90

def main():
    # Cargar datos
    data = json.load(open('docs/data/models.json'))
    models = {m['key']: m for m in data['models']}
    
    # Cargar dominancia
    dom_file = Path('benchmarks/dominancia_resultado.json')
    if not dom_file.exists():
        print("⚠️  Ejecutar primero: python3 benchmarks/analizar_dominancia.py")
        return 1
    
    dominados_data = json.load(open(dom_file))
    dominados_list = dominados_data['lista_dominados']  # Ya ordenados por dominancia_score
    
    # Paso 1-3: Aplicar criterios con prioridad
    jubilados_1_2_3 = []
    for key, m in models.items():
        if m.get('retired'):
            jubilados_1_2_3.append(('retired', key, m))
        elif m.get('provider_variant'):
            jubilados_1_2_3.append(('provider_variant', key, m))
        elif m.get('runs', 0) == 0:
            jubilados_1_2_3.append(('sin_runs', key, m))
    
    jubilados_keys_1_2_3 = {k for _, k, _ in jubilados_1_2_3}
    candidatos = {k: m for k, m in models.items() if k not in jubilados_keys_1_2_3}
    
    print(f"{'='*60}")
    print(f"ANÁLISIS DE JUBILACIÓN - Paso a Paso")
    print(f"{'='*60}\n")
    print(f"Total modelos:                  {len(models)}")
    print(f"\nCriterios 1-3:")
    print(f"  Retired:                      {sum(1 for m, _, _ in jubilados_1_2_3 if m == 'retired')}")
    print(f"  Provider variant:             {sum(1 for m, _, _ in jubilados_1_2_3 if m == 'provider_variant')}")
    print(f"  Sin runs:                     {sum(1 for m, _, _ in jubilados_1_2_3 if m == 'sin_runs')}")
    print(f"  Subtotal jubilados (1-3):     {len(jubilados_1_2_3)}")
    print(f"\nCandidatos post-1-3:            {len(candidatos)}")
    print(f"Meta activos:                   {META_ACTIVOS}")
    print(f"Deben jubilarse por criterio 4: {len(candidatos) - META_ACTIVOS}")
    
    # Paso 4: Jubilar solo los N más dominados necesarios
    necesitamos_jubilar = len(candidatos) - META_ACTIVOS
    dominados_a_jubilar = []
    
    for d in dominados_list:
        if len(dominados_a_jubilar) >= necesitamos_jubilar:
            break
        if d['key'] in candidatos:  # Solo si es candidato
            dominados_a_jubilar.append(d)
    
    print(f"\nCriterio 4 (dominados):")
    print(f"  Total dominados detectados:   {len([d for d in dominados_list if d['key'] in candidatos])}")
    print(f"  Jubilados (los N más claros): {len(dominados_a_jubilar)}")
    print(f"  Quedan activos (menos dominados): {len([d for d in dominados_list if d['key'] in candidatos]) - len(dominados_a_jubilar)}")
    
    # Construir categorías finales
    categorias = {
        'retired': [(k, m) for mot, k, m in jubilados_1_2_3 if mot == 'retired'],
        'provider_variant': [(k, m) for mot, k, m in jubilados_1_2_3 if mot == 'provider_variant'],
        'sin_runs': [(k, m) for mot, k, m in jubilados_1_2_3 if mot == 'sin_runs'],
        'dominado': [(d['key'], models[d['key']]) for d in dominados_a_jubilar],
        'activo': [(k, m) for k, m in candidatos.items() if k not in {d['key'] for d in dominados_a_jubilar}]
    }
    
    # Verificar
    total_jubilados = sum(len(v) for k, v in categorias.items() if k != 'activo')
    total_activos = len(categorias['activo'])
    
    print(f"\n{'='*60}")
    print(f"RESUMEN FINAL")
    print(f"{'='*60}")
    print(f"\nJubilados por motivo:")
    for cat in ['retired', 'provider_variant', 'sin_runs', 'dominado']:
        print(f"  {cat.replace('_', ' ').title():<25} {len(categorias[cat]):>3}")
    print(f"  {'─'*40}")
    print(f"  TOTAL JUBILADOS:              {total_jubilados:>3}")
    print(f"\nActivos:                        {total_activos:>3}")
    print(f"Cupos reservados:                10")
    print(f"{'─'*40}")
    print(f"TOTAL (90 + jubilados):         {total_activos + total_jubilados:>3}")
    
    if total_activos + total_jubilados != len(models):
        print(f"\n❌ ERROR: {total_activos} + {total_jubilados} ≠ {len(models)}")
        return 1
    
    if total_activos != META_ACTIVOS:
        print(f"\n❌ ERROR: Activos {total_activos} ≠ Meta {META_ACTIVOS}")
        return 1
    
    print(f"\n✓ ¡Perfecto! {total_activos} activos + {total_jubilados} jubilados = {len(models)}")
    
    # Guardar
    resultado = {
        'fecha': '2026-10-10',
        'total_modelos': len(models),
        'meta_activos': META_ACTIVOS,
        'jubilados': total_jubilados,
        'activos': total_activos,
        'cupos_reservados': 10,
        'desglose_jubilados': {
            'retired': len(categorias['retired']),
            'provider_variant': len(categorias['provider_variant']),
            'sin_runs': len(categorias['sin_runs']),
            'dominado': len(categorias['dominado'])
        },
        'dominados_info': {
            'total_detectados': len([d for d in dominados_list if d['key'] in candidatos]),
            'jubilados': len(dominados_a_jubilar),
            'quedan_activos': len([d for d in dominados_list if d['key'] in candidatos]) - len(dominados_a_jubilar),
            'motivo_quedan_activos': 'Se mantienen los menos dominados para preservar diversidad dentro de familias grandes y alcanzar exactamente 90 activos'
        },
        'listas': {
            'dominados_jubilados': dominados_a_jubilar,
            'retired': [{'key': k, 'name': m['name']} for k, m in categorias['retired']],
            'provider_variant': [{'key': k, 'name': m['name']} for k, m in categorias['provider_variant']],
            'sin_runs': [{'key': k, 'name': m['name']} for k, m in categorias['sin_runs']],
            'activos': [{'key': k, 'name': m['name']} for k, m in categorias['activo']]
        }
    }
    
    with open('docs/jubilacion-2026-10-final.json', 'w', encoding='utf-8') as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Guardado en docs/jubilacion-2026-10-final.json")
    return 0

if __name__ == '__main__':
    sys.exit(main())
