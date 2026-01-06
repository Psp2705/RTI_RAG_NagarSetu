# RTI RAG Agent for NagarSetu  
*A Hallucination-Free, Low-Latency Retrieval-Augmented Generation System for RTI Drafting*

---

## 📌 Project Overview

This project implements a **Retrieval-Augmented Generation (RAG) agent** to assist citizens in drafting **Right to Information (RTI)** applications in a **legally correct, structured, and bilingual (English/Hindi)** manner.  

The system is developed as part of the **NagarSetu: Bilingual AI System for Civic Complaint and Information Assistance** project and directly addresses the limitation of existing RTI portals, which only provide submission mechanisms without drafting guidance.

Unlike generic chatbots, this system is designed as a **legal document assembler**, ensuring **zero hallucination** by grounding every output strictly in authoritative RTI documents.

---

## 🎯 Objectives

- Generate **RTI drafts compliant with RTI Act, 2005**
- Eliminate hallucination through **retrieval-first, template-locked generation**
- Support **municipal-level RTI queries** (e.g., Thane Municipal Corporation)
- Achieve **low latency (<2 seconds)** for real-time use
- Ensure **academic and legal defensibility**

---

## 🧠 Key Design Principle

> **RTI drafting is a legally constrained task, not a creative task.**  
> Therefore, generation is strictly controlled and grounded in retrieved legal text.

---

## 🏗 System Architecture

```
User Query (EN / HI)
        ↓
Language Detection
        ↓
Hybrid Retrieval (BM25 + Dense)
        ↓
Authoritative RTI Context
        ↓
Template-Locked RTI Draft Assembly
        ↓
Citation & Faithfulness Validation
        ↓
Final RTI Draft (No Hallucination)
```

---

## 🧰 Technology Stack

### Core Framework
- **LlamaIndex** – Retrieval orchestration and RAG pipeline

### Document Parsing
- Granite Docling / Unstract (optional for structured PDF extraction)
- LlamaIndex SimpleDirectoryReader (for prototyping)

### Retrieval Layer
- **Hybrid Retrieval** (Keyword + Semantic)
- **FAISS** – In-memory vector store
- **BGE-small-en-v1.5** – Lightweight embedding model

### Generation Layer
- Template-locked generation (no free-form text)
- Deterministic decoding (`temperature = 0`, `top_p = 0`)
- Optional local LLMs (Phi-3 / Gemma via Ollama)

### Backend & Dev Environment
- **Google Colab** – Experimentation & execution
- **GitHub** – Version control
- **FastAPI** (future integration)

---

## 📂 Repository Structure

```
rti-rag-nagarsetu/
│
├── data/
│   └── rti_docs/              # RTI Acts, rules, formats, contacts
│
├── notebooks/
│   └── RTI_RAG_NagarSetu.ipynb
│
├── src/
│   ├── ingest.py              # Document loading & parsing
│   ├── retriever.py           # Hybrid retrieval logic
│   ├── templates.py           # RTI draft templates
│   └── pipeline.py            # End-to-end RTI RAG pipeline
│
├── requirements.txt
└── README.md
```

---

## 📄 Data Sources

### Authoritative (High Priority)
- RTI Act, 2005 (Central & State rules)
- Government RTI contact pages (`.gov.in`)
- PIO / APIO / Appellate Authority listings

### Supplementary (Low Priority)
- RTI drafting guidance websites (used only for examples, not legal facts)

> ⚠️ Non-government sources are **never treated as legal ground truth**.

---

## 🛡 Hallucination Control Mechanisms

| Layer | Technique |
|-----|----------|
| Retrieval | Hybrid search with metadata filtering |
| Generation | Fixed RTI template (no creative freedom) |
| Decoding | Deterministic softmax |
| Validation | Mandatory citation coverage |
| Failure Mode | Safe refusal if no legal context |

**No retrieval → No answer**

---

## ⚡ Performance Targets

| Metric | Target |
|-----|------|
| End-to-End Latency | < 2 seconds |
| Hallucination Rate | 0 tolerated |
| Citation Coverage | 100% |
| Faithfulness (RAGAS) | ≥ 0.95 |

---

## 🚀 How to Run (Google Colab)

1. Open Google Colab  
2. Load notebook from GitHub  
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Upload RTI documents to `data/rti_docs/`
5. Run notebook cells sequentially

---

## 📊 Evaluation

- Manual legal validation of RTI drafts
- RAGAS metrics for faithfulness and context precision
- Latency measurement for real-time usability

---

## 📌 Academic Alignment

This implementation directly fulfills **Objective 4 (RTI Drafting Support)** of the NagarSetu project report and aligns with **SDG 11 – Inclusive and Transparent Urban Governance**.

---

## 🧾 Disclaimer

This system assists in **drafting RTI applications**.  
Final submission and legal responsibility remain with the applicant.

---

## 👩‍💻 Author

**Prachiti Parab**  


---

## 🧠 One-Line Summary 

> “This RTI RAG agent uses hybrid retrieval over authoritative RTI documents with deterministic, template-locked generation to eliminate hallucination while maintaining low latency.”

---
