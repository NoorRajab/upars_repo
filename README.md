

# UPAS: Umma University Point Allocation System

**Developer:** Noor Rajab

**Institution:** Umma University – School of Business and Technology

**Project Type:** Information System for Academic & Extracurricular Meritocracy

---

##  Project Overview

UPAS is a gamified information system designed to combat low student morale and a "dismal campus culture" at Umma University. By rewarding academic excellence, leadership, and community engagement with a points-based system, UPAS fosters a competitive yet rewarding environment.

### Key Features

* **Tiered Meritocracy:** Students progress through four tiers: **Bronze, Silver, Gold, and Platinum**.
* **Automated Logic:** Real-time point calculation and tier upgrades using Django Signals.
* **Admin Verification:** A secure workflow where staff verify activities before points are finalized.
* **RESTful API:** Full integration capability for mobile or external web apps.
* **Leaderboard:** Real-time global rankings to encourage healthy competition.
* **Reward Catalog:** A system for students to redeem points for virtual or physical university rewards.

---

##  Tech Stack

* **Backend:** Python 3.x, Django 5.x
* **API Framework:** Django REST Framework (DRF)
* **Database:** SQLite (Development)
* **Frontend:** HTML5, Bootstrap 5 (Responsive Design)
* **Authentication:** Token-based and Session-based security

---

##  The Algorithm: Tiers & Thresholds

The system automatically updates a student's status based on their **total verified points**:

| Tier | Point Range | Status |
| --- | --- | --- |
| **Bronze** | 0 - 1,000 | Entry Level |
| **Silver** | 1,001 - 2,000 | Active Participant |
| **Gold** | 2,001 - 3,000 | Campus Leader |
| **Platinum** | 3,001+ | Excellence Exemplified |

---

##  Project Structure

```text
upars/
├── upars/              # Main Project Settings (settings.py, urls.py)
├── api/                # Application Logic
│   ├── models.py       # UserProfile, Points, Rewards, Redemption
│   ├── signals.py      # Automated Tier Update Logic
│   ├── serializers.py  # DRF Serializers
│   ├── views.py        # API ViewSets & Template Views
│   └── templates/      # HTML User Interface
├── manage.py           # Django CLI
└── db.sqlite3          # Database

```

---

##  Getting Started

### 1. Prerequisites

Ensure you have Python installed.

### 2. Installation & Setup

```bash
# Clone the repository
git clone <repository-url>
cd upars

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install django djangorestframework

```

### 3. Database Initialization

```bash
python manage.py makemigrations api
python manage.py migrate

```

### 4. Create an Administrator

```bash
python manage.py createsuperuser

```

### 5. Run the Project

```bash
python manage.py runserver

```

Visit the application at: `http://127.0.0.1:8000/`

---

##  API Endpoints (Quick Reference)

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/api/auth-token/` | POST | Get Token for API access |
| `/api/profiles/` | GET | View current student tier and points |
| `/api/leaderboard/` | GET | View top 10 ranked students |
| `/api/transactions/` | POST | Admins submit points for a student |
| `/api/redeem/` | POST | Students claim a reward item |

---



**© 2025 Ahmed Noor Rajab**
