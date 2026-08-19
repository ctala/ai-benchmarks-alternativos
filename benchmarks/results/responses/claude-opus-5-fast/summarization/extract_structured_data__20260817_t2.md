# Claude Opus 5 Fast — summarization/extract_structured_data

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 6.05 | quality: 6.8
- latency_total: 5.405s | tokens_per_second: 223.7
- input_tokens: 447 | output_tokens: 1209
- judge_score: 3.0 | justificación: La respuesta es precisa para los dos primeros candidatos, pero incluye información no solicitada para el tercero, afectando la relevancia; la profundidad es limitada ya que no se exploran más detalles o insights.

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
    "availability": {
      "type": "notice_period",
      "days": 14,
      "raw": "2 semanas"
    },
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
    "availability": {
      "type": "notice_period",
      "days": 30,
      "raw": "1 mes de aviso"
    },
    "email": "jrodriguez@mail.com",
    "certifications": ["AWS Solutions Architect"]
  },
  {
    "name": "Sofia Chen",
    "age": 31,
    "current_role": "Fullstack Developer",
    "years_experience": 7,
    "current_company": "Freelancer (independiente)",
    "skills": ["React", "Node.js", "PostgreSQL", "Docker"],
    "salary_expectation": {
      "min": 85000,
      "max": 100000,
      "currency": "USD",
      "raw": "$85K-$100K"
    },
    "availability": {
      "type": "immediate",
      "days": 0,
      "raw": "Disponible inmediatamente"
    },
    "email": "sofia.chen@dev.io",
    "certifications": [],
    "portfolio": "sofiadev.com"
  }
]
```

**Notas sobre la extracción:**

- **Moneda:** se asumió USD, ya que los perfiles solo indican `$`. Verificar si aplica otra moneda.
- **Salarios:** normalizados a números enteros con `min`/`max` para poder filtrar/ordenar; se conservó el texto original en `raw`.
- **Disponibilidad:** convertida a días para permitir comparación; también se conservó el texto original.
- **Sofia Chen:** "Freelancer los últimos 3 años" no es una empresa; se registró como trabajo independiente. Se añadió el campo extra `portfolio` que no estaba en el esquema pedido (se puede eliminar si el formato debe ser estricto).
- **Certificaciones:** solo Juan declara una; los demás quedaron con array vacío (ausencia de dato, no necesariamente ausencia de certificaciones).