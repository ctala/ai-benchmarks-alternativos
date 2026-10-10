#!/usr/bin/env python3
"""
Análisis final de jubilación con orden de prioridad.
Soporta dos opciones:
  A) Regla estricta: jubilar TODOS los dominados (62) → 59 activos + 41 cupos
  B) Regla flexible: jubilar solo los 31 más dominados → 90 activos + 10 cupos
"""
import json
import sys
import argparse
from pathlib import Path

ROSTER_TOTAL = 100

def get_meta_activos(opcion):
    """Retorna la meta de activos según la opción."""
    if opcion == 'A':
        return 59  # Jubilar todos los dominados
    else:  # opcion == 'B'
        return 90  # Jubilar solo los más dominados

def main():
    parser = argparse.ArgumentParser(description='Análisis de jubilación con dos opciones')
    parser.add_argument('--opcion', choices=['A', 'B'], default='B',
                      help='A: regla estricta (59 activos), B: flexible (90 activos, default)')
    args = parser.parse_args()
    
    opcion = args.opcion
    meta_activos = get_meta_activos(opcion)
    cupos = ROSTER_TOTAL - meta_activos
    
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
    print(f"ANÁLISIS DE JUBILACIÓN - Opción {opcion}")
    print(f"{'='*60}\n")
    print(f"Total modelos:                  {len(models)}")
    print(f"Roster objetivo:                {ROSTER_TOTAL} ({meta_activos} activos + {cupos} cupos)")
    print(f"\nCriterios 1-3:")
    print(f"  Retired:                      {sum(1 for m, _, _ in jubilados_1_2_3 if m == 'retired')}")
    print(f"  Provider variant:             {sum(1 for m, _, _ in jubilados_1_2_3 if m == 'provider_variant')}")
    print(f"  Sin runs:                     {sum(1 for m, _, _ in jubilados_1_2_3 if m == 'sin_runs')}")
    print(f"  Subtotal jubilados (1-3):     {len(jubilados_1_2_3)}")
    print(f"\nCandidatos post-1-3:            {len(candidatos)}")
    print(f"Meta activos:                   {meta_activos}")
    print(f"Deben jubilarse por criterio 4: {len(candidatos) - meta_activos}")
    
    # Paso 4: Jubilar dominados según la opción
    necesitamos_jubilar = len(candidatos) - meta_activos
    dominados_a_jubilar = []
    
    if necesitamos_jubilar > 0:
        for d in dominados_list:
            if len(dominados_a_jubilar) >= necesitamos_jubilar:
                break
            if d['key'] in candidatos:  # Solo si es candidato
                dominados_a_jubilar.append(d)
    elif necesitamos_jubilar < 0:
        print(f"\n⚠️  WARNING: Ya hay más activos ({len(candidatos)}) que la meta ({meta_activos})")
        return 1
    
    total_dominados_candidatos = len([d for d in dominados_list if d['key'] in candidatos])
    dominados_activos = total_dominados_candidatos - len(dominados_a_jubilar)
    
    print(f"\nCriterio 4 (dominados):")
    print(f"  Total dominados detectados:   {total_dominados_candidatos}")
    if opcion == 'A':
        print(f"  Jubilados (TODOS):            {len(dominados_a_jubilar)}")
        print(f"  Quedan activos:               {dominados_activos}")
    else:
        print(f"  Jubilados (los N más claros): {len(dominados_a_jubilar)}")
        print(f"  Quedan activos (referencia):  {dominados_activos}")
    
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
    print(f"Cupos reservados:               {cupos:>3}")
    print(f"{'─'*40}")
    print(f"ROSTER TOTAL:                   {ROSTER_TOTAL:>3}")
    print(f"TOTAL MODELOS:                  {total_activos + total_jubilados:>3}")
    
    if total_activos + total_jubilados != len(models):
        print(f"\n❌ ERROR: {total_activos} + {total_jubilados} ≠ {len(models)}")
        return 1
    
    if total_activos != meta_activos:
        print(f"\n❌ ERROR: Activos {total_activos} ≠ Meta {meta_activos}")
        return 1
    
    print(f"\n✓ ¡Perfecto! {total_activos} activos + {total_jubilados} jubilados = {len(models)}")
    
    # Proyección de costos (basado en datos reales abr-sep 2026)
    COSTO_POR_MODELO_MES = 1.67  # $119/mes ÷ 71 modelos/mes
    COSTO_EXAMEN_COMPLETO = 8.56  # 22 suites
    
    costo_mensual = total_activos * COSTO_POR_MODELO_MES
    costo_examen_completo = total_activos * COSTO_EXAMEN_COMPLETO
    
    print(f"\n{'='*60}")
    print(f"PROYECCIÓN DE COSTOS (Opción {opcion})")
    print(f"{'='*60}")
    print(f"Costo mensual estimado:         ${costo_mensual:.2f}/mes")
    print(f"  ({total_activos} modelos × ${COSTO_POR_MODELO_MES}/modelo/mes)")
    print(f"  Fuente: $119/mes ÷ 71 modelos/mes (abr-sep 2026)")
    print(f"\nExamen completo de todos:       ${costo_examen_completo:.2f}")
    print(f"  ({total_activos} modelos × ${COSTO_EXAMEN_COMPLETO}/examen completo)")
    print(f"  (22 suites, si se re-midieran todos)")
    
    # Guardar
    resultado = {
        'fecha': '2026-10-10',
        'opcion': opcion,
        'roster_total': ROSTER_TOTAL,
        'total_modelos': len(models),
        'meta_activos': meta_activos,
        'jubilados': total_jubilados,
        'activos': total_activos,
        'cupos_reservados': cupos,
        'costos': {
            'mensual_estimado': round(costo_mensual, 2),
            'costo_por_modelo_mes': COSTO_POR_MODELO_MES,
            'fuente': '$119/mes ÷ 71 modelos/mes (abr-sep 2026)',
            'examen_completo_todos': round(costo_examen_completo, 2),
            'costo_examen_completo': COSTO_EXAMEN_COMPLETO
        },
        'desglose_jubilados': {
            'retired': len(categorias['retired']),
            'provider_variant': len(categorias['provider_variant']),
            'sin_runs': len(categorias['sin_runs']),
            'dominado': len(categorias['dominado'])
        },
        'dominados_info': {
            'total_detectados': total_dominados_candidatos,
            'jubilados': len(dominados_a_jubilar),
            'quedan_activos': dominados_activos,
            'motivo_quedan_activos': 
                'Todos los dominados se jubilan (regla estricta)' if opcion == 'A'
                else f'Se mantienen los {dominados_activos} menos dominados para preservar diversidad y alcanzar {meta_activos} activos'
        },
        'listas': {
            'dominados_jubilados': dominados_a_jubilar,
            'retired': [{'key': k, 'name': m['name']} for k, m in categorias['retired']],
            'provider_variant': [{'key': k, 'name': m['name']} for k, m in categorias['provider_variant']],
            'sin_runs': [{'key': k, 'name': m['name']} for k, m in categorias['sin_runs']],
            'activos': [{'key': k, 'name': m['name']} for k, m in categorias['activo']]
        }
    }
    
    output_file = f'docs/jubilacion-2026-10-opcion-{opcion}.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)
    
    # También guardar como -final para backward compat si es opción B
    if opcion == 'B':
        with open('docs/jubilacion-2026-10-final.json', 'w', encoding='utf-8') as f:
            json.dump(resultado, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Guardado en {output_file}")
    if opcion == 'B':
        print(f"✓ También en docs/jubilacion-2026-10-final.json (default)")
    return 0

if __name__ == '__main__':
    sys.exit(main())
