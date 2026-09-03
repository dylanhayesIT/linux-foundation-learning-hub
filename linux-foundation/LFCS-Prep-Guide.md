# Linux Foundation Certified System Administrator (LFCS) Prep Guide 🐧

This guide provides practical study strategies, core CLI workflows, and domain breakdowns for mastering the Linux Foundation Certified System Administrator (LFCS) performance-based exam and real-world Linux system administration.

---

### 💡 High-Yield Study Strategies & Practical CLI Tactics

* **Master Storage & LVM Setup:** Practice setting up LVM partitions (`pvcreate`, `vgcreate`, `lvcreate`), resizing logical volumes, and configuring `/etc/fstab` with persistent UUIDs under timed conditions.
* **Systemd & Service Troubleshooting:** Get comfortable creating custom `systemd` service units, analyzing service logs via `journalctl -u <service>`, and switching runlevels/targets (`systemctl set-default`).
* **Text Processing & Pipeline Efficiency:** Train heavily on essential text manipulators (`grep`, `sed`, `awk`, `find`, `xargs`) to quickly parse system configs and bulk modify user attributes.
* **Networking & Firewall Configuration:** Practice persistent IP assignment (`nmcli`, `ip`), netmask calculation, and port routing rules using `nftables` or `firewalld`.

---

### 🎯 Core Domain Breakdown

* **Essential Commands (20%):** File manipulation, archive management (`tar`, `gzip`), hard/soft link creation, and shell environment customization.
* **Operation of Running Systems (20%):** Boot process inspection, kernel parameter management (`sysctl`), system log analysis, and cron/at scheduled tasks.
* **User and Group Management (15%):** Creating/modifying user accounts, enforcing password policies, configuring sudo access, and setting elevated permissions (`chmod`, `chown`, ACLs).
* **Networking (15%):** Network interface configuration, DNS resolution troubleshooting, routing tables, and firewall service rules.
* **Storage Management (30%):** Disk partitioning (MBR/GPT), filesystem creation (ext4/XFS), LVM snapshotting, quota enforcement, and swap space allocation.

---

🔗 Official Linux Foundation Documentation & Learning Resources

* [Linux Foundation LFCS Certification Official Page](https://training.linuxfoundation.org/certification/linux-foundation-certified-sysadmin-lfcs/) - Official exam blueprint, competency list, and candidate handbook.
* [The Linux Kernel Documentation](https://www.kernel.org/doc/html/latest/) - Official Linux kernel documentation and subsystem references.
* [Systemd System and Service Manager Portal](https://systemd.io/) - Official guides for systemd unit file specifications and service management.
* [The Linux Documentation Project (TLDP)](https://tldp.org/) - Classic Linux system administration guides, HOWTOs, and man-page references.

---

📚 Recommended Architectural Guides & Deep Dives

* [LFCS Storage Management & LVM Hands-On Blueprint](#) - *Deep dive into logical volume management, RAID arrays, and persistent filesystem configuration.*
