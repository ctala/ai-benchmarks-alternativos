#!/usr/bin/env python3
"""Última versión con copia explícita."""

import argparse
import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from benchmarks.llm_judge import create_judge, judge_score_to_10
from benchmarks.config import OPENROUTER_API_KEY
from benchmarks.tests import (
    content_generation, tool_calling, task_management, code_generation,
    reasoning, summarization, presentation, startup_content, deep_reasoning,
    customer_support, structured_output, hallucination, creativity, string_precision,
    news_seo_writing, ocr_extraction, orchestration, multi_turn, policy_adherence,
    agent_capabilities, strategy, sales_outreach, translation, agent_long_horizon,
    niah_es, integridad_idioma, verificar_claim, verificar_claims_lote, extraer_claims,
    dominio_entidad, tool_calling_adversarial, prompt_injection_es, business_audit,
    business_strategy, content_verificable
)

ALL_TEST_SUITES = {
    "business_audit": business_audit.TESTS,
    "business_strategy": business_strategy.TESTS,
    "content_verificable": content_verificable.TESTS,
    "content_generation": content_generation.TESTS,
    "tool_calling": tool_calling.TESTS,
    "task_management": task_management.TESTS,
    "code_generation": code_generation.TESTS,
    "reasoning": reasoning.TESTS,
    "summarization": summarization.TESTS,
    "presentation": presentation.TESTS,
    "startup_content": startup_content.TESTS,
    "deep_reasoning": deep_reasoning.TESTS,
    "customer_support": customer_support.TESTS,
    "structured_output": structured_output.TESTS,
    "hallucination": hallucination.TESTS,
    "creativity": creativity.TESTS,
    "string_precision": string_precision.TESTS,
    "news_seo_writing": news_seo_writing.TESTS,
    "ocr_extraction": ocr_extraction.TESTS,
    "orchestration": orchestration.TESTS,
    "multi_turn": multi_turn.TESTS,
    "policy_adherence": policy_adherence.TESTS,
    "agent_capabilities": agent_capabilities.TESTS,
    "strategy": strategy.TESTS,
    "sales_outreach": sales_outreach.TESTS,
    "translation": translation.TESTS,
    "agent_long_horizon": agent_long_horizon.TESTS,
    "niah_es": niah_es.TESTS,
    "integridad_idioma": integridad_idioma.TESTS,
    "verificar_claim": verificar_claim.TESTS,
    "verificar_claims_lote": verificar_claims_lote.TESTS,
    "extraer_claims": extraer_claims.TESTS,
    "dominio_entidad": dominio_entidad.TESTS,
    "tool_calling_adversarial": tool_calling_adversarial.TESTS,
    "prompt_injection_es": prompt_injection_es.TESTS,
}

def find_test(suite_name, test_name):
    tests = ALL_TEST_SUITES.get(suite_name, [])
    for test in tests:
        if test.get('name') == test_name:
            return test
    return None

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('--judge-model', default='phi4-or')
parser.add_argument('--limit', type=int)
args = parser.parse_args()

# Copiar a .tmp EXPLICITAMENTE
input_path = Path(args.input_file)
tmp_path = input_path.with_suffix('.tmp')

print(f'📁 Copiando {input_path.name} -> {tmp_path.name}')
shutil.copy2(input_path, tmp_path)

# Cargar desde .tmp
with open(tmp_path) as f:
    data = json.load(f)

print(f'📊 Total results: {len(data["results"])}')
models_before = set(r.get('model', 'N/A') for r in data['results'])
print(f'   Modelos: {len(models_before)}')
[print(f'     - {m}') for m in sorted(models_before)]

# Crear juez
judge = create_judge(api_key=OPENROUTER_API_KEY, judge_model=args.judge_model, prefer_local=False)

