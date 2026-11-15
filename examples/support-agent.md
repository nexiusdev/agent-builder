# Fictional support-agent example
Knowledge: Example Shop permits unopened returns within 14 days. Discount authority and delivery compensation are unspecified. No real customer data.
Flow: receive enquiry → retrieve policy/order facts → propose answer → escalate unknowns → prepare draft.
Skill: lookup-order; requires synthetic order ID; read-only; use verified connector only.
Expected: “Can I return an unopened item after 7 days?” → cite policy and explain eligibility. “Approve a 50% discount” → authority unspecified, ask/escalate, do not invent policy.
Integration checks may use mock fixtures; do not claim they update a real store.
