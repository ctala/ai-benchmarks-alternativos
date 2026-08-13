# Nex-N2-Mini — reasoning/multi_constraint_decision

- model_id: `nex-agi/nex-n2-mini`
- success: True  | final: 7.44 | quality: 7.68
- latency_total: 39.018s | tokens_per_second: 210.0
- input_tokens: 179 | output_tokens: 8192
- judge_score: 3.8 | justificación: 

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


We need answer in Spanish. Need help choose tech stack for MVP with constraints. Compare at least 3 options, pros/cons, recommend one with justification, estimated monthly infra costs. Need maybe include timeline 6 weeks, team one fullstack, maintenance. Need maybe mention $5000 total infra+tools (not dev labor? likely). Need include costs monthly. Need maybe include architecture. Need maybe recommend perhaps Next.js + Supabase/Postgres + Stripe + Liveblocks? But product has Python known. Need compare options:

Option A: Next.js (React/TS) + FastAPI/Python + PostgreSQL managed (Supabase/Neon) + Stripe + Liveblocks/Ably + Algolia/Meilisearch + Vercel/Render. Pros: matches skills, fast, modern, maintainable; cons: multi-cloud complexity, search managed cost, realtime provider costs.

Option B: Django + DRF + React/Next frontend + PostgreSQL (Supabase/Neon) + Stripe + Django Channels/WebSockets + Algolia/Meilisearch. Pros: batteries included, admin panel, auth; cons: websockets complexity, slower UI dev maybe.

Option C: Laravel (PHP) + React/Vue? + MySQL/Postgres + Filament admin + Livewire/Reverb or Pusher + Stripe + Meilisearch. Pros: rapid admin/auth/payments, one person; cons: PHP ecosystem if team doesn't know PHP, scaling real-time.

Option D maybe Rails + Hotwire? But team React/Python. Need at least 3. Could include BaaS (Supabase + React + Stripe) as option. But "stack tech" maybe compare.

Need recommend one. Need consider constraints: 6 weeks, 1 fullstack, Python/React, admin panel. Marketplace requires auth, payments, real-time chat, search, admin. MVP. Need avoid overengineering. Need recommend maybe "BaaS-first" to save time: Next.js + Supabase Auth/Postgres/Storage/Realtime + Stripe + Liveblocks + Meilisearch (or Postgres FTS initially). But user says Python. They know Python basic Go, not PHP. Need use Python? Could do FastAPI. But for 6 weeks, BaaS with Next.js + FastAPI maybe. Admin panel: Supabase Dashboard + Retool? For admin panel, maybe Retool or Appsmith? But budget $5k infra+tools, one month? Need include. Admin panel can be custom simple in Next.js or Retool. For one person maintain, maybe no custom admin panel initially, use Supabase Dashboard/Retool. But requirement admin panel, need include. Could use Retool monthly $10/user? Or Appsmith free/self-hosted. Supabase has built-in table editor, but not polished. Better: Next.js admin pages (roles) with shadcn/ui or Retool. Need ensure within budget.

Need analyze options.

Need maybe include cost estimates monthly for 500 users month 1 and 5000 month 6. The user asks "costos estimados de infraestructura mensual" not necessarily both, but include both. Need budget $5k total infra+tools. For 5000 users likely under $500. Need maybe include tools. Need mention costs vary.

Let's think of optimal stack.

Option 1: "Next.js + FastAPI + Supabase/Postgres + Stripe + Liveblocks + Meilisearch" (or Next.js with FastAPI). But if using Supabase Realtime for chat, maybe no Liveblocks. But chat requires real-time, auth, presence, persistence. Supabase Realtime is included; but for chat with file uploads? Good. Search: Postgres FTS initially to avoid cost, upgrade to Meilisearch if needed. But marketplace search may need more than FTS; maybe Meilisearch. Need include cost.

