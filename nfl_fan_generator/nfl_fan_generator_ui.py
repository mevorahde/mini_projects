from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import random

global logo
nfl_teams = {
    1: {'Name': 'Arizona Cardinals', 'Logo':'Arizona-Cardinals-logo-vector.jpg'},
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
    13: {'Name': 'Dallas Cowboys', 'Logo':  'dallas-cowboys-logo-vector.png'},
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


def show_image():
    global logo
    user_num = random.randint(1, 32)
    # print(user_num)
    # print(nfl_teams[user_num])
    for n, team_info in nfl_teams.items():
        if n == user_num:
            print("You are a fan of the: {}!".format(team_info['Name']))
            logo = "team_logo_images\\{}".format(team_info['Logo'])
        lbl1.configure(image=image_tk)


root = Tk()
c = ttk.Frame(root, padding=(5, 5, 12, 0))
c.grid(column=0, row=0, sticky=(N, W, E, S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
fname = "team_logo_images\\san-francisco-49ers-logo-vector.png"
# fname = logo
image_tk = ImageTk.PhotoImage(Image.open(fname))
btn = ttk.Button(c, text="Click Here To Begin!", command=show_image)
lbl1 = ttk.Label(c)
btn.grid(column=0, row=0, sticky=N, pady=5, padx=5)
lbl1.grid(column=1, row=1, sticky=N, pady=5, padx=5)
root.mainloop()
