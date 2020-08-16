import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk
import random

# A dictionary of number 1-32 for the key and the values are a second dictionary for team information: name and logo.
nfl_teams = {
    1: {'Name': 'Arizona Cardinals', 'Logo': 'arizona-cardinals-logo.png'},
    2: {'Name': 'Chicago Bears', 'Logo': 'chicago-bears-logo-vector.png'},
    3: {'Name': 'Green Bay Packers', 'Logo': 'green-bay-packers-logo-vector.png'},
    4: {'Name': 'New York Giants', 'Logo': 'new-york-giants-logo-vector.png'},
    5: {'Name': 'Detroit Lions', 'Logo': 'detroit-lions-logo-vector-01.png'},
    6: {'Name': 'Washington Football Team', 'Logo': 'washington-football-team.png'},
    7: {'Name': 'Philadelphia Eagles', 'Logo': 'philadelphia-eagles-logo.png'},
    8: {'Name': 'Pittsburgh Steelers', 'Logo': 'pittsburgh-steelers-logo-vector-01.png'},
    9: {'Name': 'Los Angeles Rams', 'Logo': 'st-louis-rams-vector-logo.png'},
    10: {'Name': 'San Francisco 49ers', 'Logo': 'san-francisco-49ers-logo-vector.png'},
    11: {'Name': 'Cleveland Browns', 'Logo': 'cleveland-browns-logo.png'},
    12: {'Name': 'Indianapolis Colts', 'Logo': 'indianapolis-colts-logo.png'},
    13: {'Name': 'Dallas Cowboys', 'Logo': 'dallas-cowboys-logo-vector.png'},
    14: {'Name': 'Kansas City Chiefs', 'Logo': 'kansas-city-chiefs-logo.png'},
    15: {'Name': 'Los Angeles Chargers', 'Logo': 'san-diego-chargers-logo-vector.png'},
    16: {'Name': 'Denver Broncos', 'Logo': 'denver-broncos-logo-vector.png'},
    17: {'Name': 'New York Jets', 'Logo': 'new-york-jets-logo-vector-01.png'},
    18: {'Name': 'New England Patriots', 'Logo': 'new-england-patriots-logo-preview.png'},
    19: {'Name': 'Las Vegas Raiders', 'Logo': 'las-vegas-raiders-logo-vector.png'},
    20: {'Name': 'Tennessee Titans', 'Logo': 'tennessee-titans-logo.png'},
    21: {'Name': 'Buffalo Bills', 'Logo': 'buffalo-bills-logo-vector-01.png'},
    22: {'Name': 'Minnesota Vikings', 'Logo': 'minnesota-vikings-logo-vector.png'},
    23: {'Name': 'Atlanta Falcons', 'Logo': 'atlanta-falcons-logo-vector.png'},
    24: {'Name': 'Miami Dolphins', 'Logo': 'miami-dolphins-vector-logo.png'},
    25: {'Name': 'New Orleans Saints', 'Logo': 'new-orleans-saints-logo-vector.png'},
    26: {'Name': 'Cincinnati Bengals', 'Logo': 'cincinnati-bengals-tiger-logo.png'},
    27: {'Name': 'Seattle Seahawks', 'Logo': 'seattle-seahawks-logo-vector.png'},
    28: {'Name': 'Tampa Bay Buccaneers', 'Logo': 'tampa-bay-buccaneers-logo-vector.png'},
    29: {'Name': 'Carolina Panthers', 'Logo': 'carolina-panthers-logo-vector.png'},
    30: {'Name': 'Jacksonville Jaguars', 'Logo': 'jacksonville-jaguars-logo.png'},
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
    width = 325
    height = 325
    # load the image and display it
    img = Image.open(img)
    img = img.resize((width, height), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    team_logo.img = img  # keep a reference so it's not garbage collected
    team_logo['image'] = img


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
win.geometry('480x480')  # set window size
win.resizable(0, 0)  # fix window
f1 = tk.Frame(win, bg="white", height=350, width=350)
f1.pack(pady=25)
team_logo = tk.Label(f1)
team_logo.lift()
team_logo.pack()


# Button for the user to start/continue the program
btn = tk.Button(text='Click to Begin!', padx=5, pady=5, command=next_img)
# Label to describe the user what to do and result
tnl = tk.Label(
    win, text="Let's find out which NFL Team you are a fan of!", font="helv36")
tnl.pack()
btn.pack(pady=25)

# show the first image
start_img()

# App Title
win.title("NFL Fan Generator")
# App Favicon
win.wm_iconbitmap("team_logo_images\\favicon.ico")
win.mainloop()