Maybe recommend "Next.js + FastAPI + Supabase (Auth, Postgres, Storage, Realtime) + Stripe + Meilisearch + Vercel/Render + Retool" is robust. But using both Next.js and FastAPI might introduce deployment complexity. For one fullstack, maybe Next.js API routes + Python not needed? They know Python, but can use FastAPI. For MVP, using Python backend plus Next.js frontend. Need auth, payments, chat, search, admin. Supabase Auth/Auth via NextAuth? If using FastAPI with OAuth? Complexity.

Alternative "Next.js full-stack (App Router) + Supabase" eliminates API deployment. But Python knowledge unused. Search maybe Supabase Postgres. Admin panel via Supabase/Retool. This is fastest. But if they know Python, maybe not necessary. Product requires payments, chat, search; BaaS covers. Maintenance one person. Use TypeScript in Next.js. Cost low. Pros: fastest, fewer infra pieces, built-in auth/admin (Supabase dashboard). Cons: vendor lock-in, Postgres search less robust, real-time limitations, BaaS pricing changes. For MVP, recommended? I think yes.

But maybe compare options:

1. Next.js + Supabase + Stripe + Meilisearch (BaaS-first)
2. Next.js + FastAPI + PostgreSQL (Neon/RDS) + Redis + WebSockets (Ably/Socket.io) + Algolia/Meili + Vercel/Render
3. Django + React + PostgreSQL + Channels + Algolia/Meili + Filament/Django admin
4. Laravel + React + MySQL/Postgres + Livewire/Reverb + Filament + Algolia/Meili (optional).

Need at least 3. Maybe include 4 for better comparison. But desired overwordiness medium, answer moderate.

Need recommend one. Let's decide.

Given team: 1 fullstack knows React, Python, basic Go. Need 6 weeks. Requirements. Marketplace with chat and payments. Need admin. Easiest maintain: BaaS-first Next.js + Supabase + Stripe + Meilisearch/Postgres FTS + Retool. But maybe "Python" not used. Could use Python only for background jobs? Not necessary. Supabase Edge Functions maybe JS. But user knows Python, but can learn TS. Need perhaps recommend "Option A" because fastest and maintainable.

Need maybe include "No construyas chat propio, search custom, admin custom". Use managed services.

Need maybe include "payments: Stripe Connect" because marketplace payments. Important. For Fiverr-like marketplace, need marketplace payments (split payouts). Use Stripe Connect, not simple Stripe Checkout. Need include. Auth: Supabase Auth or Clerk. Supabase Auth okay. Chat: Supabase Realtime or Liveblocks. Search: Meilisearch or Algolia. Admin: Retool or simple Next.js admin with Supabase roles.

Cost estimates:
Option A:
- Vercel Pro? Hobby free for dev, Pro $20/user/mo maybe. For 6-week MVP maybe Hobby; if team one maybe $0-$20.
- Supabase Pro $25/mo (or Team $25/user). Auth, Postgres, Storage 10GB, Realtime included.
- Stripe: 2.9% + 30¢ + Connect fees; no monthly.
- Meilisearch Cloud $0-$50/mo (starter maybe $0 or $29; self-host $5 VPS). Could use Postgres FTS free initially.
- Retool Team $10-$15/admin? If 1 admin.
- Sentry free/pro $26.
- Domain/Email: Postmark $15, domain $15/yr.
- Total infra+tools: $80-$150/mo for 500; $150-$300/mo for 5k. Under $5k.
Need maybe include storage/chat cost.

Option B:
- Vercel Pro $20
- Render/Railway/ECS? Postgres Neon Pro $19 or RDS $15-$50; Redis Upstash free-$25; WebSockets Ably $0-$79; Meili/Algolia $0-$50; Retool $15; logs etc. Total $100-$250/mo; maybe more if self-host websocket.
Option C:
- DigitalOcean $60-$150 (App + DB + Redis + worker), Meili/Algolia, Retool, etc. Total $80-$250.
Option D Laravel:
- Laravel Forge $20 + DigitalOcean $12-$60 + Pusher/Reverb? If Reverb self-host websockets $12; Algolia/Meili $0-$50; Filament free; Retool $15. Total $50-$150. But team doesn't know PHP.

