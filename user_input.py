def user_input(prompt: str,max: int, allowed=()):
    while True:
        try:
            user=input(prompt)
            if user.lower() in allowed:
                return user.lower()
            user=int(user)
            if not 1<=user<=max:
                print("Invalid!")
                continue
            return user
        except ValueError:
            print("Invalid!")