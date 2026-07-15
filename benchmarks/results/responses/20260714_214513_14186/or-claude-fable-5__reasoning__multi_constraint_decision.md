# Claude Fable 5 — reasoning/multi_constraint_decision

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 7.97 | quality: 10.0
- latency_total: 30.173s | tokens_per_second: 67.9
- input_tokens: 280 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una comparación detallada de opciones de stack tecnológico con pros y contras específicos, costos y consideraciones de implementación.

## Respuesta completa

# Stack Tecnológico para MVP de Marketplace Freelance

## Análisis previo de restricciones

Antes de comparar, lo crítico de tu caso:

- **1 solo dev + 6 semanas** = minimizar código custom, maximizar servicios gestionados
- **Chat en tiempo real + pagos** = las dos features que más tiempo consumen si las construyes desde cero
- **Escala baja** (5K usuarios/6 meses) = NO necesitas microservicios, Kubernetes, ni nada "escalable". Un monolito aguanta esto sin despeinarse
- **Marketplace con pagos** = necesitas *split payments* (cobrar al cliente, pagar al freelancer, quedarte comisión). Esto descarta soluciones de pago simples

---

## Opción 1: Next.js + Supabase + Stripe Connect

**Stack:** Next.js (fullstack) · Supabase (Postgres, Auth, Realtime, Storage) · Stripe Connect · Vercel · Tailwind + shadcn/ui

### Pros
- **Supabase resuelve 3 requisitos de golpe**: auth (email, OAuth, magic links), chat en tiempo real (Realtime channels sobre Postgres), y base de datos con Row Level Security
- **Búsqueda incluida**: Postgres full-text search es suficiente para 5K usuarios. Cero infra adicional
- Next.js unifica frontend + API routes = un solo deploy, un solo repo
- **Stripe Connect** está diseñado exactamente para marketplaces (split payments, onboarding de freelancers, KYC delegado a Stripe)
- Admin panel: puedes usar el dashboard de Supabase para lo básico + Retool free tier o unas páginas protegidas en Next.js
- Deploy en Vercel = cero DevOps
- El dev ya sabe React → curva de aprendizaje mínima

### Contras
- Vendor lock-in moderado con Supabase (mitigado: es Postgres estándar, puedes migrar)
- Realtime de Supabase tiene peculiaridades; para chat muy complejo (typing indicators, presence avanzada) requiere trabajo extra
- No usa Python (si el dev prefiere backend Python, esto es todo TypeScript)

### Costo mensual estimado
| Servicio | Costo |
|---|---|
| Supabase Pro | $25 |
| Vercel Pro | $20 |
| Stripe | $0 fijo (2.9% + $0.30 por transacción + fees de Connect) |
| Dominio + email (Resend) | ~$5 |
| **Total** | **~$50/mes** |

---

## Opción 2: Next.js (frontend) + Django + PostgreSQL

**Stack:** Next.js · Django + DRF · PostgreSQL · Django Channels (WebSockets) · Redis · Stripe Connect · Railway/Render

### Pros
- **Django Admin es imbatible**: el admin panel te sale *gratis* y es potente. Para un marketplace con moderación de listings, disputas, etc., esto es oro
- El dev sabe Python → productivo desde día 1 en backend
- Django tiene baterías incluidas: auth, ORM, migraciones, permisos
- Postgres full-text search vía `SearchVector` de Django
- Sin vendor lock-in significativo

### Contras
- **Chat en tiempo real es el punto débil**: Django Channels funciona pero configurarlo bien (Redis como channel layer, ASGI, reconexión, historial) consume fácilmente 1 semana de las 6
- Dos codebases (Next.js + Django) = dos deploys, CORS, duplicación de tipos/validaciones
- Más DevOps: gestionar Redis, workers, WebSockets en Railway/Render
- Auth entre Next.js y Django requiere plomería (JWT, refresh tokens)

### Costo mensual estimado
| Servicio | Costo |
|---|---|
| Railway/Render (web + worker + Postgres + Redis) | $30–50 |
| Vercel (frontend) | $0–20 |
| Stripe | variable |
| Dominio + email | ~$5 |
| **Total** | **~$55–75/mes** |

---

## Opción 3: T3 Stack + servicios especializados

**Stack:** Next.js + tRPC + Prisma · Clerk (auth) · Pusher/Ably (chat) · Algolia (búsqueda) · PlanetScale/Neon (DB) · Stripe Connect

### Pros
- Cada servicio es best-in-class: Clerk tiene la mejor UX de auth, Algolia la mejor búsqueda, Pusher chat confiable
- tRPC da type-safety end-to-end = menos bugs para 1 solo dev
- Muy poco código de infraestructura

### Contras
- **Muerte por mil suscripciones**: 5 servicios distintos = 5 dashboards, 5 puntos de falla, 5 facturas que escalan de forma impredecible
- Clerk se pone caro rápido ($0.02/MAU después de 10K, pero los add-ons suman)
- Algolia es overkill absoluto para 5K usuarios; Postgres FTS hace el trabajo
- Integrar todo consume tiempo que no tienes
- Costos crecen no-linealmente con usuarios

### Costo mensual estimado
| Servicio | Costo |
|---|---|
| Clerk | $0–25 |
| Pusher/Ably | $0–29 |
| Algolia | $0–50 |
| Neon/PlanetScale | $0–29 |
| Vercel | $20 |
| **Total** | **~$50–150/mes** (y creciendo) |

---

## 🏆 Recomendación: Opción 1 (Next.js + Supabase + Stripe Connect)

### Justificación

1. **Timeline**: es la única opción donde realistamente cierras el M