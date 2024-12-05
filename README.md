**Project Name: User Management System**
Description:
The User Management System is a Django-based web application designed for administrators to manage users and their roles. The system allows CRUD (Create, Read, Update, Delete) operations for user accounts, role assignments, and status management. This system provides an efficient way for admins to maintain a large number of users, ensuring secure access control through roles and permissions.

**Technologies Used:**
Backend: Django (Python 3.12.5)
Frontend: HTML, CSS, JavaScript 
Database: MySQL 
Version Control: Git / GitHub 
Authentication: Django built-in user authentication system
**Features of the Project**
**1. User Management**
Create Users: Admins can create new user accounts by specifying a username, email, role, and status.
Edit Users: Admins can modify existing user details, including their username, email, role, and status.
Delete Users: Admins can delete user accounts from the system.
View Users: Admins can view a list of all users with options for sorting and pagination.
**2. Role Management**
Role CRUD Operations: Admins can manage roles by creating, updating, or deleting roles.
Role Assignment: Admins can assign roles to users to control access and permissions. Each role has a specific set of permissions associated with it.
Distinct Roles: The system fetches distinct roles for use in forms and ensures no duplication of role names in the system.
**3. Permission Management**
Role-based Access Control (RBAC): Roles are tied to specific permissions. Each role defines what actions a user can perform within the system.
Access Control: Admins and users with specific roles have access to different parts of the system. For example, only users with an admin role can add or edit other users.

**Clone the project repository:**
**1.git clone <repository-url>
2.cd <project-directory>
3.activate the environment by D:\RBAC\rbacui\Scripts\activate
4.cd D:\RBAC\RBAC_Admin 
5.pip install -r requirements.txt
6.python manage.py migrate
7.python manage.py runserver
then, copy http://127.0.0.1:8000/dashboard1 and paste it in browser then we can see the admin dashboard with useful links in the side bar.**

