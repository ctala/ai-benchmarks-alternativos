# MiMo-V2-Pro — summarization/extract_structured_data

- model_id: `xiaomi/mimo-v2-pro`
- success: True  | final: 6.95 | quality: 7.56
- latency_total: 12.212s | tokens_per_second: 68.0
- input_tokens: 529 | output_tokens: 831
- judge_score: 3.4 | justificación: 

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
    "availability": "1 mes (periodo de aviso)",
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
    "certifications": []
  }
]
```

---

### Resumen rápido de los candidatos:

| Aspecto | Maria | Juan | Sofia |
|---|---|---|---|
| **Experiencia** | 5 años | 10 años | 7 años |
| **Enfoque** | Backend/DevOps | Backend/Cloud | Fullstack |
| **Salario** | $95K | $120K | $85K-$100K |
| **Disponibilidad** | 2 semanas | 1 mes | Inmediata |

> **Nota:** El perfil de Sofia menciona un portfolio (`sofiadev.com`) que no incluí en el JSON ya que no estaba en el esquema solicitado. Si quieres agregar un campo `portfolio` o `additional_info`, avísame y lo ajusto. 😊