Need maybe include a table.

Need include timeline 6 weeks:
Week 1: requirements, DB, design, auth, payments setup.
Week 2: profiles, listing/search, admin basics.
Week 3: booking flow, checkout, email.
Week 4: chat, notifications, moderation.
Week 5: QA, security, analytics.
Week 6: launch, monitoring.
Maybe not necessary but useful. User asks stack, but we can include.

Need include "MVP scope recommendations":
- Use Stripe Connect for marketplace payments, test mode first.
- Use roles: buyer, seller, admin; RBAC.
- Start with Postgres FTS; only add Meilisearch if search quality needs relevance/filters.
- Use Supabase Realtime for chat; if SLA/high volume, Liveblocks/Ably.
- Use Retool for admin instead of custom admin.
- Use Cloudflare for DNS, Sentry, Postmark.

Need maybe include "costs per 500 users and 5k users". Need define assumptions:
- 500 users first month: 500 registered, maybe 50 sellers, 100 conversations/day, 500 transactions.
- 5k users six months: 5k registered, 500 sellers, 1000 conversations/day, 5k transactions/month.
- For Stripe fees not counted infra but include percent.
- Costs approximate.

Need maybe include "Admin panel" implementation in recommended: Retool + Supabase Postgres. Retool may require self-host? Retool team. If budget, 1 user $10/mo? Current pricing? Retool starts $10/user/month (monthly) or $8 annual maybe. Supabase $25. Vercel Pro $20. Meili Cloud maybe $0-$50. Total $60-$100. For 5k maybe $100-$250. Need be accurate enough.

Need maybe include "tools budget $5k total infra+tools": At 6 weeks, even option B under $1k. Need mention reserve $2k for tooling/contingency. Stripe fees variable.

Need maybe include "security/compliance": use managed auth and payments, don't handle card data, use Stripe hosted checkout. Need maybe mention "marketplace payouts require KYC via Stripe Connect Onboarding".

Need maybe include "risks":
- Real-time chat with Supabase Realtime may need persistence and moderation; okay for MVP.
- Search in Postgres FTS with filters may be enough for niche; Meili better.
- Vendor lock-in; can migrate from Supabase Postgres to Neon/RDS later.
- Avoid building custom admin panel.

Need maybe include "why not Django/Laravel/Rails":
- Django has admin and auth batteries included, but React + DRF + Channels and websockets adds complexity; good if Python backend is must.
- Laravel/Filament fast but PHP unfamiliar, less aligned with team.
- Go backend overkill and slower.

Need maybe include "final recommendation: Option A". But maybe if they insist on Python, we can recommend "Option A variant: Next.js + Supabase, with Python only for scheduled jobs via Cloudflare Workers? Hmm".

Let's examine possible stacks in more detail.

Option 1: Next.js + Supabase (BaaS)
Architecture:
Frontend: Next.js 14/15 App Router + TypeScript + Tailwind/shadcn
Backend/data: Supabase Auth, Postgres, Storage, Realtime, Edge Functions maybe
Payments: Stripe Connect
Search: Postgres FTS initially; Meilisearch if needed
Admin: Retool or Next.js admin
Hosting: Vercel
Comms: Postmark/SendGrid
Monitoring: Sentry
Pros:
- Fastest to ship: auth/admin/DB/storage/realtime.
- Low ops: one person maintain.
- Good for 500/5000.
- Retool admin saves 1-2 weeks.
Cons:
- Vendor lock-in, realtime/search limitations, not ideal for complex domain logic, BaaS pricing.
- TypeScript learning curve if team only React JS.
Cost:
500 users: $50-$150/mo; 5k: $100-$300/mo. Tools include Stripe fees.
Need include $5k total possible.

