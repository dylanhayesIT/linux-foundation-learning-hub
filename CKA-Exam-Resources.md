# Certified Kubernetes Administrator (CKA) Exam Resources & Blueprint ☸️

This guide outlines practical study strategies, imperative command workflows, and high-yield domain breakdowns required to master the CNCF Certified Kubernetes Administrator (CKA) exam and real-world cluster management.

---

### 💡 High-Yield Study Strategies & Speed Tactics

* **Imperative First, Declarative Second:** Avoid writing YAML manifests from scratch. Master generating base configuration files using `kubectl run` and `kubectl create --dry-run=client -o yaml > file.yaml`.
* **Vim Efficiency & Shell Configuration:** Set up quick terminal aliases (`alias k=kubectl`) and Vim auto-indentation parameters (`set tabstop=2 shiftwidth=2 expandtab`) immediately upon accessing an exam node.
* **Master Documentation Navigation:** Practice finding exact YAML examples on `kubernetes.io/docs` within 10–15 seconds, as searching speed directly determines exam performance.
* **Focus Heavy on Troubleshooting & Storage:** Cluster troubleshooting (`journalctl`, `systemctl`), ETCD backup/restore, and PersistentVolume configurations carry high weight in hands-on scenarios.

---

### 🎯 Core Domain Breakdown

* **Cluster Architecture, Installation & Configuration (15%):** Role-based Access Control (RBAC), Kubeadm cluster bootstrapping, and ETCD snapshot backup/restore.
* **Workloads & Scheduling (15%):** Deployment rollouts/rollbacks, ConfigMaps/Secrets, DaemonSets, and pod resource request limits.
* **Services & Networking (20%):** Service types (ClusterIP, NodePort), NetworkPolicies, Ingress controllers, and CoreDNS troubleshooting.
* **Storage (10%):** PersistentVolumes (PV), PersistentVolumeClaims (PVC), StorageClasses, and volume mounting modes.
* **Troubleshooting (30%):** Node failures, control plane pod crashes, worker node disconnects, and container log analysis.

---

🔗 Official CNCF & Linux Foundation Documentation

* [CNCF CKA Certification Official Page](https://www.cncf.io/certification/cka/) - Official curriculum, exam scope, and candidate guidelines.
* [Linux Foundation Training Portal](https://training.linuxfoundation.org/) - Exam registration, candidate handbook, and system prerequisites.
* [Kubernetes Official Documentation](https://kubernetes.io/docs/) - Primary documentation allowed for reference during the exam session.
* [Official Kubernetes GitHub Organization](https://github.com/kubernetes) - Core repository, release notes, and ecosystem tools.

---

📚 Recommended Architectural Guides & Deep Dives

* [CKA Hands-On Lab Setup & Cluster Troubleshooting Guide](#) - *Deep dive into ETCD restoration, CNI plugin configuration, and RBAC policies.*
