# MiMo-V2.5 Pro — reasoning/multi_constraint_decision

- model_id: `xiaomi/mimo-v2.5-pro`
- success: True  | final: 6.81 | quality: 8.03
- latency_total: 35.305s | tokens_per_second: 58.0
- input_tokens: 433 | output_tokens: 2048
- judge_score: 4.4 | justificación: 

## Respuesta completa

# Stack Tecnológico para MVP de Marketplace Freelance

---

## Contexto y Análisis de Restricciones

Antes de comparar, vale la pena destacar qué hace **especial** tu caso:

| Factor | Implicación |
|---|---|
| 1 dev, 6 semanas | Cada hora cuenta. El "time-to-feature" es la métrica #1 |
| Sabe Python + React | Descarta stacks que requieran aprender Go/TypeScript desde cero |
| $5,000 de presupuesto | Con $1,500-2,000 de infra para 6 meses, sobra para dominio, herramientas y colchón |
| 500 → 5,000 usuarios | No necesitas escalar masivamente, pero sí estabilidad |
| Mantenimiento por 1 persona | Menos moving parts = mejor. Evita microservicios |

---

## Las 3 Opciones

---

### Opción A: Django + React + PostgreSQL + Redis + Channels

```
Frontend:  React (Vite) + TailwindCSS
Backend:   Django 5 + Django REST Framework + Django Channels
DB:        PostgreSQL 16
Cache:     Redis (caching + pub/sub para chat)
Real-time: Django Channels (WebSockets)
Auth:      django-allauth (email + Google + GitHub)
Pagos:     Stripe (stripe-python)
Search:    django.contrib.postgres (full-text search nativo)
Admin:     Django Admin (incluido, cero código extra)
Deploy:    Railway.app o VPS Hetzner
```

**Costos mensuales estimados:**

| Concepto | Costo/mes |
