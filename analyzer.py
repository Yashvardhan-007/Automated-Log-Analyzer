import re
import os
import csv
from collections import defaultdict

# === CONFIG ===
LOG_FILE = "logs/sample_auth.log"
OUTPUT_FILE = "output/report.csv"

# Regex pattern to capture IP + failure attempts (SSH log format)
FAILED_LOGIN_PATTERN = r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)"

def analyze_logs(log_file):
    ip_attempts = defaultdict(int)

    if not os.path.exists(log_file):
        print(f"[!] Log file not found: {log_file}")
        return {}

    with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            match = re.search(FAILED_LOGIN_PATTERN, line)
            if match:
                ip = match.group(1)
                ip_attempts[ip] += 1

    return ip_attempts


def export_report(ip_attempts, output_file):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["IP Address", "Failed Attempts", "Threat Level"])
        for ip, count in ip_attempts.items():
            level = "HIGH" if count > 10 else "MEDIUM" if count > 5 else "LOW"
            writer.writerow([ip, count, level])
    print(f"[+] Report generated: {output_file}")


if __name__ == "__main__":
    results = analyze_logs(LOG_FILE)
    if results:
        print("[+] Analysis Complete. Exporting report...")
        export_report(results, OUTPUT_FILE)
    else:
        print("[!] No suspicious activity found.")

