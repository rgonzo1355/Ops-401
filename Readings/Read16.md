# Lessons Learned from the Capital One Data Breach

## Reading and Discussion Points

**What were the three commands used for the attack?**
- The attacker used three commands during the Capital One data breach:
  1. **List Buckets:** The attacker used the AWS CLI command `aws s3 ls` to list the S3 buckets.
  2. **Copy Data:** They used `aws s3 cp` to copy sensitive data from a specific bucket.
  3. **Data Extraction:** The attacker employed `aws s3 mv` to move the stolen data to their own controlled bucket.

**What misconfiguration of AWS components allowed the attacker to access sensitive data?**
- The misconfiguration that allowed the attacker to access sensitive data was a misconfigured web application firewall (WAF) that did not properly filter inbound traffic. This misconfiguration enabled the attacker to send a specially crafted request to the server, which triggered the server to respond with information including credentials.

**What are two of the AWS Governance practices that could have prevented such an attack?**
- Two AWS Governance practices that could have prevented such an attack include:
  1. **Least Privilege:** Ensuring that AWS IAM roles and permissions are set with the principle of least privilege, granting only the necessary permissions to perform specific tasks.
  2. **Regular Security Audits:** Performing regular security audits and assessments of AWS resources, configurations, and access controls to identify and rectify vulnerabilities and misconfigurations.

## References
- [Capital One Data Breach Lessons (PDF)](https://www.zscaler.com/resources/white-papers/capital-one-data-breach.pdf)
- [YouTube Video: Capital One Data Breach (Additional Resource)](https://www.youtube.com/watch?v=iF9fs8Rw4Uo)
