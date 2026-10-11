#!/usr/bin/env python3
"""Versión simple sin tempfile para debug."""

import argparse
import json
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

# Cargar
input_path = Path(args.input_file)
with open(input_path) as f:
    data = json.load(f)

print(f'Archivo: {input_path.name}')
print(f'Total results ANTES: {len(data["results"])}')

# Crear juez
judge = create_judge(api_key=OPENROUTER_API_KEY, judge_model=args.judge_model, prefer_local=False)

# Procesar
evaluated = 0
for idx, result in enumerate(data['results']):
    if result.get('judge_evaluation') is not None:
        continue
    
    response = result.get('response', result.get('response_preview', '')).strip()
    if not response:
        continue
    
    if args.limit and evaluated >= args.limit:
        break
    
    suite_name = result.get('suite', '')
    test_name = result.get('test_name', '')
    test_dict = find_test(suite_name, test_name)
    
    if not test_dict:
        print(f'[{idx}] {test_name} - Test no encontrado')
        continue
    
    try:
        eval_result = judge.evaluate(response, test_dict, suite_name)
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
        print(f'[{idx}] {test_name} ❌ {e}')

print(f'\n✅ Evaluados: {evaluated} tests')
print(f'Total results DESPUÉS (antes de guardar): {len(data["results"])}')

# Guardar directamente
with open(input_path, 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f'💾 Guardado: {input_path}')

# Verificar
with open(input_path) as f:
    verify = json.load(f)
    
print(f'\n🔍 Verificación:')
print(f'   Total results en archivo: {len(verify["results"])}')
with_judge = [r for r in verify["results"] if r.get("judge_evaluation")]
print(f'   Con judging: {len(with_judge)}')
