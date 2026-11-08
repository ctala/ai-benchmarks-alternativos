# Grok 4.7 — presentation/slide_outline

- model_id: `x-ai/grok-4.7`
- success: True  | final: 7.97 | quality: 9.5
- latency_total: 46.974s | tokens_per_second: 50.2
- input_tokens: 1367 | output_tokens: 2360
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando un esquema detallado y bien estructurado para una presentación ejecutiva, con sugerencias de visualización y notas del presentador.

## Entrada exacta (lo que recibió el modelo)

**user:**

Crea el outline completo para una presentacion de 15 slides sobre el estado del proyecto "Plataforma Digital 2.0". La audiencia es el board de directores. Incluye para cada slide:
- Numero y titulo
- Bullet points del contenido (3-5 por slide)
- Tipo de visual sugerido (grafico, tabla, diagrama, imagen)
- Notas del presentador (1-2 oraciones)

La presentacion debe cubrir: estado actual, metricas de progreso, riesgos, presupuesto ejecutado vs planeado, roadmap Q2-Q3, y asks al board.


## Respuesta completa

Outline de 15 slides para el board. Las cifras son ilustrativas: sustitúyalas por los datos reales del PMO antes de presentar.

**1. Plataforma Digital 2.0 — Estado del proyecto**
- Programa de transformación digital: alcance, sponsor y periodo reportado
- Mensaje clave: en curso, con desviación controlada de plazo y presupuesto
- Decisión solicitada hoy: priorización, contingencia y gobernanza Q2–Q3
- Visual: portada con semáforo global (verde / ámbar / rojo)
- Notas: Abra con el veredicto en una frase. El board debe saber en 30 segundos si hay que decidir algo hoy.

**2. Agenda y decisiones esperadas**
- Estado actual y avance por frente
- Métricas, hitos y presupuesto vs. plan
- Riesgos materiales y roadmap Q2–Q3
- Tres asks concretos y próximos pasos
- Visual: agenda lineal con tiempo por bloque (15–20 min + Q&A)
- Notas: Anticípese a que el debate se concentre en presupuesto, riesgos y asks; no en el detalle técnico.

**3. Por qué existe el programa**
- Objetivo: plataforma unificada de experiencia de cliente, datos y operaciones
- Resultados de negocio esperados: ingresos, costo de servir, time-to-market
- Fuera de alcance: sistemas legacy no migrados en esta ola
- Criterio de éxito del board: adopción, estabilidad y retorno en el horizonte acordado
- Visual: diagrama de valor (capacidades → resultados de negocio)
- Notas: Reanclen el “para qué” antes de entrar en semáforos. Evite jerga de arquitectura.

**4. Estado actual — resumen ejecutivo**
- Semáforo global: ámbar (avance sólido; dos frentes en atención)
- Avance ponderado: ~68% vs. 72% plan (ejemplo)
- Presupuesto: 61% ejecutado vs. 58% del plan a la fecha (ejemplo)
- Go-live fase 1: en fecha objetivo, con alcance reducido acordado
- Dependencia crítica: integración con core y calidad de datos maestros
- Visual: dashboard de una página con 4 KPIs y semáforo
- Notas: Lea solo el semáforo y la excepción. Ofrezca el detalle en el apéndice si lo piden.

**5. Avance por frente de trabajo**
- Experiencia de cliente: en plan; piloto interno completado
- Datos e integraciones: atrás 3–4 semanas por calidad de maestros
- Plataforma y seguridad: en plan; controles base cerrados
- Cambio y adopción: plan de capacitación listo; champions al 80%
- Visual: tabla o barras horizontales por frente (plan vs. real, semáforo, dueño)
- Notas: Señale un solo frente en rojo o ámbar fuerte. No recorra los cinco con el mismo peso.

**6. Métricas de progreso**
- Hitos del periodo: 11 de 13 cumplidos
- Velocidad de entrega: estable las últimas 6 semanas
- Defectos críticos abiertos: dentro del umbral; ninguno bloquea el piloto
- Adopción del piloto: usuarios activos y tareas completadas vs. meta
- Satisfacción interna del piloto (CSAT o NPS de proceso)
- Visual: gráfico de tendencia (burn-up de alcance + defectos críticos)
- Notas: Traduzca cada métrica a impacto: plazo, riesgo operativo o experiencia del cliente.

**7. Hitos: cumplidos, en curso y en riesgo**
- Cumplidos: diseño de experiencia, ambientes, controles de seguridad base
- En curso: migración piloto, integraciones prioritarias, UAT de negocio
- En riesgo: corte de datos maestros y ventana de integración con core
- Hito de decisión: alcance de fase 1 congelado en la fecha X
- Visual: timeline con hitos (hecho / en curso / en riesgo)
- Notas: Explique qué se movió de fase 1 a fase 2 y qué no se sacrificó (seguridad, controles, datos críticos).

