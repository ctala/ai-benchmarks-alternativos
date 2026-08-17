# Llama 4 Scout 17B (Groq preview) — summarization/extract_structured_data

- model_id: `meta-llama/llama-4-scout-17b-16e-instruct`
- success: True  | final: 7.55 | quality: 7.44
- latency_total: 1.496s | tokens_per_second: 306.1
- input_tokens: 260 | output_tokens: 458
- judge_score: 3.6 | justificación: 

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

Noté que el rango salarial de Sofia Chen no es un valor único, así que lo representé como un objeto con `min` y `max`. Si prefieres representar el rango de otra manera, házmelo saber.

También noté que Sofia Chen es freelancer y no tiene una empresa actual, así que puse `null` en el campo `current_company`. Si prefieres poner algo diferente, házmelo saber.

Finalmente, verifiqué que los campos solicitados están todos presentes en cada candidato. ¡Si necesitas algo más, no dudes en preguntar!