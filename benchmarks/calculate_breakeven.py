#!/usr/bin/env python3
"""
Análisis de break-even: cuándo conviene una suscripción vs pagar API por uso.

Define 5 perfiles de usuario por intensidad y calcula el costo mensual en
pay-per-use vs el precio de cada suscripción relevante. Identifica el punto
donde la suscripción se vuelve más barata que la API.

Uso:
    python benchmarks/calculate_breakeven.py            # tabla completa
    python benchmarks/calculate_breakeven.py --markdown # formato MD para pegar
"""

import argparse
from dataclasses import dataclass


# ====== Perfiles de uso (calls/mes y tokens promedio por call) ======
# Tokens por call: 300 input + 1500 output = 1800 total (estimado conservador
# basado en nuestros 91 tests del benchmark, donde out promedio = ~900 tokens
# pero asume un caso real de agente con prompts más largos).
TOKENS_PER_CALL_INPUT = 300
TOKENS_PER_CALL_OUTPUT = 1500

PROFILES = [
    {"name": "Light (test/dev)",        "calls_per_month": 100,    "scenario": "Probar 1-2 modelos, debuggear flujos"},
    {"name": "Casual (agente ocasional)", "calls_per_month": 500,    "scenario": "1 flow N8N corriendo cada hora laboral"},
    {"name": "Active (agente diario)",  "calls_per_month": 2_000,  "scenario": "3-5 agentes activos, uso normal de equipo"},
    {"name": "Heavy (N8N 24/7)",        "calls_per_month": 10_000, "scenario": "Workflows constantes, múltiples agentes"},
    {"name": "Power (multi-agente prod)", "calls_per_month": 30_000, "scenario": "SaaS con agentes en producción a clientes"},
]


# ====== Modelos representativos pay-per-use ======
# (precio_input, precio_output) por millón de tokens, sin markup adicional.
MODELS = [
    # (key, name, $in/M, $out/M, notes)
    ("devstral", "Devstral Small (#1 ranking, open)",     0.10, 0.30, "vía OpenRouter"),
    ("deepseek-v3", "DeepSeek V3.2 (#7, open MIT)",       0.252, 0.378, "vía OpenRouter"),
    ("deepseek-v4-flash", "DeepSeek V4 Flash (open MIT)", 0.14, 0.28, "OpenRouter, lanzado abr 2026"),
    ("nemotron", "Nemotron 3 Super (NIM gratis 40 RPM)",  0.0, 0.0, "vía NVIDIA NIM"),
    ("gemini-flash-lite", "Gemini 2.5 Flash Lite",        0.075, 0.30, "el más rápido"),
    ("minimax", "MiniMax M2.7 (SOTA agentes)",            0.30, 1.20, "API directa"),
    ("qwen3-coder", "Qwen3 Coder (open Apache)",          0.15, 0.60, "vía OpenRouter"),
    ("gpt-4.1-mini", "GPT-4.1 Mini",                      0.40, 1.60, "OpenAI directo"),
    ("gpt-4.1", "GPT-4.1",                                2.00, 8.00, "OpenAI directo"),
    ("gpt-5.5", "GPT-5.5 (thinking, 4× output real)",     8.00, 45.00, "thinking inflado"),
    ("claude-sonnet", "Claude Sonnet 4.6",                3.00, 15.00, "API directa"),
    ("claude-opus", "Claude Opus 4.7",                    15.00, 75.00, "API directa"),
    ("kimi-k2.6", "Kimi K2.6 thinking (4× output real)",  1.50, 9.00, "thinking inflado"),
]


