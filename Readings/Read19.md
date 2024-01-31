# Amazon GuardDuty: Threat Detection Controls

## Reading and Discussion Points

**What is Amazon GuardDuty?**
- Amazon GuardDuty is like having a security guard for your AWS cloud. It's a threat detection service that continuously monitors your AWS environment for malicious activities and suspicious behavior. GuardDuty's job is to alert you when it detects potential security threats, helping you keep your cloud resources safe.

### IoCs Detected by GuardDuty
**What are some of the IoCs that GuardDuty can detect?**
- GuardDuty can detect a variety of Indicators of Compromise (IoCs), including:
  1. **Unauthorized Access:** GuardDuty can spot attempts to access your resources without proper permissions.
  2. **Cryptocurrency Mining:** It can identify activities related to cryptocurrency mining, which might indicate unauthorized usage of your resources.
  3. **Communication with Known Malicious IP Addresses:** GuardDuty checks if your resources are communicating with known malicious IP addresses.
  4. **Anomalous API Activity:** It looks for unusual API requests that could signify an attack.

### Data Sources for GuardDuty
**What are some of the data sources which GuardDuty can use?**
- GuardDuty collects data from various sources, including:
  1. **AWS CloudTrail:** It analyzes CloudTrail logs to track AWS account activity.
  2. **VPC Flow Logs:** GuardDuty examines VPC flow logs to monitor network traffic.
  3. **DNS Logs:** It checks DNS logs for any suspicious domain lookups or communication.
  4. **AWS Config:** GuardDuty utilizes AWS Config data to understand resource configurations.

### Access Behavior Analysis
**How does GuardDuty use access behavior to spot potential malicious activity?**
- GuardDuty observes how users and applications access AWS resources. If it notices unusual or unexpected access patterns, it can raise alerts. For example, if a user suddenly starts accessing sensitive data they haven't accessed before, GuardDuty might consider it suspicious behavior and generate an alert.

## Resources
- [Amazon GuardDuty Overview](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)
- [YouTube Video: Threat Detection on AWS with Amazon GuardDuty ](https://www.youtube.com/watch?v=czsuZXQvD8E)
