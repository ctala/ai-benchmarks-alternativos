# Claude Fable 5.1 — reasoning/multi_constraint_decision

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 7.74 | quality: 10.0
- latency_total: 95.798s | tokens_per_second: 70.3
- input_tokens: 282 | output_tokens: 6730
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una comparación detallada de opciones de stack con pros y contras específicos para el contexto del MVP.

## Entrada exacta (lo que recibió el modelo)

**user:**

Ayudame a elegir un stack tecnologico para un MVP. Restricciones:

- Presupuesto: $5,000 total (infra + herramientas)
- Timeline: 6 semanas
- Equipo: 1 fullstack dev (sabe React, Python, basico de Go)
- Producto: marketplace de servicios freelance (como Fiverr pero nicho)
- Requisitos: auth, pagos, chat en tiempo real, busqueda, admin panel
- Escala esperada: 500 usuarios primer mes, 5,000 en 6 meses
- Debe ser facil de mantener por 1 persona

Compara al menos 3 opciones de stack, analiza pros/contras de cada uno, y recomienda uno con justificacion. Incluye costos estimados de infraestructura mensual.


## Respuesta completa

# Stack para MVP: marketplace de servicios freelance

Primero, lo que más pesa en tu caso no es la escala (5,000 usuarios en 6 meses es tráfico bajo; cualquier stack razonable lo aguanta) sino **el tiempo (6 semanas) y que una sola persona lo construya y mantenga**. Eso inclina todo hacia "comprar" infraestructura (auth, realtime, storage) en vez de construirla.

Hay 3 piezas que suelen devorar tiempo en un marketplace y conviene decidir independientemente del stack:

- **Pagos**: Stripe Connect (cuentas Express) es el estándar para marketplaces. Resuelve onboarding de freelancers, split de comisión, payouts y compliance fiscal. Si tu mercado es LATAM, Mercado Pago Marketplace es la alternativa, pero con peor DX. **No construyas tu propio ledger.**
- **Chat en tiempo real**: necesitas WebSockets o un servicio gestionado. Es el requisito que más diferencia a las opciones.
- **Búsqueda**: para < 50k listings, Postgres full-text search + `pg_trgm` es suficiente. No metas Elasticsearch/Algolia en el MVP.

---

## Opción A: Next.js + Supabase + Stripe Connect + Vercel

| Capa | Tecnología |
|---|---|
| Frontend + API | Next.js 14 (App Router, Server Actions / Route Handlers) |
| Base de datos | Supabase (Postgres gestionado) |
| Auth | Supabase Auth (email, Google, magic links) |
| Chat realtime | Supabase Realtime (Broadcast + Postgres Changes) |
| Archivos | Supabase Storage (portfolios, entregables) |
| Búsqueda | Postgres FTS + pg_trgm (ya incluido) |
| Pagos | Stripe Connect Express + webhooks |
| Admin | Supabase Studio (semanas 1–4) + rutas `/admin` en Next.js con Refine o tablas simples |
| Email | Resend |
| Hosting | Vercel |
| UI | Tailwind + shadcn/ui |

**Pros**
- Un solo lenguaje (TypeScript), un solo repo, un solo deploy. Para 1 persona esto es enorme.
- Auth, realtime, storage y DB vienen resueltos y bien integrados. Te ahorra fácilmente 1.5–2 semanas.
- Row Level Security de Postgres te da autorización a nivel de datos (un freelancer solo ve sus conversaciones) sin escribir middleware.
- Es Postgres estándar debajo: si Supabase te deja de gustar, haces `pg_dump` y te vas. El lock-in real está en Auth y Realtime, que son reemplazables.
- Vercel: deploy en cada push, previews, cero ops.
- Ecosistema con la mayor cantidad de ejemplos de exactamente este caso (marketplace + Supabase + Stripe).

**Contras**
- No usas Python, que es tu lenguaje de backend fuerte. Tendrás que acostumbrarte a lógica de servidor en TS.
- Admin panel no viene gratis: tienes que construirlo (aunque Supabase Studio cubre el 70% al inicio).
- Supabase Realtime es más simple que una solución dedicada; si el chat crece a features complejas (typing indicators avanzados, read receipts por mensaje, threads), terminarás migrando a algo como Stream o construyendo sobre Broadcast.
- Las funciones serverless de Vercel tienen límite de ejecución (webhooks de Stripe pesados o jobs largos requieren Supabase Edge Functions o cron externo).
- El plan Hobby de Vercel prohíbe uso comercial: necesitas Pro desde el día 1.

**Costo mensual estimado**

