# 🧠 Multi-Agent Recruitment AI System

This project is a multi-agent AI system designed to automate key parts of the recruitment pipeline — including JD summarization, resume parsing, candidate matching, and personalized interview scheduling.

---

## 🚀 Problem Statement

Manually matching resumes with job descriptions and handling candidate communication is tedious and time-consuming. Our goal is to build an AI-powered, multi-agent system that:

- Parses and matches resumes to JDs
- Shortlists suitable candidates
- Sends personalized interview requests

---

## 🧩 Features

✅ Extracts text from multiple resumes (PDFs)  
✅ Uses SBERT embeddings for JD-Resume similarity  
✅ Stores results in SQLite for long-term memory  
✅ Sends interview emails with personalized name, date, time, and format

---


---

## 💡 Technologies Used

- Python 🐍
- SentenceTransformers (`paraphrase-MiniLM-L6-v2`)
- PyMuPDF (for PDF reading)
- SQLite (for resume storage)
- smtplib / email (for sending mails)
- Multi-agent design pattern

---

## 🤖 Agents’ Interaction Design

- **JD Agent:** Reads, cleans, and embeds job descriptions  
- **Resume Agent:** Parses resumes, extracts names, and embeds content  
- **Matching Agent:** Uses cosine similarity for shortlisting  
- **Email Agent:** Generates and sends personalized interview emails

Agents communicate via shared memory (variables/SQLite) and work in sequence like an assembly line.

---

## 📬 Sample Email Sent

```text
Subject: Interview Invitation for Software Engineer Role

Hi Diksha Pimple,

Congratulations! Based on your profile, we’d like to invite you for an interview.

📅 Date: April 9, 2025  
⏰ Time: 11:30 AM  
💬 Format: Virtual (Google Meet)

Looking forward to meeting you.

Best Regards,  
Recruitment Team
