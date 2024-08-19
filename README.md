# Kubernetes-Load-Balancing-Demo
# Project Overview
- This project involves setting up a round-robin load balancing system using Kubernetes. The system includes two servers (server1 and server2) and a client that interacts with these servers.
- The client performs requests to both servers, and Kubernetes manages the load balancing and fault tolerance.

# Architecture
- Servers: Two server deployments (server1 and server2) that serve HTTP requests.
- Client: A client deployment that sends HTTP requests to both servers.
- Load Balancing: Managed by Kubernetes services that distribute traffic between server pods.
- Fault Tolerance: Handled by Kubernetes, which automatically restarts failed pods.
