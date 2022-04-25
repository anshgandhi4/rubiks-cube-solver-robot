# Rubik's Cube Solver Robot

## Background
My friends and I decided to make a Rubik's cube mosaic for our AP Physics C semester final project. To create this mosaic, we realized it would be fun to make a Rubik's cube solver robot, feed it a bunch of cubes, and have it solve them to make a mosaic. We hope this repository documents, at least the software portion, of our project's progress.


## Acknowledgements
Huge thanks to Ansh Gandhi, Mukunth Nagarajan, Jonathan Ma, and Athul Krishnan for working on this project. Also many thanks to Mrs. Kumar for assigning this project and giving us the opportunity to explore our common interest in robotics for a school assignment.

## How the Code Works
Here's a high level description of what happens:
1) The user specifies the initial cube state.
   1) The default form of input is through computer vision. Our vision code is basically copied, with some tweaks, from my original Rubik's cube solver project (which you can check out [here](https://github.com/anshgandhi4/Rubiks-Cube-Solver)). The color detection is tuned for a Gan 354 but also works with the Gan 11 Pro. I'm sure it works well with other cubes, although those haven't been extensively tested.
   2) The other form of input is through a cube string. This contains capital letters representing the different colors on the Rubik's cube. For example, `WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB` represents a solved cube, and `WYWYWYWYWRORORORORGBGBGBGBGYWYWYWYWYOROROROROBGBGBGBGB` represents a checkerboard pattern.
2) The user specifies the final cube state.
   1) The default final state is a solved cube.
   2) The final state can also be defined using a cube string (as explained before).
3) The user specifies the desired solving algorithm.
   1) The default algorithm is a modified version of the Old Pochmann algorithm (typically used for blindfolded solves). I wrote this by scratch (hence all the python files with `op` in their name). I also modified it so that only five sides are used for turning, because that's how our robot is designed.
   2) The other algorithm is the Kociemba algorithm. This is imported through the `kociemba` Python library. While it is slightly more computationally heavy than the Old Pochmann, it is orders of magnitude more efficient in terms of move count. While it may take ~400 moves to solve the cube using Old Pochmann, Kociemba can do it in around 20.
4) The cube solution is printed in [standard cubing notation](https://www.youtube.com/embed/24eHm4ri8WM?start=0&end=51).