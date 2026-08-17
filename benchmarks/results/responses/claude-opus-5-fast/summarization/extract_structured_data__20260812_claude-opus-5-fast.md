# Claude Opus 5 Fast — summarization/extract_structured_data

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 7.01 | quality: 8.2
- latency_total: 6.577s | tokens_per_second: 201.8
- input_tokens: 447 | output_tokens: 1327
- judge_score: 4.0 | justificación: La respuesta es precisa y clara, con una estructura bien organizada, pero incluye información no solicitada y omite algunos detalles relevantes como el año de ingreso de Maria.

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
    "current_company": "Freelance (últimos 3 años)",
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

- **Salario:** lo estructuré como objeto `min`/`max`/`currency` porque Sofía dio un rango y los otros dos un valor fijo. Si prefieres un string plano (`"$95K"`) o un solo número, lo ajusto.
- **Dato no mapeado:** Sofía incluye un portfolio (`sofiadev.com`) que no tiene campo en el esquema. Si quieres conservarlo, sugiero añadir un campo opcional `portfolio` (null para los otros dos).
- **Inferencias hechas:** el rol de Sofía aparece solo como "fullstack", lo normalicé a "Fullstack Developer"; su empresa actual se registró como "Freelance" al no haber empleador.
- **Año de ingreso:** el dato de María ("en Google desde 2023") se perdió al no existir campo para ello; se podría añadir `current_company_start_year`.