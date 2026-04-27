# MiMo V2.5-Pro (Xiaomi) — summarization/extract_structured_data

- model_id: `mimo-v2.5-pro`
- success: True  | final: 6.95 | quality: 6.72
- latency_total: 10.422s | tokens_per_second: 51.3
- input_tokens: 531 | output_tokens: 535
- judge_score: 2.8 | justificación: 

## Respuesta completa

```json
[
  {
    "name": "Maria Garcia",
    "age": 28,
    "current_role": "Ingeniera de Software",
    "years_experience": 5,
    "current_company": "Google",
    "skills": ["Python", "Go", "Kubernetes"],
    "salary_expectation": "$95,000",
    "availability": "2 semanas",
    "email": "maria.g@email.com",
    "certifications": []
  },
  {
    "name": "Juan Rodriguez",
    "age": 35,
    "current_role": "Senior Backend Developer",
    "years_experience": 10,
    "current_company": "Mercado Libre",
    "skills": ["Java", "Microservicios", "AWS"],
    "salary_expectation": "$120,000",
    "availability": "1 mes",
    "email": "jrodriguez@mail.com",
    "certifications": ["AWS Solutions Architect"]
  },
  {
    "name": "Sofia Chen",
    "age": 31,
    "current_role": "Fullstack Developer",
    "years_experience": 7,
    "current_company": "Freelancer",
    "skills": ["React", "Node.js", "PostgreSQL", "Docker"],
    "salary_expectation": "$85,000 - $100,000",
    "availability": "Inmediata",
    "email": "sofia.chen@dev.io",
    "certifications": [],
    "portfolio": "sofiadev.com"
  }
]
```

### Notas sobre la extracción:

| Campo | Observación |
|---|---|
| **salary_expectation** | Se mantuvo como string para preservar el formato original (incluyendo el rango de Sofia) |
| **current_company** | Sofia no tenía empresa asignada, se colocó "Freelancer" |
| **certifications** | Solo Juan mencionó certificación explícita |
| **portfolio** | Se agregó como campo extra para Sofia ya que lo mencionó en su perfil |

> Si necesitas que los salarios sean numéricos, que el portfolio se incluya en todos los registros (aunque sea `null`), o cualquier otro ajuste al esquema, dime y lo adapto. 🚀