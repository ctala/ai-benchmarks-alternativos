# Claude Fable 5 — reasoning/multi_constraint_decision

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 7.87 | quality: 10.0
- latency_total: 48.646s | tokens_per_second: 70.3
- input_tokens: 280 | output_tokens: 3418
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un análisis detallado y comparativo de múltiples opciones de stack tecnológico con pros y contras específicos.

## Respuesta completa

# Stack Tecnológico para Marketplace MVP

## Análisis previo rápido

Antes de comparar, dos observaciones clave de tus restricciones:

- **6 semanas con 1 dev** significa que el enemigo #1 es construir infraestructura genérica (auth, websockets, etc.) en vez del producto. Prioriza servicios gestionados.
- **Pagos en marketplace** ≠ pagos simples. Necesitas split payments / escrow (retener dinero y liberarlo al freelancer). Esto prácticamente obliga a usar **Stripe Connect** en cualquier stack.
- Descarto Go de entrada: tu nivel es básico y no aporta ventajas a esta escala. 5,000 usuarios los maneja cualquier stack.

---

## Opción A: Next.js + Supabase + Stripe Connect

**Stack:** Next.js (App Router) en Vercel · Supabase (Postgres, Auth, Realtime, Storage) · Stripe Connect · Admin con Retool/Refine

| Requisito | Cómo se resuelve |
|---|---|
| Auth | Supabase Auth (email, OAuth, magic links) — incluido |
| Pagos | Stripe Connect (Express accounts) |
| Chat realtime | Supabase Realtime (websockets sobre Postgres) — incluido |
| Búsqueda | Postgres full-text search (suficiente para tu escala) |
| Admin panel | Retool (free tier) o Refine sobre la misma DB |

**Pros:**
- Auth + realtime + DB + storage en un solo servicio = menos superficie de mantenimiento
- Todo es TypeScript/React, que ya dominas
- Row Level Security de Postgres te da seguridad declarativa sin escribir middleware
- Deploy trivial (git push), cero DevOps
- Es Postgres estándar: si Supabase te queda chico, migras la DB sin reescribir

**Contras:**
- No usas Python (tu fortaleza en backend)
- Supabase Realtime es más limitado que un sistema de chat dedicado (sin typing indicators nativos, presencia básica)
- Lógica compleja de negocio en Edge Functions (Deno) puede ser incómoda

**Costo mensual:** Vercel Pro $20 + Supabase Pro $25 + Retool $0 = **~$45/mes** (mes 1 puede ser $0 con free tiers)

---

## Opción B: React + FastAPI + Postgres (Railway/Render)

**Stack:** React (Vite) · FastAPI · PostgreSQL · Redis · Stripe Connect · Auth con Clerk o propio

| Requisito | Cómo se resuelve |
|---|---|
| Auth | Clerk ($25/mes después de free tier) o custom con FastAPI |
| Pagos | Stripe Connect |
| Chat realtime | WebSockets en FastAPI + Redis pub/sub (tú lo construyes) |
| Búsqueda | Postgres FTS o Meilisearch self-hosted |
| Admin panel | SQLAdmin / FastAPI Admin |

**Pros:**
- Máximo control y flexibilidad; Python es tu backend fuerte
- Sin vendor lock-in significativo
- Lógica de negocio compleja (matching, comisiones, disputas) más cómoda en Python
- Costos predecibles a largo plazo

**Contras:**
- **Construyes tú el chat en tiempo real** (websockets, reconexión, persistencia, presencia): fácilmente 1-1.5 semanas de tus 6
- Auth custom = riesgo de seguridad + tiempo; Clerk mitiga pero suma costo
- Más DevOps: dos deploys (front + back), Redis, migraciones, monitoreo
- Mantenimiento por 1 persona es más pesado

**Costo mensual:** Railway ~$20-40 + Clerk $25 + Vercel $0-20 = **~$50-85/mes**

---

## Opción C: Firebase + React

**Stack:** React · Firebase (Auth, Firestore, Cloud Functions, Storage) · Stripe Connect · Algolia para búsqueda

**Pros:**
- Chat en tiempo real es el caso de uso estrella de Firestore — trivial de implementar
- Auth muy maduro
- Escala automática sin pensar

**Contras:**
- **Firestore es pésimo para queries de marketplace** (filtros combinados, joins, agregaciones). Un marketplace es relacional por naturaleza: usuarios ↔ servicios ↔ órdenes ↔ reviews
- Búsqueda requiere Algolia sí o sí (~$0-50/mes extra, y sube rápido)
- Lock-in fuerte: migrar de Firestore después es reescribir
- Costos impredecibles con lecturas/escrituras (un chat activo genera muchas lecturas)
- Modelar comisiones, escrow y reporting en NoSQL es doloroso

**Costo mensual:** $0-25 al inicio, pero **impredecible** a 5,000 usuarios (podría ser $50-150 con chat activo + Algolia)

---

## Comparación resumen

| Criterio | A: Supabase | B: FastAPI | C: Firebase |
|---|---|---|---|
| Velocidad para llegar al MVP | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| Mantenibilidad (1 persona) | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| Fit con modelo de datos de marketplace | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| Costo predecible | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |
| Flexibilidad futura | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| Costo mensual (mes 1-6) | $0-45 | $50-85 | $0-150 |

---

## Recomendación: Opción A (Next.js + Supabase + Stripe Connect)

**Justificación:**

1. **El timeline manda.** Auth, realtime, DB y storage resueltos desde el día 1 te devuelven ~2 semanas que la Opción B consumiría en plumbing. Esas 2 semanas van a lo que diferencia tu producto: el flujo de contratación, perfiles y pagos.

2. **Un marketplace es relacional.** Postgres es el fit correcto (a diferencia de Firebase), y su full-text search cubre búsqueda hasta decenas de miles de listings sin servicios extra.

3. **Mantenible por 1 persona.** Un solo lenguaje (TypeScript), un solo repo, un solo proveedor de backend, deploys automáticos. Cuando estés solo apagando fuegos post-launch, esto vale oro.

4. **Ruta de escape clara.** Si en 6 meses necesitas lógica pesada, agregas un servicio FastAPI que hable con el mismo Postgres. No es una decisión irreversible.

### Presupuesto estimado (6 meses)

| Concepto | Costo |
|---|---|
| Infra (Vercel Pro + Supabase Pro) | ~$45/mes × 6 = $270 |
| Dominio + email transaccional (Resend) | ~$50 |
| Stripe | $0 fijo (2.9% + $0.30 por transacción + fee de Connect) |
| Herramientas (GitHub, Sentry free tier, Retool free) | $0 |
| Buffer para imprevistos | ~$200 |
| **Total infra/herramientas** | **~$520 de tus $5,000** |

Te sobra presupuesto de sobra — úsalo en diseño (una plantilla premium tipo Tailwind UI, ~$300, te ahorra días) y marketing de lanzamiento.

### Plan sugerido de 6 semanas

- **S1:** Setup, modelo de datos, auth, perfiles
- **S2:** Listings de servicios + búsqueda/filtros
- **S3:** Stripe Connect (onboarding de freelancers + checkout) — *la parte más riesgosa, no la dejes para el final*
- **S4:** Flujo de órdenes + chat realtime
- **S5:** Reviews, notificaciones, admin panel (Retool)
- **S6:** Testing, pulido, contenido seed, launch

¿Quieres que profundice en alguna parte, por ejemplo el diseño del flujo de Stripe Connect (escrow y comisiones) o el modelo de datos inicial?