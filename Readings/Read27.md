# PowerShell Empire and Post-Exploitation

## Reading and Discussion Points

### PowerShell Empire Overview
**What is one of the significant advantages of PowerShell Empire?**
- One of the significant advantages of PowerShell Empire is its stealthiness. PowerShell Empire leverages PowerShell, a legitimate and built-in scripting language in Windows, making it difficult for traditional antivirus software to detect its activities. This stealthiness allows attackers to bypass security controls and remain undetected within compromised systems.

**What are some of the APT groups that have been known to use PS Empire, and into which step of the Cyber Kill Chain does the use of PS Empire fall?**
- Some Advanced Persistent Threat (APT) groups known to use PowerShell Empire include APT29 (also known as Cozy Bear), APT32 (also known as OceanLotus), and APT33. PowerShell Empire typically falls into the "exploitation" and "installation" steps of the Cyber Kill Chain, where attackers gain access to systems and establish persistence for further malicious activities.

**What are the four main components needed to pull off an attack using PS Empire?**
- The four main components needed to pull off an attack using PowerShell Empire are:
  1. **Listener:** A listener is set up to listen for incoming connections from compromised systems.
  2. **Module:** Modules are used to perform specific tasks or actions on compromised systems, such as executing commands, gathering information, or escalating privileges.
  3. **Agent:** An agent is the payload delivered to compromised systems, allowing attackers to maintain control and execute commands remotely.
  4. **Stager:** Stagers are used to deliver the initial payload (agent) to compromised systems, often using techniques to bypass security controls and execute code.

## Resources
- [PowerShell Empire No Longer Maintained (BleepingComputer)](https://www.bleepingcomputer.com/news/security/powershell-empire-framework-is-no-longer-maintained/)
- [Hacking with Empire – PowerShell Post-Exploitation Agent (Hacking Articles)](https://www.hackingarticles.in/hacking-with-empire-powershell-post-exploitation-agent/)
- [YouTube Video: Hacking with PowerShell Empire (Additional Resource)](https://www.youtube.com/watch?v=bTun7InPfew)
