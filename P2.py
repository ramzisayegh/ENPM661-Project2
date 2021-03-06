#link to GitHub
#https://github.com/ramzisayegh/ENPM661-Project2

import numpy as np 
import cv2

#Function to define obstacle space using half-planes and algebraic models
#Returns True if (x,y) is in obstacle space, False if not
def Obstacle(state):
	x = state[0]
	y = state[1]
	if (x > 400 or x < 0 or y > 300 or y < 0):
		return True
	elif (y>=0.7*x+74.38 and y<=0.7*x+98.8 and y>=-1.43*x+176.55 and y<=-1.43*x+438.4):
		return True
	elif ((x-90)**2 + (y-70)**2 <= 35**2):
		return True
	elif (x>=200 and x<=210 and y>=230 and y<=280):
		return True
	elif (x>=210 and x<=230 and y>=230 and y<=240):
		return True
	elif (x>=210 and x<=230 and y>=270 and y<=280):
		return True
	elif ((x-246)**2/60**2 + (y-145)**2/30**2 <=1):
		return True
	elif (y<=1.00131*x-180.575 and y>=1.00131*x-265.431 and y>=-1*x+391 and x<=381.03 and y<=-0.24375*x+224.288):
		return True
	elif (y<=1.22198*x-294.579 and y>=-0.24375*x+224.288 and x<=381.03):
		return True
	else:
		return False

#Next 8 functions are used to describe the action sets to find children
#All 8 functions follow same logic
#Returns child if child is not in obstacle space, 0 if in obstacle space
def MoveUp(state):
	x = state[0]
	y = state[1]
	child_up = [x,y+1]
	if (Obstacle(child_up)==False):
		return child_up
	else:
		return 0

def MoveDown(state):
	x = state[0]
	y = state[1]
	child_down = [x,y-1]
	if (Obstacle(child_down)==False):
		return child_down
	else:
		return 0
	
def MoveRight(state):
	x = state[0]
	y = state[1]
	child_right = [x+1,y]
	if (Obstacle(child_right)==False):
		return child_right
	else:
		return 0

def MoveLeft(state):
	x = state[0]
	y = state[1]
	child_left = [x-1,y]
	if (Obstacle(child_left)==False):
		return child_left
	else:
		return 0

def MoveUpRight(state):
	x = state[0]
	y = state[1]
	child_upright = [x+1,y+1]
	if (Obstacle(child_upright)==False):
		return child_upright
	else:
		return 0

def MoveUpLeft(state):
	x = state[0]
	y = state[1]
	child_upleft = [x-1,y+1]
	if (Obstacle(child_upleft)==False):
		return child_upleft
	else:
		return 0

def MoveDownRight(state):
	x = state[0]
	y = state[1]
	child_downright = [x+1,y-1]
	if (Obstacle(child_downright)==False):
		return child_downright
	else:
		return 0

def MoveDownLeft(state):
	x = state[0]
	y = state[1]
	child_downleft = [x-1,y-1]
	if (Obstacle(child_downleft)==False):
		return child_downleft
	else:
		return 0

#Function to convert list to string
def ListToString(state):
	s = str(state)
	return s

#Function to check if current state is the goal state
def AtGoal(state):
	if (ListToString(state)==ListToString(goal)):
		return True
	else:
		return False

#Function to visualize and find optimal path using back tracking with parent information after goal is found
#Splits track into vis state and parent state
#Find the parent states index in vis list and use the parent of that state to perform backtracking
#Show back tracking in visual window
#Add back tracking to optimal path
def BackTrack(track):
	vis = []
	parent = []
	for i in range(len(track)):
		vis.append(track[i][0])
		parent.append(track[i][1])
	back = parent[-1]
	optimal_path.append(back)
	visual[299-back[1],back[0]-1] = [255,0,0]
	cv2.imshow("final_map", visual)
	cv2.waitKey(1)
	while (ListToString(back) != ListToString(initial)):
		visual[299-back[1],back[0]-1] = [255,0,0]
		back_index = vis.index(back)
		back = parent[back_index]
		optimal_path.append(back)
		cv2.imshow("final_map", visual)
		cv2.waitKey(1)


#Get user inputted starting and goal locations
#Throws error and asks to re-enter point if it is in obstacle space
x_i = int(input("Enter starting x: "))
y_i = int(input("Enter starting y: "))
initial = [x_i,y_i]
if (Obstacle(initial)==True):
	print('starting point invalid')