Option 2: Next.js + FastAPI + PostgreSQL/Neon/RDS + Redis + Ably/Socket.io + Meili/Algolia + Retool
Architecture:
Frontend Next.js
Backend FastAPI
DB Neon/Supabase/Render/RDS
Redis Upstash/Upstash for rate limiting/queues
Realtime Ably/Liveblocks/Supabase Realtime
Search Meilisearch/Algolia
Admin Retool
Pros:
- More control, can use Python, clean API, easy to scale, less BaaS lock-in.
- Good if marketplace logic complex.
Cons:
- More services/deployment, more ops; WebSocket scaling; 6 weeks risk; one person maintain; need auth/session/JWT, rate limiting, queues, background workers.
Cost:
500: $100-$250/mo; 5k: $200-$500/mo.
Need maybe include specific:
Vercel Pro $20
FastAPI on Render/Railway $7-$25
Postgres Neon Pro $19 or RDS $20-$80
Redis Upstash $0-$25
Ably $0-$79
Meili $0-$50
Retool $15
Sentry $0-$26
Total $70-$225 (500), $150-$450 (50k). Good.

Option 3: Django + React + PostgreSQL + Channels + Algolia/Meili + Retool
Pros:
- Django admin built-in, auth, ORM, security, batteries; Python; DRF.
- Admin panel requirement satisfied; faster than custom.
Cons:
- Channels/WebSockets can be more complex; DRF auth; React integration; less "one framework" than Laravel; deployment more pieces.
- If use Django admin as admin panel, can be used by one person but styling not marketplace admin.
Cost:
500: $80-$200; 5k: $150-$400.
Option 4: Laravel + Filament + React/Livewire + MySQL/Postgres + Pusher/Reverb + Algolia/Meili
Pros:
- Extremely fast for marketplace admin/auth/payments; Filament admin; Livewire/Reverb reduces frontend complexity.
Cons:
- Team doesn't know PHP; less aligned; maintaining PHP stack by Python/React dev maybe costly; market ecosystem okay.
Cost:
500: $50-$150; 5k: $100-$300.
Need include at least 3, maybe include 4. Good.

Need maybe mention "Go" not recommended for MVP: not needed; increases complexity.

Need maybe include "Payment details: Stripe Connect". For marketplace, need split payments, marketplace holds? Need not overcomplicate.

Need maybe include "Admin panel options: Retool vs custom: Retool recommended. If strict no third-party admin, use Next.js admin with shadcn but costs dev time. For 6 weeks, Retool." Need maybe include "Retool may have data privacy concerns; if need self-host, Appsmith maybe." But okay.

Need maybe include "search: Use Postgres FTS for first launch if niche and small; add Meilisearch before 5k if filters. Could use Meili from day 1 to avoid migration; cost small." Good.

Need maybe include "Real-time chat: Use Supabase Realtime initially; if need high reliability, Liveblocks/Ably. For MVP, Supabase is enough." But in recommended Option A we can use Supabase Realtime. If using Liveblocks, cost maybe $0-$25. Which is better? Let's decide final recommended stack:

"Next.js + TypeScript + Tailwind/shadcn + Supabase + Stripe Connect + Meilisearch (or Postgres FTS initially) + Retool + Postmark + Sentry"

Would this be enough? It doesn't use Python. But user knows Python. Could say "Python se deja para tareas futuras o jobs; no lo uses como backend si la prioridad es 6 semanas." Or "si quieres conservar Python, usa Option B, but risk." The recommendation can justify using BaaS over Python due to timeline. Need maybe mention "No uses Go para MVP".

Need maybe include "If you absolutely require Python backend, choose Option B (Next.js + FastAPI + Neon/Upstash/Ably/Meili/Retool) but it's the second-best."

