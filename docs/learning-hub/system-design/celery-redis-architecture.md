# Celery + Redis — Background Task Processing

**What it is:** Celery is a system that runs tasks in the background (separate from your main web server). Redis is the "mailbox" that holds tasks until a worker picks them up.

**Why it matters for the bot:** The bot needs to scrape Crunchbase and HN on a schedule — without blocking the web server. Celery does this work silently in the background while Django stays responsive.

**The mental model:**

```
Post office analogy:

Celery Beat   = The person who writes letters on a schedule
Redis         = The mailbox (holds the letters)
Celery Worker = The postman who picks up letters and delivers them
```

**Real example from the bot:**

```
Every 6 hours:
  Celery Beat  → drops "scrape_crunchbase" task into Redis
  Celery Worker → picks it up → hits Crunchbase API → scores result → saves to PostgreSQL
```

**Why Celery over simpler options:**

| Option | Problem |
|--------|---------|
| Simple cron job | No retry on failure, no monitoring, not scalable |
| APScheduler | Simpler but less production-grade, fewer features |
| **Celery + Redis** ✅ | Retries, monitoring, scalable workers, industry standard |

**Key components:**

- **Celery Beat** — the scheduler. Fires tasks on a schedule (like cron but smarter).
- **Celery Worker** — the executor. Actually runs the task code.
- **Redis** — the broker. Passes tasks from Beat → Worker.
- **Task** — a Python function decorated with `@celery.task`

**The "always-on" insight:** The bot is an *opportunity listener*, not a *request handler*. It doesn't wait for you to click something — it runs 24/7 watching for signals. That's why we need Celery instead of just Django views.

**Related concepts:** [[django-drf]], [[postgresql]], [[system-architecture-diagram]]
