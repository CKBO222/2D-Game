#Author: Christopher Bond
#Email: CKBO222@g.uky.edu
#Section:401

#Pre-conditions: The user will give inputs for the number of rounds, level of 
#                difficulty, angle, and initial velocity.

#Post-conditions: The program will display whether or not the bird hit the pig
#                 and keep score of how many times it did so.  It will show an
#                 animation of the bird flying.

#Purpose: To create a game similar to angry birds where the user enters an angle
#         and velocity to hit a pig which appears at a random distance each round.

from graphics import *
from random import *
from math import *
def angle_velocity(window, prompt1, prompt2, x_location, y_location):
    '''Pre-Conditions: The user will enter the name of the graphics window,
                       the first prompt, the second prompt, and the x and y 
                       location that you want the first prompt to be located at.
    
       Post-Conditions: The function will return the distance the bird traveled 
       and the maximum height that it reached.
       
       Purpose: To create a prompt for the angle and velocity to give to the user.
                Then take the given angle and velocity to calculate the distance
                and maximum height traveled by the bird.
    
    '''    
    #Display the prompts
    
    angle_prompt = Text(Point(x_location, y_location), prompt1)
    angle_prompt.setSize(18)
    angle_prompt.draw(window)
    
    velocity_prompt = Text(Point(x_location, y_location + 50), prompt2)
    velocity_prompt.setSize(18)
    velocity_prompt.draw(window)
    
    #create the entry boxes
    
    angle_entry_box = Entry(Point(x_location, y_location + 25), 10)
    velocity_entry_box = Entry(Point(x_location, y_location + 75), 10)
    
    angle_entry_box.draw(window)
    velocity_entry_box.draw(window)
    
    #Move to the next screen and undraw the prompts from the previous screen
    window.getMouse()
    angle_entry_box.undraw()
    velocity_entry_box.undraw()
    angle_prompt.undraw()
    velocity_prompt.undraw()
    
    #Get the inputs from the prompts
    angle = angle_entry_box.getText()
    velocity = velocity_entry_box.getText()
    
    #if statement for missing input
    if angle == '':
        angle = 60
        
    if velocity == '':
        velocity = 60
    
    #convert velocity to float
    velocity = float(velocity)
   
    #convert the angle to a float and from degrees to radians
    angle = float(angle)
    angle = radians(angle)
    
    #create the distance formula and round it
    distance = ((velocity**2) * sin(2 * angle)) / 9.8
    distance = round(distance)
    
    #create the height formula and round it.       
    height = ((velocity**2) * (sin(angle)**2)) / (2 * 9.8) 
    height = round(height)
    
    return distance, height
                               

