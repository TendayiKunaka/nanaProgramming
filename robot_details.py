import person

robot = person.Robot("Tanya", "red", 80, 'New Diet')
robot.get_robot_info()
robot.change_name(input("Enter desired name: "))
robot.change_color(input("Enter my new color: "))
robot.change_weight(input("Enter your weight, so that I can suggest diet options: "))
robot.select_option_list(input("answer: "))
robot.get_robot_info()
robot.change_diet(input("Enter request (eg New Diet: "))

