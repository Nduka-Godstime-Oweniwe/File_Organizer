def user_input(prompt: str,max: int, allowed: str):
    while True:
        try:
            user=input(prompt)
            if user.lower()==allowed.lower():
                return user.lower()
            user=int(user)
            if not 1<=user<=max:
                print("Invalid!")
                continue
            return user
        except ValueError:
            print("Invalid!")