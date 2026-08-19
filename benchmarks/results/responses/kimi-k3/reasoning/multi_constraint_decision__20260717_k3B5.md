# Kimi K3 — reasoning/multi_constraint_decision

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 7.79 | quality: 10.0
- latency_total: 265.227s | tokens_per_second: 30.2
- input_tokens: 275 | output_tokens: 8008
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una comparación detallada de opciones de stack tecnológico con pros y contras bien articulados.

## Respuesta completa

# Stack para tu MVP de marketplace freelance

Antes de comparar: un punto clave. **Tu restricción real no es el presupuesto ($5k sobran a esta escala), sino 6 semanas × 1 dev.** Cada decisión debe optimizar velocidad de desarrollo y simplicidad de mantenimiento, no ahorro de infraestructura ni escala futura.

## Decisiones transversales (iguales en cualquier stack)

- **Pagos: Stripe Connect (cuentas Express)**. Es el estándar para marketplaces: Stripe maneja el KYC de los freelancers, retención de fondos hasta completar el servicio, y comisiones vía `application_fee`. No construyas escrow propio jamás.
- **Búsqueda: Postgres full-text search + `pg_trgm`** al inicio. Con miles de listings sobra. Meilisearch/Algolia son upgrades posteriores.
- Email transaccional (Resend/Postmark), Sentry, PostHog, Cloudflare — todos con free tier generoso.

---

## Opción 1: Next.js + Supabase

**Stack:** Next.js (App Router) + Supabase (Postgres, Auth, Realtime, Storage) + Stripe + Vercel.

**Pros:**
- Usa React directamente (skill existente)
- Auth, chat en tiempo real y DB resueltos en un solo servicio
- Free tiers generosos; despliegue trivial
- Refine.dev o el table editor de Supabase dan un admin básico rápido

**Contras:**
- La lógica de negocio de un marketplace (órdenes, comisiones, disputas, reembolsos) termina en Edge Functions + RLS policies — se vuelve frágil y difícil de debuggear con transacciones entre 3 partes (comprador, vendedor, plataforma)
- **No hay admin panel real**: tendrías que construirlo (1-2 semanas de trabajo)
- Vercel Hobby no permite uso comercial → $20/mo desde el día 1
- RLS mal configurado = vulnerabilidades de seguridad

## Opción 2: Monolito Django ⭐

**Stack:** Django + templates con HTMX/Alpine (o Next.js + DRF si prefieres React) + Postgres + Redis + Stripe Connect + Pusher o Django Channels. Deploy en Railway o Render.

**Pros:**
- **Django Admin resuelve el admin panel gratis.** Un marketplace lo necesita desde el día 1: moderar usuarios, gestionar disputas, reembolsos, payouts manuales. Esto solo te ahorra 1-2 semanas
- Python es tu skill fuerte; el ecosistema es maduro: `django-allauth` (auth + social login), `dj-stripe`, `django-filter`
- SSR por defecto = buen SEO para los listings (crítico en un marketplace)
- Un solo despliegue, un solo modelo mental → ideal para mantener 1 persona
- Modelo relacional perfecto para órdenes/pagos/estados

**Contras:**
- Chat en tiempo real requiere decidir: Channels (self-hosted, +complejidad de ops) o Pusher/Ably (menos código, vendor externo)
- Si eliges HTMX, hay curva de aprendizaje de 1-2 días (pequeña, pero existe)
- Menos "cool" que un stack JS moderno (irrelevante para el negocio)

## Opción 3: Next.js + SaaS componible (best-of-breed)

**Stack:** Next.js + Clerk (auth) + Neon (Postgres) + Pusher (chat) + Algolia (búsqueda) + Stripe + Vercel.

**Pros:**
- Cada componente es el mejor de su categoría, con SDKs pulidos
- Escala sin tocar infraestructura
- Cero ops de base de datos

**Contras:**
- **6 vendors = 6 dashboards, 6 facturas, 6 puntos de fallo** para 1 persona
- Cliffs de precio: Pusher salta a ~$49/mo, Algolia se encarece rápido, Clerk cobra por MAU tras 10k
- Sigue sin resolver admin panel ni lógica de negocio compleja
- Acoplar webhooks de Stripe con 4 servicios externos es tedioso