def main():
    '''Pre-Conditions: The user will give an input for the number of rounds they
                       want to play as well as the level of difficulty.
                       
       Post-Conditons: The program will display the bird and pig at their starting
                       points, the bird at the halfway point, and where the bird 
                       lands.  It will also tell the user whether or not they
                       hit the pig and at the end of the game, how many times
                       they did so.
                       
       Purpose: To show the graphics of the bird and pig as the game is being 
                played.
    '''
    
    #Create the graphics window
    win = GraphWin('Angry Birds', 500, 500)
    win.setBackground('seashell')
    
    #Create the title
    title = Text(Point(250, 20), 'ANGRY BIRDS!')
    title.setSize(25)
    title.draw(win)
    
    #Display the prompts for rounds played and difficulty
    rounds_prompt = Text(Point(250, 175), 'How many rounds to play?')
    rounds_prompt.setSize(15)
    rounds_prompt.draw(win)
    
    difficulty_prompt = Text(Point(250, 225), 'What level of difficulty? (Smaller is harder)')
    difficulty_prompt.setSize(15)
    difficulty_prompt.draw(win)
    
    #create and draw the entry boxes
    rounds_box = Entry(Point(250, 200), 10)
    diff_box = Entry(Point(250, 250), 10)
    
    rounds_box.draw(win)
    diff_box.draw(win)
    win.getMouse()
    
    #Get the results of the entry box 
    rounds = rounds_box.getText()
    diff = diff_box.getText()
    
    #if the entry boxes return empty strings
    if rounds == '':
        rounds = '1'
        
    if diff == '':
        diff = '10'
    
    #Display the difficulty on the screen
    difficulty_display = Text(Point(50, 110), 'Difficulty: ' + diff)
    difficulty_display.setSize(15)
    difficulty_display.draw(win)
    
    #Point total
    points_total = '0'
    
    #Display the points on the screen
    points_display = Text(Point(450, 110), 'Points: ' + points_total)
    points_display.setSize(15)
    points_display.draw(win)                      
    
    #Set the rounds input to an integer
    range_upper = rounds
    range_upper = int(range_upper)
    
    #initialize pig hits to be used for the if statements following the loop.
    pig_hits = 0
    
    #The for loop which will run for the number of rounds that the user entered.
    for i in range(1, range_upper + 1):
        
        #Remove the previous prompts
        rounds_prompt.undraw()
        difficulty_prompt.undraw()
        rounds_box.undraw()
        diff_box.undraw()
        
        #Display the pig location and make it random
        pig_distance = randint(300, 375)
        pig_distance = str(pig_distance)
        pig_distance_display = Text(Point(240, 155), 'Pig is at ' + pig_distance)
        pig_distance_display.setSize(16)
        pig_distance_display.draw(win)        
        
        #convert i and range_upper to strings so that they can be displayed.
        i = str(i)
        range_upper = str(range_upper)
        
        #Display rounds played
        rounds_played = Text(Point(225, 110), 'Round #' + i)
        rounds_played2 = Text(Point(275, 110), ' of ' + range_upper)
        rounds_played.setSize(17)
        rounds_played2.setSize(17)
        rounds_played.draw(win)
        rounds_played2.draw(win)
        
        
        #First images for bird and pig
        bird_image = Image(Point(25,485), "bird.gif")
        bird_image.draw(win)
        
        pig_distance = int(pig_distance)
        pig_image = Image(Point(pig_distance, 485), "pig.gif")
        pig_image.draw(win)
        
        #Call the angle_velocity function
        distance, height = angle_velocity(win, 'What angle?', 'What velocity?', 250,200)        
        
        #Second image for bird
        bird_image.undraw()
        bird_image = Image(Point(((distance - 25) / 2), 500 - height), "bird.gif")
        bird_image.draw(win)
        
        #Display telling you to click.
        click_text = Text(Point(250, 300), 'Click')
        click_text.setSize(14)
        click_text.draw(win)
        win.getMouse()
        
        #Third image for the bird
        bird_image.undraw()
        bird_image = Image(Point(distance, 485), "bird.gif")
        bird_image.draw(win)
        
        #Convert pig_distance and diff to integers for the if statement
        pig_distance = int(pig_distance)
        diff = int(diff)
        
        #if-else statement to determine whether or not the pig was hit
        if pig_distance - diff <= distance <= pig_distance + diff:
            click_text.undraw()
            hit_text = Text(Point(240, 300), 'You got the pig!')
            hit_text.setSize(14)
            hit_text.draw(win)
            
            #If hit, add to the point total and pig hit total
            points_total = int(points_total)
            points_total += 1
            pig_hits += 1
            points_total = str(points_total)
            points_display.setText('Points: ' + points_total)
            win.getMouse()
            hit_text.undraw()
            
        else:
            click_text.undraw()
            miss_text = Text(Point(250, 300), 'You missed!')
            miss_text.setSize(14)
            miss_text.draw(win)
            win.getMouse()
            miss_text.undraw()
            
          
        #Convert i back to an int and add 1 to it
        i = int(i)
        i = i + 1
        
        #click to undraw and reset text
        rounds_played.undraw()
        rounds_played2.undraw()
        pig_distance_display.undraw()
        bird_image.undraw()
        pig_image.undraw()
        rounds_played.setText(i)
        
                             
    #if statements for pig hits    
    if pig_hits == 1:
        hit_text = Text(Point(245, 300), 'You hit one pig!')
        hit_text.setSize(15)
        hit_text.draw(win)
        
    if pig_hits == 0:
        hit_text = Text(Point(245, 300), 'You hit no pigs!')
        hit_text.setSize(15)
        hit_text.draw(win)
   
    if pig_hits >= 2:
        hit_text = Text(Point(230, 300), 'You hit ' + points_total)
        hit_text2 = Text(Point(275, 300), ' pigs!')
        hit_text.setSize(15)
        hit_text2.setSize(15)
        hit_text.draw(win)
        hit_text2.draw(win)
       
    #Create the click to end display
    click_to_end = Text(Point(243, 320), 'Click to end')
    click_to_end.setSize(15)
    click_to_end.draw(win)
    
    
    
    win.getMouse()
    win.close()

main()
    
    