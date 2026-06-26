# Claude Fable 5 (suscripción) — agent_capabilities/agent_team_delegation

- model_id: `claude-fable-5`
- success: True  | final: 7.42 | quality: 10.0
- latency_total: 27.032s | tokens_per_second: 68.3
- input_tokens: 2 | output_tokens: 1847

## Respuesta completa

# Plan de ejecución — Landing "AutoFlow AI"

## Análisis de dependencias

```
researcher (1) ──→ writer (2) ──→ coder (3) ──┐
                       │                       ├──→ reviewer (5)
                       └──→ designer (4) ──────┘
```

- El **writer** no puede redactar copy diferenciado sin saber qué dice la competencia → depende del researcher.
- El **coder** necesita el copy final para estructurar el HTML (secciones, jerarquía, longitudes reales de texto) → depende del writer.
- El **designer** necesita el copy del hero y features para que las imágenes refuercen el mensaje (no genéricas) → depende del writer. Puede correr **en paralelo con el coder**.
- El **reviewer** va al final: necesita copy + código + assets integrados.

Ruta crítica: researcher → writer → coder → reviewer. El designer trabaja en paralelo a la fase 3, así no agrega tiempo.

---

## Delegaciones

### Fase 1 — researcher (prioridad ALTA, bloquea todo)
**Tarea:** Análisis competitivo de 3 herramientas de automatización para startups (sugeridos: Zapier, Make, n8n — ajustar si AutoFlow compite en otro nicho).
**Entregable:**
- Propuesta de valor y mensaje del hero de cada uno
- Estructura de pricing (tiers, precio de entrada, qué gatea cada plan)
- Features que destacan above-the-fold
- Gaps/quejas comunes de usuarios (ángulo de diferenciación para AutoFlow)

### Fase 2 — writer (prioridad ALTA, espera Fase 1)
**Tarea:** Copy completo de la landing usando el informe del researcher.
**Entregable:**
- **Hero:** headline + subheadline + CTA primario (atacar el gap detectado, no repetir lo que ya dicen los 3 competidores)
- **Features:** 4-6 bloques, beneficio antes que funcionalidad
- **Pricing:** 3 tiers con copy por plan, posicionado contra el pricing de la competencia
- **CTA final:** cierre con urgencia de lanzamiento
- Español neutro, cifras concretas, sin localismos.

### Fase 3a — coder (prioridad ALTA, espera Fase 2)
**Tarea:** Landing en HTML/CSS estático, single file o estructura mínima.
**Specs:**
- Mobile-first, responsive
- Cero dependencias JS innecesarias (performance = conversión)
- Placeholders con dimensiones exactas para los assets del designer (hero 1920×1080, features 800×600)
- Meta tags OG + título SEO incluidos

### Fase 3b — designer (prioridad MEDIA, en paralelo con 3a, espera Fase 2)
**Tarea:**
- 1 imagen hero alineada al headline (concepto: automatización/flujo, no stock genérico)
- 4-6 ilustraciones de features, estilo consistente
- Paleta y formato coordinados con el coder (entregar en WebP optimizado)

### Fase 4 — reviewer (prioridad ALTA, espera 3a + 3b)
**Checklist de revisión:**
- Copy: claims verificables, sin errores, consistencia de tono
- Código: HTML válido, responsive en 3 breakpoints, Lighthouse >90, links del CTA funcionando
- Visual: assets integrados sin distorsión, contraste accesible (WCAG AA)
- Coherencia copy↔imagen↔pricing entre secciones
**Entregable:** informe go/no-go con fixes bloqueantes vs. nice-to-have.

---

## Puntos de control contigo

1. **Tras Fase 1:** te muestro el ángulo de diferenciación elegido antes de escribir copy (es la decisión más cara de revertir).
2. **Tras Fase 2:** apruebas el copy antes de invertir en código + assets.
3. **Tras Fase 4:** revisión final → **nada se publica sin tu "ok" explícito.**

---

**Antes de lanzar la Fase 1, necesito 3 datos que afectan todo el pipeline:**

1. ¿Quiénes son los competidores reales de AutoFlow AI? (¿compite con Zapier/Make/n8n, o es otro nicho?)
2. ¿Tienes pricing definido o el writer lo propone basado en el research?
3. ¿Hay brand existente (colores, logo, tipografía) o el designer define la identidad visual desde cero?

Si no respondes, arranco con los supuestos indicados (Zapier/Make/n8n, pricing propuesto por research, identidad nueva). ¿Procedo?