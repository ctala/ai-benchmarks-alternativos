# MiniMax M3 (directo / sub) — task_management/weekly_planning

- model_id: `MiniMax-M3`
- success: True  | final: 6.9 | quality: 8.6
- latency_total: 228.249s | tokens_per_second: 32.2
- input_tokens: 354 | output_tokens: 7356
- judge_score: 4.0 | justificación: 

## Respuesta completa

<think>
The user is a product manager who needs me to create a detailed weekly plan with specific time blocks. Let me analyze the constraints and tasks carefully.

**Constraints (fixed commitments):**
- Monday: Board meeting 9-11 AM, client lunch 1-2 PM
- Tuesday: Free all day
- Wednesday: Product demo 3-4 PM
- Thursday: Hiring interviews 10 AM - 1 PM
- Friday: Retrospective 4-5 PM

**Tasks to schedule:**
1. Prepare presentation for demo (3 hours) - Must be before Wednesday 3 PM
2. Review pending PRDs (2 hours)
3. Write Q3 OKRs (4 hours)
4. Respond to stakeholder emails (1 hour daily) - 5 days
5. Review product metrics (1 hour)
6. One-on-ones with 3 direct reports (30 min each) = 1.5 hours total

**Total time needed:**
- Task 1: 3 hours
- Task 2: 2 hours
- Task 3: 4 hours
- Task 4: 5 hours (1 hour × 5 days)
- Task 5: 1 hour
- Task 6: 1.5 hours
**Total: 16.5 hours**

**Available time per day (assuming 9 AM - 6 PM work day = 9 hours):**
- Monday: 9-11 (meeting), 1-2 (lunch) blocked = 7 hours free (subtract 1 hour for actual lunch if not the client lunch, but the user has a client lunch from 1-2, so they need to account for their own lunch time too)
- Tuesday: 9 hours free
- Wednesday: 3-4 blocked = 8 hours free
- Thursday: 10-1 blocked = 6 hours free
- Friday: 4-5 blocked = 8 hours free

**Total available: 7+9+8+6+8 = 38 hours**
**Total needed: 16.5 hours**

So there's plenty of room. Let me think about the logic of placement:

**Strategic placement principles:**
1. **Emails daily** - Should be at the start of the day (before checking Slack) or end of day. I'll put them at the start of the day to clear the inbox before deep work.
2. **Presentation prep** - MUST be before Wednesday 3 PM. Should do this Monday or Tuesday. Tuesday is good for deep work.
3. **OKRs Q3** - Deep thinking work, needs focus time. Tuesday or Thursday afternoon is best.
4. **PRDs review** - Moderate focus work
5. **Metrics review** - Quick task, can be done in any slot
6. **One-on-ones** - Should be distributed through the week, not all on same day

**Let me design the schedule:**

**Monday:**
- 8:00-8:30 AM: Email stakeholders (start the day)
- 8:30-9:00 AM: Quick prep for board meeting
- 9:00-11:00 AM: Board meeting
- 11:00 AM-12:00 PM: Email follow-ups + metrics review
- 12:00-1:00 PM: Lunch (personal)
- 1:00-2:00 PM: Client lunch
- 2:00-3:00 PM: 1:1 with report 1
- 3:00-3:30 PM: 1:1 with report 2
- 3:30-5:00 PM: Review pending PRDs (1.5 hours, 30 min left for transition)
- Wait, let me recalculate

Let me re-think with cleaner blocks:

