# Autonomous Brand Manager Agent

An Agentic AI system that operates as an autonomous digital marketer. Unlike linear automations, this agent utilizes a reasoning loop to monitor e-commerce inventory, make independent decisions about what needs to be promoted, and use tools to draft, review, and schedule marketing campaigns.

Instead of manually checking stock and writing posts, this system gives an AI agent access to your inventory database and social media scheduling tools, allowing it to execute your brand's Standard Operating Procedures (SOPs) autonomously.

---

## Agentic Workflow Execution

The agent operates on a ReAct (Reason + Act) loop. Upon execution, the agent observes the current inventory state, reasons about which products require urgent movement, uses tools to generate highly targeted copy, and finally executes API calls to schedule the content.

---

##  Project Overview

This project demonstrates how e-commerce brands can deploy Agentic AI using Python, LangChain, Claude AI, Claude Code, and mock external tools (Shopify API & Buffer API).

The system begins when the scheduled CRON job wakes the agent. The agent is provided with a system prompt defining its persona and given access to specific tools (e.g., `check_inventory()`, `write_copy()`, `schedule_post()`). It autonomously decides which tools to use and in what order, routing its own outputs based on the results of its actions.

Each execution creates a unique trace of the agent's "Thought -> Action -> Observation" process.

---

## Agent Capabilities

*   **Autonomous Tool Selection:** Chooses the right tool for the job without human intervention.
*   **Inventory Observation:** Uses API tools to fetch real-time product data and margins.
*   **Urgency Reasoning:** Calculates stock-to-sales ratios to identify overstocked SKUs.
*   **Platform-Specific Generation:** Adapts tone for Twitter, Instagram, and Email.
*   **Self-Correction:** Validates character counts and formatting before attempting to post.
*   **Memory Management:** Logs executed campaigns to prevent spamming the same product.

---

## Agent Configuration

![Agent Configuration Demonstration](./assets/agent-configuration.png)

---

## Agent State & Memory Log

The agent maintains a memory log (vector database or flat file) to remember past actions and track campaign status.

| Product SKU | Stock Level | Agent Decision | Executed Tools | Status |
| :--- | :--- | :--- | :--- | :--- |
| SKU-9921 | 185 (High) | Needs immediate promotion | `generate_ig_post`, `schedule_buffer` | Completed |
| SKU-4012 | 12 (Low) | Skip promotion | None | Skipped |

---

## Agentic Architecture Overview

```text
[ Trigger: Daily CRON ]
       │
       ▼
[ Initialize Agent with System Prompt & Tools ]
       │
       ▼
[ Observation ] ◄────── Use Tool: get_inventory()
       │
       ▼
[ Reasoning ] ────────► "SKU-9921 is overstocked. I need to run a flash sale."
       │
       ▼
[ Action ] ◄─────────── Use Tool: generate_copy(SKU-9921, platform="Slack")
       │
       ▼
[ Verification ] ─────► "Does this meet brand guidelines?"
       │
       ▼
[ HITL Approval ] ────► Use Tool: send_slack_approval() -> Wait for human input
       │
       ▼
[ Execution ] ────────► Use Tool: schedule_campaign() (Only if Approved)
```

---

## Tech Stack

| Component | Technology |
|----------|----------|
| Agent Framework | LangChain / LangGraph |
| LLM Reasoning Engine | Anthropic Claude 3.5 Sonnet |
| Memory / State | SQLite / JSON |
| Tools (Mocked) | Shopify API, SendGrid, Buffer |
| Version Control | GitHub |

---

## Respository Structure

```
.github/
    workflows/             # CI/CD pipelines (GitHub Actions)
agent/
    main.py                # Core agent ReAct loop
    tools.py               # Shopify and Buffer mock API tools
    prompts.py             # System prompts and personas
    test_tools.py          # Pytest file for tool testing
assets/
    workflow-execution.jpg # Visual proof of life
docs/
    architecture.md        # System design
    setup-guide.md         # Instructions to run the agent
    tool-definitions.md    # API tool documentation
.gitignore
LICENSE
README.md
requirements.txt           # Python dependencies
```

