import tkinter as tk
import webbrowser


gui = tk.Tk()

# Color variables that is used for the gui using HEX code
BaseColor = '#6B9393'

# Create screen
gui.title("Sigma Gamer")
gui.geometry("600x600")
# background of the window
gui['background'] = BaseColor

# Force fullscreen
#width = gui.winfo_screenwidth()
#height = gui.winfo_screenheight()
#gui.geometry("%dx%d" % (width, height))
#gui.title("Sigma gamer")

#Uncomment if i want a label
#label1 = tk.Label(gui, text="TEST")
#label2 = tk.Label(gui, text="TEST")
# Positioning of the labels in the window
#label1.grid(row = 0, column = 2) # if i specify grid, i don't need label.pack()
#label2.grid(row = 1, column = 0)
# Set background for specific labels
#label1['background'] = BaseColor
#label2['background'] = BaseColor
#label.pack() ## is needet to initilize the labels if grid is not specifed

#### CREATE SEARCH BAR ######
# label
labelSearchBar = tk.Label(gui, text = "Search bar :", padx = 3, pady = 5)
labelSearchBar.grid(row = 0, column = 0)
#entry, where i can write
entry=tk.Entry(gui, width=20, font = 10)
entry.grid(row = 0, column = 1)
# Button to click
button = tk.Button(gui, text = 'Search', padx = 5, pady = 3)
button.grid(row = 0, column = 2, columnspan = 10, pady = 10)

#TODO Take input from entry
#TODO Click button then presing enter, or the button
#TODO Create frame so i can move the search to the bottom
#TODO Create a scroll down window where all the information is shown

#TODO create an insert data popup window with checkboxes etc


gui.mainloop()