**Descartadas:** *Go* — con nivel básico y 6 semanas, aprender el lenguaje mientras construyes es riesgo innecesario; además no tiene equivalente a Django Admin. *Firebase* — el modelo NoSQL encaja mal con transacciones de marketplace (órdenes, pagos, reembolsos).

---

## Tabla comparativa

| Criterio | Next.js + Supabase | Django | SaaS componible |
|---|---|---|---|
| Velocidad para este dev | ✅ Alta | ✅ Muy alta | ⚠️ Media |
| Auth | ✅ Incluida | ✅ allauth | ✅ Clerk |
| Lógica de pagos compleja | ⚠️ RLS/functions frágiles | ✅ ORM + transacciones | ⚠️ Dispersa |
| Chat | ✅ Realtime incluido | ⚠️ Pusher/Channels | ✅ Pusher |
| Admin panel | ❌ Construirlo | ✅ **Gratis** | ❌ Construirlo |
| Mantenimiento (1 persona) | ⚠️ 2-3 servicios | ✅ Monolito | ❌ 6 vendors |
| Costo mes 1 | ~$45-65 | ~$30-55 | ~$40-70 |
| Costo mes 6 (5k users) | ~$60-90 | ~$60-120 | ~$120-250 |

## Recomendación: **Opción 2 — Monolito Django**

1. **El admin panel es tu diferenciador oculto.** En un marketplace, las operaciones manuales (disputas, moderación, refunds) consumen más tiempo que el código. Django Admin te lo da el día 1.
2. Usa tu skill más fuerte (Python) en lo más riesgoso (lógica de dinero).
3. Menos vendors = menos cosas que se rompen a las 2am cuando mantienes todo solo.
4. Sin cliffs de precio: Railway/Render escala de forma lineal y predecible hasta mucho más de 5k usuarios.

**Frontend:** recomiendo templates + HTMX + Alpine (un despliegue, SEO gratis, ~1-2 semanas más rápido). Si te sientes significativamente más productivo en React, Next.js + DRF funciona, pero suma un segundo despliegue y una capa de API que serializar/mantener.

## Costos estimados del stack recomendado

| Concepto | Mes 1 | Mes 6 |
|---|---|---|
| App + worker (Railway/Render) | $10-20 | $25-40 |
| Postgres gestionada | $5-15 | $15-25 |
| Redis | $5-10 | $10 |
| Pusher (o Channels = $0) | $0 | $0-49 |
| Email (Resend/Postmark) | $0 | $10-15 |
| Sentry + PostHog + Cloudflare | $0 | $0-26 |
| Storage (R2/S3) | $1 | $3-5 |
| **Total/mes** | **~$20-45** | **~$65-170** |
| **Total 6 meses** | | **~$400-650** |

**Stripe** cobra ~2.9% + $0.30 por cargo + ~$2/cuenta conectada activa/mes (varía por país — verifica precios actuales), pero eso sale del volumen transaccionado, no de tus $5k. **Conclusión: gastarás <$700 de los $5,000.** Reserva el resto para términos legales (un marketplace que mueve dinero los necesita), diseño/logo y contingencia.

## Plan de 6 semanas

| Semana | Entregable |
|---|---|
| 1 | Setup, CI/CD, auth, modelos de datos, onboarding Stripe Connect en sandbox |
| 2 | Publicación de servicios, perfiles, búsqueda con Postgres FTS |
| 3 | Flujo de orden + checkout + comisiones + webhooks de Stripe |
| 4 | Chat + notificaciones por email |
| 5 | Admin: disputas, reembolsos, moderación + reviews/ratings |
| 6 | Hardening, tests de flujos de dinero, monitoreo, SEO, launch |

## Qué NO construir

- ❌ Microservicios, Kubernetes, Docker orquestado complejo
- ❌ Escrow propio (usa los patrones de Stripe: charge ahora, transfer al completar)
- ❌ App móvil nativa (responsive web alcanza)
- ❌ Elasticsearch/Algolia desde el día 1
- ❌ Chat con WebSockets desde cero

¿Quieres que profundice en el diseño del flujo de pagos con Stripe Connect (cuándo liberar fondos, manejo de disputas) o en el esquema de modelos de Django para el marketplace?