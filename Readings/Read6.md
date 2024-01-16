## Data File Encryption

# Applying The CIA Triad To Your Enterprise File Transfer

## Reading and Discussion Points

### Preserving the CIA Triad for the Company’s File Server
**How would you preserve the three elements of the CIA triad for the company’s file server?**
- Implementing Confidentiality: Use access controls and encryption to restrict access to authorized users.
- Ensuring Integrity: Implement hashing to verify the integrity of files during transfers and storage.
- Maintaining Availability: Implement redundancy and backup strategies to ensure data availability.

### Explaining Data Integrity Verification with Hashing
**Explain how hashing verifies data integrity using non-technical terms.**
- Hashing is like creating a unique digital fingerprint for a file. When you transfer a file, you generate its fingerprint (hash) at the source and compare it to the fingerprint at the destination. If they match, it means the file arrived without any changes, ensuring data integrity.

### Difference Between Hashing and Encryption
**How is hashing different from encryption?**
- Hashing creates a fixed-size string (hash) from data, and it's a one-way process. The same data will always produce the same hash. It's used for data integrity verification.
- Encryption transforms data into a different format using a key, and it's a reversible process. Encrypted data can be decrypted back to its original form using the key. It's used for data confidentiality.

## Resources
- [Implementing the CIA Triad When Transferring Files Through the Internet](https://www.jscape.com/blog/implementing-the-cia-triad-when-transferring-files-through-the-internet)
- [What Are MD5, SHA-1 Hashes, and How Do I Check Them?](https://www.howtogeek.com/67241/htg-explains-what-are-md5-sha-1-hashes-and-how-do-i-check-them/)
- [YouTube Video: Hashing and Data Integrity Explained](https://www.youtube.com/watch?v=4_s9lOuUpZ4)
