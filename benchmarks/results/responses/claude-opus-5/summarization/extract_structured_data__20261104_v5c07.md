# Claude Opus 5 — summarization/extract_structured_data

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 5.98 | quality: 6.8
- latency_total: 12.58s | tokens_per_second: 83.0
- input_tokens: 447 | output_tokens: 1044
- judge_score: 3.0 | justificación: La respuesta es correcta y clara, pero incluye información no solicitada y omite algunos detalles relevantes, como la antigüedad en el puesto actual de Maria y el tipo de empleo de Sofia.

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
    "current_role": "Ingeniera de Software",
    "years_experience": 5,
    "current_company": "Google",
    "skills": ["Python", "Go", "Kubernetes"],
    "salary_expectation": {
      "min": 95000,
      "max": 95000,
      "currency": "USD",
      "raw": "$95K"
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
      "currency": "USD",
      "raw": "$120K"
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
      "currency": "USD",
      "raw": "$85K-$100K"
    },
    "availability": "Inmediata",
    "email": "sofia.chen@dev.io",
    "certifications": []
  }
]
```

**Notas sobre la extracción:**

- **Salarios**: los convertí a objeto con `min`/`max` porque el Candidato 3 tiene un rango. Si tu esquema requiere un string simple, usa el campo `raw`.
- **Datos no capturados por el esquema**:
  - Maria: trabaja en Google **desde 2023** (antigüedad en el puesto actual).
  - Sofia: **portfolio** `sofiadev.com` y el detalle de que es freelancer **los últimos 3 años** (los 4 anteriores fueron en otro contexto no especificado).
  - Si te sirven, puedo agregar campos como `portfolio_url`, `current_role_since` o `employment_type`.
- **Inferencias que hice** (no estaban literales):
  - `current_company: "Freelance"` para Sofia — no es una empresa, pero es el dato más cercano.
  - Nivel de seniority: solo Juan dice explícitamente "senior". Maria y Sofia no lo declaran, así que no lo inventé.
  - Moneda: asumí USD por la notación `$...K`, pero no está confirmado (Mercado Libre sugiere LATAM, podría ser otra).

¿Quieres que lo deje como un array plano con salarios en string, o que agregue los campos extra?