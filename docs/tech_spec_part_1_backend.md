# Sanctum Tech Spec Part 1: The Backend Core & API

## 1. The Vision: The Central Nervous System

The backend is the heart of Sanctum. It is the central nervous system that powers every interaction, safeguards every secret, and ensures every conversation is fluid, reliable, and secure. It is more than just a collection of endpoints; it is the trustworthy foundation upon which our sanctuary is built. Its design prioritizes three pillars: **impenetrable security**, **instantaneous performance**, and **rock-solid reliability**.

This document details the architecture of this system, from the user's first registration to the complex flow of a real-time AI conversation.

---
## 2. Core Responsibilities

The backend has three primary duties:
1.  **Identity & Access Management:** To securely manage user identities, providing robust authentication and ensuring that each user's sanctuary is for their eyes only.
2.  **Data Persistence:** To reliably store and retrieve all user-related data, including profiles, conversation history, and the memories that give our AI personas their context.
3.  **Secure Gateway to the AI Core:** To act as the sole, secure conduit between the user-facing application and our powerful AI Core, orchestrating the flow of information seamlessly.

---
## 3. User Stories

These stories define our backend requirements from a user's perspective.

* **Registration:** As a new user, I want to create an account with my email and a secure password so that I can establish my own private sanctuary.
* **Authentication:** As a returning user, I want to log in quickly and securely so I can seamlessly resume my journey.
* **Interaction:** As an authenticated user, I want to send a message to an AI persona and receive a response in real-time so the conversation feels natural and fluid.
* **Persistence:** As a user, I want my conversation history to be saved automatically so that both I and my AI companions can refer back to it at any time.

---
## 4. Database Schema: The Foundation of Memory

We will use PostgreSQL for its reliability and strong data integrity. The schema is designed to be simple, robust, and centered around the user.

### Entity Relationship Diagram (ERD)

This diagram illustrates the relationships between our core data tables.

[View Database ERD](diagram/database_schema.md)

### Table Definitions

* **`users`**
    * `user_id` (UUID, PK): Unique identifier for each user.
    * `email` (VARCHAR, UNIQUE): User's login email.
    * `hashed_password` (VARCHAR): Securely hashed and salted password.
    * `created_at` (TIMESTAMPTZ): Timestamp of account creation.

* **`conversations`**
    * `conversation_id` (UUID, PK): Unique identifier for a chat session.
    * `user_id` (UUID, FK -> users.user_id): Links the conversation to a user.
    * `persona` (VARCHAR): The AI persona for this conversation (e.g., "Gem", "Abby").
    * `created_at` (TIMESTAMPTZ): Timestamp of conversation start.

* **`messages`**
    * `message_id` (UUID, PK): Unique identifier for each message.
    * `conversation_id` (UUID, FK -> conversations.conversation_id): Links the message to a conversation.
    * `sender` (VARCHAR): Who sent the message ("user" or "ai").
    * `content` (TEXT): The actual text of the message.
    * `timestamp` (TIMESTAMPTZ): When the message was sent.

---
## 5. API Specification

The API is the contract between the frontend and the backend. It will be RESTful, secure, and intuitive. All endpoints are prefixed with `/api/v1`.

### 5.1. Authentication (`/auth`)

This flow governs how users securely access their sanctuary.

[View Authentication Sequence Diagram](diagram/auth_flow.md)

* **`POST /auth/register`**
    * **Description:** Creates a new user account. Hashes the password using a strong algorithm (e.g., bcrypt) before storing it.
    * **Request Body:** `{ "email": "user@example.com", "password": "Str0ngP@ssw0rd!" }`
    * **Success Response (201 Created):** `{ "user_id": "...", "email": "..." }`

* **`POST /auth/token`**
    * **Description:** Authenticates a user and returns a JWT access token.
    * **Request Body (Form Data):** `{ "username": "user@example.com", "password": "..." }`
    * **Success Response (200 OK):** `{ "access_token": "...", "token_type": "bearer" }`

### 5.2. Core Interaction (`/conversations`)

This is the primary endpoint for user-AI interaction.

* **`POST /conversations/{conversation_id}/messages`**
    * **Description:** The heart of the application. It receives a user's message, orchestrates the AI response, and saves the interaction.
    * **Auth:** JWT required.
    * **Request Body:** `{ "content": "Hello, Gem. I'm feeling a bit stuck." }`
    * **Success Response (200 OK):** An object containing the AI's full message. `{ "message_id": "...", "sender": "ai", "content": "I understand. It's okay to feel stuck. Let's talk about it. Where do you feel the 'stuckness' is coming from?" }`

### Message Processing Flow

This diagram illustrates the backend journey of a single user message.

[View Message Processing Flow Diagram](diagram/message_flow.mmd)

* **`GET /conversations/{conversation_id}`**
    * **Description:** Retrieves the message history for a specific conversation.
    * **Auth:** JWT required.
    * **Success Response (200 OK):** A list of message objects, ordered by timestamp.
