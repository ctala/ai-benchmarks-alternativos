# Llama 4 Scout 17B — summarization/extract_structured_data

- model_id: `meta-llama/llama-4-scout`
- success: True  | final: 8.3 | quality: 8.0
- latency_total: 1.544s | tokens_per_second: 286.2
- input_tokens: 260 | output_tokens: 442
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con buena claridad y utilidad práctica, aunque la profundidad es solo aceptable ya que no ofrece insights adicionales más allá de la información proporcionada.

## Respuesta completa

Aquí te dejo la información de los 3 perfiles de candidatos en formato JSON:

```json
[
  {
    "name": "Maria Garcia",
    "age": 28,
    "current_role": "ingeniera de software",
    "years_experience": 5,
    "current_company": "Google",
    "skills": ["Python", "Go", "Kubernetes"],
    "salary_expectation": 95000,
    "availability": "2 semanas",
    "email": "maria.g@email.com",
    "certifications": []
  },
  {
    "name": "Juan Rodriguez",
    "age": 35,
    "current_role": "senior backend developer",
    "years_experience": 10,
    "current_company": "Mercado Libre",
    "skills": ["Java", "microservicios", "AWS"],
    "salary_expectation": 120000,
    "availability": "1 mes",
    "email": "jrodriguez@mail.com",
    "certifications": ["AWS Solutions Architect"]
  },
  {
    "name": "Sofia Chen",
    "age": 31,
    "current_role": "fullstack",
    "years_experience": 7,
    "current_company": null,
    "skills": ["React", "Node.js", "PostgreSQL", "Docker"],
    "salary_expectation": {
      "min": 85000,
      "max": 100000
    },
    "availability": "inmediatamente",
    "email": "sofia.chen@dev.io",
    "certifications": []
  }
]
```

Noté que el salario esperado de Sofia Chen es un rango, así que lo representé como un objeto con `min` y `max`. Si prefieres que sea un solo valor o se maneje de otra manera, házmelo saber.

También noté que Sofia Chen es freelancer y no tiene una empresa actual, así que puse `null` en el campo `current_company`. Si prefieres que se omita este campo o se maneje de otra manera, házmelo saber.