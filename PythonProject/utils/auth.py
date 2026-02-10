def login(user):
    if user == "bad_user":
        raise ValueError("AuthenticationError")
