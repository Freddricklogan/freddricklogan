# Profile README copy — Featured grid and five-minute review

Drop-in copy for the `portfolio-refresh` branch. Thumbnails are the existing Unsplash images for each project (the generator should pull them from `projects.yml`); only the words are new. Every claim below is measured or visible in the demo — nothing aspirational.

---

## Featured (3 × 2 grid, above the fold)

```html
<h2 id="featured">Featured</h2>
<p>Six projects that show the range: security operations, learning analytics, digital credentials, cloud infrastructure, and computational modelling — each with a live demo that needs no account.</p>

<table border="0">
<tr>
<td width="33%" valign="top" align="center">
<img src="{{siem-log-analyzer.thumbnail}}" width="280" alt="SIEM Log Analyzer thumbnail" /><br />
<b><a href="https://freddricklogan.github.io/siem-log-analyzer/">SIEM Log Analyzer</a></b><br />
<sub>Raw security telemetry in, ranked ATT&amp;CK-mapped incidents out. Eight detection rules, six correlation rules, all client-side.</sub><br />
<a href="https://freddricklogan.github.io/siem-log-analyzer/"><b>Live demo</b></a> &middot; <a href="https://github.com/Freddricklogan/siem-log-analyzer">Source</a>
</td>
<td width="33%" valign="top" align="center">
<img src="{{student-engagement-api.thumbnail}}" width="280" alt="Student Engagement API thumbnail" /><br />
<b><a href="{{student-engagement-api.demo}}">Student Engagement Analytics API</a></b><br />
<sub>Finds the students who are disengaging before the withdrawal form does. FastAPI, role-based access, 146 tests at 98% coverage.</sub><br />
<a href="{{student-engagement-api.demo}}"><b>Live demo</b></a> &middot; <a href="https://github.com/Freddricklogan/student-engagement-api">Source</a>
</td>
<td width="33%" valign="top" align="center">
<img src="{{verifiable-academic-credentials.thumbnail}}" width="280" alt="Verifiable Academic Credentials thumbnail" /><br />
<b><a href="https://freddricklogan.github.io/verifiable-academic-credentials/">Verifiable Academic Credentials</a></b><br />
<sub>Learner-owned credentials any verifier can check without calling the issuer. Real <code>did:key</code>, P-256 signatures, revocation via status list.</sub><br />
<a href="https://freddricklogan.github.io/verifiable-academic-credentials/"><b>Live demo</b></a> &middot; <a href="https://github.com/Freddricklogan/verifiable-academic-credentials">Source</a>
</td>
</tr>
<tr>
<td width="33%" valign="top" align="center">
<img src="{{aws-terraform-gameday.thumbnail}}" width="280" alt="AWS Terraform Game Day thumbnail" /><br />
<b><a href="https://freddricklogan.github.io/aws-terraform-gameday/">AWS Terraform Game Day</a></b><br />
<sub>Production-grade three-tier infrastructure, taught by breaking it. Six challenges, six solutions, 148 passing security checks.</sub><br />
<a href="https://freddricklogan.github.io/aws-terraform-gameday/"><b>Live demo</b></a> &middot; <a href="https://github.com/Freddricklogan/aws-terraform-gameday">Source</a>
</td>
<td width="33%" valign="top" align="center">
<img src="{{neural-network-playground.thumbnail}}" width="280" alt="Neural Network Playground thumbnail" /><br />
<b><a href="https://freddricklogan.github.io/neural-network-playground/">Neural Network Playground</a></b><br />
<sub>Watch a network learn one gradient step at a time. Build the layers, press Train, and see the decision boundary move.</sub><br />
<a href="https://freddricklogan.github.io/neural-network-playground/"><b>Live demo</b></a> &middot; <a href="https://github.com/Freddricklogan/neural-network-playground">Source</a>
</td>
<td width="33%" valign="top" align="center">
<img src="{{epidemic-modeling-dashboard.thumbnail}}" width="280" alt="Epidemic Modeling Dashboard thumbnail" /><br />
<b><a href="https://freddricklogan.github.io/epidemic-modeling-dashboard/">Epidemic Modeling Dashboard</a></b><br />
<sub>SIR, SEIR, SIRD and SIRV simulations on a Runge-Kutta solver, with sensitivity analysis you can drive from the sliders.</sub><br />
<a href="https://freddricklogan.github.io/epidemic-modeling-dashboard/"><b>Live demo</b></a> &middot; <a href="https://github.com/Freddricklogan/epidemic-modeling-dashboard">Source</a>
</td>
</tr>
</table>
```

---

## Review this portfolio in five minutes

```html
<h2 id="five-minute-review">Review this portfolio in five minutes</h2>

<table border="0">
<tr>
<td valign="top" width="33%">
<b>1 &middot; Security operations &mdash; 90 seconds</b><br />
Open the <a href="https://freddricklogan.github.io/siem-log-analyzer/">SIEM Log Analyzer</a> and press <i>Take the 30-second tour</i>. Then click <i>Ingest sample batch</i> twice and watch the correlated-incident count change. The detection and ATT&amp;CK mapping logic is real; the telemetry is simulated.<br />
<sub>What it shows: detection engineering, threat modelling, and how I explain a security pipeline to a non-security executive.</sub>
</td>
<td valign="top" width="33%">
<b>2 &middot; Learning analytics &mdash; 2 minutes</b><br />
Open the <a href="{{student-engagement-api.demo}}">Student Engagement API explorer</a>, sign in with the read-only demo account shown on the page, and call <code>GET /api/v1/analytics/summary</code>. Then try the same call as the viewer role against a write endpoint and read the 403 response &mdash; it is a structured problem report, not a stack trace.<br />
<sub>What it shows: backend architecture, role-based access, and the engineering discipline behind a 98%-covered service.</sub>
</td>
<td valign="top" width="33%">
<b>3 &middot; Digital credentials &mdash; 90 seconds</b><br />
Open <a href="https://freddricklogan.github.io/verifiable-academic-credentials/">Verifiable Academic Credentials</a>, issue a credential, verify it, then edit one character of the payload and verify again. The second check fails because the signature covers the canonical document, not the display.<br />
<sub>What it shows: applied cryptography, W3C credential standards, and the credentialing work behind Elevate.</sub>
</td>
</tr>
</table>

<p><sub>Prefer code to demos? Every repository opens with the same six-section README: problem, competencies, architecture diagram, engineering decisions, one-command setup, and demo walkthrough. Start with any <b>Flagship</b>-tagged project below.</sub></p>
```

---

## Section VI intro line

> Nine projects, one per University of Oxford Saïd Business School executive programme, each turning the programme's frameworks into working software with a live demo.

## Roadmap intro line

> Three convergence projects planned for 2027, each sitting at the intersection of security, data science, education, and distributed systems. Architecture and milestone plans are in the <a href="docs/MODERNIZATION_BLUEPRINT.md#section-2-flagship-projects">portfolio blueprint</a>.

---

## Notes for the generator

- `{{repo.thumbnail}}` and `{{repo.demo}}` resolve from `projects.yml`. The API demo URL is whichever Render/Fly URL is live for the Scalar explorer; if it is not live yet, the row must say so rather than link to nothing.
- Keep the Featured grid at 280 px thumbnails so it renders as three columns at desktop width and stacks cleanly on mobile.
- Numbers in the pitches (146 tests, 98 %, 148 checks, eight rules, six rules) are measured values from CI; update them from the badges if they change.
- Voice: direct, calibrated, no superlatives. "Real", "measured", "simulated" are load-bearing words — keep them.
