from functions import evaluator


# Command Line Interface for TweetEvaluator

def cli():
    """Generates menu for CLI"""
    
    print("***TweetEvaluator***\n")

    username = input("Enter Twitter User: ")
    amount = int(input("Enter amount of tweets (1-3200): "))
    max_display = int(input("Enter number of results to display: "))

    print("\n***\n")

    print(evaluator(username, amount, max_display))


def main():
    """Main loop for CLI"""
    
    menu_flag = True

    while menu_flag == True:

        cli()

        repeat_flag = True

        while repeat_flag == True:

            repeat = input("\nEvaluate another user? [y/n]: ").lower()

            if repeat == "n":
                print("Goodbye.")
                repeat_flag = False
                menu_flag = False
                break
            elif repeat == "y":
                print("\n")
                repeat_flag = False
                continue
            else:
                print("Invalid command.")
                continue


if __name__ == "__main__":
    main()
