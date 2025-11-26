# 🔬 ResearchLab-AI: Autonomous Multi-Agent Research System

ResearchLab-AI is a fully automated multi-agent system that transforms **any topic** into a complete research workflow, producing:

- 📚 Structured Literature Review  
- 🧪 Experiment Design Plan  
- 🧠 Auto-Generated ML Code  
- ⚙️ Code Execution + Logs  
- 📈 Metrics & Accuracy Plot  
- 📄 Research Paper (PDF)  
- 📑 Slide Deck (PPTX)

This project was developed as part of the **Kaggle Agents Intensive – Capstone Project (2025)** in collaboration with Google.

---

# 🚀 Overview

Traditional research requires multiple complex steps:
- Searching literature  
- Designing the experiment  
- Writing ML code  
- Executing the code  
- Analyzing results  
- Preparing a paper and presentation  

**ResearchLab-AI automates this entire pipeline.**  
You give a topic → The system generates everything end-to-end.

---

# 🧠 Multi-Agent Architecture

ResearchLab-AI uses a modular multi-agent system:

### 1️⃣ Orchestrator Agent  
Controls workflow, message-passing, and session management.

### 2️⃣ Researcher Agent  
Generates structured literature summaries related to the topic.

### 3️⃣ Designer Agent  
Creates a full experiment plan, including:
- Dataset parameters  
- Model selection  
- Metrics to optimize  
- Experiment steps  

### 4️⃣ Coder-Executor Agent  
Auto-writes Python ML code based on the plan and executes it to produce logs + results.

### 5️⃣ Analyst Agent  
Extracts metrics, generates accuracy plots, and saves structured metrics.

### 6️⃣ Writer Agent  
Generates:
- 📄 A research paper (PDF)
- 📑 A slide deck (PPTX)

---

# 📁 Project Structure

autonomous-research-agent/
│
├── agents/
│ ├── init.py
│ ├── orchestrator.py
│ ├── researcher.py
│ ├── designer.py
│ ├── coder_executor.py
│ ├── analyst.py
│ └── writer.py
│
├── templates/
│ ├── code_template.py
│ ├── paper_template.md
│ └── slide_outline.txt
│
├── demo/
│ └── demo_pipeline.ipynb
│
├── artifacts/ # auto-generated after pipeline runs
│
├── run_pipeline.py
├── requirements.txt
└── README.md


Requirements include:

1.numpy
2.pandas
3.scikit-learn
4.matplotlib
5.reportlab
6.python-pptx
7.Pillow
8.jinja2


# ▶️ How to Run Locally

1.✅ Run with default topic:
    python run_pipeline.py

    
2.🎯 Run with your own topic:
  python run_pipeline.py --topic "Sentiment Analysis"

  #📂 Output Directory
  All generated artifacts are saved in:
      artifacts/<session_id>/

 Inside this folder you will find:

✔ experiment.py (auto-generated ML code)

✔ run_logs.txt

✔ metrics.json

✔ accuracy.png

✔ paper.pdf

✔ slides.pptx






































