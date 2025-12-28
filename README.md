

# UPAS Backend - Points Allocation and Reward System

This directory contains the **Django REST Framework (DRF)** backend for the Umma University Points Allocation and Reward System (UPAS). The backend manages the core logic for the Point Allocation Algorithm, Tier Progression, and the Administrative Verification Algorithm (AVA).

##  System Architecture

The backend is structured into two main components as per the project requirements:

* **`upars/`**: Project configuration, settings, and root URL routing.
* **`api/`**: The core application logic containing models, serializers, signals (for algorithms), and ViewSets.

---

##  Core Technical Features

### 1. The Algorithm Engine (`api/signals.py`)

The backend utilizes Django Signals to maintain an **Immediate Feedback Loop**.

* **Point Allocation**: Calculates student merit based on category-specific weighting constants.
* **Tier Allocation**: Automatically updates student status between **Bronze, Silver, Gold, and Platinum** based on point thresholds (e.g., Platinum  3001 points).

### 2. Administrative Verification Algorithm (AVA)

All point-earning activities are stored in a `PointTransaction` model. Points are only credited to the student's profile once the `is_verified` boolean is set to `True` by an authorized administrator.

### 3. API Endpoints

| Endpoint | ViewSet | Purpose |
| --- | --- | --- |
| `/api/auth-token/` | `obtain_auth_token` | Secure Token-based login. |
| `/api/profiles/` | `UserProfileViewSet` | Student profile and current tier status. |
| `/api/transactions/` | `PointTransactionViewSet` | Point awarding and history. |
| `/api/leaderboard/` | `LeaderboardViewSet` | Top 10 rankings by total points. |
| `/api/rewards/` | `RewardItemViewSet` | Catalog of items available for redemption. |

---

##  Getting Started

### Prerequisites

* Python 3.10+
* MySQL Server (XAMPP/WAMP or Standalone)
* Virtual Environment (Recommended)

### Installation

1. **Clone the repository**:
```bash
git clone https://github.com/NoorRajab/upars_repo.git
cd upars_repo

```


2. **Setup Virtual Environment**:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

```


3. **Install Dependencies**:
```bash
pip install django djangorestframework django-cors-headers mysqlclient

```


4. **Database Configuration**:
Create a database named `upas_db` in your MySQL server. Update the `DATABASES` setting in `upars/settings.py` if your local credentials differ from the default.
5. **Run Migrations**:
```bash
python manage.py makemigrations
python manage.py migrate

```


6. **Start the Development Server**:
```bash
python manage.py runserver

```



---

##  Security & Permissions

The backend enforces strict permission classes:

* **`IsAuthenticated`**: Required for all students to view their own data and rewards.
* **`IsStaffOrAdmin`**: Custom permission required for creating `ActivityCategories` and verifying `PointTransactions`.
* **CORS**: Configured in `settings.py` to allow secure communication with the desktop/web frontend.

---

##  Testing

To run the test suite (located in `api/tests.py`):

```bash
python manage.py test api

```

---

**Developed by:** Ahmed Noor Rajab

**Affiliation:** Umma University - Faculty of Information Technology

**Date:** November 2025