# ====== Suscripciones con precio fijo ======
# Solo las que dan acceso a API (no chat-only): Claude Pro NO da API
# = inútil para agentes. ChatGPT Plus tampoco.
SUBSCRIPTIONS = [
    # (price_per_month, name, gives_api, equivalent_model_in_pay_per_use)
    (10,  "MiniMax Coding Starter",      True,  "minimax",          "100 prompts/5h"),
    (19,  "MiniMax Agent Pro",            True,  "minimax",         "M2.7 generoso"),
    (20,  "MiniMax Coding Plus",          True,  "minimax",         "300 prompts/5h"),
    (20,  "Ollama Cloud Pro",             True,  "devstral",        "open-source todos"),
    (20,  "Google AI Pro",                True,  "gemini-flash-lite", "Gemini 2.5 Pro generoso"),
    (30,  "SuperGrok",                    True,  "gpt-4.1",         "Grok 4.20 generoso"),
    (50,  "MiniMax Coding Max",           True,  "minimax",         "1000 prompts/5h"),
    (50,  "Qwen Coding Pro",              True,  "qwen3-coder",     "90K req/mes, 10× tokens"),
    (69,  "MiniMax Agent Pro+",           True,  "minimax",         "M2.7 muy generoso"),
    (100, "Ollama Cloud Max",             True,  "devstral",        "todos open generosos"),
    (150, "MiniMax Coding Ultra",         True,  "minimax",         "1000 prompts/5h max-speed"),
    (200, "ChatGPT Pro",                  True,  "gpt-5.5",         "GPT-5.5/o3 generoso"),
]


def cost_per_month(input_per_M: float, output_per_M: float, calls: int) -> float:
    """Calcula costo mensual de un modelo dado un volumen de calls."""
    total_in = calls * TOKENS_PER_CALL_INPUT / 1_000_000
    total_out = calls * TOKENS_PER_CALL_OUTPUT / 1_000_000
    return total_in * input_per_M + total_out * output_per_M


def find_breakeven(sub_price: float, model_input: float, model_output: float) -> int:
    """Calls/mes en que la suscripción supera al pay-per-use."""
    cost_per_call = (TOKENS_PER_CALL_INPUT * model_input + TOKENS_PER_CALL_OUTPUT * model_output) / 1_000_000
    if cost_per_call <= 0:
        return -1  # gratis, nunca conviene
    return int(sub_price / cost_per_call)


def print_pay_per_use_matrix(markdown: bool = False):
    """Tabla: costo mensual de cada modelo por perfil de uso."""
    if markdown:
        print("## Costo mensual pay-per-use por perfil")
        print()
        print("Asumiendo " + f"{TOKENS_PER_CALL_INPUT}+{TOKENS_PER_CALL_OUTPUT} tokens por call (input+output).")
        print()
        header = "| Modelo |" + "".join(f" {p['name']} |" for p in PROFILES)
        print(header)
        print("|---|" + "".join("---:|" for _ in PROFILES))
        for key, name, ci, co, notes in MODELS:
            row = f"| **{name}** |"
            for p in PROFILES:
                cost = cost_per_month(ci, co, p["calls_per_month"])
                row += f" ${cost:,.2f} |"
            print(row)
        print()
        print("> Tokens/call asumidos: " + f"{TOKENS_PER_CALL_INPUT} input + {TOKENS_PER_CALL_OUTPUT} output. ")
        print("> Para thinking models multiplica × ~4 el costo (reasoning interno facturado).")
    else:
        print(f"\n=== Costo mensual pay-per-use ({TOKENS_PER_CALL_INPUT}+{TOKENS_PER_CALL_OUTPUT} tok/call) ===")
        print(f"{'Modelo':<55}", *(f"{p['name'][:17]:>17}" for p in PROFILES))
        for key, name, ci, co, notes in MODELS:
            costs = [cost_per_month(ci, co, p["calls_per_month"]) for p in PROFILES]
            print(f"{name[:55]:<55}", *(f"${c:>15,.2f}" for c in costs))


