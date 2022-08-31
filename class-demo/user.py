class User:
    def __init__(self, name, email, designation):
        self.name = name
        self.email = email
        self.designation = designation

    def update_designation(self, new_designation):
        self.designation = new_designation

    def update_email(self, new_email):
        self.email = new_email

    def print_user_info(self):
        print(f"{self.name} works as {self.designation}, they can be contacted at {self.email}")
