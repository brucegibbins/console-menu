import sys

from consolemenu import *
from consolemenu.format import *
from consolemenu.items import *


import yaml


def helloworld():
    print("HelloWorld")
    PromptUtils(Screen()).enter_to_continue()


def main():
    menudef = """\
    main:
        title: Root Menu
        subtitle: This is the Root Menu Subtitle
        items:
            - text: Menu Item 1
              class: MenuItem
              
            - text: Call Class Function
              class: ClassFunctionItem
              action: consolemenu.screen.Screen.input 
              args: ["Please enter input here: "]

            - text: Call Module Function
              class: ModuleFunctionItem
              action: examples.example7.helloworld 
              args:

            - text: Command
              class: CommandItem
              action: 'cmd /c \"echo this is a shell. Press enter to continue." && set /p=\"'
              
              
    """

    menu = ConsoleMenu("Root Menu", "This is the Root Menu Subtitle", menudef=yaml.safe_load(menudef))
    menu.show()


if __name__ == "__main__":
    main()
