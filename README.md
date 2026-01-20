# 🌍 WayFario: AI-Powered Travel Architect

**WayFario** is a premium travel planning application that leverages autonomous AI agents to curate personalized, high-fidelity itineraries. Built for the modern traveler, it transforms simple travel queries into complete daily plans with structured activity breakdowns, budget estimates, and localized travel tips.

🚀 **Live Demo:** [https://wayfario.onrender.com/](https://wayfario.onrender.com/)

---

## ✨ Key Features

- **Agentic Reasoning:** Powered by **Pydantic AI** and **Gemini 2.5 Flash** to reason through travel logistics and create optimized schedules.
- **Type-Safe Itineraries:** Implements strict Pydantic schema validation to ensure 100% valid JSON responses, eliminating LLM hallucinations.
- **Dynamic Costing:** Provides realistic budget estimations for every activity within the trip to help travelers plan financially.
- **Premium UI/UX:** A high-end interface built with **Tailwind CSS**, featuring custom animations (Animate.css) and a responsive, mobile-first design.
- **Secure Deployment:** Built using industry-standard environment variable management to protect sensitive API credentials.

---

## 🛠️ Technology Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | Python, FastAPI |
| **AI Framework** | Pydantic AI (Agentic Orchestration) |
| **LLM** | Google Gemini 2.5 Flash |
| **Frontend** | HTML5, Tailwind CSS, JavaScript (ES6+) |
| **Styling** | Plus Jakarta Sans Fonts, Animate.css |
| **Hosting** | Render (CI/CD via GitHub) |

---

## 📂 Project Structure

```text
WayFario/
├── main.py              # FastAPI server & AI Agent logic
├── requirements.txt     # Python dependencies
├── templates/
│   └── index.html       # Single-page application frontend
├── .gitignore           # Security rules (excludes .env)
└── README.md            # Documentation
