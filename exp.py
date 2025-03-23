malicious_ips = [
    "192.168.1.100",
    "203.0.113.50",
    "185.199.108.153"
]

# Ports that are being targeted
blocked_ports = [22, 80, 443, 3306]  # Example: SSH, HTTP, HTTPS, MySQL

def block_malicious_ips():
    """Block identified malicious IPs using iptables."""
    for ip in malicious_ips:
        subprocess.run(["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])
        subprocess.run(["iptables", "-A", "OUTPUT", "-d", ip, "-j", "DROP"])
        print(f"Blocked IP: {ip}")

def block_suspicious_ports():
    """Block targeted ports to prevent further exploitation."""
    for port in blocked_ports:
        subprocess.run(["iptables", "-A", "INPUT", "-p", "tcp", "--dport", str(port), "-j", "DROP"])
        print(f"Blocked Port: {port}")

def enable_logging():
    """Enable logging for further forensic analysis."""
    subprocess.run(["iptables", "-A", "INPUT", "-m", "limit", "--limit", "10/min", "-j", "LOG", "--log-prefix", "Blocked Traffic: "])
    print("Logging enabled for suspicious traffic.")

def apply_firewall_rules():
    """Apply firewall rules to mitigate malware spread."""
    block_malicious_ips()
    block_suspicious_ports()
    enable_logging()
    print("Firewall mitigation rules applied successfully.")

if __name__ == "__main__":
    apply_firewall_rules()
