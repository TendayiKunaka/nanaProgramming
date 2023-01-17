import other


app_user = other.User("nana@gmail.com", "Nana", "qwerty", "Tester")
app_user.chane_job_title("Developer")
app_user.get_user_info()

app_user = other.User("gari@gmail.com", "Gari", "qwerty", "Tester")
app_user.chane_job_title("Administrator")
app_user.get_user_info()

app_user = other.User("peter@gmail.com", "Peter", "qwerty", "Tester")
app_user.chane_job_title("Teacher")
app_user.get_user_info()