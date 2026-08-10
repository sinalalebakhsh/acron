# 🚀 ACRON — Enterprise Django Reference Architecture

> **Plant the acorn seed, and it will grow into a mighty oak.**

**ACRON** is an open-source e-commerce reference project built to demonstrate how a Django application can evolve from a simple CRUD application into a structured, production-oriented system.

The project is intentionally developed as a **domain-based modular monolith**, with a clear separation between HTTP/API concerns and business logic.

The goal is not simply to make an online store work.  
The goal is to demonstrate **how to engineer the system behind it**.

---

## ✨ What is ACRON?

ACRON is designed to bridge the gap between:

**Django tutorials → real-world backend engineering**

It focuses on:

- Clean domain boundaries
- Service-layer business logic
- REST API design
- JWT authentication
- Database integrity
- Transactional operations
- Historical financial data integrity
- Query optimization
- React frontend integration
- Security-aware development
- A roadmap toward scalable production architecture

ACRON follows an **80/20 engineering philosophy**:

- **80% Engineering:** architecture, correctness, maintainability, scalability and security
- **20% Creativity:** flexibility and room for experimentation

---

# 🏗️ Architecture

ACRON follows a **domain-based modular monolith** rather than a collection of tightly coupled Django views.

The current architecture separates responsibilities across domains such as:

```text
ACRON
│
├── Backend
│   ├── API
│   ├── Customers
│   ├── Products
│   ├── Carts
│   ├── Orders
│   ├── Payments
│   ├── Shipments
│   └── Advisor
│
└── Frontend
    ├── React
    ├── Vite
    ├── React Router
    ├── Authentication Context
    ├── Product domain
    ├── Cart domain
    └── Orders domain
```

### Core architectural principle

HTTP concerns belong in:

- Views
- Serializers
- URLs

Business rules belong in:

- `services.py`

This keeps the application easier to test, extend and reason about.

---

# 🧩 Backend

## Django + Django REST Framework

The backend is built around Django and Django REST Framework.

The API is organized around business domains rather than putting every endpoint into one large API module.

### Current domains

| Domain | Responsibility |
|---|---|
| Customers | Customer profiles and addresses |
| Products | Product catalog |
| Carts | Shopping cart and cart items |
| Orders | Order lifecycle and order items |
| Payments | Payment-related domain |
| Shipments | Shipment-related domain |
| Advisor | Intelligent/advisor-related API |
| API | Authentication and shared API endpoints |

---

# 🛒 Customer Domain

ACRON includes a dedicated customer domain.

### Customer

A customer is associated with the project's custom user model through a one-to-one relationship.

The customer domain supports:

- Customer profile
- Phone number
- Birth date
- User information
- Multiple shipping addresses

### Address

Customers can manage multiple addresses.

Address information includes:

- Title
- Receiver name
- Phone number
- Province
- City
- Street
- Postal code
- Default-address state

The system ensures that a customer can select an address as their default address.

Address ownership is enforced at the API level so authenticated users only access their own addresses.

---

# 📦 Product Domain

The product domain provides the store catalog used by the frontend.

Products currently expose information such as:

- Name
- Slug
- Description
- Price
- Inventory
- Brand
- Category
- Main image

The frontend contains:

- Product listing
- Product detail
- Product cards
- Product availability state

---

# 🛍️ Cart Domain

The cart domain handles the user's shopping cart.

Current functionality includes:

- Customer-specific carts
- Cart items
- Product association
- Quantity management
- Add/remove operations
- Cart totals
- Cart API integration
- React cart page
- Cart context integration

The cart is intentionally separated from the order domain.

A cart represents a **temporary purchasing state**.

An order represents a **historical business record**.

---

# 🧾 Order Domain

The order domain is one of the most important parts of ACRON.

An order contains:

- Customer
- Status
- Creation timestamp
- Order items
- Frozen unit prices
- Shipping information
- Calculated total

