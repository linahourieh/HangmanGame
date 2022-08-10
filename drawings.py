import sys
import time
from OptionScreen import color

stickman_8 =color.BLUE + color.BOLD+ "\
                                        |------\n\
                                        |   ( )\n\
                                        |  --|--\n\
                                        |   / \\ \n\
                                        |  /   \\ \n\
                                        |_____" + color.END

stickman_7 = "\
                                        |------\n\
                                        |   ( )\n\
                                        |  --|--\n\
                                        |   / \\ \n\
                                        |  /      \n\
                                        |_____"

stickman_6 = "\
                                        |------\n\
                                        |   ( )\n\
                                        |  --|--\n\
                                        |   / \\ \n\
                                        |         \n\
                                        |_____"

stickman_5 = "\
                                        |------\n\
                                        |   ( )\n\
                                        |  --|-\n\
                                        |   / \\ \n\
                                        |         \n\
                                        |_____"

stickman_4 = "\
                                        |------\n\
                                        |   ( )\n\
                                        |   -|-\n\
                                        |   / \\ \n\
                                        |         \n\
                                        |_____"

stickman_3 = "\
                                        |------\n\
                                        |   ( )\n\
                                        |   -|-\n\
                                        |     \\ \n\
                                        |         \n\
                                        |_____"

stickman_2 = "\
                                        |------\n\
                                        |   ( )\n\
                                        |   -| \n\
                                        |     \\ \n\
                                        |         \n\
                                        |_____"

stickman_1 = "\
                                        |------\n\
                                        |   ( )\n\
                                        |   -| \n\
                                        |        \n\
                                        |         \n\
                                        |_____"

stickman_0 = "\
                                        |------\n\
                                        |   ( )\n\
                                        |    | \n\
                                        |        \n\
                                        |         \n\
                                        |_____"

stickman_list = [stickman_0, stickman_1, stickman_2, stickman_3, stickman_4, stickman_5, stickman_6, stickman_7,
                 stickman_8]


def draw_hangman(i):
    drawing = stickman_list[i]
    print(color.BLUE+color.BOLD+drawing+ color.END)



draw_hangman(8)
