import tkinter as tk
import time
import copy
import gc

WIDTH = 60
HEIGHT = 60
CELL_SIZE = 20
STEPS = 1000
WIN_SIZE = str((WIDTH + 2) * CELL_SIZE) + "x" + str(int(HEIGHT * CELL_SIZE * 1.3))
FPS = 60
# for direction, 0, 1, 2, 3 represents up, right, down and left respectively

def init():
  window = tk.Tk()
  window.title("Game of Life")
  window.geometry(WIN_SIZE)
  return window

'''
def on_click(val, hi, wid):
  if (val[hi][wid] == 0):
    val[hi][wid] = 1
  elif (val[hi][wid] == 1):
    val[hi][wid] = 0
  print(hi, wid)
'''

class NumBut(tk.Button):

  def __init__(self, hi, wid, **k):
    tk.Button.__init__(self, **k)
    self.hi = hi
    self.wid = wid

  def on_click(self):
    if (val[self.hi][self.wid] == 0):
      val[self.hi][self.wid] = 1
      but[self.hi][self.wid].config(bitmap='gray75')
    elif (val[self.hi][self.wid] == 1):
      val[self.hi][self.wid] = 0
      but[self.hi][self.wid].config(bitmap='gray12')
    
    

def main():

  select = init()
  global val, but
  val = [([0]*WIDTH) for i in range(HEIGHT)]
  but = copy.deepcopy(val)
  for i in range(WIDTH*HEIGHT):
    wid = i%WIDTH
    hi = i//WIDTH
    but[hi][wid] = NumBut(hi, wid, bitmap = 'gray12', width = CELL_SIZE, height = CELL_SIZE)
    but[hi][wid].place(x= (wid + 1)*CELL_SIZE, y = hi*CELL_SIZE)
    but[hi][wid].config(command = but[hi][wid].on_click)
  select.mainloop()

  wd = init()
  
  # draw canvas
  cv = tk.Canvas(wd, bg = 'white', height = WIDTH * CELL_SIZE + 1, width = HEIGHT * CELL_SIZE + 1)
  cv.pack()
  # draw cells
  cells = [([0]*WIDTH) for i in range(HEIGHT)]

  # set initial stat here
  # val[1][0] = val[1][1] = val[2][0] = val[2][1] = 1
  # val[16][11] = val[16][13] = val[15][13] = val[14][15] = val[13][15] = val[12][15] = val[13][17] = val[12][17] = val[11][17] = val[12][18] = 1
  # val[2][1] = val[3][1] = val[4][2] = val[1][3] = val[2][4] = val[3][4] = 1
  # val[1][0] = val[2][1]=val[0][2]=val[1][2]=val[2][2] = 1
  
  for i in range(WIDTH*HEIGHT):
    wid = i%WIDTH
    hi = i//WIDTH
    cells[hi][wid] = cv.create_rectangle(wid*CELL_SIZE+2, hi*CELL_SIZE+2, wid*CELL_SIZE+CELL_SIZE+2, hi*CELL_SIZE+CELL_SIZE+2)

  for i in range(WIDTH*HEIGHT):
    wid = i%WIDTH
    hi = i//WIDTH
    if (val[hi][wid] == 1):
      cv.itemconfig(cells[hi][wid], fill='black')
  cv.update()

  # time.sleep(1)
  for i in range(STEPS):
    t0= time.time()
    new = copy.deepcopy(val)
    for j in range(WIDTH*HEIGHT):
      wid = j%WIDTH
      hi = j//WIDTH
      neigh = 0
      # top-left corner
      if (wid == 0 and hi == 0):
        if (val[hi][wid+1] == 1):
          neigh += 1
        if (val[hi+1][wid] == 1):
          neigh += 1
        if (val[hi+1][wid+1] == 1):
          neigh += 1
      # bottom-left corner
      elif (wid == 0 and hi == HEIGHT - 1):
        if (val[hi][wid+1] == 1):
          neigh += 1
        if (val[hi-1][wid] == 1):
          neigh += 1
        if (val[hi-1][wid+1] == 1):
          neigh += 1
      # top-right corner
      elif (wid == WIDTH - 1 and hi == 0):
        if (val[hi][wid-1] == 1):
          neigh += 1
        if (val[hi+1][wid] == 1):
          neigh += 1
        if (val[hi+1][wid-1] == 1):
          neigh += 1
      # bottom-right corner
      elif (wid == WIDTH - 1 and hi == HEIGHT - 1):
        if (val[hi][wid-1] == 1):
          neigh += 1
        if (val[hi-1][wid] == 1):
          neigh += 1
        if (val[hi-1][wid-1] == 1):
          neigh += 1
      # upper bound
      elif (hi == 0):
        if (val[hi][wid+1] == 1):
          neigh += 1
        if (val[hi][wid-1] == 1):
          neigh += 1
        if (val[hi+1][wid] == 1):
          neigh += 1
        if (val[hi+1][wid+1] == 1):
          neigh += 1
        if (val[hi+1][wid-1] == 1):
          neigh += 1
      # left bound
      elif (wid == 0):
        if (val[hi][wid+1] == 1):
          neigh += 1
        if (val[hi+1][wid+1] == 1):
          neigh += 1
        if (val[hi-1][wid+1] == 1):
          neigh += 1
        if (val[hi+1][wid] == 1):
          neigh += 1
        if (val[hi-1][wid] == 1):
          neigh += 1
      # lower bound
      elif (hi == HEIGHT - 1):
        if (val[hi][wid+1] == 1):
          neigh += 1
        if (val[hi][wid-1] == 1):
          neigh += 1
        if (val[hi-1][wid] == 1):
          neigh += 1
        if (val[hi-1][wid+1] == 1):
          neigh += 1
        if (val[hi-1][wid-1] == 1):
          neigh += 1
      # right bound
      elif (wid == WIDTH - 1):
        if (val[hi][wid-1] == 1):
          neigh += 1
        if (val[hi+1][wid-1] == 1):
          neigh += 1
        if (val[hi-1][wid-1] == 1):
          neigh += 1
        if (val[hi+1][wid] == 1):
          neigh += 1
        if (val[hi-1][wid] == 1):
          neigh += 1
        # middle area:
      else:
        if (val[hi-1][wid-1] == 1):
          neigh += 1
        if (val[hi-1][wid] == 1):
          neigh += 1
        if (val[hi-1][wid+1] == 1):
          neigh += 1
        if (val[hi][wid-1] == 1):
          neigh += 1
        if (val[hi][wid+1] == 1):
          neigh += 1
        if (val[hi+1][wid-1] == 1):
          neigh += 1
        if (val[hi+1][wid] == 1):
          neigh += 1
        if (val[hi+1][wid+1] == 1):
          neigh += 1
      if (val[hi][wid] == 0):
        if (neigh == 3):
          new[hi][wid] = 1
          cv.itemconfig(cells[hi][wid], fill='black')
        else:
          new[hi][wid] = 0
      elif (val[hi][wid] == 1):
        if (2 <= neigh and neigh <= 3):
          new[hi][wid] = 1
        else:
          new[hi][wid] = 0
          cv.itemconfig(cells[hi][wid], fill='white')
    val = new
    cv.update()
    gc.collect()
    t1 = time.time()
    time.sleep(max(1.0/FPS - (t1-t0), 0))

main()
