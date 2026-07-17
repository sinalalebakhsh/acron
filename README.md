# 🚀 ACRON: Enterprise Django Reference Architecture

> *"Plant the acorn seed, and it will grow into a mighty oak."*

**ACRON** is an open-source reference architecture designed to bridge the gap between basic Django tutorials and real-world, enterprise-grade software engineering. It provides a structured, step-by-step development roadmap for both Junior and Senior developers. 

Our core philosophy follows the **80/20 Rule**:
* **80% Progress Structure & Engineering:** Strict adherence to clean architecture, scalability, financial data integrity, and industry best practices.
* **20% Creativity & "Artomize":** Leaving room for developer innovation, flexibility, and randomized artistic problem-solving!

---

## 🔗 Documentation & Methodology
* 📖 **Core Methodology Documentation:** [Read Documentation Parts](https://github.com/sinalalebakhsh/acron/blob/main/Documentation.md)
* 🧠 **Project Roadmap & Introduction:** [View on Notion](https://sinalalenakhsh.notion.site/ACRON-387da1eb8b9d8005a372ce7394463792)
* 🤝 **Contributing Guide:** [How to Contribute](https://github.com/sinalalebakhsh/acron/blob/main/CONTRIBUTING.md)

---

## 🏛️ Architecture & Technical Highlights (What We Built)

Unlike standard Django apps that rely on "Fat Views" or messy serializers, ACRON is built upon a **production-ready, highly decoupled architecture**:

* **True Service-Layer Architecture:** Complete separation of concerns. HTTP requests and formatting live in Views/Serializers, while 100% of the business logic is isolated in highly testable `services.py` modules.
* **Financial Integrity & ACID Compliance:** Utilization of `@transaction.atomic` boundaries, immutable order snapshots (freezing historical prices), and automated Time-To-Live (TTL) expiration mechanisms for inventory safety.
* **Database & Query Optimization:** Built-in protection against N+1 query disasters using Django ORM's `select_related` and `prefetch_related`.
* **Enterprise Security:** Implementing non-sequential UUID primary keys for sensitive domains (Carts, Orders) and strict JWT authentication flows.
* **Modern API Documentation:** Fully automated, interactive OpenAPI 3.0 documentation integrated via `drf-spectacular` (Swagger UI & Redoc).

---

## 👥 Who Are You? (Welcome to the Community!)

We believe in open, collaborative software development. No matter your current role, there is a place for you here:

* 💻 **Can you be a contributor to this project?** **Yes!** Check our contributing issues and submit a PR.
* 🚪 **Can you invite yourself into this project?** **Yes!** This is an open-source initiative built for the community.
* 👁️ **Can you just be a visitor exploring the code?** **Yes!** Feel free to use ACRON as an architectural template for your own projects.
* 📈 **Can you invest in or adopt this reference project?** **Yes!** It is built to scale for commercial and financial systems.
* 🔍 **Can you be a code reviewer?** **Yes!** We welcome architectural critiques and code reviews.

---

## 🗺️ Roadmap & Future Developments

We are actively developing and expanding the architecture. Next steps in our roadmap include:
- [x] **API Documentation:** Integrated OpenAPI 3.0 / Swagger UI.
- [x] **Payment Gateway Domain:** Connecting orders to banking interfaces with secure callback handling.
- [x] **MCP:** Model Context Control to Responsing interfaces with secure callback handling.
- [ ] **Asynchronous Background Tasks:** Integrating Celery and Redis for automated inventory release and notification systems.
- [ ] **Shared Core Services:** Expanding `core/services.py` for enterprise SMS, Email, and PDF generation.

---

## 🤖 Our Philosophy on AI & Code Quality: No "Vibe Coding"

We explicitly **do not use "Vibe Coding"** in this project. 

Copy-pasting unverified AI-generated code without understanding the underlying architectural mechanics is the number one trap for modern developers. In the ACRON ecosystem, **artificial intelligence is treated strictly as an assistant and a tool—nothing more, nothing less.** The core architecture, database schema design, and domain logic are driven by human engineering and critical thinking.

We acknowledge the assistance of the following AI tools in debugging, translating, and refining code details:
* [Gemini](https://gemini.google.com/)
* [Claude](https://claude.ai/)
* [ChatGPT](https://chatgpt.com)
* [Chat Z AI](https://chat.z.ai) / [DeepSeek](https://chat.deepseek.com/)
* [OCR & Converting Tools](https://ocr.z.ai/)
* [Image & Design Assistants](https://image.z.ai/)

### 🌍 A Note from the Founder
Despite the severe challenges and limitations imposed by geographical sanctions on developers in Iran, this project was developed with passion, resilience, and the aid of modern technology. **It is my sincere hope that a future of friendly relationships, open collaboration, and borderless connection will be established between Iranian developers and the global tech community.**


### How to run
* after cloning
* write in Terminal:  pipenv shell
* than: pipenv install Pipefile.lock

