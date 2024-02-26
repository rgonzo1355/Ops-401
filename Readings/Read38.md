# Attacking Juice Shop with Burp Suite

## Reading and Discussion Points

### Understanding Burp Suite
**Explain how Burp Suite allows us to analyze web application traffic.**
- Burp Suite is a comprehensive web application security testing tool that allows security professionals to intercept, manipulate, and analyze HTTP requests and responses between a web browser and a web application. It provides various modules and features for performing tasks such as intercepting requests, identifying vulnerabilities, scanning for security issues, and automating attacks. With Burp Suite, analysts can gain insights into the behavior of web applications, identify security weaknesses, and assess their overall security posture.

**What does the Repeater tool allow us to do with requests?**
- The Repeater tool in Burp Suite allows users to manually modify and replay HTTP requests sent to a web application. It provides a convenient interface for making alterations to individual parameters, headers, or request payloads and observing the server's corresponding responses. Additionally, users can customize and repeat requests multiple times, making it easier to test different scenarios, analyze application behavior, and identify vulnerabilities.

**Why might this be a useful tool for an attacker?**
- The Repeater tool can be handy for attackers during an attack's reconnaissance and exploitation phases. By intercepting and modifying requests using Burp Suite, attackers can manipulate input parameters, inject malicious payloads, or bypass security controls to exploit vulnerabilities in the target web application. Additionally, replay requests enable attackers to fine-tune their attack payloads, evade detection mechanisms, and launch targeted attacks against specific vulnerabilities, such as SQL injection or cross-site scripting (XSS).

## Resources
- [Attacking Juice Shop with Burp Suite (YouTube)](https://www.youtube.com/watch?v=nH4r6xv-qGg)
- [What is Burp Suite? (TechniPages)](https://www.technipages.com/what-is-burp-suite/)