Need maybe include "Stack details":
- Frontend: Next.js 14/15 App Router, TypeScript, Tailwind, shadcn/ui.
- Backend: Supabase (Auth, Postgres, Storage, Realtime, Row Level Security)
- Payments: Stripe + Stripe Connect (Checkout + Payment Intents + webhooks + Connect onboarding)
- Search: Postgres full-text initially; Meilisearch when need relevance; use indexes on title/skills/tags/location.
- Admin: Retool or Appsmith (or Next admin if budget)
- Hosting: Vercel for frontend/edge functions; Supabase DB; Cloudflare DNS; Postmark for email; Sentry for errors.
- Background jobs: Supabase scheduled functions or Cron; later Temporal? No, keep simple.

Need maybe include "DB tables": users, profiles, services/listings, categories, bookings, payments, chat_messages, chat_conversations, reviews, admin logs. But not asked. Could include maybe not.

Need maybe include "Risks and mitigations":
- Auth: Supabase Auth.
- Security: RLS, Stripe webhooks, admin roles.
- Payments: use webhooks for state; don't trust frontend.
- Chat: moderation and blocking; store messages.
- Search: index fields; avoid expensive queries.
- Admin: Retool restrict to admin.
- Monitoring: Sentry, logs, health checks.

Need maybe include "estimated costs" table. Let's craft carefully.

Cost estimates:

For recommended Option A:
Monthly cost for 500 users:
- Vercel Hobby/Pro: $0-$20
- Supabase Pro: $25
- Meilisearch Cloud: $0-$50 (or $0 if Postgres FTS; $29 if Meili)
- Retool: $10-$15
- Postmark: $10-$15
- Sentry: $0
- Domain/email tools: $10-$20
- Stripe: 2.9%+30¢ + Connect 0.25%+30¢? Actually Stripe Connect standard charges: 2.9% + $0.30 charged to recipient + 0.25% + $0.05 platform fee (US). Maybe not exact. Include variable.
- Total infra+tools: ~$55-$120/mo (500 users), excluding Stripe fees.
For 5k users:
- Vercel Pro $20
- Supabase Pro $25 (maybe team if seats; still $25)
- Meilisearch $0-$50
- Retool $15
- Postmark $15
- Additional storage/egress maybe $20-$50
- Total ~$100-$250/mo.
Need maybe include if using Liveblocks instead of Supabase Realtime: +$0-$25. If Algolia instead of Meili: +$0-$150. Good.

For Option B:
- Vercel Pro $20
- FastAPI hosting $7-$25
- Neon/RDS $19-$80
- Redis/Upstash $0-$25
- Ably/Liveblocks $0-$79
- Meili/Algolia $0-$50
- Retool $15
- Sentry $0-$26
- Total 500: $70-$200; 5k: $150-$450.

Option C Django:
- Render/Railway/RDS $20-$100
- Redis $0-$25
- Channels (same app) $0-$25
- Meili/Algolia $0-$50
- Retool $15
- Sentry $0-$26
- Total 500: $60-$200; 5k: $120-$350.
Need maybe mention if self-host Postgres/Redis can lower.

Option D Laravel:
- Forge $20
- DO $12-$60
- DB managed maybe included? If RDS extra $15-$80
- Reverb self-host $0-$12 or Pusher $0-$79
- Algolia/Meili $0-$50
- Retool $15
- Total 500: $50-$150; 5k: $100-$300.
But team doesn't know PHP.

Need maybe include "total infra+tools over 6 weeks" maybe:
- Option A: $400-$1,000 for 6 weeks.
- Option B: $500-$1,500.
- Option C: $400-$1,200.
- Option D: $300-$900.
All under $5k, but Option A leaves buffer for Stripe? Stripe fees not infra. Tools maybe.

Need maybe mention "Budget $5k total includes infra+tools, not dev labor; if includes dev contractor, impossible for 6 weeks with marketplace features; but assumption excludes dev labor." Could include.

Need maybe include "When to choose other options":
- Choose Option B if you need Python backend and full control.
- Choose Django if Python backend and built-in admin are top priority.
- Choose Laravel only if willing to learn/maintain PHP.
- Choose Rails? Could include as fourth? But enough.

