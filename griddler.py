import math
mm = 2.8346456693
# HOW TO USE GRIDDLER? basic instructions at the bottom of the code

# —————————————————————————————————
# ########## SETTINGS #############
# —————————————————————————————————
# Composition
page_size = [420 * mm, 297 * mm]
number_of_lines = 3
margin = 22 * mm
print_settings = True  # True | False
y_offset = 2 * mm
horizontal_margin = 5 * mm
line_height_indicator = True
line_gap = 0 * mm # leave at 0 to centre automatically

# METRICS | 0 = off
x_height = 35 * mm
cap_height = x_height + 10 * mm
ascender_height = x_height + 20 * mm # e.g. x_height + 12 * mm
descender_height = 20 * mm

# tolerances / overshoots
tolerance = 1.4 * mm
tolerance_style = 1  # 0 = line | 1 = rectangle | 2 = both
tolerance_color_stroke = [0, 1]
tolerance_color_fill = [0.9, 0.4, 0.1, 0.5]

print_italic_angle = True
italic_angle = 11
italic_guide_interval = 15.0 * mm
italic_guide_color = [0, 1]
italic_guide_overshoot = 0 * mm # or e.g. = tolerance

# USE SAVED SETTINGS by filling out the parameters
setting_parameters = []

# LINE STYLING
line_thickness = 0.6
line_color = [0, 1]

alt_color = [1, 0, 0, 1]
alt_color_selector = []

# Math sophistry
rounding_decimals = 2


# ——————————————————————————————
############ LOGIC #############
# ——————————————————————————————
rd = rounding_decimals

# SAVED SETTINGS
if setting_parameters:
    if len(setting_parameters) != 15:
        print(
            "Wrong number of parameters in setting_parameters. Individual inputs will be used"
        )
    else:
        number_of_lines = setting_parameters[0]
        margin = setting_parameters[1] * mm
        y_offset = setting_parameters[2] * mm
        horizontal_margin = setting_parameters[3] * mm
        ascender_height = setting_parameters[4] * mm
        cap_height = setting_parameters[5] * mm
        x_height = setting_parameters[6] * mm
        descender_height = setting_parameters[7] * mm
        italic_angle = setting_parameters[8]
        italic_guide_interval = setting_parameters[9][0] * mm
        italic_guide_overshoot = setting_parameters[9][1]*mm
        print_settings = bool(setting_parameters[10]) * mm
        tolerance = setting_parameters[11]
        tolerance_style = setting_parameters[12]
        tolerance_color_stroke = setting_parameters[13][0]
        tolerance_color_stroke = setting_parameters[13][1]
        page_size = [setting_parameters[14][0]*mm, setting_parameters[14][1]*mm]

def context_int(n):
    value = round(n / mm, rd)
    return int(value) if value == int(value) else value


print(
    "used setting_parameters:\n"
    + str(
        [
            number_of_lines,
            context_int(margin),
            context_int(y_offset),
            context_int(horizontal_margin),
            context_int(ascender_height),
            context_int(cap_height),
            context_int(x_height),
            context_int(descender_height),
            italic_angle,
            [context_int(italic_guide_interval),
            context_int(italic_guide_overshoot)],
            int(print_settings),
            context_int(tolerance),
            tolerance_style,
            [tolerance_color_stroke, tolerance_color_fill],
            [context_int(page_size[0]), context_int(page_size[1])]
        ]
    )
)
size(*page_size)

mHor = horizontal_margin
pWidth = width()

descender_height = abs(descender_height)
x_height = abs(x_height)
cap_height = abs(cap_height)
ascender_height = abs(ascender_height)
number_of_lines = abs(int(number_of_lines))

total_line_height = max(x_height, cap_height, ascender_height) + descender_height

if line_gap != 0:
    gap_value = line_gap
elif number_of_lines > 1:
    gap_value = (height() - margin * 2 - ((number_of_lines) * total_line_height)) / (
        number_of_lines - 1
    )
elif number_of_lines == 0:
    gap_value = 0
if number_of_lines == 1:
    gap_value = 0


# PRINT SETTINGS
textOffset = max(30, horizontal_margin)
txt = FormattedString()
txt.append("lines: ")
txt.append(str(number_of_lines))
txt.append("    ")
if italic_angle:
    txt.append("italic guides: " + f"{float(round(italic_angle, rd)):g}"+"°    ")
