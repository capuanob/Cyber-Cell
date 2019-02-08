

class UI():

    def print_menu(self):
        print(
            "Welcome to Cyber Cell! Would you like to view instructions on how to play? [Y/N]")
        if self.validate_input():
            self.print_instructions()

    def validate_input(self):
        response = input("Enter your choice: ")
        while response != 'Y' and response != 'N':
            print("Incorrect input, please try again.")
            response = input("Enter your choice: ")
        return True if response == 'Y' else False

    def print_instructions(self):
        print("""
        You play as the warden of your own virtual prison and are tasked with maintaining the security of
        your grounds and the safety of those within your walls.

        HOW TO PLAY:
        At the end of each round, you are granted investment points (IP) which can be used to 
        \t1) Hire an additional guard
        \t2) Install a security camera
        \t3) Increase prisoner morale

        Your choices have consequences and will impact the moods and motives of your prisoners and guards.
        If you perform poorly and allow prisoners to escape, you will LOSE. 
        In order to WIN, you must achieve >90% prisoner morale or maintain your prison for a month.

        TIP:
        Listen to the gossip around the prison, it just may help you prevent a prison break!

        With that, best of luck warden, your prison awaits!
        """)
