# Tencent Hy4 — reasoning/multi_constraint_decision

- model_id: `tencent/hy4`
- success: True  | final: 8.38 | quality: 9.8
- latency_total: 57.895s | tokens_per_second: 84.9
- input_tokens: 202 | output_tokens: 4916
- judge_score: 5.0 | justificación: 

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

## Veredicto Rápido (TL;DR)

Te recomiendo **React (Vite/Next) + Supabase + un micro-endpoint en Python (Cloud Run) para Stripe**.

**El diagnóstico clave:** Tu presupuesto ($5,000) es holgado, pero tu **timeline (6 semanas) y tu equipo (1 persona) son el verdadero cuello de botella**. Para 5,000 usuarios, la escala es irrelevante (cabe en una Raspberry Pi). Cualquier hora que gastes configurando Redis, WebSockets, Elasticsearch o pipelines de deploy es una hora que le robas al *Product-Market Fit*. 

Descarta Go para este MVP: saberlo "básico" + manejar webhooks de pagos + 6 semanas = riesgo innecesario de debugging a medianoche.

---

## Comparativa de 3 Opciones

| Criterio | **Opción 1: Supabase (BaaS SQL)** ⭐️ | **Opción 2: Django Monolito** | **Opción 3: Firebase (BaaS NoSQL)** |
| :--- | :--- | :--- | :--- |
| **Stack** | React + Postgres (Supabase) + Python (webhook) | React + Django DRF + Channels + Celery + Redis | React + Firestore + Cloud Functions (Python) |
| **Auth** | Listo en 1h (GoTrue + RLS) | `dj-rest-auth` / JWT (medio día) | Listo en 1h (Firebase Auth) |
| **Chat** | Realtime escuchando `INSERT` (1 día) | Django Channels + Redis (3-4 días ⚠️) | `onSnapshot` (Magia, 1 día) |
| **Admin** | Supabase Studio + 1 página React (1 día) | **Django Admin (10/10, 0 días)** | Consola cruda + React custom (3 días) |
| **Search** | Postgres `tsvector` + `pg_trgm` (Gratis) | Postgres `SearchVector` (Gratis) | Requiere extensión Algolia ⚠️ |
| **Datos (Órdenes/Gigs)** | **Relacional (Ideal)** | **Relacional (Ideal)** | NoSQL (Doloroso para transacciones) ⚠️ |
| **Fit con el Dev** | 95% React + SQL / 5% Python | **100% Python + React** | 90% React / 10% Python |
| **Riesgo en 6 semanas** | **Bajo** | **Alto** (demasiados servicios) | Medio (denormalización) |
| **Costo / Mes** | ~$26 - $35 | ~$55 - $70 | ~$15 - $25 (+ Algolia si crece) |

---

### Análisis de Pros / Contras

#### 1. React + Supabase (El recomendado)
*   **Pros:** El **RLS (Row Level Security)** es el superpoder aquí. Defines las reglas de "Solo el comprador ve su orden" en SQL y tu frontend React puede consultar la BD directamente sin escribir una sola línea de API CRUD. El chat es simplemente suscribirse a la tabla `messages` (tienes historial persistido gratis, sin gestionar sockets). El Admin Panel es Supabase Studio para el día a día + una ruta `/admin` en React para "Aprobar Gig / Resolver Disputa".
*   **Contras:** Las *Edge Functions* de Supabase son TypeScript/Deno, no Python (fricción mínima, la resolvemos abajo). El Free tier **se pausa a los 7 días de inactividad**, así que hay que pagar Pro sí o sí antes del launch.
*   *Search:* `WHERE to_tsvector('spanish', titulo) @@ plainto_tsquery('diseno')` + `pg_trgm` para tolerar typos. Para 10,000 gigs vuela y cuesta $0. Olvida Algolia/Elastic.

#### 2. Django + DRF + Channels (El "cómodo" pero peligroso)
*   **Pros:** 100% en la zona de confort del dev. **Django Admin es insuperable** para un marketplace (gestionar disputas, reembolsos y usuarios banneados sin escribir UI). Control total del state-machine de las órdenes.
*   **Contras:** **No llega en 6 semanas con 1 persona.** Para el chat necesitas Django Channels + ASGI + Redis. Para emails/webhooks necesitas Celery + otro Worker + Redis. De pronto tienes 4 contenedores (Web, Worker, Postgres, Redis) que desplegar, monitorizar y parchear en Railway/Render. La mantenibilidad por 1 persona se degrada rápido.

