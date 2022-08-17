import automation


def title():
    heading = "*      AUTOMATION      *"
    print(' * ' * int(len(heading) / 3))
    print(heading)
    print(' * ' * int(len(heading) / 3))
    print('')


if __name__ == '__main__':
    title()
    automation.new_automation()
    automation.dashboard()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
