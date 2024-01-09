Rodolfo Gonzalez
01-08-24

# Reading Notes

## Cloud Security Principles and Frameworks

### Discussion Points

1. **Explain the levels of abstraction in AWS to someone without a technical background.**
   - In AWS, levels of abstraction refer to how users interact with the cloud without needing to understand the underlying technical details. Imagine AWS like a multi-layered cake:
     - **Bottom Layer (Physical Servers):** This is where the actual hardware, like physical servers, is located. AWS manages this layer.
     - **Middle Layers (Virtualization and Management Services):** AWS uses virtualization to create 'virtual' versions of physical hardware. This layer also includes services for managing these resources.
     - **Top Layer (User Interfaces and APIs):** This is what users see and interact with, including user-friendly interfaces and APIs for accessing AWS services.

2. **What are the control plane and data plane responsible for in container abstraction?**
   - **Control Plane:** Manages and orchestrates containers, including tasks like scheduling and monitoring containers.
   - **Data Plane:** Responsible for the actual running of containers and their networking, handling data processing and network traffic management.

3. **Where does AWS Lambda fall in the layers of abstraction and what makes it so special?**
   - AWS Lambda is a serverless computing service, representing a higher level of abstraction. It automates server management for running code, letting users focus solely on writing code without worrying about the underlying infrastructure.

### Additional Resources

- [AWS Architecture Blog - Compute Abstractions on AWS: A Visual Story](https://aws.amazon.com/blogs/architecture/compute-abstractions-on-aws-a-visual-story/)
- [13 Compliance Frameworks for Cloud-based Organizations](https://www.horangi.com/blog/13-compliance-frameworks-for-cloud-based-organizations)
- [Cloud Security Alliance (CSA)](https://cloudsecurityalliance.org/)
- [Cloud Controls Matrix (CCM)](https://cloudsecurityalliance.org/research/cloud-controls-matrix/)
- [CSA Security Guidance for Cloud Computing](https://cloudsecurityalliance.org/research/guidance/)