**Monday:**
- 8:00-9:00 AM: Email stakeholders (1h)
- 9:00-11:00 AM: Board meeting (fixed)
- 11:00-12:00 PM: Continue emails overflow + quick follow-ups (extending from email time if needed, but I'll structure it differently)
- Actually, let me restart and be more careful

**Monday Schedule:**
- 8:00-9:00 AM: Stakeholder emails (1h)
- 9:00-11:00 AM: Board meeting [FIXED]
- 11:00-12:30 PM: One-on-ones (1.5h = 3 × 30min) → wait, this is back to back, maybe too much
- Actually let me space out 1:1s

Let me think about this differently. I'll do 1:1s on different days to spread the load:

- Report 1: Monday afternoon
- Report 2: Wednesday morning
- Report 3: Thursday morning (before interviews) or Friday morning

**Final plan:**

**Monday:**
- 8:00-9:00 AM: Stakeholder emails
- 9:00-11:00 AM: Board meeting [FIXED]
- 11:00-12:00 PM: Review product metrics (1h) - good to do after board meeting, mind is fresh on strategy
- 12:00-1:00 PM: Lunch
- 1:00-2:00 PM: Client lunch [FIXED]
- 2:00-2:30 PM: 1:1 with Report 1
- 2:30-4:30 PM: Review pending PRDs (2h)
- 4:30-5:30 PM: Buffer / overflow / follow-ups

**Tuesday (free day - perfect for deep work):**
- 8:00-9:00 AM: Stakeholder emails
- 9:00-12:00 PM: Prepare demo presentation (3h) - first thing when fresh
- 12:00-1:00 PM: Lunch
- 1:00-5:00 PM: Write Q3 OKRs (4h with break)
- 1:00-3:00 PM: OKRs Part 1 (2h)
- 3:00-3:15 PM: Break
- 3:15-5:15 PM: OKRs Part 2 (1h45m)... wait that's not 4h total

Let me recalculate Tuesday:
- 8:00-9:00 AM: Emails (1h)
- 9:00-12:00 PM: Demo presentation prep (3h)
- 12:00-1:00 PM: Lunch
- 1:00-3:30 PM: OKRs writing - block 1 (2.5h, with focus)
- 3:30-3:45 PM: Break
- 3:45-5:15 PM: OKRs writing - block 2 (1.5h)
- 5:15-6:00 PM: Wrap up / overflow

That's 4h of OKRs. Good.

**Wednesday:**
- 8:00-9:00 AM: Stakeholder emails
- 9:00-9:30 AM: 1:1 with Report 2
- 9:30-10:00 AM: Buffer / final review of demo materials
- Actually wait, I should leave more time for demo prep
- 9:00-10:30 AM: Final review/practice of demo presentation
- 10:30-12:00 PM: Some OKR work overflow or planning
- 12:00-1:00 PM: Lunch
- 1:00-2:30 PM: Final demo preparation / run-through
- 2:30-3:00 PM: Pre-demo prep
- 3:00-4:00 PM: Product demo [FIXED]
- 4:00-5:00 PM: Demo follow-ups / stakeholder communication

Hmm, but I already have OKRs done on Tuesday, so Wednesday is more flexible.

Let me re-plan Wednesday:
- 8:00-9:00 AM: Stakeholder emails
- 9:00-9:30 AM: 1:1 with Report 2
- 9:30-11:00 AM: Final demo preparation
- 11:00-12:00 PM: Review metrics (1h) - good time, fresh data
- 12:00-1:00 PM: Lunch
- 1:00-2:30 PM: Final demo run-through
- 2:30-3:00 PM: Pre-demo buffer
- 3:00-4:00 PM: Product demo [FIXED]
- 4:00-5:00 PM: Demo follow-ups, send notes

**Thursday:**
- 8:00-9:00 AM: Stakeholder emails
- 9:00-9:30 AM: 1:1 with Report 3
- 9:30-10:00 AM: Buffer / prep
- 10:00-1:00 PM: Hiring interviews [FIXED]
- 1:00-2:00 PM: Lunch
- 2:00-4:00 PM: Strategic planning / follow-ups from interviews
- 4:00-5:00 PM: Wrap up

Wait, I need to fit PRDs in but I scheduled them Monday. Let me check.

Monday: 
- PRD review: 2:30-4:30 PM ✓ (2h)
Tuesday: 
- Demo prep: 9-12 ✓ (3h)
- OKRs: 1-3:30 + 3:45-5:15 ✓ (4h)
Wednesday:
- Demo final prep
- Metrics review: 11-12 ✓ (1h)
Thursday: 
- 1:1 with Report 3 ✓
Friday:
- Retrospective 4-5 [FIXED]
- Need to schedule: 1:1 with... wait, I have 3 reports, I scheduled 2. Let me recheck.

I have 3 1:1s:
- Report 1: Monday 2:00-2:30 PM
- Report 2: Wednesday 9:00-9:30 AM
- Report 3: Thursday 9:00-9:30 AM (before interviews)

That's 3 × 30 min = 1.5h ✓

OK, let me check all tasks:
1. Demo prep (3h): Tuesday 9-12 ✓
2. PRDs review (2h): Monday 2:30-4:30 ✓
3. OKRs Q3 (4h): Tuesday 1-3:30 + 3:45-5:15 ✓
4. Emails (1h daily): 
   - Monday 8-9 ✓
   - Tuesday 8-9 ✓
   - Wednesday 8-9 ✓
   - Thursday 8-9 ✓
   - Friday ? need to add
5. Metrics review (1h): Wednesday 11-12 ✓
6. 1:1s (1.5h): Monday, Wednesday, Thursday ✓

**Friday:**
- Need: 1h emails
- Free time: 8-4, 4-5 retro
- 8:00-9:00 AM: Stakeholder emails
- 9:00-12:00 PM: Free for overflow, additional work, weekly planning
- 12:00-1:00 PM: Lunch
- 1:00-4:00 PM: Free for overflow, weekly planning, Q3 prep continuation
- 4:00-5:00 PM: Retrospective [FIXED]

Friday has lots of free time. I should note that the user can use this for overflow or strategic thinking.

Let me put this all together in a nice table format. I should:
1. Use a clear visual format (table or list per day)
2. Explain the logic
3. Note any considerations
4. Highlight that this is a proposal and they can adjust

Let me also think about energy/focus patterns:
- Monday morning: Board meeting (high stakes) - so morning prep is right
- Tuesday is free: Best for deep work → OKRs and demo prep
- Wednesday: Demo day, so demo should be in the afternoon
- Thursday: Interviews take a chunk, morning is more free
- Friday: Retrospective at 4, so afternoon is taken

I think my plan is good. Let me also add some reasoning notes.

One more consideration: The user said "1 hora diaria" for emails, which is 5 hours total across the week. I have that. But realistically, emails don't need to be a full 1-hour block every day - they can be split. But since the user specified "1 hora diaria", I'll respect that as a single 1-hour block, perhaps at the start of the day to clear the inbox.

Actually, having emails be the FIRST thing every day is a great PM habit. So that's good.

Let me also think about whether 4h of OKRs on Tuesday is too much in one day. It's a lot, but Tuesday is the only free day. The user could split it: 2h Tuesday, 2h Thursday afternoon. But OKRs benefit from sustained focus. I'll keep them on Tuesday but note that the user might want to break it up.

Actually, let me reconsider: Maybe 2h of OKRs on Tuesday and 2h on Thursday afternoon is better for cognitive load. But the user said OKRs are 4h, so they can decide. I'll present Tuesday as the main option but note the alternative.

Hmm, I think I should present one clean plan and offer optional adjustments. Let me finalize.

**Final Plan:**

| Day | Time | Activity | Type |
|-----|------|----------|------|
| **Monday** | 8:00-9:00 | Stakeholder emails | Recurring |
| | 9:00-11:00 | Board meeting | Fixed |
| | 11:00-12:00 | Review product metrics | Task |
| | 12:00-1:00 | Lunch | |
| | 1:00-2:00 | Client lunch | Fixed |
| | 2:00-2:30 | 1:1 Report 1 | Task |
| | 2:30-4:30 | Review pending PRDs | Task |
| | 4:30-5:30 | Buffer / follow-ups | |
| **Tuesday** | 8:00-9:00 | Stakeholder emails | Recurring |
| | 9:00-12:00 | Demo presentation prep | Task |
| | 12:00-1:00 | Lunch | |
| | 1:00-3:30 | OKRs Q3 - Block 1 | Task |
| | 3:30-3:45 | Break | |
| | 3:45-5:15 | OKRs Q3 - Block 2 | Task |
| | 5:15-6:00 | Buffer | |
| **Wednesday** | 8:00-9:00 | Stakeholder emails | Recurring |
| | 9:00-9:30 | 1:1 Report 2 | Task |
| | 9:30-11:00 | Final demo preparation | |
| | 11:00-12:00 | Review metrics (overlap with Monday? No, separate task) | |

Wait, I scheduled metrics review on Monday already. Let me check the original list: "Revisar metricas del producto (1 hora)" - just 1 hour total for the week. I put it on Monday 11-12. Good.

But wait, I had Wednesday 11-12 in my earlier plan. Let me decide: Is metrics review better on Monday (after board meeting, strategic context) or Wednesday (fresh data)? 

Actually, for a PM, metrics should be checked at least weekly. I think Monday after the board meeting is good - you can discuss strategy with fresh data. Let me put it Monday.

But I also want Wednesday to have meaningful work. Let me think...

Actually, the demo prep needs review/practice time on Wednesday morning. So Wednesday morning: 1:1 with Report 2, then demo run-through. That works.

OK let me also think: Should I split demo prep between Tuesday and Wednesday? The user said it's 3 hours total. I could do 2h Tuesday, 1h Wednesday morning. But better to do most of it Tuesday and just do final run-through Wednesday. So Tuesday: 3h of focused creation. Wednesday morning: 1:1 + final run-through.

OK final plan:

**Monday:**
- 8:00-9:00 AM: Stakeholder emails
- 9:00-11:00 AM: Board meeting [FIXED]
- 11:00-12:00 PM: Review product metrics
- 12:00-1:00 PM: Personal lunch
- 1:00-2:00 PM: Client lunch [FIXED]
- 2:00-2:30 PM: 1:1 with Report 1
- 2:30-4:30 PM: Review pending PRDs
- 4:30-5:30 PM: Email overflow / slack catch-up / day wrap-up

**Tuesday:**
- 8:00-9:00 AM: Stakeholder emails
- 9:00-12:00 PM: Demo presentation prep (3h deep work)
- 12:00-1:00 PM: Lunch
- 1:00-3:30 PM: OKRs Q3 (2.5h deep work)
- 3:30-3:45 PM: Break / walk
- 3:45-5:15 PM: OKRs Q3 continued (1.5h)
- 5:15-6:00 PM: Buffer / planning for Wednesday

**Wednesday:**
- 8:00-9:00 AM: Stakeholder emails
- 9:00-9:30 AM: 1:1 with Report 2
- 9:30-10:30 AM: Demo final review & run-through
- 10:30-12:00 PM: Strategic work / OKR refinement / prep for demo
- 12:00-1:00 PM: Lunch
- 1:00-2:30 PM: Final demo prep / pre-meeting review
- 2:30-3:00 PM: Buffer / settle in for demo
- 3:00-4:00 PM: Product demo [FIXED]
- 4:00-5:00 PM: Demo follow-ups, send notes, stakeholder comms

**Thursday:**
- 8:00-9:00 AM: Stakeholder emails
- 9:00-9:30 AM: 1:1 with Report 3
- 9:30-10:00 AM: Prep for interviews
- 10:00-1:00 PM: Hiring interviews [FIXED]
- 1:00-2:00 PM: Lunch
- 2:00-4:00 PM: Strategic work, follow-ups from interviews
- 4:00-5:00 PM: End-of-day wrap-up, planning Friday
- 5:00-6:00 PM: Buffer

**Friday:**
- 8:00-9:00 AM: Stakeholder emails
- 9:00-12:00 PM: Deep work / overflow / weekly planning / OKR finalization
- 12:00-1:00 PM: Lunch
- 1:00-4:00 PM: Free for strategic projects, learning, deep thinking
- 4:00-5:00 PM: Retrospective [FIXED]
- 5:00-5:30 PM: Weekly wrap-up, prep for next week

Wait, I'm double-counting metrics review. Let me check the tasks again:
- Tarea 5: Revisar metricas del producto (1 hora) - just 1 hour total for the week

I scheduled it Monday 11-12. Good.

Let me verify all tasks are covered:
1. ✓ Demo prep: Tuesday 9-12 (3h)
2. ✓ PRDs: Monday 2:30-4:30 (2h)
3. ✓ OKRs: Tuesday 1-3:30 + 3:45-5:15 (4h total)
4. ✓ Emails: 8-9 AM every day (5h total)
5. ✓ Metrics: Monday 11-12 (1h)
6. ✓ 1:1s: Monday, Wednesday, Thursday (1.5h total)

All tasks covered. 

Now, I should present this in a clear, professional way. Let me structure the response:

1. Brief intro
2. The weekly plan as a table or organized list
3. Key reasoning/logic
4. Important notes/considerations

I'll use a table format for clarity. Let me think about formatting - tables are great for this kind of data.

Actually, I should also think about whether I should include buffers. PMs often have unscheduled time for slack, fire drills, etc. I have some buffer time built in.

Let me also note that the user mentioned 9-6 work hours implicitly, but I should be flexible. I'll assume 8-6 work day (10 hours) which is reasonable for a PM.

One more consideration: I scheduled OKRs for 4h straight (with one break). This is intense. Maybe I should split: 2h Tuesday afternoon + 2h Friday morning. But Tuesday is the only "free" day, so doing OKRs there makes sense to leave other days with more flexibility. I'll keep Tuesday but mention the option to split.

Also, I should think about what happens on Friday morning - I left it very open. Maybe I should suggest something specific. Options:
- Continue OKR work
- Strategic thinking time
- Catch up on missed tasks
- Pre-work for next week

I'll leave it flexible but suggest using it as overflow/strategic time.

Let me write the response now. I'll use Spanish since the user wrote in Spanish.

Format considerations:
- Use a clean table for the schedule
- Use headers for each day
- Add a "Lógica del plan" or "Por qué esta estructura" section
- Add notes/considerations
- Keep it scannable but informative

Let me draft this in Spanish.

Actually, looking at this again, I want to make sure my hours line up properly. Let me re-verify:

Monday total time:
- 8-9: emails (1h)
- 9-11: board (2h) [fixed]
- 11-12: metrics (1h)
- 12-1: lunch (1h)
- 1-2: client lunch (1h) [fixed]
- 2-2:30: 1:1 (0.5h)
- 2:30-4:30: PRDs (2h)
- 4:30-5:30: buffer (1h)
Total: 9.5h. Good.

Tuesday:
- 8-9: emails (1h)
- 9-12: demo prep (3h)
- 12-1: lunch (1h)
- 1-3:30: OKRs (2.5h)
- 3:30-3:45: break (0.25h)
- 3:45-5:15: OKRs (1.5h)
- 5:15-6: buffer (0.75h)
Total: 10h. Good.

Wednesday:
- 8-9: emails (1h)
- 9-9:30: 1:1 (0.5h)
- 9:30-10:30: demo run-through (1h)
- 10:30-12: strategic work (1.5h)
- 12-1: lunch (1h)
- 1-2:30: final demo prep (1.5h)
- 2:30-3: buffer (0.5h)
- 3-4: demo (1h) [fixed]
- 4-5: follow-ups (1h)
Total: 9.5h. Good.

Thursday:
- 8-9: emails (1h)
- 9-9:30: 1:1 (0.5h)
- 9:30-10: prep (0.5h)
- 10-1: interviews (3h) [fixed]
- 1-2: lunch (1h)
- 2-4: strategic (2h)
- 4-5: wrap-up (1h)
- 5-6: buffer (1h)
Total: 10h. Good.

Friday:
- 8-9: emails (1h)
- 9-12: deep work/overflow (3h)
- 12-1: lunch (1h)
- 1-4: strategic (3h)
- 4-5: retro (1h) [fixed]
- 5-5:30: wrap-up (0.5h)
Total: 9.5h. Good.

All checks out. Let me write the final response.

For the response format, I think:
1. A short intro
2. The full week schedule (could be one big table or day-by-day)
3. Brief explanation of the logic
4. Notes/tips

I'll use one big table that includes all 5 days, with the time as the first column. This will be the most scannable.

Actually, day-by-day might be clearer since blocks vary so much. Let me think...

A combined table could work like this:
| Hora | Lunes | Martes | Miércoles | Jueves | Viernes |

That's clean. Let me try this format.

Hmm, but the demo prep is 3 hours and OKRs are 4 hours, so cells would be wide. Let me see if that works.

Actually, day-by-day with clear headers might be cleaner. Let me do that approach but use compact lists within each day.

Let me draft:

# Plan Semanal — Product Manager

## 🗓️ Vista general

| Hora | Lunes | Martes | Miércoles | Jueves | Viernes |
|------|-------|--------|-----------|--------|---------|
| 8:00-9:00 | 📧 Emails | 📧 Emails | 📧 Emails | 📧 Emails | 📧 Emails |
| 9:00-10:00 | 🎯 Directiva | 🎯 Demo prep | 👥 1:1 + demo | 👥 1:1 + prep | 🧠 Overflow/estratégico |
| ... etc

This could work but might be cramped. Let me try day-by-day instead.

I'll go with day-by-day for clarity, with each day as its own subsection.

Let me write the final response now.

Actually, thinking more about it, I think a hybrid approach works best:
- A brief "weekly at a glance" summary
- Day-by-day detailed breakdown
- Logic notes

Let me write it out.
</think>
# Plan Semanal — Product Manager

## 📅 Vista semanal (resumen)

| | Lunes | Martes | Miércoles | Jueves | Viernes |
|---|---|---|---|---|---|
| 🌅 Mañana | Emails + Métricas | Emails + **Demo prep (deep work)** | Emails + 1:1 + Demo run-through | Emails + 1:1 + **Entrevistas** | Emails + Trabajo profundo |
| 🌞 Mediodía | 🍽️ Client lunch (1-2) | OKRs Q3 (deep work) | Demo final + **🎤 Demo 3-4 PM** | Trabajo estratégico | Trabajo estratégico |
| 🌇 Tarde | PRDs pendientes | OKRs Q3 (cierre) | Follow-ups demo | Wrap-up | 🔁 **Retrospectiva 4-5 PM** |

---

## 📋 Detalle por día

### **Lunes** — *"Arranque estratégico"*
| Hora | Actividad | Notas |
|------|-----------|-------|
| 8:00-9:00 | 📧 Emails stakeholders | Inbox a cero antes de reuniones |
| 9:00-11:00 | 🎯 **Reunión directivos** | *[fijo]* |
| 11:00-12:00 | 📊 Revisar métricas producto | Mente fresca post-directiva |
| 12:00-1:00 | 🍽️ Almuerzo personal | |
| 1:00-2:00 | 🤝 **Almuerzo cliente** | *[fijo]* |
| 2:00-2:30 | 👤 1:1 Reporte 1 | 30 min |
| 2:30-4:30 | 📄 Revisar PRDs pendientes | 2h bloque continuo |
| 4:30-5:30 | 🛟 Buffer / Slack catch-up | Imprevistos del día |

### **Martes** — *"Deep work day"* 🧠
| Hora | Actividad | Notas |
|------|-----------|-------|
| 8:00-9:00 | 📧 Emails stakeholders | |
| **9:00-12:00** | 🎤 **Preparar presentación demo** | **3h seguidas** — cuando la mente está más fresca |
| 12:00-1:00 | 🍽️ Almuerzo | |
| 1:00-3:30 | 🎯 Escribir OKRs Q3 — Bloque 1 | 2.5h |
| 3:30-3:45 | ☕ Descanso / caminata | Reset cognitivo |
| 3:45-5:15 | 🎯 Escribir OKRs Q3 — Bloque 2 | 1.5h → **cierra 4h totales** |
| 5:15-6:00 | 🛟 Buffer / preview del miércoles | |

### **Miércoles** — *"Demo day"*
| Hora | Actividad | Notas |
|------|-----------|-------|
| 8:00-9:00 | 📧 Emails stakeholders | |
| 9:00-9:30 | 👤 1:1 Reporte 2 | 30 min |
| 9:30-10:30 | 🎤 Demo: ensayo final | Run-through en voz alta |
| 10:30-12:00 | 🧠 Trabajo estratégico / refinamiento | Si quedó algo pendiente |
| 12:00-1:00 | 🍽️ Almuerzo | |
| 1:00-2:30 | 🎤 Demo: últimos ajustes | Imprimibles, slides, demo del producto |
| 2:30-3:00 | 🛟 Buffer pre-demo | Respirar, preparar setup |
| **3:00-4:00** | 🎤 **DEMO DE PRODUCTO** | *[fijo]* |
| 4:00-5:00 | 📝 Follow-ups demo | Enviar notas, responder preguntas |

### **Jueves** — *"Hiring + cierre"*
| Hora | Actividad | Notas |
|------|-----------|-------|
| 8:00-9:00 | 📧 Emails stakeholders | |
| 9:00-9:30 | 👤 1:1 Reporte 3 | 30 min |
| 9:30-10:00 | 📋 Preparar entrevistas | Revisar candidatos |
| **10:00-1:00** | 🧑‍💼 **Entrevistas hiring** | *[fijo]* |
| 1:00-2:00 | 🍽️ Almuerzo | |
| 2:00-4:00 | 🧠 Trabajo estratégico | Follow-ups entrevistas, planning |
| 4:00-5:00 | 📌 Cierre del día | To-do list viernes |
| 5:00-6:00 | 🛟 Buffer | |

### **Viernes** — *"Reflexión + overflow"*
| Hora | Actividad | Notas |
|------|-----------|-------|
| 8:00-9:00 | 📧 Emails stakeholders | |
| 9:00-12:00 | 🧠 Trabajo profundo / overflow | Terminar OKRs, OKR review, planning |
| 12:00-1:00 | 🍽️ Almuerzo | |
| 1:00-4:00 | 🎯 Trabajo estratégico | Si todo va bien, espacio para pensar en roadmap |
| **4:00-5:00** | 🔁 **Retrospectiva** | *[fijo]* |
| 5:00-5:30 | 📌 Cierre semanal | Prep próxima semana |

---

## 🧠 Lógica del plan

1. **Emails siempre a las 8 AM** → limpias inbox antes de que llegue el ruido. Coherente con la regla "1h diaria".
2. **Demo prep el martes completo** → tu único día sin reuniones. Lo bloqueé como deep work antes que la energía cognitiva baje.
3. **OKRs集中在 el martes** → 4h seguidas con un break. Si lo prefieres, puedes partir: 2h martes + 2h viernes mañana.
4. **Métricas después de la directiva del lunes** → contexto estratégico fresco, mejor interpretación.
5. **1:1s repartidos L-X-J** → no acumulas feedback el mismo día, y cada uno entra en un contexto diferente.
6. **PRDs el lunes tarde** → tarea semi-deep pero requiere cabeza despejada, y el martes lo necesitas 100% para la demo.
7. **Viernes con espacio libre** → está intencionalmente abierto para overflow, trabajo estratégico o lo que no haya cabido.

---

## ⚠️ Consideraciones

- **Total tareascheduled: 16.5h** sobre ~38h disponibles → hay ~20h de buffer para Slack, imprevistos, reuniones 1:1 no planificadas, etc. Si tu semana suele ser más caótica, avísame y ajusto los buffers.
- **No incluí tiempos de comida** (lunch personal) en la mayoría de los días, asumiendo que los pones tú. Si quieres que los fije, dímelo.
- **El bloque de demo prep es agresivo** (3h seguidas). Si necesitas 2h creación + 1h ensayo, podemos partirlo entre martes y miércoles mañana.
- **¿Falta alguna reunión recurrente?** (weekly de equipo, sync con design, etc.) Si me las das, las agrego al plan.

¿Quieres que ajuste algo? Por ejemplo: mover la presentación al lunes en vez del martes, o partir los OKRs en dos días.