Need maybe include "decision matrix" with criteria:
- time to MVP
- maintenance burden
- fit with team
- cost
- scalability.
Use scores maybe:
A: 5/5, 5, 4, 5, 4
B: 4, 3, 5, 4, 5
C: 4, 4, 4, 4, 4
D: 5, 3, 2, 4, 4
Need maybe include.

Need maybe include "MVP scope in 6 weeks" maybe:
- Auth
- Listings & profiles
- Search/filter
- Booking/payment flow
- Chat
- Admin
- Reviews
- Emails
- Analytics
Need maybe include "defer: advanced ratings, subscriptions, multi-vendor payouts, mobile apps, complex search ranking, custom chat infrastructure".

Need maybe include "architecture diagram textual":
User -> Vercel Next.js -> Supabase Auth/Postgres/Storage/Realtime -> Stripe Connect -> Meili -> Retool.
Emails -> Postmark; errors -> Sentry.

Need maybe include "Why not custom chat with Socket.io": scaling websockets, sticky sessions, storage, moderation; managed provider saves time. But Option B includes Ably/Ably.

Need maybe include "Search plan":
- MVP: Postgres FTS + indexes + trigram extension (pg_trgm) for simple search.
- At 5k users: Meilisearch if need facets/filters/relevance.
Maybe in recommended Option A choose Postgres FTS initially to save cost. But "busqueda" requirement: Postgres FTS is search. If marketplace needs filters (category, price, location, rating) Postgres can handle. Use Meili only if needed. That reduces cost. But if recommend Option A with Meilisearch from day 1, more robust. Which is better? For one person and budget, Meili Cloud free? Actually Meilisearch Cloud has free? It may have "starter" $0? Not sure. Algolia free tier. Meili self-host on VPS $5 is easy. But managed is okay. Could say "start with Postgres FTS; budget Meili as optional upgrade." But product is marketplace; search quality matters. However niche MVP, Postgres FTS enough. If using Postgres FTS, no separate search service. Option A cost lower. But if "like Fiverr" search with filters/relevance might need more. Could include "Meilisearch optional; add in week 2 if search is core".

Need maybe include "payments: Stripe Connect" cost:
- For 500 users maybe 100 transactions/mo: 100*(2.9%+30c) = $5.90? plus Connect.
- For 5k users maybe 1,000 transactions: $59.
- Not infra but total cost.
Need maybe include.

Need maybe include "Admin panel: Retool can be used by internal team. If only one admin, $10/mo. If privacy concerns, build Next.js admin with shadcn but adds 1 week." Good.

Need maybe include "deployment and maintainability":
- Use IaC? For 6 weeks, no Terraform. Use managed services.
- Use Docker? Next.js serverless, Supabase.
- Use migrations via Supabase SQL/Prisma? Supabase doesn't use Prisma? Could use Supabase migrations. For FastAPI, Alembic.
- Use GitHub Actions.

Need maybe include "Data model / RLS" maybe not.

Need maybe include "Scalability to 5k":
- 5k users not high. Supabase/Neon/Vercel/Meili can handle. Real-time chat maybe 5k registered but concurrent lower. Use managed provider.
- If using Postgres FTS, indexes and partitioning maybe. At 5k, no issue.
- Add CDN, caching.

Need maybe include "Security":
- Use RLS in Supabase.
- Webhooks signatures.
- Admin roles in DB.
- Rate limits.
- PII minimal.
- Do not store card info.

Need maybe include "Recommendation with justifications":
- Best fit: Option A.
- Reason 1: fastest for 6 weeks (BaaS handles auth, DB, storage, realtime).
- Reason 2: low ops, one person maintain.
- Reason 3: costs under $5k and under $250/mo at 5k.
- Reason 4: can migrate core DB/API later.
- Reason 5: React aligned.

Need maybe include "If you insist on Python, choose Option B but reduce scope: no custom admin, no complex search, no custom WebSocket." Good.

Need maybe include "Final answer structure":
1. Executive summary.
2. Assumptions.
3. Comparison table.
4. Option details.
5. Recommendation.
6. Cost estimates.
7. 6-week implementation plan.
8. Final stack.

