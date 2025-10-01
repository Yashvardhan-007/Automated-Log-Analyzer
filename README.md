# Automated Log Analyzer 🕵️‍♂️

## Overview
**Automated Log Analyzer** is a Python-based cybersecurity tool designed to analyze server log files, detect suspicious activity (such as failed login attempts), and generate detailed reports.  
This project demonstrates expertise in **Python programming**, **regex parsing**, and **cybersecurity monitoring**, making it perfect for your portfolio or placement projects.

---

## 🚀 Features
- **Detect Suspicious IPs**: Identifies IPs with multiple failed login attempts.  
- **Threat Level Classification**: Classifies activity as LOW, MEDIUM, or HIGH based on frequency.  
- **Export Reports**: Generates CSV reports for easy analysis.  
- **Customizable Logs**: Works with any `.log` file format with minor tweaks.  
- **Ready for Integration**: Can be extended with email alerts, dashboards, or automated workflows.

---

## 🛠️ Tech Stack
- **Language:** Python 3.x  
- **Libraries:** Built-in (`re`, `csv`, `os`, `collections`)  
- **Tools:** Git/GitHub for version control  
- **Concepts Used:** Regex, Dictionaries, File Handling, Automation

---

## 📂 Project Structure
automated_log_analyzer/

│── logs/ # Sample log files

│ └── sample_auth.log

│── analyzer.py # Main Python script

│── README.md

│── .gitignore


---

## ⚡ How It Works
1. Reads a log file line by line.  
2. Uses **regex** to identify failed login attempts.  
3. Counts failed attempts per IP address.  
4. Classifies threat levels:  
   - LOW → 1–5 failed attempts  
   - MEDIUM → 6–10 failed attempts  
   - HIGH → >10 failed attempts  
5. Exports the results to `output/report.csv`.

---

## 📈 Sample Output
| IP Address     | Failed Attempts | Threat Level |
|---------------|----------------|--------------|
| 192.168.1.10  | 2              | LOW          |
| 192.168.1.11  | 1              | LOW          |
| 10.0.0.5      | 2              | LOW          |

---

## 💻 Installation & Usage

1. Clone the repository:
```bash
git clone https://github.com/<your-username>/automated_log_analyzer.git
cd automated_log_analyzer
```
