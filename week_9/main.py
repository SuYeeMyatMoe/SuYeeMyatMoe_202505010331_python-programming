from display import display_ticket
from ticket import create_ticket


def main():
    # Call create_ticket and store returned dictionary
    ticket_data = create_ticket()

    # Conditional statement to ensure ticket was created successfully
    if ticket_data:
        # Call display function from display.py
        display_ticket(ticket_data)


if __name__ == "__main__":
    main()