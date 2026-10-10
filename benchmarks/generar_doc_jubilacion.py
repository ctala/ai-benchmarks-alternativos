#!/usr/bin/env python3
"""Genera docs/jubilacion-2026-10.md completo con todos los modelos."""
import json
from pathlib import Path

def main():
    # Cargar datos
    data_final = json.load(open('docs/jubilacion-2026-10-final.json'))
    data_dom = json.load(open('benchmarks/dominancia_resultado.json'))
    models_full = json.load(open('docs/data/models.json'))['models']
    models_dict = {m['key']: m for m in models_full}
    
    # Mapear dominador por key
    dom_map = {d['key']: d for d in data_dom['lista_dominados']}
    jubilados_dom_keys = {d['key'] for d in data_final['listas']['dominados_jubilados']}
    
    md = []
    md.append("# Jubilación de Modelos AI - Octubre 2026")
    md.append("")
    md.append(f"**Fecha**: {data_final['fecha']}")
    md.append(f"**Decisión**: Establecer roster activo de {data_final['meta_activos']} modelos + {data_final['cupos_reservados']} cupos = 100 total")
    md.append("")
    md.append("## Resumen Ejecutivo")
    md.append("")
    md.append(f"- **Total modelos en catálogo**: {data_final['total_modelos']}")
    md.append(f"- **Activos**: {data_final['activos']}")
    md.append(f"- **Jubilados**: {data_final['jubilados']}")
    md.append(f"- **Cupos reservados**: {data_final['cupos_reservados']}")
    md.append("")
    md.append("### Desglose de Jubilados")
    md.append("")
    for cat, count in data_final['desglose_jubilados'].items():
        md.append(f"- **{cat.replace('_', ' ').title()}**: {count}")
    md.append("")
    md.append("### Dominados")
    md.append("")
    md.append(f"- Total detectados: {data_final['dominados_info']['total_detectados']}")
    md.append(f"- Jubilados (los más claramente dominados): {data_final['dominados_info']['jubilados']}")
    md.append(f"- Quedan activos: {data_final['dominados_info']['quedan_activos']}")
    md.append("")
    md.append(f"**Motivo**: {data_final['dominados_info']['motivo_quedan_activos']}")
    md.append("")
    md.append("## Definición de Familia")
    md.append("")
    md.append("**Familia** = mismo proveedor y misma línea base, sin importar generación.")
    md.append("")
    md.append("Ejemplos:")
    md.append("- Qwen 3.5, 3.6, 3.7, 3.8 → familia \"Qwen\"")
    md.append("- GPT-5.5, GPT-5.6 Luna → familia \"GPT\"")
    md.append("- Claude Opus 4.7, 4.8 → familia \"ClaudeOpus\"")
    md.append("")
    md.append("Ver `METODOLOGIA.md` para definición completa.")
    md.append("")
    md.append("## Proyección de Costo Mensual")
    md.append("")
    md.append("**⚠️ SUPUESTO**: Asumimos medir 33% de los 100 modelos cada mes (33 modelos).")
    md.append("")
    md.append("- Costo promedio: ~$8.56 por modelo completo (22 suites)")
    md.append("- **Costo mensual estimado**: 33 × $8.56 ≈ **$282/mes**")
    md.append("")
    md.append("## Criterios de Jubilación (Orden de Prioridad)")
    md.append("")
    md.append("1. **Retired** — Proveedor deprecó el modelo")
    md.append("2. **Provider variant** — Mide serving, no calidad")
    md.append("3. **Sin runs** — Nunca medido (0 runs)")
    md.append("4. **Dominado** — Otro de su familia tiene Q >= y costo <=")
    md.append("")
    md.append("## Listado Completo de Modelos")
    md.append("")
    
    # Activos
    md.append(f"### Activos ({data_final['activos']})")
    md.append("")
    md.append("| # | Modelo | Quality | Costo/examen | Runs | Nota |")
    md.append("|---|--------|---------|--------------|------|------|")
    for i, m in enumerate(sorted(data_final['listas']['activos'], 
                                  key=lambda x: -(models_dict[x['key']].get('quality_avg', 0) or models_dict[x['key']].get('score_global', 0))), 1):
        full = models_dict[m['key']]
        q = full.get('quality_avg') or full.get('score_global', 0)
        cost = (0.3 / 1000) * full.get('cost_input_per_M', 0) + (1.5 / 1000) * full.get('cost_output_per_M', 0)
        nota = ""
        if m['key'] in dom_map and m['key'] not in jubilados_dom_keys:
            nota = f"Dominado por {dom_map[m['key']]['dominador_name']} (Q={dom_map[m['key']]['dominador_quality']:.2f}, ${dom_map[m['key']]['dominador_cost']:.4f})"
        md.append(f"| {i} | {m['name']} | {q:.2f} | ${cost:.4f} | {full.get('runs', 0)} | {nota} |")
    md.append("")
    
    # Jubilados
    md.append(f"### Jubilados ({data_final['jubilados']})")
    md.append("")
    
    for cat, cat_name in [('retired', 'Retired'), 
                          ('provider_variant', 'Provider Variants'), 
                          ('sin_runs', 'Sin Runs')]:
        lista = data_final['listas'][cat]
        md.append(f"#### {cat_name} ({len(lista)})")
        md.append("")
        md.append("| Modelo | Runs | Nota |")
        md.append("|--------|------|------|")
        for m in sorted(lista, key=lambda x: x['name']):
            full = models_dict[m['key']]
            nota = full.get('notes', '').split('\n')[0][:50] if full.get('notes') else ''
            md.append(f"| {m['name']} | {full.get('runs', 0)} | {nota} |")
        md.append("")
    
    # Dominados jubilados
    md.append(f"#### Dominados Jubilados ({len(data_final['listas']['dominados_jubilados'])})")
    md.append("")
    md.append("Los 31 más claramente dominados:")
    md.append("")
    md.append("| # | Modelo | Quality | Costo | Dominado por | Q Dom. | Costo Dom. |")
    md.append("|---|--------|---------|-------|--------------|--------|------------|")
    for i, d in enumerate(data_final['listas']['dominados_jubilados'], 1):
        md.append(f"| {i} | {d['name']} | {d['quality']:.2f} | ${d['cost_examen']:.4f} | {d['dominador_name']} | {d['dominador_quality']:.2f} | ${d['dominador_cost']:.4f} |")
    md.append("")
    
    # Guardar
    with open('docs/jubilacion-2026-10.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))
    
    print(f"✓ Generado docs/jubilacion-2026-10.md ({len(md)} líneas)")
    print(f"\n**Comando para regenerar**:")
    print(f"```bash")
    print(f"python3 benchmarks/analizar_dominancia.py")
    print(f"python3 benchmarks/analizar_jubilacion_final.py")
    print(f"python3 benchmarks/generar_doc_jubilacion.py")
    print(f"```")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
