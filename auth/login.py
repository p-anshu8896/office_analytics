from auth.users import users

def login(username, password):
    if username in users and users[username] == password:
        return users[username]["role"]
    return None