def print_breakeven_table(markdown: bool = False):
    """Para cada suscripción, calcula el break-even en calls/mes vs pay-per-use."""
    if markdown:
        print("## Break-even: cuándo conviene una suscripción vs pay-per-use")
        print()
        print("Calls/mes en que la suscripción cuesta lo mismo que pagar API. Por encima de ese número, **la suscripción es más barata**.")
        print()
        print("| Suscripción ($/mes) | Modelo equivalente | Break-even (calls/mes) | Perfil |")
        print("|---|---|---:|---|")
        for price, sub_name, _gives_api, model_key, sub_notes in SUBSCRIPTIONS:
            model = next((m for m in MODELS if m[0] == model_key), None)
            if not model:
                continue
            _key, mname, ci, co, _ = model
            be = find_breakeven(price, ci, co)
            # Map break-even to nearest profile
            if be < 0:
                profile_match = "(modelo gratis)"
            elif be < 100:
                profile_match = "**Inmediato (cualquiera)**"
            elif be < 500:
                profile_match = "Light → Casual"
            elif be < 2_000:
                profile_match = "Casual → Active"
            elif be < 10_000:
                profile_match = "Active → Heavy"
            elif be < 30_000:
                profile_match = "Heavy → Power"
            else:
                profile_match = "Power+ (no conviene)"
            print(f"| ${price} {sub_name} ({sub_notes}) | {mname} | {be:,} | {profile_match} |")
    else:
        print("\n=== Break-even por suscripción ===")
        for price, sub_name, _gives_api, model_key, sub_notes in SUBSCRIPTIONS:
            model = next((m for m in MODELS if m[0] == model_key), None)
            if not model:
                continue
            _key, mname, ci, co, _ = model
            be = find_breakeven(price, ci, co)
            print(f"  ${price:>3}/mes {sub_name:<35} vs {mname[:30]:<30} → {be:>7,} calls/mes")


def print_recommendations(markdown: bool = False):
    """Recomendación final por perfil."""
    if markdown:
        print("## Recomendación por perfil")
        print()
        print("| Perfil | Calls/mes | Mejor opción | Por qué |")
        print("|---|---:|---|---|")
        recs = [
            ("Light (test/dev)",      100,    "**Pay-per-use OpenRouter** + DeepSeek V3.2 (~$0.10/mes) o NIM gratis",
             "Suscripción es overkill — pagás $20+ para usar $0.50"),
            ("Casual (agente ocasional)", 500,  "**Ollama Cloud Pro $20** o pay-per-use",
             "Si querés calidad alta: $20 fijo. Si suficiente con DeepSeek/Devstral: pay-per-use ~$0.50"),
            ("Active (agente diario)", 2_000,  "**MiniMax Agent Pro $19** o **Google AI Pro $19.99**",
             "Suscripción cubre M2.7 (SOTA agentes) o Gemini Pro. Pay-per-use con Devstral también funciona ($1.95)"),
            ("Heavy (N8N 24/7)",      10_000, "**MiniMax Coding Max $50** o **Qwen Coding Pro $50**",
             "Pay-per-use con GPT-4.1 = $86, Claude Sonnet = $234. Suscripción gana fácil"),
            ("Power (multi-agente prod)", 30_000, "**ChatGPT Pro $200** + **MiniMax Coding Ultra $150** combinado, o **Ollama Cloud Max $100**",
             "Stack mixto: GPT-5.5 para razonamiento, MiniMax para volumen, Ollama para fallback open"),
        ]
        for profile, calls, rec, why in recs:
            print(f"| **{profile}** | {calls:,} | {rec} | {why} |")
        print()
        print("> Hallazgo cualitativo: **Ningún plan oficial de Anthropic/OpenAI da acceso API**. ChatGPT Plus / Claude Pro son **chat web only**. Para agentes (OpenClaw, N8N, Hermes) hay que pagar API directa o usar suscripciones que sí incluyen API: MiniMax, Google AI, Ollama Cloud, Qwen, Grok.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--markdown", action="store_true")
    args = ap.parse_args()

    if args.markdown:
        print("# Análisis de Suscripciones — Break-Even por Perfil")
        print()
        print("> Auto-generado por `benchmarks/calculate_breakeven.py`. Re-correr cada vez que cambien precios o se agreguen suscripciones.")
        print()
    print_pay_per_use_matrix(args.markdown)
    print_breakeven_table(args.markdown)
    print_recommendations(args.markdown)


if __name__ == "__main__":
    main()
