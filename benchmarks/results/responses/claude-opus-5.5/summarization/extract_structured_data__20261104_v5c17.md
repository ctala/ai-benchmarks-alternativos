# Claude Opus 5.5 — summarization/extract_structured_data

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 6.14 | quality: 6.8
- latency_total: 11.695s | tokens_per_second: 106.7
- input_tokens: 449 | output_tokens: 1248
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante, pero incluye información no solicitada y omite detalles importantes, como la antigüedad de Maria en Google.

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

**Notas sobre la extracción:**

- **salary_expectation**: lo estructuré como objeto `{min, max, currency}` para manejar de forma uniforme tanto montos fijos como el rango de Sofia. Asumí **USD** por el símbolo `$`, aunque no se especifica. Si prefieres un valor simple (por ejemplo, `"$95K"`), lo ajusto.
- **Información fuera del esquema**: el portfolio de Sofia (`sofiadev.com`) y su antigüedad como freelancer (3 años) no tienen campo asignado, así que no aparecen en el JSON. También se omitió que Maria trabaja en Google desde 2023. Puedo añadir campos como `portfolio` o `current_company_since` si te sirven.
- **Juan**: el certificado "AWS Solutions Architect" no indica el nivel (Associate o Professional).