# Log Clearing and Tampering

## Reading and Discussion Points

### Log Clearing Motives
**Explain why a hacker might want to clear log files to a family member. Do not use the example from the article.**
- Imagine you're playing a game of hide-and-seek, and you accidentally leave behind clues that reveal your hiding spot. Similarly, when hackers infiltrate systems, they leave digital footprints in log files. Clearing log files is like erasing those footprints to avoid being caught. Hackers clear log files to cover their tracks and hide Evidence of their unauthorized activities, making it harder for security professionals to detect and investigate their intrusion.

### Methods to Clear Logs in Windows
**What are three methods by which you can clear logs in a Windows system?**
- Three methods to clear logs in a Windows system include:
  1. **Using Event Viewer:** Event Viewer is a built-in Windows tool that allows users to view and manage event logs. You can manually clear event logs using Event Viewer by right-clicking on a record and selecting the "Clear Log" option.
  2. **PowerShell Command:** PowerShell provides a command-line interface to manage Windows systems. You can use PowerShell commands, such as `Clear-EventLog,` to clear specific event logs or all logs simultaneously.
  3. **Third-Party Tools:** Various third-party tools offer features to manage and clear event logs in Windows systems. These tools often provide additional functionalities and automation options for log management.

### Steps in Covering Your Tracks
**What are the four steps in the process of covering your tracks?**
- The four steps in the process of covering your tracks are:
  1. **Erase Evidence:** Clear log files and delete any traces of unauthorized access or activities.
  2. **Modify Timestamps:** Change timestamps on files and system logs to create false timelines and confuse investigators.
  3. **Delete Artifacts:** Remove any artifacts or remnants left behind during the intrusion, such as temporary files or scripts.
  4. **Misdirection:** Plant false information or red herrings to mislead investigators and divert attention away from the actual attacker.

## Resources
- [Log Tampering 101 (Infosec Institute)](https://resources.infosecinstitute.com/topics/hacking/ethical-hacking-log-tampering-101/)
- [NIST SP800-154 Guide to Data-Centric Threat Modeling (NIST)](https://csrc.nist.gov/pubs/sp/800/154/ipd#pubs-abstract-header)
- [YouTube Video: Log Tampering and Threat Modeling (Additional Resource)](https://www.youtube.com/watch?v=oVed8I9VhEE)
