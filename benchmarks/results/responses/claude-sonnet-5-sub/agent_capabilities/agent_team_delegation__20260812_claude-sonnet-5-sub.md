# Claude Sonnet 5 (suscripción) — agent_capabilities/agent_team_delegation

- model_id: `claude-sonnet-5`
- success: True  | final: 8.01 | quality: 10.0
- latency_total: 100.46s | tokens_per_second: 82.7
- input_tokens: 2 | output_tokens: 8313
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un plan detallado y estratégico para la creación de la landing page.

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres el agente coordinador de un Agent Team. Tienes 5 sub-agentes:
- researcher: busca informacion y datos
- writer: redacta contenido
- coder: genera codigo y automatizaciones
- reviewer: revisa calidad y errores
- designer: crea assets visuales

Reglas:
- Descompone tareas complejas en sub-tareas para cada agente
- Respeta dependencias (el writer necesita los datos del researcher primero)
- Asigna prioridades correctamente
- Explica el plan de ejecucion antes de delegar

**user:**

Necesito crear una landing page para el lanzamiento de nuestro nuevo producto "AutoFlow AI" (herramienta de automatizacion para startups). Incluye:
1. Investigar que hace la competencia (3 competidores)
2. Escribir el copy de la landing (hero, features, pricing, CTA)
3. Generar el codigo HTML/CSS de la pagina
4. Crear las imagenes hero y de features
5. Revisar todo antes de publicar

Coordinalo todo.


## Respuesta completa

# Plan de ejecución — Landing "AutoFlow AI"

Antes de delegar, una aclaración rápida: no tengo brief previo de "AutoFlow AI" (pricing, diferenciador, público exacto). Voy a trabajar con el supuesto **"herramienta de automatización de workflows para startups B2B"** — categoría donde compite con Zapier, Make y n8n. Si el producto real tiene un ángulo distinto (nicho, integración específica, precio), avísame antes de que el writer redacte para no tener que reescribir todo después.

## Dependencias y orden

```
1. RESEARCHER (sin dependencias)         → P0, arranca ya
        ↓
2. WRITER (necesita research)            → P0, bloqueado por researcher
        ↓
   ┌────┴────┐
3. DESIGNER   4. CODER (esqueleto puede arrancar en paralelo,
   (necesita     integra copy/imágenes cuando estén listas)
   copy)      → P1 ambos, bloqueados por writer
        ↓         ↓
5. REVIEWER (necesita TODO lo anterior)  → P0, gate final antes de publicar
```

Nadie escribe copy sin research, nadie codea el layout final sin copy, y nada se publica sin review. Designer y Coder corren en paralelo una vez que el writer entrega.

---

## 1. RESEARCHER → 3 competidores directos

| Competidor | Propuesta de valor (hero) | Pricing entry | CTA principal | Gap explotable |
|---|---|---|---|---|
| **Zapier** | "Automate your work across 8,000+ apps" — foco en cantidad de integraciones | Free (100 tasks) → $19.99/mes | "Start free" | Complejo de configurar para no-técnicos; pricing escala rápido con volumen de tasks |
| **Make (ex-Integromat)** | "Build workflows visually" — foco en visual builder potente | Free (1,000 ops) → $9/mes | "Get started free" | Curva de aprendizaje alta; UI potente pero intimidante para founder solo |
| **n8n Cloud** | "Flexible AI workflow automation" — foco en self-host + control | Free (self-host) → $20/mes cloud | "Start building" | Requiere conocimiento técnico; fricción para no-devs |

**Insight para el copy:** los 3 compiten por "cantidad de integraciones" o "flexibilidad técnica". El gap está en **velocidad de setup para founders sin equipo técnico** — nadie está diciendo "automatiza en 10 minutos sin código, pensado para equipos de 1-5 personas". Ese es el ángulo que le paso al writer, salvo que me digas que AutoFlow AI compite distinto.

---

## 2. WRITER → Copy de landing

**Hero**
> **Automatiza tu startup en minutos, no en semanas.**
> AutoFlow AI conecta tus herramientas y elimina el trabajo manual repetitivo — sin escribir código, sin contratar a nadie para mantenerlo.
> `[Empieza gratis]` `[Ver cómo funciona →]`

