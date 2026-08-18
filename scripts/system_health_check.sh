#!/usr/bin/env bash
# Linux System & Kubernetes Node Health Audit Tool

set -eo pipefail

echo "=================================================="
echo "   Linux System & Node Infrastructure Audit       "
echo "=================================================="

# 1. System Memory & Swap Check
echo -e "\n[*] Memory & Swap Usage:"
free -h

# 2. Storage Partition & Disk Usage Check
echo -e "\n[*] Disk Space & Partition Status:"
df -hT | grep -E '^/dev/'

# 3. System Load Average & CPU Utilization
echo -e "\n[*] System Load Average:"
uptime

# 4. Check Failed Systemd Services
echo -e "\n[*] Checking Failed Systemd Services:"
if systemctl list-units --failed --state=failed | grep -q "0 loaded"; then
    echo "  └── All systemd units are running healthy."
else
    systemctl list-units --failed --state=failed
fi

# 5. Optional Kubernetes Node Readiness Check (if kubectl present)
if command -v kubectl &> /dev/null; then
    echo -e "\n[*] Kubernetes Cluster Node Status:"
    kubectl get nodes -o wide 2>/dev/null || echo "  └── kubectl detected, but cluster is unreachable or unconfigured."
fi

echo -e "\n[+] Health Audit Completed."
