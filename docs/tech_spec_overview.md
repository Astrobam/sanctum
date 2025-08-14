# Sanctum: A Technical Vision

## 1. The Mission: A Sanctuary for Ambition

The modern career journey is a paradox: more connected than ever, yet profoundly lonely. Professionals, especially those battling insecurity, are given tools—resume builders, job boards—but not the one thing they truly need: a confidant. The process is a silent, solitary struggle against self-doubt and the blank page.

**Sanctum is the answer.**

We are not building another tool. We are crafting a **sanctuary**. A private, intelligent space where ambition is nurtured, confidence is built, and careers are forged through conversation. Sanctum is a team of dedicated AI companions—a coach, a strategist, a tutor—who listen, understand, and guide. Our mission is to transform the isolating ordeal of career development into an empowering, collaborative journey. This document outlines the technical vision for bringing that mission to life.

---
## 2. Guiding Principles: The DNA of Sanctum

Our architecture is built upon a foundation of core principles that reflect our mission.

* **A Sanctuary of Trust:** Security is our bedrock. Every technical decision, from data encryption to authentication, is made with the explicit goal of creating an inviolable, private space for our users. Trust is not a feature; it is our entire product.
* **A Living Conversation:** The user experience must be seamless, fluid, and instantaneous. The technology must disappear, leaving only the sense of a real, present conversation. This demands a high-performance, asynchronous, and real-time architecture.
* **Intelligent Empathy at Scale:** Our AI must be more than just smart; it must be wise. It needs memory, context, and the ability to understand the unspoken. Our RAG and Agentic systems are designed to provide this deep, personalized empathy to every user, 24/7.
* **Modular & Future-Ready:** The world of AI is evolving at a breathtaking pace. Our system is designed to be modular, allowing us to upgrade components—like swapping in a more advanced LLM or a new avatar engine—without rebuilding from the ground up.

---
## 3. High-Level Architecture

Sanctum is a service-oriented application composed of three primary systems working in concert: the **Frontend Client**, the **Backend API**, and the **AI Core**.

### Component Architecture Diagram

This diagram shows the high-level relationship between the core systems. The user interacts only with the Frontend, which communicates with the Backend. The Backend acts as a secure orchestrator, managing data and making requests to the AI Core.

[View Component Architecture Diagram](./diagram/component_architecture.md)

---
## 4. The Technology Stack: Tools for a New Experience

Our technology choices are deliberate, prioritizing performance, security, and a rich user experience.

| Component | Technology | Rationale |
| :--- | :--- | :--- |
| **Backend Framework** | **FastAPI** (Python) | Chosen for its blazing-fast, asynchronous performance which is essential for a real-time conversational feel. Its automatic data validation with Pydantic ensures API security and reliability. |
| **Frontend Framework**| **React** (with Vite) | The gold standard for building complex, interactive user interfaces. Vite provides a lightning-fast development experience, allowing us to iterate quickly. |
| **AI Orchestration** | **crewAI** | We're building a team of AIs, not a single chatbot. crewAI provides a sophisticated framework for defining our personas as distinct "Agents" with unique goals and tools, enabling complex, collaborative tasks. |
| **RAG Toolkit** | **LangChain** | The foundational toolkit for connecting LLMs to external data. It provides the robust, pre-built components needed to give our AI crew a reliable long-term memory. |
| **Avatar Engine** | **@pixiv/three-vrm** | This is our "out-of-the-box" solution for avatars. It's a high-level library that handles the immense complexity of rendering, animating, and lip-syncing standardized VRM avatars, allowing us to focus on the user experience instead of low-level 3D graphics. |
| **User Database** | **PostgreSQL** | The gold standard for reliable, structured data storage. It will house all user account information, conversation metadata, and application state. |
| **Vector Database** | **ChromaDB** | A powerful, open-source vector store designed for AI applications. Its support for metadata filtering is critical for our multi-tenant security model. |

---
## 5. Key System Flows

### User Authentication Flow

Security begins at the front door. We will use a standard, secure JWT-based flow to authenticate users.

[View User Authentication Flow Diagram](./diagram/auth_flow.md)

### The Core Conversational Loop

This is the journey of a single message, the lifeblood of Sanctum.

[View Core Conversational Loop Diagram](./diagram/conversational_loop.md)

---
## 6. The MVP: The First Chapter

Our MVP is the first, critical chapter of the Sanctum story. It is designed to deliver our most unique value proposition: turning a daunting task into an empowering conversation.

* **The Narrative:** A user logs in, feeling anxious about their resume. They are greeted by **Gem**, a warm and engaging persona. Through a natural "podcast-style" interview, Gem helps the user articulate their entire professional story. At the end of the conversation, **Abby**, the sharp strategist, presents them with a beautifully formatted, professional resume generated from their own words.
* **The Experience:** The user leaves their first session not with just a document, but with a newfound sense of clarity and confidence. They have been seen, heard, and understood.

This focused MVP establishes our core promise and builds the foundation for the full "crew" of personas to come.
