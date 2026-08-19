# Qwen 3.8 Max — summarization/extract_structured_data

- model_id: `qwen/qwen3.8-max`
- success: True  | final: 7.15 | quality: 8.0
- latency_total: 13.741s | tokens_per_second: 55.7
- input_tokens: 313 | output_tokens: 765
- judge_score: 4.0 | justificación: La respuesta es precisa en la mayoría de los campos, con una ligera inexactitud en la disponibilidad de Juan Rodriguez. Es altamente relevante ya que extrae y presenta toda la información solicitada. La profundidad es aceptable, ya que se limita a la información proporcionada sin añadir insights adicionales. La claridad es excelente, con una estructura bien organizada y fácil de entender. La utilidad práctica es alta, ya que un emprendedor podría usar directamente esta información para tomar decisiones de contratación.

## Entrada exacta (lo que recibió el modelo)

**user:**

Extrae la informacion de estos 3 perfiles de candidatos y devuelvelos como JSON:

Candidato 1: Maria Garcia, 28 anos, ingeniera de software con 5 anos de experiencia. Trabaja en Google desde 2023. Maneja Python, Go, Kubernetes. Pide $95K. Disponible en 2 semanas. Email: maria.g@email.com

Candidato 2: Juan Rodriguez, 35 anos, senior backend developer. 10 anos de experiencia, actualmente en Mercado Libre. Especialista en Java, microservicios, AWS. Salario esperado $120K. Necesita dar 1 mes de aviso. Contacto: jrodriguez@mail.com. Tiene certificacion AWS Solutions Architect.

Candidato 3: Sofia Chen, 31 anos, fullstack. 7 anos experiencia. Freelancer los ultimos 3 anos. React, Node.js, PostgreSQL, Docker. Pide entre $85K-$100K. Disponible inmediatamente. sofia.chen@dev.io. Portfolio: sofiadev.com

Formato JSON con campos: name, age, current_role, years_experience, current_company, skills[], salary_expectation, availability, email, certifications[]


## Respuesta completa

[
  {
    "name": "Maria Garcia",
    "age": 28,
    "current_role": "Ingeniera de software",
    "years_experience": 5,
    "current_company": "Google",
    "skills": [
      "Python",
      "Go",
      "Kubernetes"
    ],
    "salary_expectation": "$95K",
    "availability": "Disponible en 2 semanas",
    "email": "maria.g@email.com",
    "certifications": []
  },
  {
    "name": "Juan Rodriguez",
    "age": 35,
    "current_role": "Senior backend developer",
    "years_experience": 10,
    "current_company": "Mercado Libre",
    "skills": [
      "Java",
      "Microservicios",
      "AWS"
    ],
    "salary_expectation": "$120K",
    "availability": "Necesita dar 1 mes de aviso",
    "email": "jrodriguez@mail.com",
    "certifications": [
      "AWS Solutions Architect"
    ]
  },
  {
    "name": "Sofia Chen",
    "age": 31,
    "current_role": "Fullstack",
    "years_experience": 7,
    "current_company": "Freelance",
    "skills": [
      "React",
      "Node.js",
      "PostgreSQL",
      "Docker"
    ],
    "salary_expectation": "$85K-$100K",
    "availability": "Disponible inmediatamente",
    "email": "sofia.chen@dev.io",
    "certifications": []
  }
]