if x_height:
    txt.append("x-height: " + f"{float(round(x_height / mm, rd)):g}"+" mm    ")
if cap_height:
    txt.append("cap height: "+f"{float(round(cap_height / mm, rd)):g}"+" mm    ")
if ascender_height:
    txt.append("ascender height: "+f"{float(round(ascender_height / mm, rd)):g}"+" mm    ")
if descender_height:
    txt.append("descender height: "+f"{float(round(descender_height / mm, rd)):g}"+" mm    ")
if tolerance:
    txt.append("overshoots: "+f"{float(round(tolerance / mm, rd)):g}"+" mm    ")
if gap_value:
    txt.append("gap: "+f"{float(round(gap_value / mm, rd)):g}"+" mm    ")
# txt.append("[mm]")
if print_settings:
    txt.openTypeFeatures(onum=True)
    text(txt, (textOffset, margin / 2-4+y_offset/2))


############## DRAWING LINES / FUNCTIONS
def drawLine(origin, color=0, toleranceDir = -2):
    drawTolerance(origin, toleranceDir)
    if color == 1:
        stroke(*tolerance_color)
    elif color == 2:
        stroke(*italic_guide_color)
    line((horizontal_margin, origin), (pWidth - horizontal_margin, origin))
    stroke(*line_color)


def drawTolerance(origin, direction):
    if tolerance == 0: return
    if direction == -2: return
    offset = direction * tolerance
    if tolerance_style == 1 or tolerance_style == 2:
        fill(*tolerance_color_fill)
        stroke(None)
        rect(horizontal_margin, origin,pWidth-2*horizontal_margin, offset)
        fill(None)
        stroke(*line_color)
        if tolerance_style == 1: return
    stroke(*tolerance_color_stroke)
    line(
        (horizontal_margin, origin + offset),
        (pWidth - horizontal_margin, origin + offset),
    )
    stroke(*line_color)


# ITALIC
deg = math.pi / 180
italX = total_line_height / math.tan((90 - italic_angle) * deg)
startY = 0
ital_amount = (width() - max(textOffset, horizontal_margin)) / italic_guide_interval


def calcPointOnAngle(y_distance):
    return y_distance / math.tan((90-italic_angle)*deg)
def drawItalicGuide(start):
    if italic_guide_overshoot != 1:
        startY = baseline - descender_height - italic_guide_overshoot
        italX = calcPointOnAngle(total_line_height+italic_guide_overshoot)
    if (start + italX) > (width() - max(textOffset, horizontal_margin)): return
    if start + italX < max(textOffset, horizontal_margin): return
    line((start, startY), (start + italX, startY + total_line_height + italic_guide_overshoot*2))


############## INITIAL STROKE STYLING
lineCap("square")
stroke(*line_color)
strokeWidth(line_thickness)
startingPoint = height() - margin + y_offset


############## GRID DRAWING LOOP
for i in range(0, number_of_lines):
    baseline = startingPoint - max(cap_height, x_height, ascender_height)
    # VERTICAL GUIDES
    if line_height_indicator:
        line((textOffset, startingPoint), (textOffset, startingPoint - total_line_height))
        line(
            (width() - max(horizontal_margin, textOffset), startingPoint),
            (
                width() - max(horizontal_margin, textOffset),
                startingPoint - total_line_height,
            ),
        )

    # HORIZONTAL GUIDES
    drawLine(baseline, 0, -1)
    if x_height:
        drawLine(baseline + x_height, 0, 1)
    if ascender_height:
        drawLine(baseline + ascender_height, 0, 1)
    if cap_height:
        drawLine(baseline + cap_height, 0, 1)
    if descender_height != 0:
        drawLine(baseline - descender_height, 0, -1)

    # ITALIC GUIDES
    startY = baseline - descender_height
    stroke(*italic_guide_color)
    for i in range(0, int(ital_amount)):
        if not print_italic_angle:
            continue
        if line_height_indicator and i==0: continue
        drawItalicGuide(
            max(horizontal_margin, textOffset) + i * italic_guide_interval
        )
    stroke(*line_color)
    startingPoint -= gap_value + total_line_height