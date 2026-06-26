# DiffusionGemma 26B-A4B (DGX Spark Q8_0) — summarization/extract_structured_data

- model_id: `hf.co/unsloth/diffusiongemma-26B-A4B-it-GGUF:Q8_0`
- success: True  | final: 6.86 | quality: 6.88
- latency_total: 19.824s | tokens_per_second: 64.6
- input_tokens: 0 | output_tokens: 1280
- judge_score: 3.2 | justificación: 

## Respuesta completa

thought

*   Input: Three candidate profiles in text format.
*   Output: A JSON array.
*   Required JSON fields: `name`, `age`, `current_role`, `years_experience`, `current_company`, `skills[]`, `salary_expectation`, `availability`, `email`, `certifications[]`.

    *   *Candidate 1:*
        *   Name: Maria Garcia
        *   Age: 28
        *   Role: ingeniera de software
        *   Experience: 5
        *   Company: Google (since 2023)
        *   Skills: Python, Go, Kubernetes
        *   Salary: $95K
        *   Availability: 2 semanas
        *   Email: maria.g@email.com
        *   Certifications: [None mentioned]

    *   *Candidate 2:*
        *   Name: Juan Rodriguez
        *   Age: 35
        *   Role: senior backend developer
        *   Experience: 10
        *   Company: Mercado Libre
        *   Skills: Java, microservicios, AWS
        *   Salary: $120K
        *   Availability: 1 mes
        *   Email: jrodriguez@mail.com
        *   Certifications: [AWS Solutions Architect]

    *   *Candidate 3:*
        *   Name: Sofia Chen
        *   Age: 31
        *   Role: fullstack
        *   Experience: 7
        *   Company: Freelancer
        *   Skills: React, Node.js, PostgreSQL, Docker
        *   Salary: $85K-$100K
        *   Availability: inmediatamente
        *   Email: sofia.chen@dev.io
        *   Certifications: [None mentioned]

    ```json
    [
      {
        "name": "Maria Garcia",
        "age": 28,
        "current_role": "ingeniera de software",
        "years_experience": 5,
        "current_company": "Google",
        "skills": ["Python", "Go", "Kubernetes"],
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
        "skills": ["Java", "microservicios", "AWS"],
        "salary_expectation": "$120K",
        "availability": "1 mes",
        "email": "jrodriguez@mail.com",
        "certifications": ["AWS Solutions Architect"]
      },
      {
        "name": "Sofia Chen",
        "age": 31,
        "current_role": "fullstack",
        "years_experience": 7,
        "current_company": "Freelancer",
        "skills": ["React", "Node.js", "PostgreSQL", "Docker"],
        "salary_expectation": "$85K-$100K",
        "availability": "inmediatamente",
        "email": "sofia.chen@dev.io",
        "certifications": []
      }
    ]
    ```

    *   Check fields? Yes.
    *   Check JSON format? Yes.
    *   Check data accuracy? Yes.```json
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
    "availability": "1 mes",
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
    "certifications": []
  }
]
```