**8. Presupuesto ejecutado vs. planeado**
- Presupuesto total aprobado vs. forecast a fin de programa
- Ejecutado a la fecha vs. plan a la fecha (variación en % y en moneda)
- Comprometido no ejecutado (PO y contratos)
- Forecast: sobre-ejecución contenida o necesidad de contingencia
- Run-rate mensual vs. plan restante
- Visual: gráfico de cascada o barras acumuladas plan / real / forecast
- Notas: Diga primero si el forecast cabe en lo aprobado. El detalle de partidas va en la siguiente slide.

**9. De dónde viene la variación**
- Drivers: integraciones adicionales, retrabajo de datos, refuerzo de proveedores
- Ahorros o underspend: licencias diferidas, vacantes no cubiertas
- Partidas rígidas vs. discrecionales de aquí a Q3
- Uso propuesto de contingencia (monto y disparador)
- Qué no se financiará si no hay decisión
- Visual: waterfall de variación por driver, con dueño de cada barra
- Notas: No defienda cada peso. Muestre la decisión: absorber, reasignar o pedir contingencia.

**10. Riesgos materiales**
- Datos maestros: calidad insuficiente retrasa migración y UAT
- Dependencia del core: ventana de cambio limitada en Q2
- Capacidad del negocio: key users compartidos con el día a día
- Proveedor crítico: concentración y plazo de un entregable
- Adopción: riesgo de “go-live técnico” sin uso real
- Visual: matriz probabilidad × impacto, top 5 solamente
- Notas: Limítese a riesgos que cambian plazo, costo o reputación. El resto queda en el registro del PMO.

**11. Mitigaciones y decisiones que no pueden esperar**
- Datos: squad dedicado y criterio de “listo para migrar”
- Core: reserva de ventana y plan B de integración por fases
- Negocio: liberación parcial de key users en las 6 semanas de UAT
- Proveedor: hito con penalidad o respaldo interno
- Adopción: meta de uso en piloto como condición de go-live
- Visual: tabla riesgo → mitigación → dueño → fecha → estado
- Notas: Pida dueños con nombre, no áreas. Cierre cada riesgo con “qué pasa si no se actúa en 30 días”.

**12. Roadmap Q2**
- Abril: cierre de datos piloto, integraciones P1, inicio de UAT
- Mayo: UAT de negocio, remediación, ensayo de corte
- Junio: go / no-go de fase 1, despliegue controlado, hiper-care
- Capacidades que salen en fase 1 vs. las que quedan para Q3
- Dependencias externas que el board debe desbloquear
- Visual: roadmap trimestral por mes y por frente
- Notas: Sea explícito sobre el criterio de go-live: estabilidad, datos y adopción mínima, no solo fecha.

**13. Roadmap Q3**
- Julio–agosto: estabilización, oleada 2 de procesos y canales
- Septiembre: expansión de usuarios y depreciación del proceso anterior
- Beneficios que empiezan a medirse (ingresos, costo, ciclo)
- Inversiones que se activan solo si fase 1 cumple umbrales
- Riesgo de Q3 si Q2 se desliza más de X semanas
- Visual: roadmap Q3 con “puerta” de entrada condicionada a fase 1
- Notas: Evite prometer el año completo. Amarre Q3 a evidencia de Q2, no a un deseo de alcance.

**14. Asks al board**
- Aprobar uso de contingencia hasta un monto tope, con disparadores definidos
- Respaldar la liberación de key users de negocio en la ventana de UAT
- Confirmar alcance de fase 1 (qué queda fuera) para proteger la fecha
- Designar un ejecutivo responsable de la dependencia con el core
- Próxima revisión: fecha, umbral de escalamiento y qué se reportará
- Visual: tabla de decisiones (ask, monto o recurso, consecuencia de no decidir, recomendación)
- Notas: Lea los asks en voz alta y pause. No los diluya en el cierre narrativo.

**15. Cierre y próximos 30 días**
- Veredicto: avanzamos a go-live de fase 1 si se cierran datos, ventana de core y UAT
- Tres movimientos de los próximos 30 días, con dueño
- Qué volverá al board (forecast, semáforo de go-live, adopción del piloto)
- Agradecimiento y espacio para decisión
- Visual: una diapositiva con el veredicto y los tres movimientos; sin gráficos nuevos
- Notas: Termine pidiendo la decisión, no un resumen. Si no hay consenso, acuerde fecha y dueño del seguimiento antes de cerrar la sala.