# Dev Playbook — Design Spec

> A personal, living knowledge base for software engineering processes and lifecycles.

## Problem

Tri has 3 static files (SDLC guide, Codebase Understanding playbook, Feature Development Lifecycle) containing valuable engineering knowledge. They're frozen — no way to grow them over time, no structure for deepening content, no beautiful unified presentation.

## Vision

A web app that renders markdown playbooks into a polished, interactive knowledge base. Content grows organically as Tri gains experience — each step starts as a seed and deepens with verified, industry-validated approaches over time.

## Audience

Personal-first. Structured well enough to share publicly later.

## Content Workflow

1. Tri experiences something new in a real project
2. Brings raw notes/learnings to Claude
3. Claude verifies against industry best practices, standard frameworks, and established approaches
4. Claude writes a clean `.mdx` file with proper structure and components
5. File is placed in the correct folder in the project
6. The app renders it beautifully — no manual HTML/CSS work needed

## Content Structure

Content lives as folders and `.mdx` files. The folder structure IS the knowledge tree.

```
content/
├── sdlc/                              # Hub 1: SDLC (9 phases)
│   ├── index.mdx                      # Hub overview
│   ├── 01-ideation/
│   │   ├── index.mdx                  # Phase overview
│   │   ├── problem-statement.mdx      # Step
│   │   ├── target-users.mdx           # Step
│   │   └── moscow-features/           # Step with sub-steps
│   │       ├── index.mdx
│   │       ├── must-have.mdx
│   │       └── prioritization.mdx
│   ├── 02-system-design/
│   │   ├── index.mdx
│   │   ├── api-design/
│   │   │   ├── index.mdx
│   │   │   ├── rest-endpoints.mdx
│   │   │   └── auth-patterns.mdx
│   │   └── ...
│   └── ... (phases 3-9)
├── codebase-understanding/            # Hub 2 (11 phases)
│   ├── index.mdx
│   ├── 01-orient-yourself/
│   └── ...
└── feature-development/               # Hub 3 (9 phases)
    ├── index.mdx
    ├── 01-understand-the-feature/
    └── ...
```

### Nesting

Unlimited depth. Any step can become a folder with sub-steps. Adding depth = creating a subfolder + dropping `.mdx` files in it. No code changes needed.

### Frontmatter

Each `.mdx` file has metadata:

```yaml
---
title: "REST API Design"
order: 1                    # Sort order within parent
status: "growing"           # seed | growing | mature
tags: ["backend", "api"]
lastUpdated: "2026-05-21"
---
```

- `status` indicates content maturity: seed (placeholder/thin), growing (has real content), mature (well-developed and verified)
- `order` controls display order within a phase/step
- `tags` enable cross-hub search and filtering

## App Layout

### Home / Dashboard

Landing page showing all hubs as cards. Each card displays:
- Hub title and description
- Progress indicator (how many steps are seed vs growing vs mature)
- Click to enter the hub

### Hub View

Three areas:
- **Left sidebar**: Collapsible tree navigation auto-generated from folder structure. Status indicators (seed/growing/mature) next to each node.
- **Main content area**: Rendered MDX content for the selected step
- **Breadcrumbs**: e.g., `SDLC > System Design > API Design > REST Endpoints`

### Navigation

- Previous / Next buttons at the bottom of content area
- Sidebar tree for jumping anywhere
- Search across all hubs by keyword

## Tech Stack

| Technology | Purpose |
|-----------|---------|
| Next.js 15 (App Router) | Framework, SSG for fast pages |
| MDX (via next-mdx-remote) | Content format — markdown + React components |
| Tailwind CSS | Styling |
| Framer Motion | Animations (expand/collapse, transitions) |
| Vercel | Hosting (free tier, auto-deploy from GitHub) |

No database. No backend. No auth. Content is files, app is a reader.

## Component Library

Reusable MDX components for playbook content:

| Component | Purpose |
|-----------|---------|
| `<Callout type="insight\|warning\|tip">` | Highlighted boxes for key insights |
| `<ExpandableStep>` | Collapsible step with status badge |
| `<Checklist>` | Interactive task checklist |
| `<PhaseHeader>` | Hero section with icon, title, duration, color |
| `<DocOutput>` | Documentation deliverable cards |
| `<ToolTag>` / `<SkillTag>` | Styled chips for tools and skills |
| `<FlowDiagram>` | Text-based flow visualization (A -> B -> C) |
| `<StatusBadge>` | Seed / Growing / Mature indicator |
| `<QuoteBlock>` | Scripture quotes and key insights |

More components can be added over time as content needs evolve.

## Design

Visual design to be discussed separately before implementation. Key decisions:
- Fresh modern design (not carrying over the current warm-tone aesthetic)
- Full custom CSS via Tailwind
- Per-hub color theming
- Detailed design direction TBD in a dedicated design conversation

## What This Is NOT

- Not a CMS — no in-app editing, content is managed as files
- Not a blog — organized by knowledge structure, not chronologically
- Not a wiki — curated and verified, not crowd-sourced
- Not a documentation site — it's a personal playbook with experiential knowledge

## Initial Content

Migrate existing content from:
1. `SDLC/SDLC.md` → 9 phases with checklists, tools, skills, docs
2. `CodeBase Understanding.md` → 11 phases, 13 steps
3. `The Professional Feature Development Lifecycle.md` → 9 phases, 9 steps

Each gets converted to the MDX folder structure with proper frontmatter. Initial status for most steps: "seed" — ready to be deepened over time.
