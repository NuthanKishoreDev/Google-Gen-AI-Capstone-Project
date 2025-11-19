# JourneyWeaver AI Agent (Google-Gen-AI-Capstone-Project)

JourneyWeaver AI Agent is a multi-agent travel planning system that automatically researches destinations, builds personalized itineraries, and optimizes trips with smart, real-time insights.

Below is your **complete, polished, submission-ready capstone documentation** for your project:

# 🌍 **JourneyWeaver AI Agent**

### *End-to-End Automated Travel Planning System*

**Capstone Project Documentation — Google AI Agents Course**

---

# 1. **Project Overview**

**JourneyWeaver AI Agent** is a multi-agent travel planning system built using **Google ADK**, **Gemini 2.5 Flash**, and **Google Search Tools**.

It automates the entire travel planning workflow:

* Researching destinations
* Creating structured itineraries
* Optimizing travel plans with practical advice

This project showcases multi-agent orchestration, tool usage, LLM reasoning, function calling, and dynamic research automation learned during the course.

The final deliverable demonstrates a real-world, production-ready AI agent that reduces travel planning time from **6–10 hours to under 1 minute**.

---

# 2. **Track Selection**

**Selected Track:**

### 🧭 *Research & Automation Agents*

This track focuses on agents that gather information, process data, and perform multi-step automated tasks — perfectly aligned with the requirements of travel planning.

---

# 3. **Problem Statement**

Planning travel is traditionally a **time-consuming, fragmented, and manual** process.
Travelers often need to:

* Research weather, seasons, and safety
* Identify attractions and must-visit spots
* Build day-by-day itineraries
* Estimate budgets, commute, and timing
* Search for local tips and backup plans

This process usually requires visiting **10+ different websites**, cross-checking sources, and manually assembling information.

This results in:

* **High time expenditure**
* **Inconsistent planning quality**
* **Overwhelm due to information overload**
* **Difficulty optimizing for budget, weather, or preferences**

---

# 4. **Solution Pitch**

**JourneyWeaver AI Agent** solves this problem using a **three-stage sequential agent system**.

### ✔ It researches the destination

✔ Builds a complete day-wise travel itinerary
✔ Optimizes the plan with budget tips, packing lists, backups, and cultural guidance

Powered by **Gemini 2.5 Flash**, **Google Search**, and **SequentialAgent logic**, JourneyWeaver becomes a **personal AI travel concierge**.

### **Key agent capabilities:**

* Live Google Search research
* AFC-based decision-making
* Multi-agent pipeline
* Rich, structured output
* Practical travel insights
* Budget-conscious planning
* Reliability with retry logic (429/500/503 handling)

---

# 5. **Architecture Overview**

JourneyWeaver is built using a **Sequential Multi-Agent Architecture**.

## **5.1 System Diagram**

```
User Input
    ↓
DestinationResearchAgent
    ↓
ItineraryBuilderAgent
    ↓
TravelOptimizerAgent
    ↓
Final Optimized Travel Plan
```

---

# 6. **Agent Components**

## 6.1 **Agent 1: DestinationResearchAgent**

**Role:** Travel Researcher
**Tools:** Google Search
**Outputs:**

* Weather & best time to visit
* Top attractions
* Local culture & customs
* Safety guidelines
* Transportation modes

This agent gathers **real-time data** using Google Search Tool and provides structured research output.

---

## 6.2 **Agent 2: ItineraryBuilderAgent**

**Role:** Travel Planner
**Input:** Research output from Agent 1
**Outputs:**

* Day-by-day itinerary
* Recommended timings
* Accommodation zones
* Dining suggestions
* Budget estimation per day

Creates a practical, usable itinerary like a professional travel agent.

---

## 6.3 **Agent 3: TravelOptimizerAgent**

**Role:** Expert Travel Consultant
**Input:** Itinerary output
**Outputs:**

* Budget hacks
* Packing recommendations
* Weather-related backup plans
* Cultural do’s & don’ts
* Helpful local apps, websites, or resources

Formats the final answer into a clean, user-friendly structure:

```
ITINERARY: ...
OPTIMIZATION TIPS: ...
TRAVEL ESSENTIALS: ...
BACKUP PLANS: ...
```

---

# 7. **Technical Design & Configuration**

### ✔ Google ADK

### ✔ Gemini 2.5 Flash

### ✔ google_search Tool

### ✔ Sequenced multi-agent pipeline

### ✔ Retry Options

### ✔ AFC (Automatic Function Calling)

### ✔ Pydantic-driven ToolConfig

### ✔ Up to 20 remote tool calls supported

---

# 8. **Code Repository**

Add your link here:

📎 **GitHub Repository:** *[https://github.com/NuthanKishoreDev/Google-Gen-AI-Capstone-Project](Google-Gen-AI-Capstone-Project)*

📎 **Kaggle Notebook:** *[https://kaggle.com/your-notebook](https://kaggle.com/your-notebook)*

---

# 9. **How the JourneyWeaver AI Agent Works**

### **Step 1 — User Input**

User gives:

* Destination
* Trip duration
* Preferences
* Budget

Example prompt:

> “Plan a 6-day budget trip to Tokyo with food, culture, and public transportation focus.”

---

### **Step 2 — Destination Research**

The agent calls Google Search, compiles reliable insights, and produces a research summary.

---

### **Step 3 — Itinerary Building**

The Itinerary agent converts research into a structured day-wise plan.

---

### **Step 4 — Optimization Layer**

Adds budget tips, essentials, contingency plans, and cultural pointers.

---

### **Step 5 — Final Output Delivery**

The user receives a **full optimized travel plan** ready to execute.

---

# 10. **Value & Impact**

JourneyWeaver AI Agent provides:

### ✔ **Time Savings**

Reduces planning time from **6–10 hours → under 60 seconds**

### ✔ **High Accuracy**

Search-backed and systematically verified information

### ✔ **Consistency**

Same quality every time, adaptable to any destination

### ✔ **Customization**

Meals, budget, pace, weather preferences, etc.

### ✔ **Practicality**

Backup plans, packing lists, and cultural insights

### ✔ **Scalability**

Can power:

* Travel agencies
* Tourism apps
* Personal travel assistants
* Chatbots
* LLM workflows
---

