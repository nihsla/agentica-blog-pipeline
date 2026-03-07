# 🤖 AI Blog Automation Pipeline
### Automated content generation & publishing for agentica.blog

> This is a live, production system powering [agentica.blog](https://agentica.blog) — an AI-focused blog delivering regular content with zero manual writing.

---

## What This Does

This pipeline automatically:

1. **Generates** a full blog post using the Claude AI API, based on a predefined topic queue
2. **Formats** the content for WordPress (title, body, SEO meta, tags, categories)
3. **Publishes** the post to a live WordPress site via the REST API
4. **Logs** each run with timestamps and post URLs for tracking

The entire process — from blank page to published post — runs without human intervention.

---

## Why This Exists

Most businesses have something worth writing about but no time to write it. This pipeline solves that by combining AI content generation with automated publishing, producing consistent, on-brand blog content at scale.

I built this to power my own blog, and I now offer it as a service for business clients who want to:

- Maintain a steady content publishing schedule
- Improve SEO through regular, keyword-targeted posts
- Free up their team from content production bottlenecks

---

## Tech Stack

| Layer | Tool |
|---|---|
| AI Content Generation | [Claude API](https://anthropic.com) (Anthropic) |
| Workflow Orchestration | [n8n](https://n8n.io) (self-hosted via Docker) |
| Publishing Target | WordPress REST API |
| Language | Python 3 |
| Scheduling | n8n cron trigger (KST timezone) |

---

## Project Structure

```
agentica-blog-pipeline/
├── scripts/
│   ├── generate_post.py     # Calls Claude API to write the post
│   ├── publish_post.py      # Sends the post to WordPress
│   └── utils.py             # Shared helpers
├── prompts/
│   └── blog_post_prompt.txt # Prompt templates for Claude
├── config/
│   └── topics.json          # Topic queue (what to write about next)
├── logs/                    # Run history (gitignored)
├── .env.example             # Environment variable template
├── requirements.txt
└── README.md
```

---

## How to Run It

**1. Clone the repo and install dependencies**
```bash
git clone https://github.com/YOUR_USERNAME/agentica-blog-pipeline
cd agentica-blog-pipeline
pip install -r requirements.txt
```

**2. Set up your environment variables**
```bash
cp .env.example .env
# Fill in your API keys and WordPress credentials
```

**3. Run the pipeline manually**
```bash
python scripts/generate_post.py
python scripts/publish_post.py
```

Or let n8n handle it on a schedule automatically.

---

## Live Output

You can see this pipeline in action at **[agentica.blog](https://agentica.blog)**.

Every post on that site was generated and published through this system.

---

## Interested in Using This for Your Business?

I build and configure custom versions of this pipeline for clients. If you want consistent, AI-generated content publishing to your own site:

📩 **[Contact me](mailto:nihsla@gmail.com)**

---

*Built by Albert Shin — AI Consultant & Web Specialist based in Korea and the US.*  
*Specializing in AI-powered automation for Korean and international businesses.*
