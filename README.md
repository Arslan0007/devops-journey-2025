# 🚀 DevOps & AI Journey 2025
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat&logo=python)![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit)
![Status](https://img.shields.io/badge/Status-Active_Development-green)

**From Embedded Systems to Intelligent Agents.**
This repository documents my engineering journey as I transition from a background in UAV R&D and Technical Project Management to **AI Engineering and DevOps**.

Here, I build and deploy real-world applications to master the modern software lifecycle—focusing on Python, Containerization, and AI integration.

---

## 📂 Featured Project: The Gist
**Status:** *In Development*

> **Problem:** Information overload makes it hard to distinguish noise from signal.
> **Solution:** A "digital declutter" assistant that processes text and returns the bottom line.

In an age of information overload, **The Gist** is a "digital declutter" assistant designed to cut through the noise. It processes large blocks of text and returns exactly what you need to know.

### Core Features
* **The Bottom Line:** Generates a one-sentence summary of the input text.
* **Action Items:** Automatically extracts tasks and "to-dos."
* **Urgency Score:** Analyzes the tone to determine priority.

### Tech Stack
* **Language:** Python 3.x
* **Frontend:** Streamlit
* **Logic:** NLP / Text Processing (Planned integration with LLMs)

## 🚀 Quick Start
To run this project locally:

1. **Clone the repository**
   ```bash
   git clone [https://github.com/Arslan0007/devops-journey-2025.git](https://github.com/Arslan0007/devops-journey-2025.git)
   cd devops-journey-2025 
   ``` 

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App**
   ```bash
   streamlit run main.py
   ```

## 🛠️ Technical Architecture
This MVP is built on a lightweight, deployable stack:

* **Frontend (Streamlit):** Chosen for its ability to rapidly turn data scripts into shareable web apps without needing a separate React/Vue frontend.
* **NLP Engine (TextBlob):** Used for the initial backend logic to handle part-of-speech tagging and sentiment analysis.
    * *Why TextBlob?* It provides a simple API for common NLP tasks, making it perfect for the MVP phase before integrating heavier LLMs (like OpenAI/Llama).
* **Python 3.x:** The core logic handles the scoring algorithms for "Urgency" and extracts actionable keywords.

---

## 🗺️ The Roadmap
I am building this repository "in public" to demonstrate competency in the following areas:

- [x] **Python Application Development** (Building "The Gist")
- [ ] **Containerization:** Dockerizing the application for consistent environments.
- [ ] **CI/CD:** Setting up pipelines (GitHub Actions) for automated testing.
- [ ] **Cloud Deployment:** Hosting the application on a cloud provider (AWS/GCP).
- [ ] **Infrastructure as Code (IaC):** Managing resources with Terraform/Ansible.

---

## 👨‍💻 About Me
I am an **Independent R&D Engineer** with a background in **UAV Systems** and **Computer Vision**. I have managed complex technical projects, from autonomous drone targeting systems to ERP implementations. I am now applying that same engineering rigor to build scalable software solutions.

* **LinkedIn:** [Naci Arslan](https://www.linkedin.com/in/arslan-naci)
* **Focus:** AI Agents, DevOps, Python, Computer Vision

---
*“The best way to master a technology is to ship it.”*