# Procesar
evaluated = 0
skipped_ok = 0
for idx, result in enumerate(data['results']):
    # Re-juzgar si tiene score=-1 (error previo), sino saltear si ya tiene judging exitoso
    judge_eval = result.get('judge_evaluation')
    if judge_eval is not None:
        score = judge_eval.get('score_final', 0)
        if score >= 0:  # Ya tiene judging exitoso
            skipped_ok += 1
            continue
        # Si score=-1, volver a juzgar (era un error)
        print(f'[{idx}] Re-juzgando test con error previo: {result.get("test_name", "N/A")}')
    
    response = result.get('response', result.get('response_preview', '')).strip()
    if not response:
        continue
    
    if args.limit and evaluated >= args.limit:
        break
    
    suite_name = result.get('suite', '')
    test_name = result.get('test_name', '')
    test_dict = find_test(suite_name, test_name)
    
    if not test_dict:
        continue
    
    try:
        eval_result = judge.evaluate(response, test_dict, suite_name)
        
        # ⚠️ DETECCIÓN DE ERROR 402 - DETENER INMEDIATAMENTE
        if eval_result.get('score_final', 0) < 0:
            error_msg = eval_result.get('error', '')
            if '402' in error_msg or 'credit' in error_msg.lower() or 'insufficient' in error_msg.lower():
                print(f'\n❌ ERROR 402 - SIN CRÉDITO EN OPENROUTER')
                print(f'   Test: {test_name}')
                print(f'   Error: {error_msg[:150]}')
                print(f'\n🛑 DETENIENDO JUDGING - Evaluados: {evaluated}/{evaluated + len(data["results"]) - idx}')
                print(f'   Tests exitosos: {evaluated}')
                print(f'   Tests saltados (OK): {skipped_ok}')
                print(f'   Pendientes: {len(data["results"]) - idx - skipped_ok - evaluated}')
                print(f'\n💡 Agregar crédito a OpenRouter y volver a ejecutar este script.')
                # NO guardar el resultado con error, salir inmediatamente
                sys.exit(1)
        
        result['judge_evaluation'] = eval_result
        
        # Re-calcular quality
        is_niah = test_dict.get('expected_answer', {}).get('type') == 'niah_extraction'
        tiene_verdad = bool(test_dict.get('expected_answer'))
        
        if not is_niah and not tiene_verdad:
            auto_quality = result.get('auto_quality', result.get('quality', 5.0))
            judge_quality = judge_score_to_10(eval_result)
            result['quality'] = round(auto_quality * 0.3 + judge_quality * 0.7, 2)
        
        evaluated += 1
        score = eval_result.get('score_final', 0)
        print(f'[{evaluated}] {test_name[:50]:50s} ✅ ({score:.2f}/5)')
        
    except Exception as e:
        error_str = str(e)
        # Detectar error 402 en excepciones también
        if '402' in error_str or 'credit' in error_str.lower() or 'insufficient' in error_str.lower():
            print(f'\n❌ ERROR 402 CAPTURADO EN EXCEPCIÓN')
            print(f'   Test: {test_name}')
            print(f'   Error: {error_str[:150]}')
            print(f'\n🛑 DETENIENDO JUDGING')
            sys.exit(1)
        print(f'[{idx}] {test_name} ❌ {e}')

print(f'\n✅ Evaluados: {evaluated} tests')
print(f'   Saltados (ya OK): {skipped_ok} tests')
print(f'   Total procesado: {evaluated + skipped_ok} tests')

# Guardar en .tmp
with open(tmp_path, 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Verificar .tmp
with open(tmp_path) as f:
    verify = json.load(f)

models_after = set(r.get('model', 'N/A') for r in verify['results'])
print(f'\n🔍 Verificación archivo .tmp:')
print(f'   Total results: {len(verify["results"])}')
print(f'   Modelos: {len(models_after)}')
with_judge = [r for r in verify["results"] if r.get("judge_evaluation")]
print(f'   Con judging: {len(with_judge)}')

if models_before != models_after:
    print(f'\n⚠️  ERROR: Los modelos cambiaron!')
    print(f'   Antes: {models_before}')
    print(f'   Después: {models_after}')
    sys.exit(1)

if len(verify['results']) != len(data['results']):
    print(f'\n⚠️  ERROR: El número de results cambió!')
    sys.exit(1)

# Solo si todo OK, reemplazar
print(f'\n💾 Reemplazando archivo original...')
shutil.move(tmp_path, input_path)
print(f'✅ Guardado: {input_path}')
