# social_network
Build a Django Rest Framework API for a Social Networking App: User authentication, friend requests, search users by email/name, pagination
*Social Network App*
This project is a social networking application built using Django Rest Framework. The app provides user authentication, friend requests, and a search feature.

Features
User Signup/Login: Users can sign up with their email and log in with their email and password. Emails are case-insensitive.
Authentication: All APIs except signup and login require authentication.
Search Users: Search users by email or name with pagination (up to 10 records per page). If the search keyword matches an exact email, the associated user is returned. If the keyword is a substring of a name, all matching users are returned.
Friend Requests: Send, accept, or reject friend requests.
Friends List: View a list of users who have accepted friend requests.
Pending Requests: List all received friend requests.
Rate Limiting: Users can send a maximum of 3 friend requests per minute.
Project Components
Django Models: Define the user, friend requests, and other necessary models.
Django Views: Handle API requests and responses for user interactions.
Django URLs: Route URLs to the appropriate views.
Authentication: Implement token-based authentication for secure access.
Throttling: Apply rate limiting to control the frequency of friend requests.
Docker: Containerize the application for easy deployment.
Setup Instructions
Clone the repository.
Install dependencies using pip install -r requirements.txt.
Set up the database and run migrations.
Start the Django development server.
Use the provided Postman collection to test API endpoints.
