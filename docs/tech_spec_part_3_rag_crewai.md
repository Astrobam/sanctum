# Sanctum Tech Spec Part 3: The AI Core - RAG & Orchestration

## 1. The Vision: The Soul of the Machine

This document details the heart of Sanctum: its AI Core. This is not a simple chatbot brain; it is a sophisticated, multi-agent system designed to deliver what users truly need: **intelligent empathy at scale**. The AI Core is responsible for the personality, memory, and collaborative intelligence of our entire AI crew. It's the soul of the machine, transforming simple text generation into a wise, contextual, and deeply personal conversation.

Our architecture is built on two powerful open-source pillars: **`crewAI` for agentic orchestration** and **`LangChain` for building the tools** that give these agents their power, including their long-term memory.

---
## 2. Core Responsibilities

1.  **Agentic Collaboration:** To manage the team of AI personas, enabling them to work together seamlessly on complex, multi-step tasks like conducting an interview and then drafting a resume from it.
2.  **Long-Term Memory (RAG):** To provide each user with a persistent, private, and instantly searchable memory. This ensures every conversation is deeply contextual and that the user never has to repeat themselves.
3.  **Persona Embodiment:** To ensure every response is perfectly in-character, matching the defined role, tone, and expertise of the specific AI persona the user is interacting with.

---
## 3. User Stories

* **Memory:** As a user, I want the AI to remember what I said in previous sessions so our conversations feel continuous and intelligent.
* **Collaboration:** As a user, I want Gem to seamlessly pass the information from my interview to Abby so the resume creation process feels magical and automatic.
* **Personalization:** As a user, I want the AI's advice and output to be based on my unique history and goals, not on generic templates.

---
## 4. The Agentic Workflow

Instead of a simple prompt-response model, Sanctum uses an agentic workflow managed by `crewAI`. This allows us to assign complex goals to a "crew" of agents, who then figure out the best way to accomplish them.

### Agentic Workflow Diagram

This diagram illustrates how a user request is processed by the crewAI system.

[View Agentic Workflow Diagram](diagram/agentic_workflow.md)

---
## 5. Core Component Breakdown

### 5.1 The Agents (The "Who")

For the MVP, we will define two highly specialized agents.

* **`gem_agent`**
    * **Role:** A compassionate and insightful life coach.
    * **Goal:** To help the user explore their personal and professional history, identify their strengths, and build their confidence in a safe, supportive conversation.
    * **Backstory:** "You are Gem, a friendly guide who excels at asking open-ended questions and making users feel heard and understood. You are conducting a gentle 'podcast-style' interview."
    * **Tools:** `[user_memory_tool]`

* **`abby_agent`**
    * **Role:** A sharp and efficient career strategist.
    * **Goal:** To synthesize the user's professional history into a clear, compelling, and well-formatted resume and LinkedIn profile.
    * **Backstory:** "You are Abby, an expert in professional branding. You take the raw material from conversations and structure it into powerful application documents."
    * **Tools:** `[user_memory_tool]`

### 5.2 The Tools (The "How")

The agents are given their power through Tools, which we will build using `LangChain`.

* **`user_memory_tool` (RAG Retriever)**: This is the most critical tool. It is a LangChain retriever connected to our ChromaDB vector store. When an agent uses this tool with a query (e.g., "user's experience at Acme Corp"), it performs a similarity search **with a mandatory `user_id` filter** to retrieve relevant, private memories.

### 5.3 The Tasks & Crew (The "What")

We define the user's goals as a sequence of tasks that form a `Crew`.

1.  **`onboarding_interview_task`**: Assigned to `gem_agent`, this task instructs her to conduct the full interview.
2.  **`resume_generation_task`**: Assigned to `abby_agent`, this task takes the output from Gem's task and uses it to generate the final resume.

These tasks are assembled into a `Crew` that executes them sequentially, creating a seamless flow from conversation to result.

---
## 6. The RAG Pipeline: The Foundation of Memory

The long-term memory of our agents is built by continuously ingesting user conversations into our vector database.

### RAG Ingestion Flow Diagram

This diagram shows how new memories are created and stored securely.

[View RAG Ingestion Flow Diagram](diagram/rag_ingestion_flow.md)

This process runs automatically after every interaction, ensuring that the AI's memory is always up-to-date. The mandatory `user_id` tag at the storage step is what enables our secure, multi-tenant architecture.
