<img src="assets/icon_network_security.png" alt="Network Security Toolkit" width="100">

# Zafer Steele's Network Security Toolkit

A set of scripts and tools focused on enhancing network security. Automate security checks, analyze traffic, manage firewall rules, and implement best practices to protect and monitor your network environment.

---

## 🔐 Features

### 🧪 Python Tools

* `log_pattern_scanner.py`: Scan logs for suspicious patterns.
* `multi_protocol_ping.py`: Test host availability using ICMP, TCP, and UDP.
* `multiple_files_acl_log_filter.py`: Filter ACL-related logs across multiple files.
* `tcp_syn_scanner.py`: Lightweight TCP SYN port scanner.

---

## 📁 Directory Structure

```bash
Network_Security/
├── log_pattern_scanner.py
├── multi_protocol_ping.py
├── multiple_files_acl_log_filter.py
├── tcp_syn_scanner.py
```

---

## 🛠️ Getting Started

### Setup

```bash
python3 -m venv venv
source venv/bin/activate
```

If not present, install:

```bash
pip install scapy
```

---

## 💡 Usage Examples

### Run scripts manually:

```bash
python3 log_pattern_scanner.py --log syslog.log --pattern "deny"
python3 multi_protocol_ping.py --host 192.168.1.1
python3 multiple_files_acl_log_filter.py --dir ./logs --keyword "ACL_DROP"
python3 tcp_syn_scanner.py --target 192.168.1.1 --ports 22,80,443
```

## 📦 Requirements

* `scapy`
* `os`, `re`, `socket` (standard libs

---

## 👤 Author

**Zafer Steele**
GitHub: [@zaferSteele](https://github.com/zaferSteele)

---

## 📝 License

This repository is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

