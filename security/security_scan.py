import datetime
import sys

RULES = [
    {"id": "SEC-001", "name": "Hardcoded credentials", "severity": "CRITICAL", "pattern": "password="},
    {"id": "SEC-002", "name": "SQL injection risk", "severity": "HIGH", "pattern": "SELECT * FROM"},
    {"id": "SEC-003", "name": "Unencrypted HTTP", "severity": "MEDIUM", "pattern": "http://"},
    {"id": "SEC-004", "name": "Debug mode enabled", "severity": "LOW", "pattern": "debug=True"},
    {"id": "SEC-005", "name": "Missing input validation", "severity": "HIGH", "pattern": "eval("},
]

FILES_TO_SCAN = ["app/index.html", "app/login.html", "app/dashboard.html", "app/patient.html"]

def run_sast_scan():
    print("=" * 60)
    print("  MediSecure — SAST Security Scanner")
    print(f"  Scan started: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    findings = []
    for filepath in FILES_TO_SCAN:
        try:
            with open(filepath, "r") as f:
                content = f.read()
            for rule in RULES:
                if rule["pattern"].lower() in content.lower():
                    findings.append({**rule, "file": filepath})
                    print(f"[{rule['severity']}] {rule['id']}: {rule['name']} in {filepath}")
        except FileNotFoundError:
            print(f"[INFO] Skipping {filepath} — not found")

    print("\n" + "=" * 60)
    critical = [f for f in findings if f["severity"] == "CRITICAL"]
    high = [f for f in findings if f["severity"] == "HIGH"]

    print(f"  Scan complete. Findings: {len(findings)} total")
    print(f"  Critical: {len(critical)} | High: {len(high)}")
    print(f"  HIPAA compliance check: {'PASS' if not critical else 'FAIL'}")
    print("=" * 60)

    if critical:
        print("\n[PIPELINE BLOCKED] Critical vulnerabilities found. Fix before deployment.")
        sys.exit(1)
    else:
        print("\n[PIPELINE CLEAR] No critical issues. Proceeding to build stage.")
        sys.exit(0)

if __name__ == "__main__":
    run_sast_scan()