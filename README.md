# Rearange-bar-by-shape
This script automates the renumbering, sorting, and merging of reinforcement bars using Allplan PythonParts. It helps organize reinforcement bars by length, diameter, or shape code as specified by the user, and simplifies the preparation of clear drawings and reinforcement schedules.

Main script features
Renumbering all reinforcement bars in open files.

Sorting bars by length, diameter, or shape code.

Merging identical bars.

Differentiating between straight and bent bars.

Control options
The script provides several modes:

Complete renumbering: renumbers all bars according to the current order or sorting.

Renumbering only straight bars.

Renumbering and merging straight bars.

Renumbering bent bars.

Renumbering and merging bent bars.

All operations are visualized in the Allplan environment using a progress bar.

What the script does
Finds all reinforcement bars in the drawing.

Differentiates straight and bent bars by their shape.

Sorts bars according to selected criteria (length, diameter, shape).

Renumbers the bars (changes the mark number) in the required order.

Optionally merges identical bars and simplifies the reinforcement schedule.

Result
Reinforcement bars will be newly marked, sorted, and, if selected, merged according to the chosen rules.

This makes it easier to prepare production documentation and to export schedules.
