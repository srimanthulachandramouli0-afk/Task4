import time
import datetime

# Firewall Rules Setup
firewall_rules = {
    23: "BLOCK (Telnet - Insecure)",
    22: "ALLOW (SSH - Secure)",
    80: "ALLOW (HTTP)",
    443: "ALLOW (HTTPS)"
}

def check_packet(port):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    rule = firewall_rules.get(port, "BLOCK (Default Deny Policy)")
    
    if "ALLOW" in rule:
        status = "✅ PASSED"
    else:
        status = "❌ DROPPED (Blocked by Firewall)"
    
    return f"[{timestamp}] Port {port} -> {rule} -> Packet {status}"

# --- Main Simulation ---
print("=====================================")
print("  UFW FIREWALL SIMULATION - ACTIVE")
print("=====================================")
print("Applying Rules: sudo ufw enable\n")
time.sleep(1)

# Test packets
test_ports = [23, 22, 80, 443, 3389]

for p in test_ports:
    result = check_packet(p)
    print(result)
    time.sleep(0.7)  # Real firewall lag

print("\n-------------------------------------")
print("Final UFW Status: sudo ufw status")
print("23 DENY | 22 ALLOW | Default: DENY")
print("Firewall Log: All threats blocked!")