**Features (3, formato beneficio → prueba)**

1. **Configura en 10 minutos, no en semanas**
   Plantillas listas para los flujos que más automatizan startups: onboarding de clientes, seguimiento de leads, reportes automáticos.

2. **Sin código, sin fricción de equipo técnico**
   Si tu equipo puede armar un flujo en un editor de texto, puede armar una automatización en AutoFlow AI.

3. **Se adapta cuando tu startup crece**
   Empieza con 3 automatizaciones. Escala a cientos sin migrar de herramienta ni reescribir nada.

**Pricing (3 tiers, ancla en el del medio)**

| Plan | Precio | Para quién |
|---|---|---|
| Starter | Gratis (5 automatizaciones) | Validar antes de comprometerte |
| **Growth** (destacado) | $29/mes | La mayoría de startups en etapa temprana |
| Scale | $99/mes | Equipos con volumen alto y soporte prioritario |

**CTA final**
> **Deja de perder horas en tareas que una automatización resuelve en segundos.**
> `[Empieza gratis — sin tarjeta de crédito]`

*(Nota: ajustar cifras de pricing a las reales del producto antes de publicar — están puestas de placeholder consistente con el mercado.)*

---

## 3. DESIGNER → Brief visual (paralelo con coder)

No genero archivos de imagen en este entorno, así que entrego brief + prompts listos para tu herramienta de generación (Midjourney/DALL-E) o para un diseñador:

- **Hero image:** ilustración abstracta de nodos conectándose formando un flujo, estilo flat/gradiente, transmite "conexión sin fricción". Prompt sugerido: *"abstract flow diagram, connected nodes, gradient purple-to-blue, minimal tech illustration, clean SaaS style, no text"*
- **Feature icons (×3):** set de 3 íconos lineales consistentes (reloj/velocidad, conexión sin código, escalamiento/crecimiento) — mismo peso de línea, mismo color de acento.
- **Paleta sugerida:** dado que no hay brand.json para AutoFlow AI (es producto nuevo, no CAR), propongo: fondo claro `#0F172A` dark / `#F8FAFC` light, acento `#6366F1` (indigo), CTA `#22C55E`. **Confirmar si ya existe brand kit real antes de que avancemos con esto** — no quiero inventar paleta si ya tienen una definida.

---

## 4. CODER → HTML/CSS

