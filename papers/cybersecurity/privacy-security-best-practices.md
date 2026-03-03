# Privacy and Security in Educational Data Systems

## Data Classification and Access Control

Implement a four-tier classification scheme: Public, Internal, Confidential, and Restricted. Student education records, Social Security numbers, financial aid data, and health records fall into Restricted. Apply the principle of least privilege so that users only access what their role requires. Role-based access control works well for administrative systems; consider attribute-based access for research environments with more dynamic needs. Review permissions quarterly and revoke immediately upon role change or separation.

## Encryption and Technical Safeguards

Encrypt data at rest and in transit without exception. Enforce TLS 1.2 or higher across all web applications, email, and API integrations. Use AES-256 on databases containing Confidential or Restricted data. Require full-disk encryption on all institutional devices. Deploy multi-factor authentication for all administrative systems, VPN access, and any system containing student records -- MFA alone blocks over 99% of automated credential attacks. Segment networks to isolate sensitive systems from general campus traffic.

## Vendor Security Management

Every third-party vendor with access to institutional data needs a security assessment before contract signing. Require HECVAT questionnaire completion and SOC 2 Type II report review. Contracts must include data breach notification requirements, data ownership clauses, data deletion upon termination, and audit rights. Build vendor risk assessment into procurement workflows so that security review happens before the purchase order, not after the incident.

## Incident Response and Awareness

Maintain a documented incident response plan with clearly defined roles: who declares an incident, who leads response, who handles communications, who contacts legal. Test through tabletop exercises twice per year. Supplement annual compliance training with monthly phishing simulations, department-specific data handling sessions, and just-in-time training triggered by risky behavior. The goal is building security-conscious culture, not checking a compliance box.
