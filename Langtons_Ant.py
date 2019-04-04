import tkinter as tk
import time

WIDTH = 120
HEIGHT = 120
CELL_SIZE = 5
STEPS = 15000
WIN_SIZE = str((WIDTH + 2) * CELL_SIZE) + "x" + str(int(HEIGHT * CELL_SIZE * 1.3))
# for direction, 0, 1, 2, 3 represents up, right, down and left respectively
def init():
  window = tk.Tk()
  window.title("Ant Simulator")
  window.geometry(WIN_SIZE)
  return window

def main():
  wd = init()
  
  # draw canvas
  cv = tk.Canvas(wd, bg = 'white', height = WIDTH * CELL_SIZE + 1, width = HEIGHT * CELL_SIZE + 1)
  cv.pack()
  # draw cells
  cells = [([0]*WIDTH) for i in range(HEIGHT)]
  val = [([0]*WIDTH) for i in range(HEIGHT)]
  for i in range(WIDTH*HEIGHT):
    wid = i%WIDTH
    hi = i//WIDTH
    cells[hi][wid] = cv.create_rectangle(wid*CELL_SIZE+2, hi*CELL_SIZE+2, wid*CELL_SIZE+CELL_SIZE+2, hi*CELL_SIZE+CELL_SIZE+2)

  # initial
  loc = [int(WIDTH / 2), int(HEIGHT / 2)]
  di = 0
  for i in range(STEPS):
    if (val[loc[0]][loc[1]] == 1):
      val[loc[0]][loc[1]] = 0
      cv.itemconfig(cells[loc[0]][loc[1]], fill='white')
      di  = (di - 1) % 4
    else:
      val[loc[0]][loc[1]] = 1
      cv.itemconfig(cells[loc[0]][loc[1]], fill='black')
      di  = (di + 1) % 4
    if (di == 0):
      if (loc[1] > 0):
        loc[1] -= 1
    elif (di == 1):
      if (loc[0] < WIDTH - 1):
        loc[0] += 1
    elif (di == 2):
      if (loc[1] < HEIGHT - 1):
        loc[1] += 1
    elif (di == 3):
      if (loc[0] > 0):
        loc[0] -= 1
    cv.update()
main()