Need ensure Spanish. Use "stack" terms.

Let's think of exact table content.

Comparison table:
Columns: Stack, Cuándo conviene, Pros, Contras, Costo mensual aprox.
Rows:
1. BaaS-first: Next.js/TS + Supabase + Stripe Connect + Meili/Postgres FTS + Retool
2. Control/API: Next.js + FastAPI + Neon/RDS + Redis + Ably/Liveblocks + Meili + Retool
3. Python tradicional: Django/DRF + React + PostgreSQL + Channels + Algolia/Meili + Django admin/Retool
4. Laravel/Filament: Laravel + Filament + MySQL/Postgres + Livewire/Reverb + Algolia/Meili
Need maybe "opción 4" optional.

Pros/cons:
Option 1:
Pros:
- Auth, DB, storage, realtime, dashboard included.
- Fewest moving parts.
- Admin via Retool.
- Good for 500/5k.
- Costs low.
Cons:
- Vendor lock-in.
- Complex marketplace logic may outgrow Supabase.
- Realtime/search may need paid provider.
- Less Python.
Cost:
- 500: $50-$150; 5k: $100-$250.

Option 2:
Pros:
- Python backend, control, scalable, decoupled, can use Go later.
- Better for complex business logic.
Cons:
- More deployment/ops; WebSocket scaling; auth/JWT; queues; background jobs; 6-week risk.
Cost:
- 500: $100-$250; 5k: $200-$500.

Option 3:
Pros:
- Django admin built-in, security, batteries; Python; good for marketplace CRUD.
- Less custom admin.
Cons:
- Channels/websockets and DRF add complexity; React integration; still multiple services.
Cost:
- 500: $80-$220; 5k: $150-$400.

Option 4:
Pros:
- Laravel + Filament fastest for admin/auth; Livewire/Reverb simple.
Cons:
- Team doesn't know PHP; maintenance risk; less aligned.
Cost:
- 500: $50-$160; 5k: $100-$300.

Need maybe include "score" table:
Criteria:
- Velocidad 6 semanas: A 5, B 4, C 4, D 5
- Mantenimiento 1 persona: A 5, B 3, C 4, D 4
- Ajuste equipo: A 5, B 5, C 5, D 2
- Control/escalabilidad: A 4, B 5, C 4, D 4
- Costo: A 5, B 4, C 4, D 5
Total maybe. But not necessary. Could include.

Need maybe include "Costs for recommended stack table":
Line item:
- Vercel: $0 Hobby or $20 Pro
- Supabase: $25 Pro
- Meilisearch: $0 (Postgres FTS) to $50 Cloud; or $5 self-host
- Retool: $10-$15
- Postmark: $10-$15
- Sentry: $0
- Domain/DNS: $2-$5 (domain amortized; Cloudflare free)
- Stripe fees variable
Total 500: $50-$120/mo; 5k: $100-$250/mo.
Need maybe "si agregas Liveblocks/Ably: +$0-$80/mo" and "si usas Algolia: +$0-$150/mo".

Need maybe include "Budget $5k total":
- For 6 weeks, recommended stack will spend roughly $300-$1,500 (including 6 months? Wait 6 weeks monthly costs ~2 months; at $100/mo = $200; if 6 months at $200 = $1,200. Under $5k). Tools like Retool/Meili maybe. Stripe fees variable.
- If include 6 months of ops at 5k: $600-$1,500. Good.
Need maybe include "reserve for Stripe Connect fees: 3.2% approx + fixed fees; not included".

Need maybe include "Admin panel":
- Retool: fastest; if you need no external admin, build Next.js admin but add 1 week.
- Retool data connection to Supabase; restrict to admins; no need to maintain.

Need maybe include "Real-time chat":
- Supabase Realtime for MVP.
- Use Postgres tables for messages and RLS; persist messages.
- Add moderation/blocking.
- At higher scale, Liveblocks/Ably.

