# Nemotron 3 Super 120B (DGX Spark Q4_K_M) — agent_capabilities/agent_team_delegation

- model_id: `nemotron-3-super:120b`
- success: True  | final: 6.04 | quality: 6.82
- latency_total: 29.261s | tokens_per_second: 16.6
- input_tokens: 1312 | output_tokens: 486
- judge_score: 3.8 | justificación: 

## Respuesta completa

We need to coordinate tasks: researcher to investigate competition; writer to write copy; coder to generate HTML/CSS; designer to create images; reviewer to review everything.

We need to explain plan before delegating. So we should first output plan, then delegate tasks accordingly.

We need to delegate tasks with delegate_to_agent tool.

We need to set priorities: researcher high; writer after researcher; designer maybe after copy? Could be parallel with writer for images based on copy; coder after copy and images; reviewer after everything.

We'll produce plan then call delegate_to_agent for each.

We need to actually call the tool to delegate. Likely we need to make calls sequentially? Could do multiple calls.

We'll first delegate researcher: task: research competition (3 competitors) for AutoFlow AI, find features, pricing, messaging.

Then after researcher returns (we assume they will provide results), we delegate writer with context from researcher.

But we don't have results yet. We can still delegate with placeholder context: "Use findings from researcher". Might need to ask human? Probably not.

We'll delegate writer: task: write copy for landing page (hero, features, pricing, CTA) based on researcher findings.

Designer: task: create hero image and feature images based on copy and product description.

Coder: task: generate HTML/CSS landing page using copy and images.

Reviewer: task: review copy, design, code for quality, consistency, errors.

We need to set priorities: researcher high, writer high after researcher, designer medium, coder high after writer/designer, reviewer high after coder.

We'll need to use delegate_to_agent multiple times.

Let's start with researcher.