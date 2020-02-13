import tkinter as tk
from tkinter.font import Font
from PIL import ImageTk, Image
import random

# A dictionary of number 1-32 for the key and the values are a second dictionary for team information: name and logo.
nfl_teams = {
    1: {'Name': 'Arizona Cardinals', 'Logo': 'Arizona-Cardinals-logo-vector.jpg'},
    2: {'Name': 'Chicago Bears', 'Logo': 'chicago-bears-logo-vector.png'},
    3: {'Name': 'Green Bay Packers', 'Logo': 'green-bay-packers-logo-vector.png'},
    4: {'Name': 'New York Giants', 'Logo': 'new-york-giants-logo-vector.png'},
    5: {'Name': 'Detroit Lions', 'Logo': 'detroit-lions-logo-vector-01.png'},
    6: {'Name': 'Washington Redskins', 'Logo': 'washington-redskins-logo-vector.png'},
    7: {'Name': 'Philadelphia Eagles', 'Logo': 'philadelphia-eagles-logo.png'},
    8: {'Name': 'Pittsburgh Steelers', 'Logo': 'pittsburgh-steelers-logo-vector-01.png'},
    9: {'Name': 'Los Angeles Rams', 'Logo': 'st-louis-rams-vector-logo.png'},
    10: {'Name': 'San Francisco 49ers', 'Logo': 'san-francisco-49ers-logo-vector.png'},
    11: {'Name': 'Cleveland Browns', 'Logo': 'cleveland-browns-logo-vector-download.jpg'},
    12: {'Name': 'Indianapolis Colts', 'Logo': 'indianapolis-colts-logo-vector-download.jpg'},
    13: {'Name': 'Dallas Cowboys', 'Logo': 'dallas-cowboys-logo-vector.png'},
    14: {'Name': 'Kansas City Chiefs', 'Logo': 'kansas-city-chiefs-logo-vector-download.jpg'},
    15: {'Name': 'Los Angeles Chargers', 'Logo': 'san-diego-chargers-logo-vector.png'},
    16: {'Name': 'Denver Broncos', 'Logo': 'denver-broncos-logo-vector.png'},
    17: {'Name': 'New York Jets', 'Logo': 'new-york-jets-logo-vector-01.png'},
    18: {'Name': 'New England Patriots', 'Logo': 'new-england-patriots-logo-preview.png'},
    19: {'Name': 'Oakland Raiders', 'Logo': 'oakland-raiders-logo-vector.png'},
    20: {'Name': 'Tennessee Titans', 'Logo': 'tennessee-titans-logo-vector-download.jpg'},
    21: {'Name': 'Buffalo Bills', 'Logo': 'buffalo-bills-logo-vector-01.png'},
    22: {'Name': 'Minnesota Vikings', 'Logo': 'minnesota-vikings-logo-vector.png'},
    23: {'Name': 'Atlanta Falcons', 'Logo': 'atlanta-falcons-logo-vector.png'},
    24: {'Name': 'Miami Dolphins', 'Logo': 'miami-dolphins-vector-logo.png'},
    25: {'Name': 'New Orleans Saints', 'Logo': 'new-orleans-saints-logo-vector.png'},
    26: {'Name': 'Cincinnati Bengals', 'Logo': 'cincinnati-bengals-logo-vector-01.png'},
    27: {'Name': 'Seattle Seahawks', 'Logo': 'seattle-seahawks-logo-vector.png'},
    28: {'Name': 'Tampa Bay Buccaneers', 'Logo': 'tampa-bay-buccaneers-logo-vector.png'},
    29: {'Name': 'Carolina Panthers', 'Logo': 'carolina-panthers-logo-vector.png'},
    30: {'Name': 'Jacksonville Jaguars', 'Logo': 'jacksonville-jaguars-logo-vector-download.jpg'},
    31: {'Name': 'Baltimore Ravens', 'Logo': 'baltimore-ravens-logo-vector-01.png'},
    32: {'Name': 'Houston Texans', 'Logo': 'houston-texans-logo-vector.png'}
}


def team():
    # Set global variable for team name and the program label slot
    global team_name
    global tnl
    # create a list
    images = []
    # Get a Random number from 1 to 32
    user_num = random.randint(1, 32)

    # Get all data from the 'nfl_teams' dictionary
    for number, team_info in nfl_teams.items():
        # Match the random, user number with the number from the 'nfl_teams' dictionary
        if number == user_num:
            # Get the Team Name and Logo information that goes with the matched number
            team_name = "You are a fan of the: {}!".format(team_info['Name'])
            logo = "team_logo_images\\{}".format(team_info['Logo'])
            # Append the logo to the list
            images.append(logo)
    return images


def load_image(img):
    # load the image and display it
    img = Image.open(img)
    img = ImageTk.PhotoImage(img)
    panel.img = img  # keep a reference so it's not garbage collected
    panel['image'] = img


def start_img():
    # Starting function for the app, show the NFL logo, instructions for the user in a label and a button to click to
    # start the goal of the program
    img = "team_logo_images\\nfl-logo-National-Football-League.png"
    load_image(img)


def next_img():
    a = team()
    # Show the user what team they are a 'fan' of
    tnl.config(text=team_name)
    # Change the button text to ask if the user wants to play again
    btn.config(text="Play Again?!")
    images = iter(a)  # make an iterator
    img = next(images)  # get the next image from the iterator
    team()
    # Show the Team Logo image
    load_image(img)


win = tk.Tk()
win.geometry('1000x1000')  # set window size
win.resizable(0, 0)  # fix window
panel = tk.Label(win)
panel.pack()
# Main Font
helv36 = Font(family='Helvetica', size=42, weight='bold')
# Button for the user to start/continue the program
btn = tk.Button(text='Click to Begin!', font="helv36", padx=5, pady=5, command=next_img)
# Label to describe the user what to do and result
tnl = tk.Label(win, text="Let's find out which NFL Team your a fan of!", font="helv36")
tnl.pack()
btn.pack(pady=25)

# show the first image
start_img()

# App Title
win.title("NFL Fan Generator")
# App Favicon
win.wm_iconbitmap("team_logo_images\\favicon.ico")
win.mainloop()
