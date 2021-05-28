
import rospy
from robot_skills import get_robot


Text = ["Dear European commissioner Gabriel",
        #"Dear ministers van Engelshoven and Keijzer",
        "Dear ministers van Engels hoven and Kaiser",
        "And all participants",
        "I am happy to see you",
        "And I am grateful that I may welcome you to the High Level Lunch",
        "I wish that you will enjoy your lunch and have a fruitful discussion",
        "Please follow our hosts",
        "They are to my right",
        "I hope to see you soon again in beautiful Brain port",
        # "I hope to see you soon again in beautiful Brainport",
        "Thank you and bon appetit!"]

rospy.init_node("speech_demonstration")
robot = get_robot("hero")
current_sentence = 0

while not rospy.is_shutdown():
    print("next sentence:")
    print(Text[current_sentence])

    cmd = input("provide input\n")
    cmd = str(cmd)
    print("you entered: {}".format(cmd))
    if cmd == 'a':
        current_sentence = current_sentence - 1
    elif cmd == 's':
        robot.speech.speak(Text[current_sentence])
        current_sentence = current_sentence + 1
    elif cmd == 'd':
        current_sentence = current_sentence + 1
    else:
        print("invalid command")

    current_sentence = max(min(current_sentence, len(Text)-1), 0)


