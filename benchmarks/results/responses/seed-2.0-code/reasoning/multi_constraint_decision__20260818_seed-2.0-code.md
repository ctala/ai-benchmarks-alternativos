# Seed 2.0 Code — reasoning/multi_constraint_decision

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 7.4 | quality: 8.4
- latency_total: 39.08s | tokens_per_second: 52.4
- input_tokens: 217 | output_tokens: 2048
- judge_score: 4.0 | justificación: 

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


El usuario necesita un análisis de 3 stacks tecnológicos para un MVP de marketplace freelance nicho, con restricciones claras: presupuesto total $5k, 6 semanas, 1 dev (React, Python, Go básico), requisitos específicos, escala baja inicial, mantenimiento fácil.

Primero, voy a identificar 3 stacks que se adapten a sus habilidades y restricciones. No puede ser algo muy complejo, ni herramientas caras.

Primer stack: **React (Next.js App Router) + Python (FastAPI) + Servicios gestionados low-code**. Porque el dev sabe React y Python, esto es natural. Aquí usar servicios gestionados para reducir trabajo: Supabase para auth, BD (PostgreSQL), almacenamiento? Wait, o mejor Supabase + Stripe Connect (para pagos de marketplace) + Pusher (chat) o Supabase Realtime? Wait, Supabase tiene Realtime, así que no necesitamos Pusher. Admin panel: Next.js Admin Dashboard con Supabase o Directus? Wait, Directus es headless CMS/Admin panel, pero si usamos Supabase, su propio Studio es admin, pero tal vez un panel personalizado en Next.js o usar Retool? Pero Retool tiene plan free. Wait, costos: hay que calcular infra mensual y total dentro de $5k.

Segundo stack: **React (Vite) + Python (Django REST Framework) + Servicios gestionados básicos**. Django tiene más out-of-the-box (admin panel incluido, auth), lo que acelera desarrollo. Pero Django es más monolítico? Wait, DRF para API. Infra: Railway o Render para backend, Vercel para frontend. BD: PostgreSQL en Supabase o Railway. Pagos: Stripe Connect. Chat: Django Channels? Pero Channels requiere Redis, o mejor usar Supabase Realtime también aquí, para no gestionar Channels. Wait, el dev sabe Python, Django es más rápido para auth y admin.

Tercer stack: **React (Next.js) + Go (Fiber) + Servicios gestionados low-code**. Aquí aprovechar el Go básico del dev, pero Go es más performante pero tiene menos librerías out-of-the-box. Pero tal vez para escala posterior, pero el dev solo tiene básico, así que este stack es más arriesgado pero lo incluyo para comparar. Servicios: Supabase para auth, BD, chat (realtime), Stripe Connect, etc.

Ahora, tengo que estructurar cada stack con:
- Componentes técnicos detallados (frontend, backend, BD, auth, pagos, chat, búsqueda, admin panel)
- Pros (adaptados a restricciones: velocidad de desarrollo, habilidades del dev, costo, mantenimiento)
- Contras
- Costos estimados MENSALES (y total en 6 semanas, para ver si entra en $5k)
- Adaptación a escala (500 -> 5k usuarios)

Luego, recomendar uno con justificación.

Primero, voy a definir los REQUISITOS TÉCNICOS A CUBRIR en cada stack:
1. Auth: registro/inicio de sesión, roles (freelancer, cliente, admin)
2. Pagos: marketplace, es decir, split de pagos (cliente paga, plataforma se queda comisión, freelancer recibe el resto) → STIPE CONNECT es imprescindible, porque no hay herramientas low-code más baratas para split. Stripe tiene tarifas por transacción, no mensuales (o plan free para pruebas, luego tarifas por transacción: 2.9% + $0.30 por transacción, más comisión de Connect: 0.25% + $0.25 por transacción). Pero en el presupuesto de $5k, las transacciones iniciales serán bajas, así que Stripe no afecta mucho el presupuesto mensual fijo.

3. Chat en tiempo real: entre cliente y freelancer, mensajes, archivos?
4. Búsqueda: búsqueda de servicios freelance por nicho, filtros (precio, calificación, ubicación si es necesario)
5. Admin panel: gestión de usuarios, servicios, pagos, reportes
6. Infra: alojamiento frontend, backend, BD, almacenamiento (para fotos de perfil, servicios)