#### 3. Firebase / Firestore (El señuelo del Realtime)
*   **Pros:** El chat es trivial y la extensión de Stripe te ahorra el webhook. Cloud Functions ya soportan Python (Gen2). Muy barato.
*   **Contras:** **NoSQL es el enemigo de un marketplace.** Tienes `User` → `Gig` → `Order` → `Transaction` → `Message`. Si un freelancer edita el precio de un Gig, ¿actualizas las 40 órdenes abiertas denormalizadas? Ese tipo de bugs de consistencia te comerá la semana 5. Además, su consola de Admin es demasiado técnica para gestionar un negocio y la búsqueda *full-text* nativa no existe (te obliga a integrar Algolia).

---

## Cómo resolvemos el único Trade-off (El Python)

Supabase manejará Auth, Chat, Storage y BD. Para **Pagos (Stripe)**, el dev quiere Python. No lo fuerces a aprender Deno bajo presión:

👉 **Despliega un único endpoint `POST /webhooks/stripe` en Google Cloud Run con FastAPI (20 líneas de Python).**
*   Recibe `checkout.session.completed`.
*   Verifica la firma con `stripe.Webhook.construct_event`.
*   Usa el cliente `supabase-py` (oficial, Python) con la *Service Role Key* para hacer un `UPDATE orders SET status='paid'`.
*   **Costo:** $0 (Cloud Run tiene 2M requests/mes gratis, escala a cero, cero servidores que mantener).

*Alternativa aún más rápida:* Stripe → Make.com (~$9/mo) → Supabase REST. Pero el Cloud Run en Python le da al dev control total sobre la lógica de comisiones del marketplace.

---

## Costos Estimados (Infra + Herramientas)

| Servicio | Plan / Uso | Costo Mensual | 6 Meses |
| :--- | :--- | :--- | :--- |
| **Vercel / Netlify** (React) | Hobby (Free) | $0 | $0 |
| **Supabase** (DB, Auth, Chat) | **Pro** (Backups + No pausa) | $25 | $150 |
| **Cloud Run** (Webhook Python) | Free Tier (2M req) | $0 | $0 |
| **Resend** (Emails transacc.) | Free (3,000/mes / 100/día) | $0 | $0 |
| **Sentry** (Errores) | Developer (Free) | $0 | $0 |
| **Dominio** (.com en Cloudflare) | Anual (~$12/año) | ~$1 | $6 |
| **Stripe** | 2.9% + $0.30 / txn | *OpEx* (se descuenta del payout) | *OpEx* |
| **TOTAL INFRA** | | **~$26 / mes** | **~$156** |

**Contra el presupuesto:** Gastas **~$156 de los $5,000 (3.1%)** en 6 meses. Te sobran **~$4,844** para el dominio premium, legales (Términos/Condiciones del marketplace), un diseñador en Figma por 2 días, o simplemente como buffer. **No gastes el presupuesto en infraestructura, gástalo en quitarle trabajo al dev.**

---

## Hoja de Ruta (Validando las 6 semanas)

Para que veas que el stack cierra en tiempo:

*   **Semana 1:** Schema SQL (`users`, `gigs`, `orders`, `messages`) + Políticas RLS + Login React + Stripe Checkout (Redirect).
*   **Semana 2:** CRUD de Gigs + Upload de imágenes (Supabase Storage) + **Búsqueda** (`tsvector` expuesto vía RPC).
*   **Semana 3:** Webhook Python en Cloud Run + State Machine de Órdenes (`pending` → `paid` → `delivered`) + Emails (Resend).
*   **Semana 4:** **Chat** (Supabase Realtime + indicador de "escribiendo" con `presence`) + Sistema de Reviews.
*   **Semana 5:** `/admin` en React (Aprobar gigs, mediar disputas, ver comisiones) + Sentry + Manejo de reembolsos.
*   **Semana 6:** Pulido mobile-first, tests E2E de los 3 flujos críticos (Comprar, Chatear, Entregar) y **Soft Launch** con los 500 usuarios.

### 🛑 Lo que explícitamente NO debes construir (Regla de oro para 1 dev):
❌ Microservicios en Go · ❌ Redis / Celery · ❌ Elasticsearch / Meilisearch · ❌ WebSockets custom · ❌ Kubernetes / Docker Compose local complejo · ❌ Panel de Admin desde cero (usa Studio + RLS).

**Siguiente paso accionable:** Crea el proyecto en Supabase, pásale a tu dev el [CLI de Supabase](https://supabase.com/docs/guides/local-development) para tener el schema en Git desde el día 1, y sube el Pro ($25) en la Semana 3 para no llevarte el susto del "Project Paused" el día del lanzamiento.