 # SDN-Based Port Monitoring and Access Control

## Problem Statement

This project demonstrates how Software Defined Networking (SDN) can be used to monitor and control network traffic. The system allows HTTP traffic (port 80) and blocks Telnet traffic (port 23) using a POX controller.

## Objective

* Understand SDN architecture
* Implement Mininet topology
* Apply traffic control rules
* Monitor allowed and blocked traffic

## Tools Used

* Mininet
* POX Controller
* Python
* OpenFlow

## Network Topology

* 1 Switch (s1)
* 2 Hosts (h1, h2)
* 1 Controller

## Steps to Run the Project

### 1. Start POX Controller

```bash
cd pox
./pox.py log.level --DEBUG port_monitor
```

### 2. Start Mininet (Open New Terminal)

```bash
sudo mn -c
sudo mn --topo single,2 --controller remote
```

### 3. Test Connectivity

```bash
mininet> h1 ping h2
```

Expected Output: Ping should be successful.

### 4. Test HTTP (Allowed Traffic)

```bash
mininet> h2 python3 -m http.server 80
mininet> h1 curl http://10.0.0.2
```

Expected Output: HTML page displayed (HTTP allowed).

### 5. Test Telnet (Blocked Traffic)

```bash
mininet> h1 telnet 10.0.0.2 23
```

Expected Output: Connection fails (Telnet blocked).

### 6. Check Flow Table (Open New Terminal)

```bash
sudo ovs-ofctl dump-flows s1
```

### 7. Test Network Performance (Optional)

```bash
mininet> iperf h1 h2
```

### 8. Exit Mininet

```bash
mininet> exit
```

## Expected Output

* Ping: Successful
* HTTP: Allowed
* Telnet: Blocked
* Flow table: Displays rules

## Proof of Execution

Include screenshots of:

* Ping result
* HTTP output
* Telnet blocked
* Flow table
* Controller logs

## Conclusion

The project successfully demonstrates SDN-based traffic monitoring and access control using a POX controller. It shows how traffic can be dynamically allowed or blocked using SDN principles.

## References

1. Mininet Official Website: http://mininet.org
2. POX Controller Documentation: https://github.com/noxrepo/pox
3. OpenFlow Specification
