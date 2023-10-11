import sys
sys.path.append('NineMensMorris/Prod/NineMenMorrisInterface')  
import tkinter as tk
from tkinter import messagebox
from PieceLogic import Locations  

class NineMansMorrisGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Nine Mans Morris')
        self.geometry('900x600')
        self.locations = Locations()  
        self.buttons = {}
        
        validLoc = [(0,0), (0,3), (0,6),
                    (1,1), (1,3), (1,5),
                    (2,2), (2,3), (2,4),
                    (3,0), (3,1), (3,2), (3,4), (3,5), (3,6),
                    (4,2), (4,3), (4,4),
                    (5,1), (5,3), (5,5),
                    (6,0), (6,3), (6,6)]

        for row in range(7):
            for col in range(7):
                if (row, col) in validLoc:
                    index = validLoc.index((row, col))
                    self.buttons[index] = tk.Button(self, text=' ', width=10, height=3, command=lambda index=index: self.click(index))
                    self.buttons[index].grid(row=row, column=col)
                else:
                    tk.Label(self, text=' ', width=10, height=3).grid(row=row, column=col)


    def click(self, position):
        tempPlayer = self.locations.current_player
        if self.locations.place_piece(position):
            self.buttons[position].config(text=str(tempPlayer))
            print(f"Piece placed by {self.locations.current_player} at position {position}")
        else:
            print("Invalid move. Try again.")
            messagebox.showinfo('Invalid', 'Invalid move. Try again.')


if __name__ == '__main__':
    app = NineMansMorrisGUI()
    app.mainloop()

