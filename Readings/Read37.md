# XSS with w3af, DVWA

## Reading and Discussion Points

### Understanding Cross-site Scripting (XSS)
**Explain how a cross-site scripting attack works in non-technical terms.**
- A cross-site scripting (XSS) attack occurs when a malicious actor injects malicious scripts (typically JavaScript) into a web application, which is then executed in the context of other users' browsers. This allows the attacker to manipulate the behavior of the web page, steal sensitive information, or perform unauthorized actions on behalf of the user, such as stealing session cookies or redirecting users to phishing websites.

**What are the three types of XSS attacks?**
- The three types of XSS attacks are:
  1. **Reflected XSS**: The malicious script is injected into the web page's response and executed when the user visits a specially crafted URL.
  2. **Stored XSS**: The malicious script is stored on the server and executed when the user visits a vulnerable page where the script is retrieved and displayed.
  3. **DOM-based XSS**: The malicious script is executed on the client side, directly manipulating the web page's Document Object Model (DOM).

**If an attacker successfully exploits an XSS vulnerability, what malicious actions would they be able to perform?**
- If an attacker successfully exploits an XSS vulnerability, they can perform various malicious actions, including:
  - Stealing sensitive information such as login credentials, session cookies, or personal data.
  - Hijacking user sessions to impersonate legitimate users and perform unauthorized actions.
  - Defacing websites by modifying the content or layout of web pages.
  - Redirecting users to malicious websites or phishing pages.
  - Executing arbitrary code on the victim's browser to perform further attacks.

**What are some security controls that can be implemented to prevent XSS attacks?**
- Some security controls to prevent XSS attacks include:
  - Input validation: Sanitize and validate user input to prevent malicious scripts from being injected into web applications.
  - Output encoding: Encode user-generated content before rendering it in web pages to prevent script execution.
  - Content Security Policy (CSP): Implement CSP headers to restrict the execution of scripts and mitigate the impact of XSS attacks.
  - Use of security libraries and frameworks: Utilize security-focused libraries and frameworks that provide built-in protections against XSS vulnerabilities.

## Bookmark and Review

### Security Report for In-Production Web Applications
- This resource provides insights and recommendations for improving the security posture of in-production web applications. It offers valuable information on common security issues, including XSS vulnerabilities and best practices for securing web applications.

## Resources
- [Cross-site scripting (PortSwigger)](https://portswigger.net/web-security/cross-site-scripting)
- [Security Report for In-Production Web Applications (Rapid7)](https://www.rapid7.com/globalassets/_pdfs/whitepaperguide/rapid7-tcell-application-security-report.pdf)
- [YouTube: XSS Attack Explained](https://www.youtube.com/watch?v=qHHADT52L5s)
