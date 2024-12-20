from property.cli import cli
if __name__ == '__main__':
    cli()
def main():
    """Main loop to run the CLI interactively."""
    while True:
        try:
            cli()  # Call the CLI function
            user_input = input("Do you want to run again? (yes/no): ").strip().lower()
            if user_input not in ['yes', 'y']:
                print("Exiting the program. Goodbye!")
                break
        except KeyboardInterrupt:
            print("\nProgram interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            continue    
    