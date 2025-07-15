# 📚 LitShelf Database Design Case Study

## 📘 Background

LitShelf, a growing online bookstore, is aiming to enhance its platform to compete with major e-commerce players. The platform supports sales of **physical books**, **e-books**, and **audiobooks**, while also introducing advanced features such as:

- Subscription-based access
- Promotional campaigns
- Multilingual support
- Integration with third-party logistics providers
- A robust recommendation engine

To enable this growth, LitShelf requires a **sophisticated relational database** that supports complex operations, maintains performance, and scales effectively.

---

## 🎯 Objective

Design a **comprehensive relational database schema** for LitShelf that:

- Supports the expanded business operations
- Applies advanced database principles (normalization, indexing, etc.)
- Handles real-world challenges such as:
  - Multilingual data
  - Temporal data
  - Third-party integration
  - Personalization and analytics

---

## ✅ Requirements

### 1. 📚 Books Management

**Entity:** `Book`  
Includes:

- Title, subtitle, authors, publishers, publication date, genres, ISBN, language
- Format: Physical, E-Book, Audiobook
- Price and stock quantity (for physical books)
- Edition number, page count
- File format (PDF, EPUB, MP3), file size
- Duration (for audiobooks)
- Multiple authors/contributors (editors, narrators)
- Belonging to multiple genres (e.g., "Mystery", "Thriller")
- Translations tracked with unique ISBNs
- Historical price changes

---

### 2. 👤 Customer Management

**Entity:** `Customer`  
Includes:

- Full name, email, phone number, preferred language, created/updated timestamps
- Multiple shipping and billing addresses (with default)

**Additional:**

- Optional social media IDs
- Loyalty program:
  - 1 point per $10 spent (rounded down)
  - Membership tiers (Bronze, Silver, Gold)
- Subscription plans:
  - Monthly audiobook or unlimited e-book access
  - Start and end dates

---

### 3. 🛒 Order Processing

**Entity:** `Order`  
Tracks:

- Order date, total amount, taxes, discounts
- Shipping method, tracking number
- Status (pending, processing, shipped, etc.)
- Partial shipments supported
- Multiple items (with quantities and prices)

**Digital Downloads:**

- Unique URLs
- Generation date
- Expiry (e.g., 30 days)
- Max download attempts (e.g., 3)

**3PL Integration:**

- Provider name, API endpoint
- Shipment tracking updates (e.g., in transit, delivered)

---

### 4. 🌟 Reviews and Ratings

- Star rating (1–5), review text, date, optional images
- Verified purchase flag
- Review moderation (approved, pending, rejected) with moderator comments
- Customers can like/report reviews

---

### 5. 🤖 Recommendations and Analytics

- **Customer Activity:**

  - Browsing history (books viewed, time spent, date)
  - Search history (terms, timestamps)

- **Recommendations:**
  - Based on purchases, browsing, genre preference
  - Source (algorithm, manual)
  - A/B testing support (test group, outcomes)

---

### 6. 💸 Promotions and Discounts

- Campaign name, start/end dates
- Discount types (percentage, fixed)
- Eligible books or genres
- Coupon codes with usage limits and expiry
- Customer coupon usage
- Bundle offers (e.g., buy 2, get 1 free)

---

### 7. 🌍 Multilingual Support

- Book titles, descriptions, and reviews in multiple languages
- Customer preferred language for UI and emails
- Localized pricing (USD, EUR, etc.)

---

### 8. 📏 Business Rules

- One customer → many orders
- One order → one customer
- One book → many reviews
- One review → one book, one customer
- E-books/audiobooks have no stock but require secure downloads
- Loyalty points expire after 12 months
- Subscription auto-renews unless canceled
- Translation = separate book (linked to original, different ISBN)
- Inappropriate reviews can be reported → moderation triggered

---

## 🧩 Schema Design

_Design the relational schema based on the requirements above, applying:_

- Normalization (up to 3NF or higher)
- Proper use of foreign keys and indexes
- Temporal tracking (e.g., price history, subscription periods)
- Junction tables for many-to-many relationships (e.g., books ↔ authors, books ↔ genres)
- Entity relationships supporting multilingual and versioned content

---

## 🛠️ Future Enhancements

- Audit logs for customer actions
- Real-time analytics via materialized views or ETL pipelines
- Machine-learning-ready tables for behavior modeling

---

## 📂 License

This project is intended for academic and training purposes. Feel free to fork and contribute!