### Order lifecycle

Current order states include:

```text
PENDING
   │
   ├──> COMPLETED
   │
   └──> CANCELED
```

Orders are exposed through authenticated API endpoints.

Users can retrieve their own orders without accessing another customer's orders.

---

# 💰 Historical Price Integrity

One of the key engineering decisions in ACRON is **freezing the product price when an order is created**.

An `OrderItem` stores:

```text
unit_price
```

instead of relying on the current product price.

For example:

```text
Product price at purchase: 12.00

OrderItem.unit_price: 12.00
```

If the product price later changes:

```text
Product price: 15.00
OrderItem.unit_price: 12.00
```

the historical order remains correct.

This is critical for financial data integrity.

---

# 📍 Shipping Snapshot

When an order is created, shipping information is copied into the order.

The order currently stores:

- Receiver name
- Phone number
- Province
- City
- Street
- Postal code

This prevents future changes to a customer's address from modifying the historical shipping information of an existing order.

In other words:

```text
Customer Address
       │
       │ order creation
       ▼
Order Shipping Snapshot
```

The order becomes an independent historical record.

---

# 🔐 Authentication & Authorization

ACRON uses JWT-based authentication through Django REST Framework and Simple JWT.

The API includes token and token-refresh endpoints.

Protected endpoints use:

```python
IsAuthenticated
```

The project also follows an ownership-based access model.

For example:

```text
Authenticated User
       │
       ├── Own Customer
       ├── Own Cart
       ├── Own Orders
       └── Own Addresses
```

This prevents users from freely accessing another customer's resources.

> Authentication hardening and the frontend login flow are still part of the active development/debugging roadmap.

---

# 🔄 Transactional Order Creation

Order creation is handled through a dedicated service:

```text
OrderService.place_order()
```

The operation is executed inside a database transaction.

Conceptually:

```text
BEGIN TRANSACTION

1. Find customer
2. Find cart
3. Validate cart
4. Create order
5. Create order items
6. Freeze product prices
7. Copy shipping information
8. Delete cart

COMMIT
```

If an error occurs during the operation, the transaction can roll back instead of leaving the database in a partially completed state.

This is implemented using Django's transaction management.

---

# 🧠 Service Layer

ACRON deliberately avoids putting complex business logic directly inside views.

For example:

```text
View
  │
  ▼
Serializer
  │
  ▼
OrderService
  │
  ├── Customer validation
  ├── Cart validation
  ├── Order creation
  ├── OrderItem creation
  ├── Price snapshot
  ├── Shipping snapshot
  └── Cart cleanup
```

This makes business logic reusable and easier to test independently from HTTP requests.

---

# ⚡ Query Optimization

The project uses Django ORM optimization techniques such as:

```python
select_related()
prefetch_related()
```

For example, the orders API prefetches order items and their products.

This is intended to reduce unnecessary database queries and prevent common N+1 query problems.

---

# 🆔 UUIDs for Sensitive Resources

Carts and orders use UUID primary keys instead of predictable sequential integer IDs.

Example:

```text
1bc01589-7012-4d51-a80e-143d06328183
```

This makes resource identifiers substantially harder to guess than:

```text
/orders/1/
/orders/2/
/orders/3/
```

UUIDs are not a replacement for authorization, but they are useful as an additional layer of resource identification design.

---

# 📚 API Documentation

ACRON integrates automated API documentation with:

- OpenAPI 3
- Swagger UI
- ReDoc
- `drf-spectacular`

The API documentation is generated from the Django REST Framework API definitions.

---

# ⚛️ Frontend

The frontend is being developed separately from the Django backend.

Current frontend stack:

- React
- Vite
- React Router
- Axios
- Context API

The frontend follows the same domain-oriented direction as the backend.

Current pages/domains include:

```text
Home
Products
Product Detail
Cart
Orders
Login
```

---

# 🛒 Current Frontend Flow

