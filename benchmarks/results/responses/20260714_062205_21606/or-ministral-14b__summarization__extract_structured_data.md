# Ministral 14B — summarization/extract_structured_data

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 7.31 | quality: 6.8
- latency_total: 4.127s | tokens_per_second: 103.5
- input_tokens: 282 | output_tokens: 427
- judge_score: 3.0 | justificación: 

## Respuesta completa

```json
[
    {
        "name": "Maria Garcia",
        "age": 28,
        "current_role": "ingeniera de software",
        "years_experience": 5,
        "current_company": "Google",
        "skills": [
            "Python",
            "Go",
            "Kubernetes"
        ],
        "salary_expectation": "$95K",
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
        "skills": [
            "Java",
            "microservicios",
            "AWS"
        ],
        "salary_expectation": "$120K",
        "availability": "1 mes de aviso",
        "email": "jrodriguez@mail.com",
        "certifications": [
            "AWS Solutions Architect"
        ]
    },
    {
        "name": "Sofia Chen",
        "age": 31,
        "current_role": "fullstack",
        "years_experience": 7,
        "current_company": "Freelancer",
        "skills": [
            "React",
            "Node.js",
            "PostgreSQL",
            "Docker"
        ],
        "salary_expectation": "$85K-$100K",
        "availability": "inmediatamente",
        "email": "sofia.chen@dev.io",
        "certifications": [],
        "portfolio": "sofiadev.com"
    }
]
```

**Nota:** Se añadió el campo `portfolio` en el perfil de Sofia Chen ya que era información relevante que no estaba incluida en los campos solicitados inicialmente. Si prefieres mantener el JSON estrictamente con los campos pedidos, se puede omitir.