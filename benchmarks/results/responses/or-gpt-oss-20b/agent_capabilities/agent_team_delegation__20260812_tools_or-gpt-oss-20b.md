# GPT-OSS 20B — agent_capabilities/agent_team_delegation

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 7.37 | quality: 7.1
- latency_total: 3.011s | tokens_per_second: 79.4
- input_tokens: 694 | output_tokens: 239
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, proporcionando una estructura útil para la delegación de tareas, aunque carece de algunos insights más profundos.

## Respuesta completa

We need to coordinate tasks. We have 5 sub-agents. Need to produce plan explanation, then delegate tasks appropriately. Steps: research competitor analysis => researcher. Then writer copy after research data. Then coder produce HTML/CSS. Designer create images. Reviewer final check. Priorities: research high priority, writer medium, coder high (depends on copy). Designer medium. Reviewer high (critical). We need to explain plan. Then delegate tasks. Use functions. We'll call delegate_to_agent for each. Use priority tags. Provide context. Let's produce plan.