| Servicio | Mes 1 (500 users) | Mes 6 (5,000 users) |
|---|---|---|
| Vercel Pro | $20 | $20–40 |
| Supabase Pro | $25 | $25–50 (si pasas de 8 GB DB o 250 GB egress) |
| Resend | $0 (3k emails) | $20 |
| Stripe | 0 fijo (2.9% + $0.30 por cobro + 0.25% Connect) | igual |
| Dominio + Cloudflare | ~$1 | ~$1 |
| Sentry (free) | $0 | $0–26 |
| **Total** | **~$46** | **~$70–140** |

---

## Opción B: Django + Django REST Framework + React/Next.js + Postgres + Channels

| Capa | Tecnología |
|---|---|
| Backend | Django 5 + DRF |
| Frontend | Next.js (o Vite + React SPA) |
| Base de datos | Postgres gestionado (Railway, Render o Neon) |
| Auth | django-allauth + dj-rest-auth (JWT) o Clerk |
| Chat realtime | Django Channels + Redis (ASGI con Uvicorn/Daphne) |
| Búsqueda | `django.contrib.postgres.search` |
| Pagos | Stripe Connect + dj-stripe |
| Admin | **Django Admin** (gratis, día 1) |
| Hosting | Railway o Render (backend + Postgres + Redis), Vercel para frontend |

**Pros**
- **Django Admin** es el argumento más fuerte: moderación de usuarios, listings, disputas, reembolsos, todo con permisos, filtros y búsqueda, en horas no días. Para un marketplace donde vas a necesitar intervenir manualmente mucho al inicio, esto vale oro.
- Trabajas en tu lenguaje de backend más fuerte. Menos fricción en lógica de negocio compleja (estados de pedido, escrow, disputas).
- ORM, migraciones, validación, permisos: todo maduro y "aburrido" en el buen sentido.
- Fácil de testear. Fácil de contratar gente después.
- Cero lock-in: corre en cualquier lado.

**Contras**
- Dos deploys, dos repos (o monorepo con tooling), dos sistemas de tipos. Para 1 persona es fricción real: cada feature toca backend + frontend + contrato API.
- **Channels es la parte dolorosa**: necesitas Redis, servidor ASGI, y el deploy es más delicado. Es la pieza con más probabilidad de darte problemas en producción y de consumir 3–4 días que no tienes.
- Auth con JWT + refresh tokens entre Next.js y DRF requiere plomería manual (o pagas Clerk, que añade otra dependencia).
- Más ops: Redis, workers (Celery o similar si necesitas jobs), logs de dos servicios.
- Timeline: realistamente 7–8 semanas para los mismos features, no 6.

**Costo mensual estimado**

| Servicio | Mes 1 | Mes 6 |
|---|---|---|
| Railway (web + Postgres + Redis) | $20–35 | $40–70 |
| Vercel Pro (frontend) | $20 | $20 |
| Clerk (si lo usas) | $0 (10k MAU gratis) | $0–25 |
| Resend | $0 | $20 |
| Stripe | variable | variable |
| **Total** | **~$40–55** | **~$80–135** |

Si sirves el frontend desde Django templates + HTMX en lugar de Next.js, eliminas Vercel y el problema de dos deploys. Esto es muy viable y a muchos devs solos les funciona mejor, pero pierdes tu ventaja en React.

---

## Opción C: Go (Echo/Chi) + React SPA + Postgres + WebSockets nativos

| Capa | Tecnología |
|---|---|
| Backend | Go + Echo o Chi, sqlc/pgx |
| Frontend | Vite + React SPA |
| Auth | Construido a mano (sessions/JWT) o Clerk |
| Chat realtime | `gorilla/websocket` o `nhooyr/websocket` + Redis pub/sub |
| Búsqueda | Postgres FTS |
| Pagos | Stripe Connect (SDK oficial de Go) |
| Admin | Construido a mano o Retool/Appsmith |
| Hosting | Fly.io o VPS en Hetzner + Postgres gestionado |

**Pros**
- Infra más barata y eficiente: un binario, 50 MB de RAM, aguanta 5,000 usuarios en una máquina de $5.
- Deploy trivial (un binario en un container).
- Tipado fuerte, concurrencia nativa para WebSockets.
- Cero lock-in.

**Contras**
- **Tienes Go básico.** En 6 semanas vas a estar aprendiendo el lenguaje mientras construyes auth, manejo de WebSockets, webhooks de Stripe y un admin. Eso no cierra.
- El ecosistema de Go es minimalista por diseño: auth, migraciones, validación, admin… todo lo ensamblas tú. Lo que en Django son 2 líneas, en Go son 200.
- Admin panel: o lo construyes desde cero (1+ semana) o pagas Retool ($10/user/mes).
- Mantenimiento: cuando algo falla a las 2 AM, prefieres estar en tu stack más fuerte, no en el más débil.

**Costo mensual estimado**

| Servicio | Mes 1 | Mes 6 |
|---|---|---|
| Fly.io (app + Redis) | $5–15 | $15–30 |
| Postgres (Neon o Fly) | $0–19 | $19–39 |
| Vercel/Cloudflare Pages (SPA) | $0–20 | $0–20 |
| Retool (admin) | $0–10 | $10–30 |
| **Total** | **~$15–60** | **~$45–120** |

