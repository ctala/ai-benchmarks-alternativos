# Qwen 3.5 397B (NIM) — business_audit/teardown_competidor_sin_inventar

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 3.45 | quality: 3.34
- latency_total: 145.984s | tokens_per_second: 14.0
- input_tokens: 193 | output_tokens: 2048

## Respuesta completa

Aquí tienes el teardown competitivo. He separado estrictamente los datos observables de las estimaciones calculadas, indicando siempre el nivel de certeza.

---

# 🕵️‍♂️ Teardown Competitivo: Comunidad de Automatización

## 1. Estimación de Facturación (Revenue)

### Lo que sabemos (Hechos)
*   **[HECHO] [Certeza: Alta]** Precio público: $39 USD/mes.
*   **[HECHO] [Certeza: Alta]** Contador público: 2.400 miembros.
*   **[HECHO] [Certeza: Alta]** No hay plan anual visible en la landing page.

### Lo que infiero (Cálculos)
*   **[INFERENCIA] [Certeza: Media]** **MRR Bruto Potencial:** Si los 2.400 miembros son activos y pagando, la facturación recurrente mensual es **$93.600 USD**.
    *   *Cálculo:* 2.400 * $39 = $93.600.
*   **[INFERENCIA] [Certeza: Baja]** **Tasa de "Miembros Reales":** En plataformas de membresía, el contador público a veces incluye usuarios en prueba gratuita, usuarios "freemium" o cuentas inactivas. Es raro que el 100% del contador sea revenue activo.
    *   *Escenario Conservador (50% pagando):* 1.200 usuarios * $39 = **$46.800 MRR**.
    *   *Escenario Optimista (80% pagando):* 1.920 usuarios * $39 = **$74.880 MRR**.
*   **[INFERENCIA] [Certeza: Media]** **Ingresos Anualizados (ARR):** Entre **$560k y $1.1M USD anuales**, asumiendo estabilidad en la base de usuarios.
*   **[INFERENCIA] [Certeza: Baja]** **Ingresos por Cursos Separados:** Si los 12 cursos se pueden comprar *fuera* de la membresía (tipo "à la carte"), la facturación real sería mayor. Asumo que están incluidos en el subscription por el modelo de comunidad, pero no es seguro.

---

## 2. Salud del Negocio

### Fortalezas (Señales Verdes)
*   **[HECHO] [Certeza: Alta]** **Autoridad del Fundador:** 60.000 seguidores es un activo de adquisición de clientes (Top of Funnel) muy sólido.