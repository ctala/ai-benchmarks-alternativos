# Gemini 3.1 Pro — code_generation/n8n_workflow_json

- model_id: `google/gemini-3.1-pro-preview`
- success: True  | final: 5.43 | quality: 4.65
- latency_total: 19.048s | tokens_per_second: 107.3
- input_tokens: 116 | output_tokens: 2044
- judge_score: 2.0 | justificación: 

## Respuesta completa


    }
    ```

6.  **Refining and Formatting:**
    *   Ensure all JSON quotes are properly escaped.
    *   Make sure n8n expressions `{{ }}` are correct. In n8n, `$json.body.email` works for the Webhook node, but after the OpenAI node, `$json` refers to OpenAI's output.