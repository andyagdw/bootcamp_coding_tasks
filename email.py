"""An email simulator using OOP

This program allows the user (who is the receiver of these emails)
to create new emails which they can view and perform actions on (e.g.,
mark as read, mark as unread, put in the spam folder,
and delete an email etc...)
"""

class Email:
    """A class to represent an email"""

    location = "United Kingdom"

    def __init__(self,
                email_address,
                subject_line,
                email_content,
                ):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False
        self.is_spam = False
        self.is_in_bin = False

    def mark_as_read(self, value):
        """
        Takes in a boolean value and marks email as read or not read
        """
        self.has_been_read = value

    def set_spam_value(self, value):
        """
        Takes in a boolean value and marks email as spam or not spam
        """
        self.is_spam = value

    def set_bin_value(self, value):
        """
        Takes in a boolean value and puts the email in the bin folder
        or removes it from the bin
        """
        self.is_in_bin = value

    def __str__(self):
        return (f"Email address:\t{self.email_address}"
                f"\nSubject line:\t{self.subject_line}"
                f"\nEmail content:\t{self.email_content}")


inbox = []  # All emails created will be put in here
NUM_OF_SAMPLE_EMAILS = 1  # Change to generate more sample emails
EMAIL_NOT_FOUND = "\nThis email does not exist"
ERROR_RESPONSE = "\nOops - incorrect input. Please try again."


# MAIN FUNCTIONS
def populate_inbox():
    """Creates x number of email objects and returns the inbox"""

    for _ in range(NUM_OF_SAMPLE_EMAILS):
        email_address = input("What is the sender's email address: ")
        subject_line = input("What is the subject line: ")
        email_content = input("What is the email content: ")
        print("")

        inbox.append(Email(email_address, subject_line, email_content))

    return inbox


def list_emails(folder=None):
    """
    Takes in a folder (if no folder is given, the default folder
    will be the inbox) and lists the subject line of all emails
    in the selected folder. It then returns the inbox
    """

    if folder is None:
        folder = inbox
    for index, email in enumerate(folder):
        print(f"-------------{index} {email.subject_line}-------------")

    print(f"\nYou have {len(folder)} email(s) in this folder\n")


def set_email_state(index, user_choice):
    """
    Takes in an index (the email the user wants to perform an
    action on) as well as their choice (what action they want to
    perform on an email)
        
    The function then checks the state of an email
    (e.g., whether it is read, in the bin folder, or spam folder)
    and changes its state (e.g., removes it from spam if it is in
    the spam folder). It then returns the inbox
    """

    email = inbox[index]  # Store email in variable

    print(f"\n{email}")

    match user_choice:
        case 1:
            if email.has_been_read:
                email.mark_as_read(False)
                print("\n\tEmail has been removed from read\n")
            else:
                email.mark_as_read(True)
                print("\n\tEmail has been marked as read\n")

        case 2:
            if email.is_spam:
                email.set_spam_value(False)
                print("\n\tEmail has been removed from spam\n")
            else:
                email.set_spam_value(True)
                print("\n\tEmail has been added to spam\n")

        case 3:
            if email.is_in_bin:
                email.set_bin_value(False)
                print("\n\tEmail has been removed from bin\n")
            else:
                email.set_bin_value(True)
                print("\n\tEmail has been added to bin\n")

    return inbox


def delete_email(index):
    """
    Takes in an index (an email the user wants to perform this
    action on) and removes the email from the inbox. It then
    returns the inbox
    """

    # Check if email index is valid
    if index < 0 or index >= len(inbox):
        print(EMAIL_NOT_FOUND)
        return None

    print(f"\n\n****************\n{inbox[index]}\n\n****************\n")

    confirmation_choice = input("""Are you sure you want to delete this email?
                                'Yes' or 'No': """)

    if confirmation_choice == "Yes":
        inbox.pop(index)
        print("\nEmail has been successfully deleted\n")
        return inbox

    print("Operation cancelled")

    return inbox


