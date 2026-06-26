# Claude Fable 5 (suscripción) — reasoning/multi_constraint_decision

- model_id: `claude-fable-5`
- success: True  | final: 7.51 | quality: 10.0
- latency_total: 41.88s | tokens_per_second: 68.3
- input_tokens: 2 | output_tokens: 2862

## Respuesta completa

# Stack para marketplace de servicios freelance — MVP en 6 semanas

Antes de comparar: con 1 dev, 6 semanas y $5K, la variable que más importa **no es performance ni escalabilidad — es velocidad de desarrollo y superficie de mantenimiento**. 5,000 usuarios en 6 meses es una carga que cualquier VPS de $20/mes maneja sin despeinarse. No optimices para escala que no tienes.

---

## Opción A: Next.js + Supabase (el "BaaS-first")

**Stack:** Next.js 14 (App Router) + Supabase (Postgres, Auth, Realtime, Storage) + Stripe Connect + Vercel + Typesense Cloud o Postgres full-text search.

| Requisito | Cómo se resuelve |
|---|---|
| Auth | Supabase Auth (email, OAuth, magic links) — 1 día de trabajo |
| Pagos | Stripe Connect (split payments marketplace) — el estándar |
| Chat realtime | Supabase Realtime (Postgres changes + channels) |
| Búsqueda | Postgres `tsvector` para MVP; Typesense si necesitas typo-tolerance |
| Admin panel | Supabase Studio para queries ad-hoc + Retool/refine.dev para gestión |

**Pros:**
- El más rápido de los tres. Auth + DB + realtime + storage en un solo servicio = semanas ahorradas.
- React lo domina → cero curva en frontend.
- RLS (Row Level Security) de Postgres te da autorización a nivel de datos sin escribir middleware.
- Comunidad enorme, cualquier problema ya está resuelto en Stack Overflow.

**Contras:**
- Vendor lock-in moderado en Realtime y Auth (la DB es Postgres estándar, eso se migra fácil).
- Supabase Realtime para chat funciona pero no es un sistema de chat completo (read receipts, typing indicators los construyes tú).
- Si el chat se vuelve el core del producto, te quedará corto.

**Costo mensual estimado:**
| Servicio | Costo |
|---|---|
| Supabase Pro | $25 |
| Vercel Pro | $20 |
| Stripe | $0 fijo (2.9% + $0.30 por transacción) |
| Resend (emails transaccionales) | $0-20 |
| Dominio + misc | $5 |
| **Total** | **~$50-70/mes** |

---

## Opción B: Django + HTMX + Postgres en un VPS (el "monolito clásico")

**Stack:** Django + Django Channels (chat WebSocket) + Postgres + Redis + HTMX/Alpine o Django templates + Hetzner/DigitalOcean VPS con Coolify o Docker Compose.

**Pros:**
- Python lo sabe. Django admin = admin panel **gratis y completo desde el día 1** (esto solo vale 1 semana de trabajo).
- Monolito = una sola cosa que deployar, monitorear y entender. Para 1 persona es el modelo mental más simple.
- Cero lock-in. Costos de infra ridículamente bajos.
- `django-allauth` (auth), `dj-stripe` (pagos), Channels (chat): todo el ecosistema existe.

**Contras:**
- Chat realtime con Channels requiere configurar ASGI + Redis + Daphne/Uvicorn — funciona, pero es la parte más frágil del stack y la que más mantenimiento pide.
- UI menos rica: si el marketplace necesita interactividad tipo SPA (filtros dinámicos, chat fluido), HTMX se queda justo y terminas metiendo React igual → dos paradigmas.
- DevOps recae 100% en ti: backups, SSL, deploys, monitoring. Coolify ayuda mucho, pero eres tu propio SRE.

**Costo mensual estimado:**
| Servicio | Costo |
|---|---|
| VPS Hetzner CPX31 (4 vCPU, 8GB) | $16 |
| Backups + S3-compatible storage | $7 |
| Stripe | % por transacción |
| Email (Postmark/Resend) | $15 |
| **Total** | **~$40/mes** |

---

## Opción C: Next.js + FastAPI + Postgres separados (el "moderno por capas")

**Stack:** Next.js frontend + FastAPI backend + Postgres + Redis + WebSockets propios + Railway/Render o VPS.

**Pros:**
- Usa lo mejor de ambos skills (React + Python).
- API limpia desde el día 1 — útil si después viene una app móvil.
- Máxima flexibilidad técnica, cero lock-in.

**Contras:**
- **Dos codebases, dos deploys, dos sistemas de tipos, un contrato API que mantener sincronizado.** Para 1 persona en 6 semanas, esto es el contra que mata.
- Construyes auth, realtime, file uploads y admin panel a mano o ensamblando librerías. Cada uno son días que no tienes.
- Es el stack correcto para un equipo de 4. No para ti hoy.

**Costo mensual estimado:** ~$50-80/mes (Railway/Render cobran por servicio; con 3 servicios + DB + Redis se acumula).

---

## Recomendación: Opción A (Next.js + Supabase)

**Justificación:**

1. **El timeline manda.** 6 semanas para auth + pagos marketplace + chat + búsqueda + admin es agresivo. Stripe Connect solo (onboarding de vendedores, KYC, split de pagos, webhooks) te va a comer 1.5-2 semanas. Necesitas que todo lo demás venga resuelto. Supabase te regala auth, realtime y storage; eso son ~2 semanas que la Opción B y C gastan en plomería.

2. **Mantenible por 1 persona.** Sin servidores que parchear, backups automáticos, dashboard para inspeccionar datos. Cuando algo falla a las 11pm, prefieres un status page de Supabase que SSH a tu VPS.

3. **Presupuesto sobra.** ~$60/mes × 6 meses = $360. Te quedan ~$4,600 para lo que realmente mueve la aguja: Stripe Atlas/legal, un diseñador freelance para el landing, o primeros ads para conseguir oferta y demanda (el problema real de un marketplace no es técnico, es el chicken-and-egg).

4. **El riesgo de lock-in es aceptable.** La DB es Postgres plano — `pg_dump` y te vas cuando quieras. Lo único atado es Auth/Realtime, y a 5,000 usuarios migrar eso es un proyecto de 2 semanas, no una crisis.

**Plan de 6 semanas sugerido:**

| Semana | Foco |
|---|---|
| 1 | Setup, modelo de datos, auth, perfiles freelancer/cliente |
| 2 | Listados de servicios, búsqueda, filtros |
| 3-4 | Stripe Connect completo (onboarding vendedores, checkout, webhooks, escrow básico) |
| 5 | Chat realtime + notificaciones email |
| 6 | Admin (Supabase Studio + refine.dev), QA, deploy, seed de primeros vendedores |

**Una advertencia final:** el feature que más subestima la gente en marketplaces es el flujo de pagos con retención (escrow: cliente paga → freelancer entrega → se libera el pago). Stripe Connect lo soporta con `manual payouts` / transfer scheduling, pero diséñalo en papel ANTES de la semana 3. Si lo improvisas, las disputas y reembolsos te van a perseguir.

¿Quieres que detalle el modelo de datos inicial o el flujo de Stripe Connect para el escrow?