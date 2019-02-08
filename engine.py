from prison import Prison
from user_interface import UI

prison = Prison()
UI = UI()
UI.print_menu()


# TO-DO NEXT
"""
Implement actual game (days actually running)
    -Somehow add people to the room they should be in at that hour
        -Remove them at end of hour
    -Implement gossip system
    -Gaining and spending
    -Update morale / skill
    -Attempt escapes
        -Send to solitary for some amount of days?
    -Check win condition

"""
