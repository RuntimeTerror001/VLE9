import datetime
import json
import os

LOG_FILE = "security/audit.log"

def log_event(user, action, resource, ip="127.0.0.1", status="SUCCESS"):
    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "user": user,
        "action": action,
        "resource": resource,
        "ip_address": ip,
        "status": status,
        "hipaa_category": "Access log"
    }
    os.makedirs("security", exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
    print(f"[AUDIT] {entry['timestamp']} | {user} | {action} | {status}")
    return entry

if __name__ == "__main__":
    log_event("dr.sharma", "LOGIN", "/dashboard", "192.168.1.10")
    log_event("john.doe", "VIEW_RECORD", "/patient/PT-20240198", "10.0.0.5")
    log_event("unknown", "LOGIN_ATTEMPT", "/login", "192.168.1.45", "FAILED")
    log_event("dr.sharma", "UPDATE_PRESCRIPTION", "/patient/PT-20240198/rx", "192.168.1.10")
    print(f"\nAudit log written to {LOG_FILE}")