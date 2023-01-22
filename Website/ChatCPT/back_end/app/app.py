from database import add_user, get_all_users, update_user_email, delete_user

# Add a new user
add_user("John Smith", "johnsmith@example.com", "password123")

# Query all users
users = get_all_users()
for user in users:
    print(user.username)

# Update a user's email
update_user_email(1, "janesmith@example.com")

# Delete a user
#delete_user(1)
