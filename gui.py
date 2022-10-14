from tkinter import *
from tkinter.font import BOLD
from tkinter.ttk import *
from functions import evaluator

def main_window():
    """Creates the main window."""
    def submit():
        """Provides submit button functionality."""
        username = username_var.get()
        amount = amount_var.get()
        display = display_var.get()

        username_var.set("")
        amount_var.set(0)
        display_var.set(0)

        results_window(username, amount, display)

    def results_window(user_name, tweet_amount, max_display):
        """Opens new window and displays results.

        Args:
            user_name (str): Twitter username
            tweet_amount (int): Amount of tweets to analyse (max: 3200)
            max_display (int): Amount of counted words to display. 
        """
        
        tweet_words = evaluator(user_name, tweet_amount, max_display)

        results_wndw = Toplevel(window)
        results_wndw.title("Tweet Results")
        results_wndw.geometry("330x500")
        lbl_res = Label(results_wndw, text=f"{user_name}'s Top Tweeted Words")
        lbl_res.config(font=("courier", 12))
        
        msg_res = Text(results_wndw, height=50, width=40)
        msg_res.insert(1.0, tweet_words)

        print(tweet_words)

        lbl_res.pack(pady=10)
        msg_res.pack(pady=15)

    # Set up main window
    window = Tk()
    window.wm_title("Tweet Evaluator")
    window.geometry("300x115")

    # Declare variables for storing username, amount, and display
    username_var = StringVar()
    amount_var = IntVar()
    display_var = IntVar()

    # Create labels, entries, and buttons for collecting input
    lbl_username = Label(window, text="Username:")
    ent_username = Entry(window, textvariable=username_var)

    lbl_amount = Label(window, text="Tweets (1-3200):")
    ent_amount = Entry(window, textvariable=amount_var)

    lbl_display = Label(window, text="Max Results:")
    ent_display = Entry(window, textvariable=display_var)

    btn_submit = Button(window, text="Submit", command=submit)
    btn_exit = Button(window, text="Exit", command=window.destroy)

    # Place labels, entries, and buttons using grid
    lbl_username.grid(row=0, column=0)
    ent_username.grid(row=0, column=1)
    lbl_amount.grid(row=1, column=0)
    ent_amount.grid(row=1, column=1)
    lbl_display.grid(row=2, column=0)
    ent_display.grid(row=2, column=1)
    btn_submit.grid(row=3,column=0, pady=10)
    btn_exit.grid(row=3, column=1, pady=10)

    # Initiate loop to display window
    window.mainloop()

if __name__ == "__main__":
    main_window()