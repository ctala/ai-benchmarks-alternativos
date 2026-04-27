# Nemotron 3 Nano 30B — agent_capabilities/agent_team_delegation

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 6.18 | quality: 9.52
- latency_total: 16.129s | tokens_per_second: 90.7
- input_tokens: 1350 | output_tokens: 1463
- judge_score: 4.8 | justificación: 

## Respuesta completa

¡Claro! Aquí tienes el plan de ejecución que seguiré para crear la landing page de **AutoFlow AI**:

1. **Investigación de la competencia**  
   - *Sub‑agente*: **researcher**  
   - Tarea: Buscar información sobre 3 competidores principales, analizando sus landing pages (qué hacen, características destacadas, precios, mensajes clave, diseño, etc.).  
   - Resultado esperado: un breve informe con los hallazgos más relevantes.

2. **Redacción del copy**  
   - *Sub‑agente*: **writer**  
   - Tarea: Con base en la investigación, redactar el texto completo de la landing page:  
     - Hero (título y subtítulo)  
     - Sección de características  
     - Pricing (estructura de precios)  
     - CTA (llamada a la acción)  
   - Dependencia: necesita el informe del researcher.

3. **Diseño de imágenes**  
   - *Sub‑agente*: **designer**  
   - Tarea: Crear dos imágenes:  
     - Imagen hero (banner principal)  
     - Imagen de características (ilustraciones o mockups de la UI)  
   - Necesitará el copy finalizado para alinear el mensaje visual.

4. **Desarrollo del código**  
   - *Sub‑agente*: **coder**  
   - Tarea: Generar el HTML y CSS de la landing page, integrando el copy y los assets de diseño.  
   - Dependencia: necesita tanto el copy como los assets del designer.

5. **Revisión de calidad**  
   - *Sub‑agente*: **reviewer**  
   - Tarea: Revisar el informe de investigación, el copy, las imágenes y el código en busca de errores, consistencia y alineación con los objetivos.  
   - Entregable: reporte de revisión con posibles ajustes.

6. **Preparación para publicar**  
   - Una vez aprobado todo, coordinaremos la publicación (por ejemplo, programando un evento de calendario o enviando un mensaje de notificación).  

---

**Próximo paso:** iniciar la delegación de la tarea de investigación al agente *researcher*. ¿Te parece bien este flujo? Si tienes alguna preferencia o información adicional que quieras incluir, házmelo saber antes de continuar.