# Kimi K3 — sales_outreach/lead_qualification

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 7.93 | quality: 10.0
- latency_total: 76.17s | tokens_per_second: 23.4
- input_tokens: 363 | output_tokens: 1781
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una evaluación detallada y acciones específicas para cada lead.

## Respuesta completa

```json
[
  {
    "lead": "Juan Perez - CEO, startup 5 personas",
    "score": 4,
    "bant": {
      "budget": "Desconocido. No mencionó presupuesto y una startup de 5 personas suele tener recursos limitados.",
      "authority": "Alta. Es CEO, decision maker total.",
      "need": "Media. Dice 'estamos viendo opciones', lo que indica interés pero en etapa exploratoria. Con 5 personas, el volumen de soporte puede no justificar aún la automatización.",
      "timeline": "Bajo. Sin urgencia ni fecha definida."
    },
    "action": "Nurture: incluir en secuencia automatizada de contenido educativo y casos de uso. Re-evaluar si muestra señales de compra (visita página de precios, responde emails, pide demo).",
    "reason": "Tiene autoridad pero está en fase exploratoria, sin presupuesto ni timeline. Empresa muy pequeña con fit incierto. No amerita tiempo del equipo de ventas todavía."
  },
  {
    "lead": "Ana Gomez - VP of Operations, empresa 200 empleados",
    "score": 9,
    "bant": {
      "budget": "Alto. Acaban de levantar Serie B, hay capital disponible para invertir en herramientas.",
      "authority": "Alta. VP of Operations es decision maker o sponsor directo para herramientas de su área.",
      "need": "Alta. Pidió demo proactivamente después del webinar: interés concreto, no exploratorio.",
      "timeline": "Alto y explícito: 'necesitamos resolver esto antes de Q3'. Urgencia clara con deadline."
    },
    "action": "Caliente: asignar a Account Executive de inmediato, contactar en menos de 24h para agendar demo y preparar propuesta alineada al deadline de Q3.",
    "reason": "Cumple los 4 criterios BANT con fuerza: presupuesto (Serie B), autoridad (VP), necesidad activa (pidió demo) y urgencia (deadline explícito). Lead prioritario."
  },
  {
    "lead": "Carlos Ruiz - Intern de marketing",
    "score": 2,
    "bant": {
      "budget": "Desconocido. Solo pide PDF de precios, sin señales de presupuesto asignado.",
      "authority": "Nula. Es intern, no decide ni influye significativamente.",
      "need": "Baja. 'Investigar herramientas de IA' es una tarea delegada y exploratoria, sin problema definido.",
      "timeline": "Ninguno. Sin fecha ni urgencia."
    },
    "action": "Enviar el PDF de precios (acción de bajo costo) y aprovechar para preguntar quién lidera la decisión: '¿Con quién de tu equipo podemos agendar 15 min para entender mejor el caso?'. Si logra intro con su jefe, re-calificar. Mientras tanto, nurture automatizado.",
    "reason": "Sin autoridad, sin timeline y necesidad difusa. Hay un posible decision maker detrás (su jefe), pero sin acceso a él el lead tiene poco valor inmediato. No invertir tiempo de ventas."
  }
]
```

**Resumen de priorización:**
1. 🔥 **Ana Gomez (9)** — Contactar hoy. Es la oportunidad real.
2. 🌱 **Juan Perez (4)** — Automatizar nurturing, sin esfuerzo manual.
3. 📄 **Carlos Ruiz (2)** — Responder lo mínimo y usarlo como puente hacia el decision maker.