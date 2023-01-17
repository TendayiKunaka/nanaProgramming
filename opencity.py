class OpenCity:
    def __init__(self, email, name, password, job_title):
        self.email = email
        self.name = name
        self.password = password
        self.job_title = job_title

    def get_user_details(self):
        print(f"Employee {self.name} is employed by Equals, Email: {self.email} and is the {self.job_title}")
        print(f"Passcode: {self.password}")

    def change_email(self, new_email):
        self.email = new_email

    def change_name(self, new_name):
        self.name = new_name

    def change_password(self, new_password):
        self.password = new_password

    def change_title(self, new_title):
        self.job_title = new_title

        #added a comment to see how best I can upload to Git withot any commands