Es la más barata de operar, pero el ahorro de ~$30/mes no justifica el riesgo en el timeline.

---

## Comparación resumida

| Criterio (peso) | A: Next.js + Supabase | B: Django + React | C: Go + React |
|---|---|---|---|
| Velocidad a MVP (muy alto) | ★★★★★ | ★★★★ | ★★ |
| Encaje con skills del dev (alto) | ★★★★ | ★★★★★ | ★★ |
| Chat realtime "fácil" (alto) | ★★★★★ | ★★★ | ★★★ |
| Admin panel (medio) | ★★★ | ★★★★★ | ★★ |
| Mantenible por 1 persona (muy alto) | ★★★★★ | ★★★ | ★★★ |
| Costo infra (bajo) | ★★★★ | ★★★★ | ★★★★★ |
| Lock-in (bajo) | ★★★ | ★★★★★ | ★★★★★ |
| Riesgo de no llegar en 6 semanas | Bajo | Medio | Alto |

---

## Recomendación: Opción A (Next.js + Supabase + Stripe Connect + Vercel)

**Justificación:**

1. **Es la única que cierra en 6 semanas con margen.** Auth, realtime, storage y DB te los dan listos. Cada uno de esos es 2–4 días si lo construyes.
2. **Un solo deploy, un solo lenguaje, un solo repo.** Para un dev solo esto reduce el costo de cada feature y de cada bug en producción. La "sobrecarga de contexto" de saltar entre Django y Next.js es real y acumulativa.
3. **El chat es el requisito más riesgoso y aquí es el más resuelto.** Supabase Realtime sobre una tabla `messages` con RLS es un día de trabajo. Channels + Redis en Railway es una semana con sorpresas.
4. **La escala no es un problema.** 5,000 usuarios es trivial para Supabase Pro y Vercel.
5. **El lock-in es aceptable.** Es Postgres. Si en 1 año necesitas migrar, migras la DB en una tarde y reemplazas Auth/Realtime con tiempo.
6. **Costo total en tu presupuesto:** ~$50/mes × 6 semanas de desarrollo ≈ $75 de infra. Más dominio, Cursor/Copilot ($20/mes), Figma free. Gastas < $300 de los $5,000 en infra y herramientas; el resto es colchón o marketing.

**La única razón para elegir B en su lugar:** si anticipas que el admin va a ser el centro de la operación (mucha moderación manual, disputas, verificación de freelancers) *y* te sientes más seguro con lógica de negocio en Python. En ese caso, haz B pero con **Django templates + HTMX** (no Next.js aparte) y chat con Pusher/Ably ($29–49/mes) en lugar de Channels para quitarte el riesgo de Redis/ASGI. Timeline sube a 7–8 semanas.

**Descarta C.** No es el momento de aprender Go.

---

## Plan de 6 semanas con la Opción A

| Semana | Entregable |
|---|---|
| 1 | Setup: Next.js + Supabase + shadcn. Auth (email + Google). Schema: `profiles`, `services`, `orders`, `conversations`, `messages`, `reviews`. RLS policies. |
| 2 | Perfiles de freelancer, CRUD de servicios, upload de imágenes (Storage), listado público. |
| 3 | Stripe Connect: onboarding Express de freelancers, checkout de un servicio, webhooks, estado de orden. Comisión de plataforma. |
| 4 | Chat (Realtime), flujo de orden (pendiente → en progreso → entregado → completado), notificaciones por email. |
| 5 | Búsqueda (FTS + filtros por categoría/precio), reviews, rutas `/admin` básicas (usuarios, servicios, órdenes, bloquear/aprobar). |
| 6 | QA, edge cases de pagos (reembolsos, disputas manuales), SEO básico, landing, deploy final, Sentry. |

**Decisiones que te ahorran tiempo:**
- Semanas 1–4: usa Supabase Studio como admin. Construye `/admin` propio solo en semana 5.
- Pagos: captura manual en Stripe (`capture_method: manual`) para retener fondos hasta que el cliente acepte la entrega. Es tu "escrow" sin complejidad.
- Chat: una tabla `messages` + `supabase.channel().on('postgres_changes')`. No typing indicators, no read receipts en el MVP.
- Búsqueda: una columna `tsvector` generada + índice GIN. Nada más.
- No uses Edge Functions salvo para webhooks de Stripe si Vercel te da timeouts.

**Qué vigilar después del MVP:** el momento de añadir Meilisearch (cuando los filtros de búsqueda se vuelvan complejos), y el momento de mover el chat a Stream o similar (cuando pidan archivos adjuntos en chat, threads o moderación automática). Ninguno llega antes de los 5,000 usuarios.