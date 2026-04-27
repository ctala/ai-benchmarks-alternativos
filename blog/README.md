# Blog drafts auto-generados

Esta carpeta contiene drafts de blog posts SEO + adaptaciones a canales sociales generados por agentes IA usando los datos del benchmark como contexto.

## Estructura

```
blog/
├── README.md                                          # este archivo
├── 2026-04-26-alternativas-claude-provider-matters.md # blog posts SEO completos
└── social/                                            # adaptaciones por canal
    ├── 2026-04-26-alternativas-claude-provider-matters-linkedin.md
    ├── 2026-04-26-alternativas-claude-provider-matters-skool.md
    ├── 2026-04-26-alternativas-claude-provider-matters-twitter.md
    └── 2026-04-26-alternativas-claude-provider-matters-newsletter.md
```

## Cómo generar contenido nuevo

### Local

```bash
export ANTHROPIC_API_KEY=sk-ant-...
python scripts/generate_blog_post.py \
    --topic "alternativas-chatgpt" \
    --insight "spearman precio-contenido es negativa"
```

### Via GitHub Actions (recomendado)

1. Settings → Secrets → agregar `ANTHROPIC_API_KEY`
2. Actions → "Generar contenido SEO semanal" → Run workflow
3. Elegir topic + insight → workflow abre PR con drafts
4. Revisar, editar, mergear (o cerrar si no convence)

## Pipeline conceptual

```
INSIGHTS.md
    ↓
seo-content-writer (Opus) → blog post Markdown completo
    ↓
content-marketer (Sonnet) → adaptaciones a 4 canales en paralelo
    ↓
PR auto-creado para revisión humana antes de publicar
```

## Costo aproximado

- Blog post completo (Opus, ~6K tokens output): ~$0.15-0.20
- 4 adaptaciones (Sonnet, ~1K tokens c/u): ~$0.05-0.10
- **Total por run**: ~$0.20-0.30 USD

## Política de contenido

- **Drafts requieren revisión humana** antes de publicar — el agente puede inventar datos si el INSIGHTS.md es ambiguo.
- **Verificá data del benchmark** contra los JSONs reales antes de publicar.
- **Editá la voz** — los drafts son un punto de partida, no producto final.
- **Si un draft es malo, cerrá el PR** y ajustá el prompt del agente en `.claude/agents/seo-content-writer.md`.

## Contenido publicado

Cuando un blog post se publique en `cristiantala.com`, agregá el link al frontmatter del MD original con `published_url:` y `published_date:` para tracking.
