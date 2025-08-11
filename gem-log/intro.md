# Project Brief: Sanctum

**Version:** 2.0
**Date:** August 11, 2025

## 1. Executive Summary

This document outlines the vision, MVP scope, and technical architecture for **Sanctum**, an AI-powered web application designed to serve as a personal and professional life coach. The application's primary goal is to help users advance their careers through personalized guidance, skill development, and application assistance. The user experience will be highly immersive and conversational, utilizing real-time animated avatars to create the feeling of interacting with a dedicated team of AI assistants within a safe and supportive environment.

## 2. Target Audience

### 2.1 Primary Target Audience 🎯

Our ideal user is the **ambitious, tech-savvy professional (ages 22-35)** who is actively seeking career growth but feels overwhelmed, insecure, or inefficient in their job search. This group, particularly women, will be drawn to the app's promise of a safe, non-judgmental space for building confidence and skills.

### 2.2 Secondary Audiences

* **Recent Graduates:** Seeking foundational guidance on building their first resume and navigating the job market.
* **Career Changers:** Individuals of any age who need to identify skill gaps and reframe their experience for a new industry.

## 3. The Full Vision

The long-term vision is to create a holistic AI companion that assists users in all facets of their career journey and provides personal support.

### 3.1 Core Concept

An AI team that helps users secure better employment through a deeply personalized, conversational experience. The application will understand the user's past, assess their present skills, and guide them toward their future goals.

### 3.2 The AI Personas ("The Crew")

The user interacts with a team of distinct AI personas, each with a specialized role:

* **Gem:** The Coach & Daily Companion for mindset, routine, and well-being.
* **Abby:** The Application Strategist for resumes, cover letters, and interview-specific preparation.
* **Arthur:** The Job Finder & Evaluator.
* **Sheldon:** The Tutor for personalized skill development.

### 3.3 User Experience

The interaction is designed to be audio/visual, simulating a "podcast with friends." The user will see and speak with real-time animated avatars for each persona, creating an engaging and personal connection.

## 4. The Minimum Viable Product (MVP)

The MVP will concentrate on delivering the most critical and unique value propositions first.

### 4.1 MVP Goal

To provide a user with a professionally written, generic resume and LinkedIn profile through a novel, conversational, and visual onboarding experience, while establishing a foundation for daily, proactive engagement in a secure environment.

### 4.2 MVP Features (In Scope)

* **Core Personas:** Gem and Abby.
* **Onboarding:** A "podcast-style" conversational interview with Gem's avatar.
* **Document Generation:** Abby generates a generic resume and LinkedIn profile summary.
* **Real-Time Avatars:** A simplified implementation of real-time animated avatars.
* **Proactive Assistance:** Daily briefings from Gem and calendar-aware application reminders from Abby via browser notifications.

### 4.3 Deferred Features (Out of Scope for MVP)

* The Arthur and Sheldon personas.
* Advanced job-to-resume customization and cover letter generation.
* Skill assessment and daily training modules.

## 5. Technical Architecture & Security

### 5.1 Multi-Tenancy & Scaling Strategy

The RAG system will be built for scale from day one. We will use a single, shared vector database instance. User data will be strictly isolated using **metadata filtering**. Every piece of data and every query will be tied to a `user_id`, ensuring a user can only ever access their own information. The infrastructure will be based on managed cloud services (e.g., Pinecone, Weaviate Cloud Services) to handle scaling automatically.

### 5.2 Security & Encryption Strategy

Security is paramount for Sanctum. We will employ a multi-layered encryption strategy:
* **Encryption in Transit:** All network communication will be protected with industry-standard TLS encryption.
* **Encryption at Rest:** All data stored in the database will be encrypted on disk by the cloud provider using AES-256.
* **Future Enhancements:** Application-level encryption can be added later for ultimate security, where user text is encrypted before even being stored in the database.

### 5.3 Core Technology Stack

| Component | Technology Decision | Rationale (Why) |
| :--- | :--- | :--- |
| **Agent Orchestration** | **crewAI** | Perfectly maps to our multi-persona concept and provides high-level orchestration for our AI "crew." |
| **Long-Term Memory (RAG)** | **LangChain**, **ChromaDB**, **Sentence-Transformers** | Provides the RAG plumbing for persona memory. These tools are open-source, powerful, and support the required metadata filtering for multi-tenancy. |
| **Real-Time Avatars** | **Three.js/R3F**, **VRM format**, **Web Audio API** | Enables a low-latency, interactive, and conversational experience. The VRM format provides a standard for web-ready, animatable avatars. |