# Back-End Developer — Technical Assessment Task

> **Please read first:** You are **not required to implement everything** in this document. Leaving out multiple sections is perfectly acceptable — we are interested in your approach and the quality of what you do build, not in full coverage. **What matters most is that you record and report how much time you spent on the project.** Please include this clearly in your README.

## Overview

Build the **back-end APIs** for a support ticketing system used by an e-commerce platform. Customers raise tickets against their orders and support staff respond; both sides are kept in sync through email and SMS notifications.

**No user interface is required.** The deliverable is the API — together with the data model, business rules, notifications, and deployment. You will expose **two API surfaces**:

- **Support portal (admin) APIs** — consumed by an internal support/admin web app.
- **User-side APIs** — consumed by a hypothetical customer-facing front-end web app.

The task is intentionally scoped to exercise back-end skills: data modeling, business-rule enforcement, conditional payloads, file handling, notifications, and query endpoints with sorting/filtering.

---

## Scenario & Domain

An order moves through the following statuses:

1. **Awaiting payment**
2. **Paid**
3. **In preparation**
4. **Shipped**
5. **Delivered**

A customer can open a support ticket against an order. The behavior and the data accepted by the ticketing APIs depend on the status of the order the ticket relates to.

---

## API Surfaces

### User-side APIs (for the hypothetical customer front end)

- List a customer's orders (both active and historical) so a ticket can be linked to one.
- Create a ticket linked to a specific order, enforcing the status-dependent rules below.
- Post messages to an existing ticket.
- Re-open a ticket (subject to the rules below).
- Fetch a customer's tickets and their messages, with timestamps.
- Upload files (image size/type validation).
- Record and expose the customer's **last activity time ("Last seen")**.

### Support portal (admin) APIs

- List tickets, with **default ordering newest → oldest**.
- Provide the data needed for response-time color coding (e.g. last-response timestamp or a computed waiting state: answered / waiting > 24h / waiting > 72h).
- Filter to show **only tickets linked to delivered orders**.
- Fetch full ticket detail (messages, uploaded files, driver info).
- Post a support reply (which triggers notifications).

> Authentication may be simplified or assumed (e.g. a header or token identifying the user / admin). Don't spend the bulk of your time on auth.

---

## Functional Requirements (server-side business rules)

### 1. Order status and ticket creation

The create-ticket endpoint must accept and validate different payloads depending on the order's status:

- **Delivered** — accept an uploaded photo and a problem description.
- **Shipped** — return the assigned driver's details, and accept a request related to the shipment.
- **Any other status** (awaiting payment, paid, in preparation) — accept only a free-text message to support.

These rules must be enforced **server-side**, not assumed to be handled by the client.

### 2. Linking a ticket to an order

- Each ticket is linked to a specific order belonging to the customer.
- **Each order can have only one ticket.** To follow up on the same order, the customer re-opens the existing ticket rather than creating a new one. Re-opening is allowed only within **one week of delivery**.

### 3. Notifications

- For every ticket message — whether a customer question or a support reply — send an **email and an SMS** to the customer at the same time.
- Persist the date and time of each message so the front end can display it.

### 4. Admin querying

- Support listing tickets ordered newest → oldest by default.
- Expose response-time information sufficient to drive color coding (answered / waiting > 24h / waiting > 72h).
- Support filtering to tickets linked to delivered orders.

### 5. Data contract

**Ticket list / overview responses should include:**
- Ticket ID
- Order ID (if linked)
- Customer name
- Ticket status (open / closed / pending)
- Creation time
- Time of last message
- Number of unanswered messages

**Ticket detail responses should include:**
- Date and time of each message
- Message text content
- Uploaded files
- Driver information (when the related order is shipped)

### 6. File upload

- Enforce size and type limits for image uploads server-side.

---

## Technical Requirements

- API style (REST, GraphQL, etc.) is your choice — design it cleanly and consistently.
- Provide API documentation (OpenAPI/Swagger, a README section, or a request collection) so the contract is clear to a front-end consumer.
- Email and SMS sending should use **placeholders** — printing a log line in place of each message is perfectly acceptable. What matters is that the integration point is clearly implemented and the events fire correctly.

---

## Deployment Requirements

- The application must be deployable using **Docker Compose**, with all services (back end, database, and any supporting services) defined as containers.
- **Nginx** must be used as the reverse proxy in front of the API.
- Include the `docker-compose.yml`, `Dockerfile`(s), and Nginx configuration in the repository, and document the full deployment process in the `README`.

---

## Deliverables

1. A working back-end exposing the APIs described above.
2. Source code in a Git repository with a clear commit history.
3. API documentation (OpenAPI, README section, or request collection).
4. A short `README` explaining how to run the project locally, **how much time you spent on the project**, any assumptions made, and any trade-offs or items left out.

---

## Evaluation Criteria

Candidates are assessed uniformly against the following:

| Area | What we look for |
|------|------------------|
| **Correctness** | Implemented endpoints behave as specified (status-dependent payloads, ticket/order rules). |
| **Data modeling** | Sensible schema for orders, tickets, messages, attachments, and drivers. |
| **API design** | Clean, consistent, well-documented endpoints for both the admin and user surfaces. |
| **Business rules** | Server-side enforcement of one-ticket-per-order, the re-open window, and status-based validation. |
| **Notifications** | Email and SMS placeholders fire correctly on the right events. |
| **Deployment** | Deployable via Docker Compose behind Nginx, with the process documented in the README. |
| **Code quality** | Readability, structure, naming, validation, and tests where appropriate. |
| **Communication** | Quality of the README/API docs and clarity around assumptions and trade-offs. |