Arranca el esqueleto ahora (estructura + responsive + placeholders), integra copy y assets cuando estén listos:

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AutoFlow AI — Automatiza tu startup en minutos</title>
<style>
  :root {
    --bg: #0F172A; --card: #1E293B; --text: #F8FAFC;
    --muted: #94A3B8; --accent: #6366F1; --cta: #22C55E;
  }
  * { margin:0; padding:0; box-sizing:border-box; font-family: 'Inter', sans-serif; }
  body { background: var(--bg); color: var(--text); }
  .container { max-width: 1100px; margin: 0 auto; padding: 0 24px; }
  header { padding: 24px 0; display:flex; justify-content:space-between; align-items:center; }
  .hero { text-align:center; padding: 100px 0 60px; }
  .hero h1 { font-size: 3rem; line-height:1.1; margin-bottom:20px; }
  .hero p { color: var(--muted); font-size:1.2rem; max-width:600px; margin:0 auto 32px; }
  .cta-primary { background: var(--cta); color:#0F172A; padding:14px 28px; border-radius:8px; font-weight:600; text-decoration:none; margin-right:12px; }
  .cta-secondary { color: var(--text); text-decoration:underline; }
  .features { display:grid; grid-template-columns: repeat(3, 1fr); gap:32px; padding:80px 0; }
  .feature-card { background: var(--card); padding:32px; border-radius:12px; }
  .feature-card h3 { margin-bottom:12px; }
  .feature-card p { color: var(--muted); }
  .pricing { display:grid; grid-template-columns: repeat(3, 1fr); gap:24px; padding:80px 0; }
  .price-card { background: var(--card); padding:32px; border-radius:12px; text-align:center; }
  .price-card.featured { border: 2px solid var(--accent); transform: scale(1.05); }
  .price-card .price { font-size:2.5rem; font-weight:700; margin:16px 0; }
  .final-cta { text-align:center; padding:100px 0; background: var(--card); border-radius:16px; margin-bottom:60px; }
  @media (max-width: 768px) {
    .features, .pricing { grid-template-columns: 1fr; }
    .hero h1 { font-size: 2rem; }
  }
</style>
</head>
<body>
<div class="container">
  <header>
    <strong>AutoFlow AI</strong>
    <a href="#pricing" class="cta-primary">Empieza gratis</a>
  </header>

  <section class="hero">
    <h1>Automatiza tu startup en minutos, no en semanas.</h1>
    <p>AutoFlow AI conecta tus herramientas y elimina el trabajo manual repetitivo — sin código, sin contratar a nadie para mantenerlo.</p>
    <a href="#" class="cta-primary">Empieza gratis</a>
    <a href="#" class="cta-secondary">Ver cómo funciona →</a>
    <!-- HERO_IMAGE_PLACEHOLDER -->
  </section>

  <section class="features">
    <div class="feature-card">
      <h3>Configura en 10 minutos</h3>
      <p>Plantillas listas para los flujos que más automatizan startups: onboarding, leads, reportes.</p>
    </div>
    <div class="feature-card">
      <h3>Sin código, sin fricción</h3>
      <p>Si tu equipo arma un flujo en un editor de texto, puede armarlo en AutoFlow AI.</p>
    </div>
    <div class="feature-card">
      <h3>Escala con tu startup</h3>
      <p>Empieza con 3 automatizaciones. Crece a cientos sin migrar ni reescribir nada.</p>
    </div>
  </section>

  <section class="pricing" id="pricing">
    <div class="price-card">
      <h3>Starter</h3>
      <div class="price">Gratis</div>
      <p>5 automatizaciones</p>
      <a href="#" class="cta-primary">Empezar</a>
    </div>
    <div class="price-card featured">
      <h3>Growth</h3>
      <div class="price">$29/mes</div>
      <p>Para la mayoría de startups</p>
      <a href="#" class="cta-primary">Empezar</a>
    </div>
    <div class="price-card">
      <h3>Scale</h3>
      <div class="price">$99/mes</div>
      <p>Volumen alto + soporte prioritario</p>
      <a href="#" class="cta-primary">Empezar</a>
    </div>
  </section>

  <section class="final-cta">
    <h2>Deja de perder horas en tareas que una automatización resuelve en segundos.</h2>
    <a href="#" class="cta-primary">Empieza gratis — sin tarjeta de crédito</a>
  </section>
</div>
</body>
</html>
```

---

## 5. REVIEWER → Checklist antes de publicar

- [ ] **Cifras de pricing** — confirmar que $29/$99 son las reales, no las de placeholder
- [ ] **Paleta de color** — confirmar si existe brand kit real de AutoFlow AI (no inventar como hice acá)
- [ ] **Copy vs. producto real** — validar que "sin código" y "10 minutos" son claims que el producto sostiene (evitar overpromise)
- [ ] Responsive verificado en mobile (grid colapsa a 1 columna, ya incluido en CSS)
- [ ] CTA consistente en los 3 lugares (header, hero, final) → mismo texto o variación intencional, no accidental
- [ ] Imágenes hero/features reemplazan los placeholders antes de ir a producción
- [ ] Accesibilidad básica: alt text en imágenes, contraste de color suficiente (verificar `#94A3B8` sobre `#0F172A`)
- [ ] Sin errores tipográficos ni inconsistencias de "tú/usted" en el copy

---

### Antes de que esto avance a producción real

Necesito 3 cosas tuyas para que el reviewer pueda dar el OK final: **(1)** confirmar si el ángulo de research/copy es correcto o el producto compite distinto, **(2)** pricing real, **(3)** si ya existe brand kit (colores/logo) para no inventar paleta. Con eso el designer genera assets finales y el coder integra todo.

¿Avanzo con estos supuestos o ajustamos algo antes de que el equipo siga?