# CALLER FUNCTIONS
# The numbers relate to the email options in the driver function
# 2
def manage_user_choice_case_2(folder_question):
    """
    Takes in the folder question from the driver function and
    checks if the user has entered in valid inputs for option 2 
    (see driver function). It then returns the 'set_email_state'
    function where the user can perform actions on a selected
    email
    """

    try:
        user_choice = int(input(
            """\nWould you like to:\n
                    1. Read or mark an email as unread
                    2. Mark an email as spam or remove from spam folder
                    3. Move email to bin or remove from bin folder
                    \nEnter selection: """))

    except ValueError:  # Catch user input if it is not an integer
        print(ERROR_RESPONSE)
        return None

    # Check if user choice matches options
    if user_choice not in {1,2,3}:
        print(ERROR_RESPONSE)
        return None

    try:
        index = int(input(folder_question))
    except ValueError:
        print(ERROR_RESPONSE)
        return None

    # Check if email index is valid
    if index < 0 or index >= len(inbox):
        print(EMAIL_NOT_FOUND)
        return None

    return set_email_state(index, user_choice)

# 3
def filter_emails(user_choice):
    """
    Takes in the user's choice (what the user would like to do) and
    filters emails using list comprehension
    """

    # User choice represents the action they want to perform
    match user_choice:
        case 1:
            print("\n\nUNREAD\n\n")
            unread_emails = [x for x in inbox if x.has_been_read is False]
            list_emails(unread_emails)
        case 2:
            print("\n\nSPAM\n\n")
            spam_emails = [x for x in inbox if x.is_spam is True]
            list_emails(spam_emails)
        case 3:
            print("\n\nBIN\n\n")
            emails_in_bin = [x for x in inbox if x.is_in_bin is True]
            list_emails(emails_in_bin)
        case _:
            print(ERROR_RESPONSE)


# Driver Function
def select_email_option():
    """
    Allows a user to perform actions on inbox list.
    Python switch syntax is used to match email options.
    Error handling is also used for incorrect inputs
    """

    folder_question = "\nWhich email would you like to add to this folder or "\
                        "remove (hint: This takes in an integer where "\
                        "the first email in this folder is considered as 0)"\
                        "\n\nEnter selection: "

    try:
        user_choice = int(input(
    """\nWould you like to:\n
            1. View all emails
            2. Manage emails (e.g., Read an email, Mark as spam, Move to bin)
            3. View a folder (e.g., View spam, View unread, View emails in bin)
            4. Delete an email (Note: Emails cannot be retrieved once deleted)
            5. Quit application
            
            Enter selection: """))

    # If user choice is not an integer call function again
    except ValueError:
        print(ERROR_RESPONSE)
        return select_email_option()

    # Takes user input and matches it to selected option/case
    match user_choice:
        case 1:  # View all emails
            print("\n\nALL\n\n")
            list_emails()

        case 2:  # Manage emails
            manage_user_choice_case_2(folder_question)

        case 3:  # View a folder
            try:
                user_choice = int(input(
                    """\nWould you like to:\n
                    1. View unread emails
                    2. View spam emails
                    3. View emails in bin
                    
                    Enter selection: """))
            except ValueError:
                print(ERROR_RESPONSE)
                return select_email_option()

            filter_emails(user_choice)

        case 4:  # Delete an email
            try:
                delete_email_choice = int(input(
                    "\nWhich email do you want to delete: "\
                    "(hint: This takes in an integer where "\
                    "the first email is considered as 0)"\
                    "\n\nEnter selection: "))
            except ValueError:
                print(ERROR_RESPONSE)
                return select_email_option()

            delete_email(delete_email_choice)

        case 5:  # Quit application
            print("\nHave a nice day👍")
            return None

        case _:  # Default - if user choice doesn't match any above case
            print(ERROR_RESPONSE)

    return select_email_option()


if __name__ == "__main__":

    populate_inbox()
    my_name = input("What is your first name: ")
    print(f"\nHello {my_name}👋\n")
    select_email_option()