The current purchasing flow is being developed in this direction:

```text
Products
   │
   ▼
Product Detail
   │
   ▼
Add to Cart
   │
   ▼
Cart
   │
   ▼
Checkout
   │
   ▼
Order
   │
   ▼
Payment
```

The Orders page is already connected to the backend orders API and displays:

- Order ID
- Status
- Creation date
- Products
- Quantity
- Unit price
- Total price

---

# 🧪 Engineering Validation

The development process includes direct validation of business rules through Django's shell and API behavior.

Examples already validated include:

### Order creation

```text
Cart
  ↓
Order
  ↓
OrderItem
```

### Frozen price

```text
Product price = 12.00

OrderItem.unit_price = 12.00
```

Changing the product's current price does not change the historical order item's price.

### Cart cleanup

After successful order creation:

```text
Cart exists → False
Order exists → True
```

### Order ownership

The orders endpoint returns the authenticated user's orders rather than exposing every order in the system.

---

# 🧭 Development Methodology

ACRON is intentionally developed incrementally.

The project does **not** follow random feature development.

The development strategy is:

```text
Infrastructure
      ↓
Domain
      ↓
Business Logic
      ↓
API
      ↓
Frontend Integration
      ↓
Validation
      ↓
Security & Hardening
      ↓
Testing
      ↓
Optimization
```

The objective is to understand why every architectural decision exists.

---

# 🗺️ Development Roadmap

## ✅ Completed / Implemented

- [x] Django backend foundation
- [x] Django REST Framework API
- [x] Custom user integration
- [x] Customer domain
- [x] Customer profile
- [x] Address management
- [x] Default address handling
- [x] Product domain
- [x] Product listing API
- [x] Product detail API
- [x] Cart domain
- [x] Cart items
- [x] Order domain
- [x] Order items
- [x] Order status management
- [x] Transactional order creation
- [x] Historical order price freezing
- [x] Shipping information snapshot
- [x] Cart cleanup after order creation
- [x] Authenticated order retrieval
- [x] Payment-status simulation endpoint
- [x] React + Vite frontend
- [x] React Router
- [x] Product pages
- [x] Cart page
- [x] Orders page
- [x] API service layer on frontend
- [x] OpenAPI / Swagger / ReDoc integration

---

## 🚧 Active Development

The following items are intentionally postponed until the current domain development path reaches the appropriate stage.

### 1. Authentication / Login

The frontend login flow and `/api/me/` integration require further debugging and hardening.

### 2. Product Images

Product images are available in the product data model/API flow, but frontend image rendering still needs a final integration pass.

### 3. Frontend UI / Layout

The current frontend prioritizes functionality and domain integration over visual polish.

The following will be improved later:

- Product grid
- Cart grid
- Order cards
- Image presentation
- Responsive layout
- Typography
- Spacing
- Empty states
- Loading states
- Error states
- Overall visual consistency

### 4. Security Hardening

After the main domain flow is stable, the project will receive a dedicated security review covering areas such as:

- Authentication
- Authorization
- Object ownership
- Input validation
- API exposure
- Sensitive data handling
- Error handling
- Rate limiting
- Security configuration

### 5. Bug & Reliability Pass

After the planned domain development stages are completed, the project will receive a dedicated debugging and reliability pass.

This includes:

- Backend/API edge cases
- Frontend state issues
- Authentication edge cases
- Order lifecycle edge cases
- Cart consistency
- Database integrity
- Error handling
- Regression testing

These five items are intentionally tracked instead of being solved with random or temporary fixes.

---

# 🔮 Future Architecture

The long-term roadmap includes:

- [ ] Complete checkout flow
- [ ] Production payment gateway integration
- [ ] Secure payment callbacks
- [ ] Shipment lifecycle
- [ ] Inventory reservation/release
- [ ] Celery background tasks
- [ ] Redis integration
- [ ] Notification services
- [ ] Shared core services
- [ ] Email / SMS infrastructure
- [ ] PDF generation
- [ ] Automated testing expansion
- [ ] CI/CD
- [ ] Monitoring and observability
- [ ] Performance profiling
- [ ] Production deployment
- [ ] AI-assisted services and integrations
- [ ] Further enterprise architecture evolution

---

# 🤖 ACRON & AI — No "Vibe Coding"

ACRON explicitly rejects **Vibe Coding** as a development methodology.

AI can assist with:

- Debugging
- Documentation
- Research
- Refactoring suggestions
- Translation
- Code review
- Exploring alternative implementations

But AI-generated code should not be accepted blindly.

The developer must understand:

```text
Why?
How?
What are the trade-offs?
What happens in the database?
What happens under failure?
What happens under concurrency?
```

The architecture and business rules must remain understandable to the engineer maintaining the system.

AI is an **engineering assistant**, not the architect.

---

# 📖 Documentation

### Core Documentation

- [Documentation](https://github.com/sinalalebakhsh/acron/blob/main/Documentation.md)
- [Project Roadmap & Introduction](https://sinalalenakhsh.notion.site/ACRON-387da1eb8b9d8005a372ce7394463792)
- [Contributing Guide](https://github.com/sinalalebakhsh/acron/blob/main/CONTRIBUTING.md)

---

# 🚀 Getting Started

## Clone the project

```bash
git clone https://github.com/sinalalebakhsh/acron.git
cd acron
```

## Backend

Move into the backend directory:

```bash
cd backend
```

Create/activate the Pipenv environment:

```bash
pipenv shell
```

Install project dependencies:

```bash
pipenv install
```

Run migrations:

```bash
python manage.py migrate
```

Start Django:

```bash
python manage.py runserver
```

The backend will normally be available at:

```text
http://127.0.0.1:8000/
```

---

# ⚛️ Frontend

Move into the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start Vite:

```bash
npm run dev
```

The frontend will normally be available at:

```text
http://localhost:5173/
```

---

# 📚 API Endpoints

The current API structure includes domains such as:

```text
/api/products/
/api/carts/
/api/orders/
/api/customers/
/api/token/
/api/token/refresh/
/api/me/
```

Interactive API documentation is provided through:

```text
/api/schema/
/api/docs/
/api/redoc/
```

---

# 🧱 Project Philosophy

ACRON is not intended to be just another e-commerce demo.

It is an evolving **engineering reference project**.

The store domain provides a realistic environment in which to explore:

- Domain-driven organization
- Business rules
- Transactions
- Financial integrity
- Authentication
- Authorization
- API design
- Database modeling
- Frontend/backend integration
- Scalability
- Security
- Testing
- Performance
- Production architecture

The implementation is expected to evolve.

The architecture is expected to become stronger with every iteration.

---

# 🌱 The Vision

> **Plant the acorn seed, and it will grow into a mighty oak.**

ACRON starts as an e-commerce application.

The long-term vision is much larger:

**Open Source + Engineering Education + AI + Production Architecture**

The project aims to become a practical reference for developers who want to move beyond tutorials and learn how real software systems are designed, implemented, tested and evolved.

---

# 🤝 Community

ACRON is open to:

- Contributors
- Code reviewers
- Backend developers
- Frontend developers
- Students
- Architects
- Researchers
- Open-source enthusiasts

Whether you want to study the architecture, contribute code, review decisions, or use ACRON as a reference for your own project, you are welcome.

---

# 👨‍💻 Author

**Sina Lalehbakhsh**

Backend-focused software developer working primarily with:

- Python
- Django
- Django REST Framework
- Go
- JavaScript / React
- Linux
- Git
- Docker
- Database systems

GitHub:

https://github.com/sinalalebakhsh

---

## ⭐ If ACRON helps you

If you find the project useful, consider giving the repository a ⭐ on GitHub.

It helps the project grow — just like the acorn.
