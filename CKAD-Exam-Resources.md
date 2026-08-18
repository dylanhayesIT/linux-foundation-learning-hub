# Certified Kubernetes Application Developer (CKAD) Exam Resources 🚀

This guide provides high-yield study strategies, imperative command cheatsheets, and domain breakdowns required to pass the CNCF Certified Kubernetes Application Developer (CKAD) performance-based exam.

---

### 💡 High-Yield Study Strategies & Speed Tactics

* **Master Multi-Container Pod Patterns:** Be fluent in configuring Sidecar, Adapter, and Ambassador container design patterns within a single Pod manifest.
* **Imperative Helm & Deployment Tricks:** Practice creating Canary and Blue-Green rollouts, managing Deployment revisions, and running Helm installs/upgrades without relying on external editors.
* **CronJobs, Jobs & Probes:** Focus heavily on Liveness, Readiness, and Startup probe configurations, along with `backoffLimit` and schedule syntax for CronJobs.
* **Configuration & Security Contexts:** Understand how to mount ConfigMaps/Secrets as environment variables or volumes, and set `securityContext` (runAsUser, capabilities, readOnlyRootFilesystem).

---

### 🎯 Core Domain Breakdown

* **Application Design and Build (20%):** Multi-container pod design, InitContainers, Jobs, and CronJobs.
* **Application Deployment (20%):** Deployment strategies (Blue-Green, Canary), Helm release management, and rolling updates/rollbacks.
* **Application Observability and Maintenance (15%):** API deprecation checks, Liveness/Readiness probes, container logging (`kubectl logs -c`), and debugging.
* **Application Environment, Configuration and Security (25%):** ConfigMaps, Secrets, SecurityContexts, ServiceAccounts, and resource Requests/Limits.
* **Services and Networking (20%):** Service types (ClusterIP, NodePort), Ingress routing rules, and NetworkPolicies for isolation.

---

🔗 Official CNCF & Linux Foundation Documentation

* [CNCF CKAD Certification Official Page](https://www.cncf.io/certification/ckad/) - Official curriculum, exam scope, and candidate guidelines.
* [Kubernetes Official Documentation - Tasks](https://kubernetes.io/docs/tasks/) - Hands-on developer guides for workloads, storage, and networking.
* [Helm Official Documentation](https://helm.sh/docs/) - Official reference for release management and chart configuration.
* [Official Kubernetes GitHub Organization](https://github.com/kubernetes) - Core repository, release notes, and ecosystem tools.

---

📚 Recommended Architectural Guides & Deep Dives

* [CKAD Multi-Container Pods & Deployment Strategies Guide](#) - *Deep dive into sidecar patterns, readiness probes, and Canary deployment scenarios.*
