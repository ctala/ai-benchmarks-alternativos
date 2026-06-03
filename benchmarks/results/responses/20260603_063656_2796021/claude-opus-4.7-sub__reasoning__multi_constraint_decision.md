# Claude Opus 4.7 (suscripción) — reasoning/multi_constraint_decision

- model_id: `claude-opus-4-7`
- success: True  | final: 7.04 | quality: 10.0
- latency_total: 89.978s | tokens_per_second: 62.3
- input_tokens: 6 | output_tokens: 5608
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un análisis detallado de múltiples opciones de stack tecnológico con pros y contras específicos, costos estimados y consideraciones operativas.

## Respuesta completa

# Stack para Marketplace de Freelance Nicho — Análisis

Antes de entrar a las opciones, dos observaciones que mueven la aguja:

1. **El "admin panel" es trabajo subestimado**. En un marketplace tenés que moderar perfiles, resolver disputas, refundear, banear, ver métricas. Construirlo a mano son 1-2 semanas de tus 6. **Si podés conseguirlo gratis, lo hacés.**
2. **"Stripe + marketplace" = Stripe Connect, no Stripe estándar**. Necesitás Express o Custom accounts para pagar a freelancers, manejar KYC y split de comisión. Sumá 3-5 días para integrarlo bien.

---

## Opción A — Django + React (Vite) + Postgres + Stripe Connect

**Stack**: Django 5 + DRF/Django Ninja · React (Vite) · Postgres (Neon o Railway) · Stripe Connect Express · Pusher Channels · Meilisearch Cloud · Render o Railway

### Pros
- **Django Admin gratis** — moderación, refunds, gestión de usuarios y disputas con cero código frontend. Solo personalización (~2-3 días vs 1-2 semanas custom).
- **Maximiza tu skill Python** — modelos, auth, permissions, signals, migraciones, todo nativo.
- **Auth + permissions sólido** (django-allauth + 2FA + social login) sin pagar SaaS.
- **Admin = ventaja operativa real** cuando estás solo: ver/editar cualquier cosa desde el navegador en producción.
- **Baja superficie de vendor lock-in** — todo es Postgres + Django, portable a cualquier VPS.

### Contras
- DRF tiene boilerplate; Django Ninja es más moderno pero menos batería incluida.
- Realtime requiere Channels + Redis (complejo) **o** un servicio externo (Pusher/Ably). Recomendado: externo para no operar Redis.
- SSR/SEO de la React app requiere setup adicional si te importa SEO (probablemente sí para descubrimiento de freelancers).

### Costo mensual estimado
| Item | Costo |
|---|---|
| Render Web Service (Django + Worker) | $14 |
| Postgres (Neon Pro o Render) | $19 |
| Frontend (Vercel Hobby o Render static) | $0 |
| Pusher Channels (Startup) | $49 |
| Meilisearch Cloud Build | $30 |
| Stripe Connect | 0.25% extra sobre 2.9%+30¢ (pass-through) |
| Sentry (Team) | $26 |
| Cloudflare R2 (uploads) | ~$5 |
| **Total** | **~$143/mes** |

**6 meses de infra: ~$860** de tu presupuesto de $5,000.

---

## Opción B — Next.js + Supabase + Stripe Connect

**Stack**: Next.js 15 (App Router) · Supabase (Postgres + Auth + Realtime + Storage) · Stripe Connect Express · Algolia o Postgres FTS · Vercel

### Pros
- **Velocidad inicial brutal** — auth, DB, realtime, storage en un solo dashboard. Realtime nativo sin Pusher.
- **Supabase Auth** maneja social login, magic link, MFA out-of-the-box.
- **Next.js** = SSR/SEO/RSC sin esfuerzo extra (importante para que Google indexe perfiles de freelancers).
- **Row Level Security** en Postgres te ahorra mucha lógica de permisos en el backend.

### Contras
- **No tenés admin panel** — Supabase Studio es para vos como dev, no para operar el marketplace. Tenés que construirlo (Refine/React-Admin acortan a ~1 semana, no gratis como Django).
- **No usás Python** — desperdicia tu skill más fuerte. Todo el backend termina en TypeScript / Edge Functions o RPC en Postgres.
- **Vendor lock-in moderado** — RLS, auth schemas y realtime channels son Supabase-flavored. Migrar es factible pero costoso.
- **Edge Functions tienen límites** que te van a pegar con webhooks largos de Stripe Connect o jobs de moderación.

### Costo mensual estimado
| Item | Costo |
|---|---|
| Vercel Pro | $20 |
| Supabase Pro | $25 |
| Algolia (Build) | $50 (gratis primeros ~10K records) |
| Stripe Connect | pass-through |
| Sentry | $26 |
| Resend (mails) | $20 |
| **Total** | **~$141/mes** |

**6 meses: ~$846**.

---

## Opción C — FastAPI + Next.js + Postgres + Clerk

**Stack**: FastAPI · Next.js · Postgres (Neon) · Clerk (auth) · Stripe Connect · Ably (realtime) · Meilisearch · Railway

### Pros
- **FastAPI es lo mejor de Python moderno** — async, typing, OpenAPI auto.
- **Clerk** = auth premium, UI components listos, organizations, MFA, sin construir nada.
- Separación clara backend/frontend, ambos en sus lenguajes idiomáticos.

