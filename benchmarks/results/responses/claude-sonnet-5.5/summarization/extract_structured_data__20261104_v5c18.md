# Claude Sonnet 5.5 — summarization/extract_structured_data

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 7.19 | quality: 8.0
- latency_total: 8.798s | tokens_per_second: 146.2
- input_tokens: 449 | output_tokens: 1286
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con buena claridad y utilidad práctica, aunque la profundidad es solo aceptable ya que no ofrece insights adicionales más allá de la información proporcionada.

## Entrada exacta (lo que recibió el modelo)

**user:**

Extrae la informacion de estos 3 perfiles de candidatos y devuelvelos como JSON:

Candidato 1: Maria Garcia, 28 anos, ingeniera de software con 5 anos de experiencia. Trabaja en Google desde 2023. Maneja Python, Go, Kubernetes. Pide $95K. Disponible en 2 semanas. Email: maria.g@email.com

Candidato 2: Juan Rodriguez, 35 anos, senior backend developer. 10 anos de experiencia, actualmente en Mercado Libre. Especialista en Java, microservicios, AWS. Salario esperado $120K. Necesita dar 1 mes de aviso. Contacto: jrodriguez@mail.com. Tiene certificacion AWS Solutions Architect.

Candidato 3: Sofia Chen, 31 anos, fullstack. 7 anos experiencia. Freelancer los ultimos 3 anos. React, Node.js, PostgreSQL, Docker. Pide entre $85K-$100K. Disponible inmediatamente. sofia.chen@dev.io. Portfolio: sofiadev.com

Formato JSON con campos: name, age, current_role, years_experience, current_company, skills[], salary_expectation, availability, email, certifications[]


## Respuesta completa

```json
[
  {
    "name": "Maria Garcia",
    "age": 28,
    "current_role": "Software Engineer",
    "years_experience": 5,
    "current_company": "Google",
    "skills": ["Python", "Go", "Kubernetes"],
    "salary_expectation": { "min": 95000, "max": 95000, "currency": "USD" },
    "availability": "2 weeks",
    "email": "maria.g@email.com",
    "certifications": []
  },
  {
    "name": "Juan Rodriguez",
    "age": 35,
    "current_role": "Senior Backend Developer",
    "years_experience": 10,
    "current_company": "Mercado Libre",
    "skills": ["Java", "Microservices", "AWS"],
    "salary_expectation": { "min": 120000, "max": 120000, "currency": "USD" },
    "availability": "1 month notice",
    "email": "jrodriguez@mail.com",
    "certifications": ["AWS Solutions Architect"]
  },
  {
    "name": "Sofia Chen",
    "age": 31,
    "current_role": "Fullstack Developer (Freelancer)",
    "years_experience": 7,
    "current_company": null,
    "skills": ["React", "Node.js", "PostgreSQL", "Docker"],
    "salary_expectation": { "min": 85000, "max": 100000, "currency": "USD" },
    "availability": "Immediate",
    "email": "sofia.chen@dev.io",
    "certifications": []
  }
]
```

Notas:
- Asumí que `$` es USD, ya que los perfiles no especifican la moneda. Cuando se da un solo valor, `min` y `max` son iguales.
- Sofia es freelancer, por eso `current_company` es `null`. Su rol lo indica en `current_role`.
- Maria y Sofia no mencionan certificaciones, así que `certifications` queda vacío.
- El portfolio de Sofia (`sofiadev.com`) no está en el esquema que pediste, así que lo omití. Si quieres, puedo agregar un campo `portfolio`.