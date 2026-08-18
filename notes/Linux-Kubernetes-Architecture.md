# Linux System Internals & Kubernetes Architecture Deep Dive

Understanding the interplay between Linux kernel subsystems and Kubernetes container runtime interfaces (CRI) is critical for managing enterprise cloud-native environments.

## 1. Linux Kernel Subsystems in Containerization

* **Control Groups (cgroups v1/v2):** Enforces resource limits (CPU, Memory, I/O) on process groups, preventing single-container resource starvation.
* **Namespaces:** Provides process isolation across Mount (mnt), Process ID (pid), Network (net), Inter-process Communication (ipc), and User realms.
* **OverlayFS:** Multi-layered file system architecture allowing efficient container layer stacking and copy-on-write (CoW) execution.

## 2. Kubernetes Control Plane Dynamics

* **kube-apiserver:** Central REST endpoint validating and configuring data for pods, services, and replication controllers.
* **etcd:** Distributed, consistent key-value store maintaining cluster state and configuration baseline.
* **kube-scheduler:** Assigns unscheduled pods to nodes based on resource availability, taints, tolerations, and node affinity rules.

## 3. Network Overlay & CNI Protocols

* **Pod-to-Pod Communication:** Every pod receives a unique IP address without NAT overhead.
* **Service Abstraction (kube-proxy):** Manages virtual IPs via iptables or IPVS modes for load balancing incoming traffic.
