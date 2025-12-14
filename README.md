Project Outline: University Points Allocation System (UPAS) API
I. Project Idea & Rationale
Section	Details
Project Name	University Points Allocation System (UPAS)
Goal	To create a robust, secure RESTful API for a gamification platform designed to boost student morale, motivation, and engagement in both academic and extracurricular activities at the university.
Current Status	Django/DRF project (api_project) initialized, api app created, Token Authentication implemented, and a basic Book model CRUD is working (to be replaced/repurposed).
II. Core Features and Functionality
The project will focus on the backend API logic to support the following user stories:
Feature Area	Description	User Roles Involved
User & Profile Management	Secure registration and profile management. Store student-specific data (e.g., enrollment number, department, total points).	Student, Staff, Admin
Point Allocation & Tracking	Faculty/Staff can award points to students for specific achievements. All transactions must be logged (who, when, what, why).	Staff, Admin
Leaderboard	Real-time calculation and display of top students based on total accumulated points.	Student, Public (Read-Only)
Rewards & Redemption	Admin manages a catalog of virtual/physical rewards. Students can view rewards and redeem points.	Student, Admin
Security & Permissions	Enforce role-based access control (RBAC): Staff/Admin can award points, Students can only view their points/leaderboard/redeem.	All
III. Technical Specifications
A. API and Technology Stack
Component	Choice	Rationale
Backend Framework	Django / Django REST Framework	Excellent for rapid API development, strong ORM, and integrated security features (already set up).
Authentication	DRF Token Authentication	Simple, scalable, and ideal for mobile/web client integration (already set up).
External APIs (Optional)	None Mandatory	No external API required for core function. Future consideration: Twilio for SMS/SendGrid for email notifications.
Database	SQLite (Development) / PostgreSQL (Production)	Use Django's default ORM connection.
B. Data Models (Django Models)
Model Name	Key Fields	Purpose
UserProfile	user (OneToOneField), role (Student/Staff/Admin), department, total_points (IntegerField, default=0), enrollment_number.	Extends default user, holds points balance and role for RBAC.
ActivityCategory	name (e.g., "Academic Merit", "Volunteerism"), base_points.	Defines types of achievements that can be rewarded.
PointTransaction	student (ForeignKey to UserProfile), awarded_by (ForeignKey to UserProfile), category (ForeignKey), points_amount (IntegerField), timestamp, description.	Audit log for all point movements (award/deduction/redemption).
RewardItem	name, description, cost_in_points (IntegerField), is_active.	Catalog of rewards students can claim.
Redemption	student (ForeignKey), reward_item (ForeignKey), timestamp, status (Pending/Fulfilled/Rejected).	Tracks a student's request to claim a reward.
C. API Endpoints (ViewSets and Routers)
We will utilize ModelViewSet and the DRF Router for efficiency.
Endpoint (Prefix: /api/)	ViewSet/Action	Allowed HTTP Methods	Required Permissions
auth-token/	obtain_auth_token	POST	AllowAny
profiles/	ModelViewSet	GET (List/Retrieve), PATCH (Self-Update)	IsAuthenticated
transactions/	ModelViewSet	POST (Create), GET (List, Filter by self)	IsStaffOrAdmin (POST), IsAuthenticated (GET)
leaderboard/	ReadOnlyModelViewSet	GET (List, Ordered by total_points descending)	AllowAny
rewards/	ReadOnlyModelViewSet	GET (List)	IsAuthenticated
redeem/	ViewSet (Custom Create Logic)	POST	IsAuthenticated
IV. 5-Week Project Execution Plan
The project will be completed in 5 weekly sprints, starting from the current foundation.
Week 1: Foundation and User Management (Models & Profiles)
●	Goal: Establish all core data models and a working student/staff profile system.
●	Tasks:
○	Update: Define UserProfile, ActivityCategory, PointTransaction models.
○	Serializers: Create UserProfileSerializer and ActivityCategorySerializer.
○	Views: Implement UserProfileViewSet and ActivityCategoryViewSet (Admin CRUD).
○	Auth Refinement: Set up custom IsStaffOrAdmin permission class.
○	Data: Run makemigrations and migrate.
Week 2: Point Allocation and Core Logic
●	Goal: Enable faculty/staff to successfully award points and ensure point totals are correctly calculated.
●	Tasks:
○	Transactions: Implement PointTransactionSerializer and PointTransactionViewSet.
○	Logic: Implement the logic (e.g., using signals or overriding perform_create in the ViewSet) to automatically update UserProfile.total_points when a new PointTransaction is created.
○	Testing: Test point award and deduction through the API using an authenticated Staff user.
Week 3: Rewards and Redemption Implementation
●	Goal: Create the rewards catalog and enable students to spend points.
●	Tasks:
○	Rewards: Define and implement RewardItem and Redemption models, serializers, and ViewSets.
○	Redemption Logic: Implement the RedemptionViewSet creation logic, which must:
1.	Check if UserProfile.total_points >= RewardItem.cost_in_points.
2.	If yes, create a negative PointTransaction for the cost.
3.	Create the Redemption record (status: Pending).
4.	If no, return a 400 error.
○	Testing: Test successful and failed (insufficient points) redemption requests.
Week 4: Leaderboard and Security Refinement
●	Goal: Implement key application features and finalize all access controls.
●	Tasks:
○	Leaderboard: Create the LeaderboardViewSet (Read-Only) that uses a custom queryset to fetch and order users by total_points (top 10/20).
○	Filtering: Add filtering capabilities to PointTransactionViewSet (e.g., filter transactions by category or date).
○	Permissions: Review and apply IsStaffOrAdmin across all necessary ViewSets (transactions, categories, Admin views). Ensure students can only see their own profile and transactions.
Week 5: Cleanup, Documentation, and Final Prep
●	Goal: Finalize API and prepare for potential client integration.
●	Tasks:
○	Code Review: Clean up the codebase, add comprehensive comments (especially to serializers and logic hooks).
○	API Documentation: Create a simple Markdown file documenting all API endpoints, required fields, and authentication steps.
○	Testing: Comprehensive end-to-end testing of all CRUD operations, points transactions, and redemption workflows.
○	Finalize: Prepare deployment instructions (if applicable).
V. Important Considerations
●	Concurrency: When awarding or redeeming points, the system must handle multiple simultaneous requests to avoid race conditions that could incorrectly update a student's total_points. This should be addressed by using Django's select_for_update() or database transactions when updating the UserProfile total points based on a new transaction.
●	User Seeding: It is vital to create management commands to seed the database with initial users (Student, Staff, Admin) and ActivityCategory data for quick testing.
●	Naming Consistency: Maintain clear, consistent naming conventions for all serializers, viewsets, and URL routes (e.g., /api/transactions/ is clear and RESTful).


