# Sanctum Tech Spec Part 2: The Frontend Experience

## 1. The Vision: The Face of the Sanctuary

If the backend is Sanctum's central nervous system, the frontend is its face and soul. This is where our sanctuary becomes tangible. It is the warm, welcoming room where the user meets their companions, shares their story, and sees their confidence reflected back at them. Our primary goal is to create an experience that is not just functional, but **immersive, intuitive, and beautiful**. The technology must be invisible, the interactions fluid, and the atmosphere one of calm focus.

This document outlines the architecture of the React-based single-page application that will deliver this experience.

---
## 2. Core Responsibilities

1.  **Secure User Interface:** To provide secure forms for user registration and login, and to manage the user's authentication state throughout their session.
2.  **Immersive Conversation View:** To render the chat history cleanly and present the AI personas as living, breathing avatars that react and speak in real-time.
3.  **Real-time State Management:** To manage the application's state efficiently, ensuring the UI is always a perfect reflection of the current conversation and user status.
4.  **Seamless API Communication:** To communicate with the backend API reliably and efficiently, handling data fetching, message sending, and error states gracefully.

---
## 3. User Stories

* **First Impression:** As a user, I want to be greeted by a clean, calming interface so that I immediately feel comfortable and safe.
* **Immersive Interaction:** As a user, I want to see a life-like avatar that makes eye contact and moves its lips when the AI speaks, so that the conversation feels deeply personal and engaging.
* **Effortless Chat:** As a user, I want a simple, uncluttered chat interface so that I can focus entirely on the conversation without distraction.
* **Proactive Engagement:** As a user, I want to receive browser notifications for important check-ins or reminders so that Sanctum can help me stay on track even when the app isn't open.

---
## 4. Component Architecture

Our frontend will be built using a modular, component-based architecture in React.

### Component Hierarchy Diagram

This diagram visualizes the primary components and their relationship to our global state managers.

[View Frontend Component Hierarchy Diagram](diagram/frontend_component_hierarchy.md)

### Key Component Descriptions

* **`ChatView.tsx`**: The main screen post-authentication. This component orchestrates the entire conversational experience, composing the `AvatarCanvas`, `MessageList`, and `MessageInput` together.
* **`AvatarCanvas.tsx`**: This is the heart of our immersive experience. It's a React Three Fiber component responsible for rendering the 3D avatar. Its logic is critical:
    1.  It loads the appropriate `.vrm` model for the current persona (Gem or Abby).
    2.  It uses the browser's Text-to-Speech (TTS) engine to generate audio from the AI's text response.
    3.  Crucially, it hooks into the TTS audio stream using the **Web Audio API**'s `AnalyserNode`.
    4.  In every render frame, it gets the current audio volume from the `AnalyserNode` and maps this value to the VRM model's pre-defined mouth blendshapes (e.g., `model.blendShapeProxy.setValue('a', volume)`), creating a seamless, real-time lip-sync effect.
* **`MessageList.tsx`**: A simple, performant component that renders the list of messages. It will use virtualization (e.g., `react-window`) to efficiently handle very long conversation histories.

---
## 5. State Management

We will use **Zustand** for global state management due to its simplicity, minimal boilerplate, and excellent performance.

* **`authStore`**: Will hold the user's authentication token, profile information, and isAuthenticated flag.
* **`chatStore`**: Will manage the state of the active conversation, including the list of messages, the current persona, and loading/error states.

This centralized state ensures that all components have a single source of truth, preventing inconsistencies and simplifying the data flow throughout the application.
