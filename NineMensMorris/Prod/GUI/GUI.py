import sys
sys.path.append('NineMensMorris/Prod/NineMenMorrisInterface')  
import tkinter as tk
from tkinter import messagebox
from PieceLogic import Locations  


class NineMansMorrisGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Nine Mans Morris')
        self.geometry('600x600')
        self.locations = Locations()
        self.buttons = {}
        for i in range(24):
            row = i // 4
            col = i % 4
            self.buttons[i] = tk.Button(self, text=' ', width=10, height=3, command=lambda i=i: self.click(i))
            self.buttons[i].grid(row=row, column=col)

    def click(self, position):
        temp = self.locations.current_player
        if self.locations.place_piece(position):
            self.buttons[position].config(text=str(temp))
            print(f"Piece placed by {temp} at position {position}")
        else:
            print("Invalid move. Try again.")
            messagebox.showinfo('Invalid', 'Invalid move. Try again.')


if __name__ == '__main__':
    app = NineMansMorrisGUI()
    app.mainloop()

