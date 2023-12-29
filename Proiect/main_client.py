# from client.client import main
from client.gui import start_application

def main():
    """
    This is the main entry point for the application.
    It starts the application by calling the start_application function from the gui module.
    """
    start_application()


if __name__ == '__main__':
    """
    This condition checks if this script is the main module being run.
    If it is, it calls the main function to start the application.
    """
    main()
