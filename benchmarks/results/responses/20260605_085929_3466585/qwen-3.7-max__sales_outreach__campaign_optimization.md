# Qwen 3.7 Max — sales_outreach/campaign_optimization

- model_id: `qwen/qwen3.7-max`
- success: True  | final: 7.42 | quality: 9.72
- latency_total: 67.751s | tokens_per_second: 64.3
- input_tokens: 309 | output_tokens: 4356
- judge_score: 4.8 | justificación: 

## Respuesta completa

🚨 **ALERTA CRÍTICA ANTES DE EMPEZAR:** 
Mencionas que tu presupuesto total es de **$5,000/mes**, pero la suma de los costos de tus campañas el mes pasado fue de **$7,100** ($2,100 + $1,800 + $3,200). **Tuviste un sobregasto del 42%.** Lo primero que debes hacer hoy es configurar límites de presupuesto diarios estrictos o un presupuesto compartido en la cuenta para que Google no vuelva a exceder tu tope de $5,000.

Dicho esto, aquí tienes el análisis estratégico de tu cuenta:

---

### 1. Métricas Clave por Campaña

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
| :--- | :--- | :--- | :--- |
| **CTR** | 3.0% | 4.0% | **6.0%** |
| **CPC** | $1.40 | **$0.38** | $3.56 |
| **CVR (Tasa de Conversión)**| 3.0% | 0.5% | **4.0%** |
| **CPA (Costo por Signup)** | **$46.67** | $75.00 | $88.89 |

---

### 2. ¿Cuál escalar y cuál pausar? (Justificación)

🟢 **ESCALAR: Campaña A (Landing principal)**
*   **Por qué:** Es tu campaña más rentable y eficiente. Tiene el **CPA más bajo ($46.67)** y un CPC muy razonable ($1.40). Las keywords ("software", "pymes") indican una intención de compra media-alta (MOFU/BOFU). Estás captando usuarios que ya saben que necesitan un software.

🔴 **PAUSAR / REESTRUCTURAR: Campaña B (Blog content)**
*   **Por qué:** Está "quemando" presupuesto. Aunque tiene el CPC más barato ($0.38) y buen CTR (4%), su **CVR es pésimo (0.5%)** y su CPA es alto ($75). 
*   **El problema de fondo:** Las keywords ("como gestionar", "problemas") son informacionales (Top of Funnel). El usuario quiere leer un artículo, no registrarse en un software. Estás pidiendo matrimonio en la primera cita. *No la pauses del todo si la usas para crear audiencias de remarketing, pero sí pausa la puja por "Signups" directos.*

🟡 **MANTENER CON CAUTELA (Optimizar): Campaña C (Competidor)**
*   **Por qué:** Tiene la mejor intención de compra (el usuario ya usa a tu rival y busca cambiar). Esto se refleja en el **mejor CTR (6%) y CVR (4%)**. Sin embargo, el **CPC es carísimo ($3.56)** y el CPA es el más alto ($88.89). Las campañas de competidor suelen ser guerras de pujas. Debes mantenerla porque trae clientes muy cualificados, pero debes poner un tope de puja (tCPA) para que no se coma tu presupuesto.

---

### 3. Redistribución del Presupuesto ($5,000)

El objetivo es alimentar lo que funciona, limitar lo que es caro y cambiar la estrategia de lo que es informacional.

*   **Campaña A (Landing): $3,000 (60%)**
    *   *Acción:* Escalar presupuesto. Al tener el CPA más bajo, inyectar más dinero aquí debería traerte más signups a un costo eficiente. Vigila que el CPA no suba al escalar.
*   **Campaña C (Competidor): $1,500 (30%)**
    *   *Acción:* Limitar. Con $1,500 y un CPC de ~$3.50, obtendrás unos 420 clicks. Si mantienes el CVR del 4%, lograrás unos 16 signups. Es caro, pero son clientes robados a la competencia. Configura una estrategia de pujas **tCPA (CPA Objetivo)** a $70 para forzar a Google a buscar conversiones más baratas.
*   **Campaña B (Blog): $500 (10%)**
    *   *Acción:* Cambiar el objetivo. Deja de pedir "Signups" de prueba. Usa este tráfico barato para ofrecer un **Lead Magnet** (ej. "Descarga nuestra plantilla Excel de inventario gratis"). Esos $500 te darán miles de leads baratos que luego nutrirás por Email Marketing hasta que estén listos para el signup.

---

### 4. A/B Tests sugeridos para el próximo mes

**Para la Campaña A (El motor de ingresos):**
1.  **Landing Page (Formulario vs. Demo):** Prueba si un formulario de registro directo (Signup) convierte mejor que un botón que ofrezca un "Tour guiado / Demo en video" de 2 minutos.
2.  **Anuncios (Beneficio vs. Característica):** 
    *   *Anuncio A:* "Reduce las mermas de tu inventario un 30%." (Beneficio/Dolor).
    *   *Anuncio B:* "Software de inventario en la nube con escáner de código de barras." (Característica).

**Para la Campaña B (Tráfico frío / Blog):**
1.  **El Gancho (Lead Magnet):** Ya que no compran directo, testea qué recurso descargan más: 
    *   *Opción A:* "Plantilla de Excel para control de inventario".
    *   *Opción B:* "Checklist: 10 errores que hacen que pierdas dinero en tu restaurante".
2.  **Ubicación del CTA:** Testea si convierte mejor un banner dentro del artículo del blog o un *Pop-up* de salida (Exit-intent) cuando el usuario intenta cerrar la pestaña.

**Para la Campaña C (Ataque a competidor):**
1.  **Landing Page "Nosotros vs. Ellos":** No mandes este tráfico a tu Home. Crea una Landing específica con una tabla comparativa donde tu software gane en 3 aspectos clave (ej. Precio, Soporte en español, Facilidad de uso).
2.  **Copy del Anuncio (Incentivo de cambio):** 
    *   *Test:* "¿Cansado de [Competidor]? Migra a nosotros en 24h y te damos 2 meses gratis". (El costo de dar 2 meses gratis es menor que tu CPA actual de $88, y aumentará drásticamente tu CVR).