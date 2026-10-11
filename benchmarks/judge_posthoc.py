#!/usr/bin/env python3
"""
Agrega judging post-facto a resultados ya medidos.

Uso:
    python benchmarks/judge_posthoc.py archivo.json --judge-model phi4-or --budget-cap 10
"""

import argparse
import json
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from benchmarks.llm_judge import create_judge, judge_score_to_10
from benchmarks.config import OPENROUTER_API_KEY
import requests

# Importar test suites para obtener criterios
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
    """Busca el test dict original."""
    tests = ALL_TEST_SUITES.get(suite_name, [])
    for test in tests:
        if test.get('name') == test_name:
            return test
    return None


def check_budget(baseline, cap, api_key):
    """Verifica presupuesto."""
    try:
        headers = {'Authorization': f'Bearer {api_key}'}
        r = requests.get('https://openrouter.ai/api/v1/auth/key', headers=headers, timeout=10)
        if r.status_code == 200:
            current = r.json().get('data', {}).get('usage', 0)
            spent = current - baseline
            return spent >= cap, current, spent
    except:
        pass
    return False, 0, 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='JSON de benchmark a juzgar')
    parser.add_argument('--judge-model', default='phi4-or', help='Modelo juez')
    parser.add_argument('--budget-cap', type=float, help='Tope de presupuesto USD')
    parser.add_argument('--limit', type=int, help='Limitar número de tests a juzgar')
    args = parser.parse_args()
    
    # Establecer línea base
    budget_baseline = None
    if args.budget_cap:
        try:
            headers = {'Authorization': f'Bearer {OPENROUTER_API_KEY}'}
            r = requests.get('https://openrouter.ai/api/v1/auth/key', headers=headers, timeout=10)
            if r.status_code == 200:
                budget_baseline = r.json().get('data', {}).get('usage', 0)
                print(f'💰 Línea base: ${budget_baseline:.2f}')
                print(f'   Tope: ${args.budget_cap:.2f}')
                print(f'   Límite total: ${budget_baseline + args.budget_cap:.2f}\n')
        except Exception as e:
            print(f'❌ Error estableciendo línea base: {e}')
            return 1
    
    # Cargar JSON
    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f'❌ Archivo no existe: {input_path}')
        return 1
    
    with open(input_path) as f:
        data = json.load(f)
    
    results = data.get('results', [])
    
    # Contar tests que necesitan judging
    need_judging_count = sum(1 for r in results 
                             if r.get('judge_evaluation') is None 
                             and (r.get('response') or r.get('response_preview', '')).strip())
    
    print(f'📊 Tests totales: {len(results)}')
    print(f'   Necesitan judging: {need_judging_count}')
    print(f'   Ya juzgados: {len([r for r in results if r.get("judge_evaluation")])}')
    
    if need_judging_count == 0:
        print('✅ Todos los tests ya tienen judging')
        return 0
    
    if args.limit:
        print(f'   Limitando a: {args.limit} tests\n')
    else:
        print()
    
    # Crear juez
    judge = create_judge(api_key=OPENROUTER_API_KEY, judge_model=args.judge_model, prefer_local=False)
    print(f'🧑‍⚖️  Juez: {args.judge_model}\n')
    
    # Procesar - iterar directamente sobre data['results']
    evaluated = 0
    processed = 0
    for idx, result in enumerate(data['results']):
        # Saltear si ya tiene judging
        if result.get('judge_evaluation') is not None:
            continue
        
        # Saltear si no tiene respuesta
        response = result.get('response', result.get('response_preview', ''))
        if not response or not response.strip():
            continue
        
        processed += 1
        
        # Límite si se especificó
        if args.limit and evaluated >= args.limit:
            break
        
        # Checkpoint cada 25
        if evaluated > 0 and evaluated % 25 == 0:
            if args.budget_cap and budget_baseline is not None:
                exceeded, current, spent = check_budget(budget_baseline, args.budget_cap, OPENROUTER_API_KEY)
                print(f'\n💰 Checkpoint {evaluated}: ${spent:.2f} / ${args.budget_cap:.2f}')
                if exceeded:
                    print(f'\n⚠️  BUDGET CAP ALCANZADO')
                    break
            
            # Guardar checkpoint
            temp_fd, temp_path = tempfile.mkstemp(suffix='.json', dir=input_path.parent)
            try:
                with os.fdopen(temp_fd, 'w') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f'   💾 Checkpoint guardado')
            except:
                os.close(temp_fd)
                if Path(temp_path).exists():
                    Path(temp_path).unlink()
                raise
        
        suite_name = result.get('suite', '')
        test_name = result.get('test_name', '')
        
        # Buscar test original
        test_dict = find_test(suite_name, test_name)
        if not test_dict:
            print(f'[{processed}] {test_name[:50]:50s} ⚠️  Test no encontrado')
            continue
        
        try:
            # Evaluar
            eval_result = judge.evaluate(response, test_dict, suite_name)
            data['results'][idx]['judge_evaluation'] = eval_result
            
            # Re-calcular quality (solo si no es niah o verificable)
            is_niah = test_dict.get('expected_answer', {}).get('type') == 'niah_extraction'
            tiene_verdad = bool(test_dict.get('expected_answer'))
            
            if not is_niah and not tiene_verdad:
                auto_quality = result.get('auto_quality', result.get('quality', 5.0))
                judge_quality = judge_score_to_10(eval_result)
                data['results'][idx]['quality'] = round(auto_quality * 0.3 + judge_quality * 0.7, 2)
            
            evaluated += 1
            score = eval_result.get('score_final', 0)
            print(f'[{processed}] {test_name[:50]:50s} ✅ ({score:.2f}/5)')
            
        except Exception as e:
            print(f'[{processed}] {test_name[:50]:50s} ❌ {str(e)[:50]}')
    
    # Guardar final con escritura atómica
    print(f'\n💾 Guardando resultado final...')
    temp_fd, temp_path = tempfile.mkstemp(suffix='.json', dir=input_path.parent)
    try:
        with os.fdopen(temp_fd, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        # Validar que el temp file carga correctamente
        with open(temp_path) as f:
            json.load(f)
        
        # Rename atómico
        os.replace(temp_path, input_path)
        print(f'✅ Guardado: {input_path}')
    except Exception as e:
        os.close(temp_fd)
        if Path(temp_path).exists():
            Path(temp_path).unlink()
        print(f'❌ Error guardando: {e}')
        return 1
    
    # Reporte final
    if args.budget_cap and budget_baseline is not None:
        exceeded, current, spent = check_budget(budget_baseline, args.budget_cap, OPENROUTER_API_KEY)
        print(f'\n💰 Gasto final: ${spent:.2f} / ${args.budget_cap:.2f}')
    
    stats = judge.get_stats()
    print(f'📊 Evaluados: {evaluated} tests')
    print(f'   Juez: {stats["evaluations"]} llamadas, ~${stats["estimated_cost_usd"]:.4f}')
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