Need maybe include "Search":
- Start with Postgres FTS + pg_trgm for exact MVP; add Meili if needed.
- Index fields: title, description, tags, category, location, rating.
- Use filters: price, availability, rating, delivery time.
Need maybe include "If using Meili day 1, cost +$29".

Need maybe include "Payments":
- Stripe Connect: marketplace escrow? Actually "connect" handles payouts; not escrow. Need maybe mention "no escrow custom; use Stripe Connect with delayed payouts or platform payments depending compliance." For MVP, use Connect standard/express.
- Use webhooks to update order status.
- Do not store card data.

Need maybe include "Timeline 6 weeks" with tasks:
Week 1: scope, DB, UI, auth, Stripe Connect skeleton, admin base.
Week 2: profiles/listings/search, admin CRUD.
Week 3: booking flow, checkout, webhooks, email.
Week 4: chat, notifications, reviews.
Week 5: QA/security, analytics, performance, admin.
Week 6: beta, bug fixes, launch.
Need maybe include "MVP feature cut if delay: defer reviews? But reviews are important; maybe keep simple. Defer subscriptions, advanced analytics, mobile apps, custom payouts, AI."

Need maybe include "Potential hidden cost: Retool seats, Meili Cloud, Stripe Connect; domain; email." Good.

Need maybe include "Conclusion: choose Option A unless you require Python backend; if Python backend is non-negotiable, choose Option B."

Need maybe include "No Go" mention:
- Go not recommended for MVP; use only if you later need a performance service. It adds deployment and complexity.

Need maybe include "Scalability to 5,000 users":
- 5k monthly is modest. Managed services can handle.
- Need to monitor:
- DB indexes, query performance.
- WebSocket concurrency.
- Stripe webhook retries.
- Storage size.
- Retool usage.
- Could migrate from Supabase to Neon/RDS later.

Need maybe include "Alternative if product requires multi-vendor payouts with KYC: Stripe Connect is mandatory; if only simple marketplace take rate, Stripe Payments still okay but not marketplace." Good.

Need maybe include "Tools total budget includes not dev labor; if includes dev labor, $5k is too low." Could mention.

Need maybe include "Stack options maybe all use TypeScript? Option D maybe not. Good.

Need maybe include "Recommendation in one sentence":
"Recomiendo Opción 1: Next.js + Supabase + Stripe Connect + Meilisearch/Postgres FTS + Retool. Es la que maximiza velocidad y minimiza operaciones para un solo fullstack."

Need maybe include "Detailed recommended stack":
- Next.js 15 + TypeScript + Tailwind + shadcn/ui
- Supabase: Auth, Postgres, RLS, Storage, Realtime, Edge Functions/Cron
- Stripe Connect
- Search: Postgres FTS initially; Meilisearch optional
- Retool for admin
- Postmark + Resend? Choose Postmark.
- Sentry
- Vercel
- Cloudflare
Need maybe include "Why not use Django admin?" Because Retool faster and less UI maintenance; Django admin if Python backend.

Need maybe include "What to avoid":
- Building custom auth, chat, admin panel, payment integrations, search engine.
- Self-hosting Redis/Postgres/WebSockets for MVP.
- Monolith too large? Hmm.

Need maybe include "If using FastAPI, use PostgreSQL migrations Alembic, Celery/RQ? But not recommended." Could mention in Option B.

Need maybe include "No need for GraphQL; use REST/Supabase clients." Good.

Need maybe include "Data privacy: if regulated, check provider; otherwise no." Not necessary.

Need maybe include "Use Supabase Edge Functions for webhooks? Actually Stripe webhooks can call Supabase Edge Function or Next.js API route. If using Vercel serverless, handle Stripe webhooks in Next.js API route. But if using Supabase only, can use Edge Function. Recommend Next.js API route for Stripe webhooks? Since frontend is Next.js, using Vercel. It's okay. But if using Supabase Auth, Next.js