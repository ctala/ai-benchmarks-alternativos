# GPT-OSS 20B — agent_capabilities/agent_team_delegation

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 7.66 | quality: 7.3
- latency_total: 2.246s | tokens_per_second: 130.9
- input_tokens: 695 | output_tokens: 294
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante, y ofrece una estructura clara y útil para la delegación de tareas, aunque podría profundizar más en detalles específicos de cada tarea.

## Respuesta completa

We need to coordinate tasks among sub-agents. Steps:

1. Research competitor analysis: researcher
2. Writer: copy
3. Coder: HTML/CSS
4. Designer: images
5. Reviewer: review

We must explain plan before delegating. Also set priorities: research first, then copy, then design, then code, then review. Or maybe design could happen earlier to inform copy. But likely copy first, design later. Actually copy needs research. Design could be done after copy. Code after design.

We should assign tasks with context. Let's explain.

We need to use function calls: delegate_to_agent. We'll call each with appropriate context. Provide priority: high for all but maybe low for design? Let's just set high. We'll need to chain tasks: research -> writer -> designer -> coder -> reviewer.

We can create a plan: 1. Research competitor. 2. Writer writes copy. 3. Designer creates images. 4. Coder builds page. 5. Reviewer checks. We'll assign tasks accordingly.

Let's proceed.