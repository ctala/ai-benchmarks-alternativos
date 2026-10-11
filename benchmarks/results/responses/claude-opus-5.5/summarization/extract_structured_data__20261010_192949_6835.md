# Claude Opus 5.5 — summarization/extract_structured_data

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 7.15 | quality: 8.2
- latency_total: 10.041s | tokens_per_second: 107.3
- input_tokens: 449 | output_tokens: 1077
- judge_score: 4.0 | justificación: 

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
    "current_role": "Ingeniera de software",
    "years_experience": 5,
    "current_company": "Google",
    "skills": ["Python", "Go", "Kubernetes"],
    "salary_expectation": {
      "min": 95000,
      "max": 95000,
      "currency": "USD"
    },
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
    "salary_expectation": {
      "min": 120000,
      "max": 120000,
      "currency": "USD"
    },
    "availability": "1 mes (periodo de aviso)",
    "email": "jrodriguez@mail.com",
    "certifications": ["AWS Solutions Architect"]
  },
  {
    "name": "Sofia Chen",
    "age": 31,
    "current_role": "Fullstack Developer",
    "years_experience": 7,
    "current_company": "Freelance",
    "skills": ["React", "Node.js", "PostgreSQL", "Docker"],
    "salary_expectation": {
      "min": 85000,
      "max": 100000,
      "currency": "USD"
    },
    "availability": "Inmediata",
    "email": "sofia.chen@dev.io",
    "certifications": []
  }
]
```

**Decisiones tomadas:**

- **`salary_expectation`**: Usé un objeto con `min`, `max` y `currency` porque Sofia dio un rango. Así los tres candidatos tienen el mismo formato y se pueden comparar o filtrar. Asumí USD por el símbolo `$`.
- **`current_company` de Sofia**: Puse `"Freelance"` porque trabaja por cuenta propia desde hace 3 años. Si prefieres, se puede usar `null`.
- **Datos fuera del esquema**:
  - El portfolio de Sofia (`sofiadev.com`) no tiene campo asignado. Puedo añadir un campo `portfolio` si lo necesitas.
  - El año de ingreso de Maria a Google (2023) tampoco tiene campo. Se podría añadir algo como `current_company_since`.