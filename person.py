class Robot:
    def __init__(self, name, color, weight, answer):
        self.name = name
        self.color = color
        self.weight = weight
        self.answer = answer

    def get_robot_info(self):
        print(f"I'm a robot and my name is {self.name} I'm {self.color} and I weigh {self.weight} kg and {self.answer}")
        print("You can change my settings at nay time: ")
        print("I'm at your service, what would you like me to do for you")

    def select_option_list(self, answer):
        self.answer = answer

    def change_name(self, new_name):
        self.name = new_name

    def change_color(self, new_color):
        self.color = new_color

    def change_weight(self, new_weight):
        self.weight = new_weight

    def change_diet(self, new_request):
        self.answer = new_request
        if new_request == "New Diet":
            print("You are overweight, you need to loose 5 kgs")
            print("I will help you")
            print("Morning Diet: Eggs, bacon, apple ")

