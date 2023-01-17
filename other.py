class User:
    def __init__(self, email, name, password, current_job_title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def chane_job_title(self, new_job):
        self.current_job_title = new_job

    def get_user_info(self):
        print(f"User {self.name} registered as {self.current_job_title} @ email: {self.email}")



