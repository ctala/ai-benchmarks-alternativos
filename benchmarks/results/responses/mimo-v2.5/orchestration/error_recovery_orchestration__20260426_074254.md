# MiMo-V2.5 (omnimodal) — orchestration/error_recovery_orchestration

- model_id: `xiaomi/mimo-v2.5`
- success: True  | final: 5.35 | quality: 2.84
- latency_total: 5.007s | tokens_per_second: 57.3
- input_tokens: 1418 | output_tokens: 287
- judge_score: 2.0 | justificación: 

## Respuesta completa

[tool_call] run_script({"language": "bash", "code": "find / -name \"*sales*\" -o -name \"*ventas*\" 2>/dev/null | head -20"})