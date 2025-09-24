# Griddler - how to

Step 0: open the python code in [Drawbot](https://www.drawbot.com/)

### Modifying the grid
All the settings are at the top of the code. This is the only part of the code you need to modify. The variables are named somewhat clearly after the things they represent.
If unsure about what a variable does, you can select the number and  Cmd + ↑  or  Cmd + ↓  to easily see what updates in the preview.

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