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
```
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

```code Output
--- Firewall Status: ACTIVE ---
Port 23 -> BLOCK (Telnet - Insecure) -> Packet DROPPED (Blocked)
Port 22 -> ALLOW (SSH - Secure) -> Packet PASSED
Port 80 -> ALLOW (HTTP) -> Packet PASSED
Port 443 -> ALLOW (HTTPS) -> Packet PASSED
Port 3389 -> BLOCK (Default Deny) -> Packet DROPPED (Blocked)
```

Firewall Setup and Configuration

## 🔥 What is Firewall? - Definition

**Firewall** is a network security device or software that monitors and controls incoming and outgoing network traffic based on predetermined security rules. It acts as a barrier between a trusted internal network and untrusted external network (like the Internet).

Think of it as a **Security Guard at the main gate** of your house. The guard checks every person (packet) - if the person is in the allow-list, he lets him in. If the person is in the block-list, he stops him.

**Key Functions:**
1.  Packet Filtering - Checks IP, Port, Protocol
2.  Blocks unauthorized access
3.  Prevents hacking, viruses, and malware
4.  Logs all traffic for monitoring

**Types:**
- Hardware Firewall (Router lo untundi)
- Software Firewall (Windows Firewall, UFW in Linux)
- Stateful Firewall (Connection gurtunchukuntundi)
- Stateless Firewall (Prathi packet ni separate ga chustundi)

**Example Rule:** `BLOCK Port 23 (Telnet)` - because Telnet is insecure. `ALLOW Port 22 (SSH)` - because SSH is secure.


...
