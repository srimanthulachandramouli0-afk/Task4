# Task4
# 🔥 TASK 4: Setup and Use a Firewall (UFW / Windows Firewall)

**Internship:** Elevate Labs - Cyber Security Internship
**Task Objective:** Configure and test basic firewall rules to allow or block traffic and understand how firewall filters traffic.

### 📱 Platform Used
- Mobile: Pydroid 3 (Python IDE for Android)
- Concept: Windows Firewall / Linux UFW (Uncomplicated Firewall)

### 🐍 Implementation in Python (Firewall Simulation)
Since mobile data uses CGNAT/IPv6, online port checkers fail. So I implemented firewall packet filtering logic in Python to simulate real firewall behavior.

**File:** `firewall_simulation.py`

```python
# Task 4: Firewall Simulation in Python
firewall_rules = {
    23: "BLOCK (Telnet - Insecure)",
    22: "ALLOW (SSH - Secure)",
    80: "ALLOW (HTTP)",
    443: "ALLOW (HTTPS)"
}

def check_packet(port):
    rule = firewall_rules.get(port, "BLOCK (Default Deny)")
    if "ALLOW" in rule:
        return f"Port {port} -> {rule} -> Packet PASSED"
    else:
        return f"Port {port} -> {rule} -> Packet DROPPED (Blocked)"

# Testing
print("--- Firewall Status: ACTIVE ---")
for p in [23, 22, 80, 443, 3389]:
    print(check_packet(p))

print("\nUFW Commands Simulated:")
print("sudo ufw deny 23")
print("sudo ufw allow 22")
print("sudo ufw status: Firewall filtering working!")

# 
#code furewall_sim.sh
sudo ufw status verbose
sudo ufw enable
sudo ufw deny 23/tcp
sudo ufw allow 22/tcp
sudo ufw status numbered
sudo ufw delete deny 23

code Output
--- Firewall Status: ACTIVE ---
Port 23 -> BLOCK (Telnet - Insecure) -> Packet DROPPED (Blocked)
Port 22 -> ALLOW (SSH - Secure) -> Packet PASSED
Port 80 -> ALLOW (HTTP) -> Packet PASSED
Port 443 -> ALLOW (HTTPS) -> Packet PASSED
Port 3389 -> BLOCK (Default Deny) -> Packet DROPPED (Blocked)
