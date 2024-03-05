# Pass the Hash with Mimikatz

## Reading

### What is Mimikatz?
Mimikatz is a powerful post-exploitation tool commonly used by attackers to extract sensitive information, particularly credentials, from memory and perform lateral movement within a compromised network. It can exploit various vulnerabilities and weaknesses in Windows systems to retrieve credentials and escalate privileges.

### Name the six credential-gathering techniques Mimikatz can perform and explain how they work.
1. **Pass-the-Hash (PtH):** Mimikatz can extract hashed credentials stored in memory and use them to authenticate to other systems without knowing the original plaintext password.
2. **Pass-the-Ticket (PtT):** This technique involves stealing Kerberos tickets from memory and using them to authenticate to other services or systems without needing the user's password.

### What are four ways we can defend against Mimikatz attacks? Explain how two of the mitigations can stop Mimikatz.
1. **Implement Credential Guard:** Microsoft Credential Guard protects against credential theft attacks, including Mimikatz, by storing sensitive credential information in a secure, isolated environment.
2. **Enable Enhanced Protection for Authentication:** Features like Protected Users group and Authentication Policies and Silos can prevent attackers from harvesting credentials by enforcing more robust authentication protocols and limiting access to privileged accounts.

## Resources
- [What is Mimikatz? (Varonis)](https://www.varonis.com/blog/what-is-mimikatz)
- [YouTube: Pass the Hash with Mimikatz](https://www.youtube.com/watch?v=Op-l4DH745o)