Ahora, los 3 STACKS:

---
STACK 1: **NEXT.JS + FASTAPI (PYTHON) + SUPABASE + STRIPE CONNECT**
(Stack "Híbrido Low-Code/Dev", adaptado a sus habilidades React + Python)
Componentes detallados:
- Frontend: Next.js App Router (React, lo sabe) → Vercel Free/Hobby para alojamiento (o Netlify, pero Vercel es mejor para Next.js)
- Backend: FastAPI (Python, lo sabe) → Alojado en **Render** (plan Hobby $7/mes o Starter $25/mes, según escala)
- BD: Supabase PostgreSQL (gestionado, tiene auth, realtime, almacenamiento) → Plan Free (hasta 500MB BD, 2GB almacenamiento, 50k MAU) o Pro ($25/mes, escalable)
- Auth: Supabase Auth (gestiona registro/inicio de sesión, roles con RLS (Row Level Security) → sin código propio para auth básico, solo configuración)
- Pagos: Stripe Connect (split de pagos, tarjeta, PayPal) → Sin costo fijo, tarifas por transacción (2.9% + $0.30 por transacción + 0.25% + $0.25 por transacción Connect = ~3.15% + $0.55 por transacción)
- Chat en tiempo real: Supabase Realtime + RLS → No necesitamos backend propio para chat, solo configurar canales en Supabase, y usar el SDK en Next.js/FastAPI. Opcionalmente, agregar almacenamiento de archivos en Supabase Storage.
- Búsqueda: Supabase PostgreSQL con índices full-text search (para nicho, suficiente) o agregar **Algolia Free Plan** (10k registros, 100k búsquedas/mes) si necesitas más rendimiento.
- Admin Panel: Supabase Studio (herramienta nativa, acceso a BD, usuarios, realtime) + Panel personalizado pequeño en Next.js (solo para acciones específicas, como ver reportes de pagos) o **Retool Free Plan** (5 usuarios, 10 apps) para paneles sin código.
- Almacenamiento: Supabase Storage (fotos de perfil, servicios) → incluido en plan Free/Pro.

PROS:
1. Velocidad de desarrollo: Supabase cubre auth, BD, realtime, almacenamiento SIN código propio (solo configuración), lo que ahorra semanas de trabajo (ideal para 6 semanas).
2. Habilidades del dev: Usa React (Next.js) y Python (FastAPI), lo que ya domina → no curva de aprendizaje.
3. Costo bajo: La mayoría de herramientas tienen plan free para MVP, y planes pagos muy baratos para escala inicial.
4. Mantenimiento fácil: Servicios gestionados (Supabase, Render, Vercel) no requieren gestión de servidores, parches, backups → solo mantenimiento de código frontend/backend.
5. Escalable: Supabase Pro escala automáticamente, Render tiene planes de escalado, Next.js en Vercel escala sin esfuerzo.
6. Chat sin código: Supabase Realtime se configura en 10 minutos, sin necesidad de gestionar WebSockets propios.

CONTRAS:
1. Dependencia de Supabase: Si Supabase tiene fallos, el servicio se cae (pero tienen SLA en Pro, 99.9%).
2. FastAPI no tiene admin panel out-of-the-box: Pero Supabase Studio lo cubre, o Retool.
3. Búsqueda full-text en PostgreSQL es limitada para nichos muy complejos: Pero Algolia Free lo soluciona sin costo.

COSTOS ESTIMADOS MENSUALES (MVP):
- Vercel (Frontend): Plan Hobby **$0/mes** (hasta 100k visitas/mes, 500k ejecuciones de función)
- Render (Backend FastAPI): Plan Hobby **$7/mes** (1 instancia, 512MB RAM, 1GB almacenamiento) → si hay tráfico inicial, subir a Starter $25/mes, pero para MVP Hobby es suficiente.
- Supabase (BD, Auth, Realtime, Storage): Plan Free **$0/mes** (hasta 500MB BD, 2GB Storage, 50k MAU) → si pasan los 50k MAU, pasar a Pro $25/mes.
- Algolia (Búsqueda, si se usa): Plan Free **$0/mes** (10k registros, 100k búsquedas)
- Retool (Admin Panel, si se usa): Plan Free **$0