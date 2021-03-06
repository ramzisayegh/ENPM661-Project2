## Ramzi Sayegh
## ENPM661 Project 2
## BFS Algorithm

# Introduction
This file contains my ENPM661 Project 2. The project objective is to implement a Breadth First Search (BFS) algorithm for a point robot. Specifically, the program will apply BFS to find the optimal path from the starting position to goal position, which are both user defined. Once the goal state is found, the visual animation begins showing each state that is searched and then backtracks to find the optimal path. The program uses the following libraries: numpy and opencv.

# How to run code
- Open a terminal and activate your environment that has python3.7, numpy, and opencv installed. I use anaconda.
- Navigate to the folder where the file was unzipped.
- Enter the following in the command line:
>> python3 P2.py
- User will be promted to enter starting x and y coordinates, followed by goal x and y coordinates.
- If user inputs are not in obstacle space, search will begin.
- Once goal location is found, program will print "solved" and the opencv visual will commence.
- Once the visual reaches the goal location, the backtracking will begin and the optimal path will be printed and displayed as a line in the animation window.

# Libraries/packages detailed
- list.append(element) - adds element to end of list
- list.pop(0) - returns first element of list used for queue data structure, follows FIFO convention
- set.add(string) - adds a string of the visited states only if there will not be a duplicate. Used this method instead of a for loop checking each visited state to reduce run time

# Following used for visual obstacles
- cv2.circle() - draws a circle in visual window given center coordinates and radius
- cv2.ellipse() - draws an ellipse in visual window given center and major/minor axes
- cv2.fillPoly() - fills a polygon given a list of vertices
cv2.imshow() - shows visual window to screen

# Code uploaded to GitHub:
https://github.com/ramzisayegh/ENPM661-Project2



