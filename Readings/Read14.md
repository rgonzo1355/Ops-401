# Firewalls vs. IDS: Differences and Considerations

## Reading and Discussion Points

### Differences Between Firewalls and IDS
**List 2 differences between firewalls and an IDS?**
- Firewalls:
  1. **Access Control:** Firewalls primarily focus on allowing or blocking traffic based on predefined rules and policies, acting as a barrier between networks.
  2. **Preventive:** Firewalls are proactive and aim to prevent unauthorized access or threats from entering the network.

- IDS (Intrusion Detection System):
  1. **Monitoring:** IDS monitors network traffic for suspicious or malicious activities and raises alerts when potential threats are detected.
  2. **Detective:** IDS is detective and aims to identify security incidents after they have occurred, providing insights into potential breaches.

### Network-based IDS vs. Host-based IDS
**Under what circumstances would you choose a network-based IDS over a host-based IDS?**
- A network-based IDS is preferred when:
  - You want to monitor and analyze network traffic across multiple devices and systems.
  - You need visibility into potential threats affecting the entire network, including unauthorized access attempts and unusual traffic patterns.

### Drawbacks of a NIDS
**Name 3 major drawbacks of a NIDS?**
- Network-based Intrusion Detection Systems (NIDS) have several drawbacks, including:
  1. **Blind Spots:** NIDS may not detect attacks within encrypted traffic or encrypted communications.
  2. **High Volume of Alerts:** They can generate a high volume of alerts, leading to alert fatigue and making it challenging to identify real threats.
  3. **Limited Visibility:** NIDS may not provide insights into host-specific vulnerabilities or attacks targeting individual devices.

## Resources
- [Rapid7 - The Pros and Cons of Intrusion Detection Systems](https://www.rapid7.com/blog/post/2017/01/11/the-pros-cons-of-intrusion-detection-systems/)
- [YouTube Video: Intrusion Detection Systems (Additional Resource)](https://www.youtube.com/watch?v=hEgWPWIuq_s)
