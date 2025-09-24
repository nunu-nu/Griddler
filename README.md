# Griddler - how to

Step 0: open the python code in [Drawbot](https://www.drawbot.com/)

### Modifying the grid
All the settings are at the top of the code. This is the only part of the code you need to modify. The variables are named somewhat clearly after the things they represent.
If unsure about what a variable does, you can select the number and  Cmd + ↑  or  Cmd + ↓  to easily see what updates in the preview.
Quick overview:
```Python
# Composition
page_size = [420 * mm, 297 * mm] # specifies page size in mm
number_of_lines = 3 # number of sets of gridlines to draw
margin = 22 * mm # vertical margin
print_settings = True  # True/False: show text at the bottom with basic metrics info
y_offset = 2 * mm # move all gridlines vertically. Useful for grids without a descender
horizontal_margin = 5 * mm # horizontal margin, might be useful depending on printer
line_height_indicator = True # draw vertical line from bottom to top of the set of gridlines
line_gap = 0 * mm # 0 to centre. Gap between calligraphy lines

# METRICS | 0 = off
x_height = 35 * mm
cap_height = x_height + 10 * mm
ascender_height = x_height + 20 * mm
descender_height = 20 * mm

# tolerances / overshoots
tolerance = 1.4 * mm # How much overshoot to draw
tolerance_style = 1  # Style of overshoot: 0 = line | 1 = rectangle | 2 = both
tolerance_color_stroke = [0, 1] # color of overshoot line
tolerance_color_fill = [0.9, 0.4, 0.1, 0.5] # color of overshoot rectangle

print_italic_angle = True
italic_angle = 11 # 0 = vertical
italic_guide_interval = 15.0 * mm # how often to draw the italic guide
italic_guide_color = [0, 1] # optional: individual different color for italic guide
italic_guide_overshoot = 0 * mm # make line extend over metrics. Can be practical when drawing to align ruler to the italic guide

# USE SAVED SETTINGS by filling out the parameters
setting_parameters = [] # fill in the parameters to reuse old settings

# LINE STYLING
line_thickness = 0.6 # thickness of all the lines
line_color = [0, 1] # color of all the lines

alt_color = [1, 0, 0, 1] # this doesn't work at the moment, ignore
alt_color_selector = [] # this doesn't work at the moment, ignore

# Math sophistry
rounding_decimals = 2 # to how many decimal places to round numbers. This comes to play mainly in what is displayed at the bottom of the sheet.
```

### Units
DrawBot's default units are points. The "mm" variable at the top of the code can be multiplied by a number of points to return value equal to that number of millimetres. 
```Python
x_height = 10       # x_height is 3.5mm
x_height = 10 * mm  # x_height is 10mm
```

### Reusing grids
Griddler will print your used setting parameters into the console. If you would like to reuse these parameters to re-generate a grid in the future, you can put them in a comment in the code and then paste the whole list (including the square brackets) into the setting_parameters variable.
```Python
setting_parameters = [3, 22, 2, 5, 55, 45, 35, 20, 11, [15, 0], 1, 1.4, 1, [[0, 1], [0.9, 0.4, 0.1, 0.5]], [420, 297]]
```
Saved settings might not work with other versions of Griddler (if new parameters are added, changing the length of the saved settings), so it's not unreasonable to save them in the code itself in a comment.

### Saving pdf
Output can be saved as pdf using Cmd+Option+P or File → Save PDF. Alternatively other common formats can be saved by adding a line of code at the end of the script. For example:
```Python
saveImage("output_subfolder/pointed_pen_grid.svg")
saveImage("output_subfolder/parallel_pen_grid.png")
saveImage("output_subfolder/lettering_grid_italic.jpeg")
saveImage("output_subfolder/lettering_grid_black.pdf")
```

[Somehow written by nu](https://letters.nu/)