### Contras
- **Demasiadas piezas para 1 persona en 6 semanas**: Clerk + FastAPI + Next + Ably + Meilisearch + Stripe Connect + Railway = 7 dashboards, 7 facturas, 7 modos de fallar.
- **No tenés admin panel** y FastAPI no te lo regala (a diferencia de Django).
- **Costo más alto** por la cantidad de SaaS.
- Más latencia entre servicios (cross-region calls).

### Costo mensual estimado
| Item | Costo |
|---|---|
| Vercel Pro | $20 |
| Railway (FastAPI) | $20 |
| Neon Postgres Pro | $19 |
| Clerk Pro | $25 |
| Ably (Standard) | $29 |
| Meilisearch Cloud | $30 |
| Sentry | $26 |
| **Total** | **~$169/mes** |

**6 meses: ~$1,014**.

---

## Tabla comparativa rápida

| Criterio | A: Django+React | B: Next+Supabase | C: FastAPI+Next+Clerk |
|---|---|---|---|
| Aprovecha tu Python | ✅ Total | ❌ Cero | ✅ Total |
| Admin panel gratis | ✅ Django Admin | ❌ Construir | ❌ Construir |
| Velocidad para shippear V0 | 🟡 Media | ✅ Alta | 🟡 Media |
| SEO/SSR built-in | 🟡 SSR aparte | ✅ Nativo | ✅ Nativo |
| Realtime chat | 🟡 Pusher externo | ✅ Nativo | 🟡 Ably externo |
| Mantener solo | ✅ Monolito | ✅ Pocas piezas | ❌ Muchas piezas |
| Vendor lock-in | ✅ Bajo | 🟡 Medio-alto | 🟡 Medio |
| Costo infra 6m | $860 | $846 | $1,014 |

---

## Recomendación: **Opción A — Django + React + Stripe Connect**

### Justificación

1. **El factor decisivo es el Django Admin**. En un marketplace solo, el 30% de tu tiempo después de lanzar son tareas operativas: aprobar perfiles, refundear, banear, ver por qué un pago falló. Django te lo da gratis con auth, búsqueda, filtros, edición inline. Esto vale literalmente 1-2 semanas de tu timeline de 6.

2. **Maximizás tu lenguaje fuerte (Python)**. Con 6 semanas y solo, no te podés permitir aprender patrones nuevos. React + Django es el matrimonio más probado del último decenio.

3. **La superficie de operación es chica**: 1 monolito Django, 1 frontend estático, 1 Postgres, 1 Pusher, 1 Meilisearch. Cinco dashboards vs 7 de la opción C.

4. **A 5,000 usuarios no te vas a quedar corto**. Django + Postgres aguantan mucho más que eso en un dyno chico. Solo cuando llegues a 50K empezás a optimizar.

5. **El costo de Next.js+Supabase es similar** pero te obliga a tirar tu skill Python a la basura y a construir el admin. No vale el cambio.

### Trade-off que estás aceptando

- **Vas a perder SEO inicial** si servís la app como SPA pura. Mitigación: poné las páginas públicas de perfiles de freelancers como páginas Django con templates (server-rendered), y la app autenticada como React. Es el patrón hybrid clásico y funciona perfecto.
- **Pusher Channels a $49/mes es notable**. Si tu chat es bajo volumen, **Ably tiene tier gratis hasta 6M mensajes/mes** — empezás ahí, migrás a Pusher si crece.

### Distribución sugerida de los $5,000

| Categoría | Asignación |
|---|---|
| Infra 6 meses (~$143/mes) | $860 |
| Dominio + email + SSL + transactional mail | $150 |
| Legal (T&C marketplace, política privacidad, contrato freelancer) | $400 |
| Diseño (logo, ilustraciones, Figma) | $500 |
| Stripe Connect: verificación de cuenta business | $0 (sin costo fijo) |
| Marketing semilla primer mes (ads, copy, SEO tools) | $1,500 |
| **Buffer de contingencia (40%)** | $1,590 |

El buffer es deliberadamente alto: en marketplaces el problema nunca es la infra, es el **fraude de pagos primer mes**, **chargebacks**, o pivots de pricing/comisión que requieren A/B test ad-hoc. Tener $1,500 sin asignar te salva.

### Plan de 6 semanas (sanity check)

- **Sem 1**: Django setup, modelos (User, FreelancerProfile, Service, Order, Message), Django Admin customizado.
- **Sem 2**: Auth + onboarding freelancer + Stripe Connect Express + KYC redirect.
- **Sem 3**: React frontend (perfil, búsqueda, detalle servicio) + integración API.
- **Sem 4**: Checkout + webhooks Stripe + estados de Order (paid, in_progress, delivered, refunded).
- **Sem 5**: Chat (Pusher/Ably) + notificaciones + Meilisearch indexing.
- **Sem 6**: Testing, hardening, landing, lanzamiento a 50 freelancers piloto.

### Cuándo elegiría B en su lugar

Solo si: (a) SEO masivo de perfiles es **el** canal de adquisición principal desde día 1, (b) el chat necesita features avanzadas (presence, typing indicators, video), (c) preferís TypeScript fullstack y aceptás construir el admin con Refine.

### Cuándo elegiría C en su lugar

Casi nunca para este perfil. Solo si necesitás multi-tenancy con organizations complejas que Clerk maneja excelente — no es tu caso.

---

¿Querés que aterricemos siguiente paso? Tres caminos posibles:
1. Esquema de modelos Django para el marketplace (User, Profile, Service, Order, Review, Message).
2. Setup de Stripe Connect Express con destination charges + flujo de webhooks.
3. Comparación más profunda Pusher vs Ably vs Supabase Realtime para tu caso.