while (Obstacle(initial) == True):
	x_i = int(input("Enter starting x: "))
	y_i = int(input("Enter starting y: "))
	initial = [x_i,y_i]
	if (Obstacle(initial)==True):
		print('starting point invalid')

x_f = int(input("Enter goal x: "))
y_f = int(input("Enter goal y: "))
goal = [x_f,y_f]
if (Obstacle(goal)==True):
	print('goal point invalid')

while (Obstacle(goal) == True):
	x_f = int(input("Enter goal x: "))
	y_f = int(input("Enter goal y: "))
	goal = [x_f,y_f]
	if (Obstacle(goal)==True):
		print('goal point invalid')


#Print initial and goal states to screen
print("Initial: ",initial)
print("Goal: ", goal)

#Initialize queue, track, and visited data structures
queue = []
track = []
visited = set()

#Add initial state to each data structure. Also add parent information to "track" list (used in back tracking)
queue.append(initial)
track.append([initial,0])
visited.add(ListToString(initial)) 


#Begin BFS search. Continue while there are still states in the queue.
while (len(queue)>0):

	#Initialize done to 0, will stay 0 until goal is reached
	done = 0

	#Pop the first element out of the queue (FIFO)
	state_i = queue.pop(0)

	#Check if state is at goal location. If it is, break out of while loop
	if (AtGoal(state_i)==True):
		break

	#Create a list of all children returned by 8 action sets
	children = [MoveUp(state_i), MoveDown(state_i), MoveRight(state_i), MoveLeft(state_i), MoveUpRight(state_i), MoveUpLeft(state_i), MoveDownRight(state_i), MoveDownLeft(state_i)]

	#Filter out children that are in obstacle space (children[i]=0)
	child_real = [i for i in children if i!=0]

	#Check each real child. If it is not visited, is it the goal state? 
	#If it is the goal state, done=1, add to visited set and add state + parent to track list, break out of for loop
	#If it is not the goal state, add child to queue, visited set, and track list
	for i in range(len(child_real)):
		c = child_real[i]
		if (ListToString(c) not in visited):
			if (AtGoal(c)==True):
				solved = c
				done = 1
				visited.add(ListToString(c))
				track.append([c,state_i])
				break
			else:
				queue.append(c)
				visited.add(ListToString(c))
				track.append([c,state_i])

	#If done=1, search is finished and break out of while loop
	if (done==1):
		break

#Print "solved" once goal is found
print("solved")


#Following is used for visual animation

#Create white canvas
visual = 255*np.ones([300,400,3])
#Create obstacles in visual window using cv2 functions: circle, ellipse, and fillPoly
visual = cv2.circle(visual, (89,299-70), 35, (0,0,0), -1)
rect_pts = np.array([[47,299-108],[36,299-124],[158,299-210],[170,299-194]], np.int32)
rect_pts = rect_pts.reshape((-1,1,2))
visual = cv2.fillPoly(visual, [rect_pts], (0,0,0))
c_pts = np.array([[199,69],[199,19],[229,19],[229,29],[209,29],[209,59],[229,59],[229,69]], np.int32)
c_pts = c_pts.reshape((-1,1,2))
visual = cv2.fillPoly(visual, [c_pts], (0,0,0))
visual = cv2.ellipse(visual, (245,299-145), (60,30), 0, 0, 360, (0,0,0), -1)
p_pts = np.array([[285,299-105],[324,299-145],[353,299-138],[380,299-171],[380,299-116],[327,299-63]], np.int32)
p_pts = p_pts.reshape((-1,1,2))
visual = cv2.fillPoly(visual, [p_pts], (0,0,0))

#Show node exploration as green pixels in visual window
for i in range(len(track)):
	cv2.imshow("final_map", visual)
	cv2.waitKey(1)
	visual[299-track[i][0][1],track[i][0][0]-1] = [0,255,0]

#Initialize optimal path list with goal state
optimal_path = [goal]

#Call BackTrack function to visualize back tracking and find optimal path
BackTrack(track)
#Reverse optimal path so it starts at initial state and ends at goal state
optimal_path.reverse()
#Print optimal path to screen
print("Optimal Path :", optimal_path)

#Once back tracking is complete, highlight initial and goal state in visual window for reference
visual = cv2.circle(visual, (initial[0]-1,299-initial[1]), 3, (255,0,0), -1)
visual = cv2.circle(visual, (goal[0]-1,299-goal[1]), 3, (0,0,255), -1)
cv2.imshow("final_map", visual)

cv2.waitKey(0)
cv2.destroyAllWindows()

