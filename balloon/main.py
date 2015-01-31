#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sfml as sf
import random as rm 

WTITLE = "PySFML Balloon"
WWIDTH, WHEIGHT = 800, 600
BALL_SPEED = 4
MAX_SIZE = 10

def run():
    size = 0
    window = sf.RenderWindow(sf.VideoMode(WWIDTH, WHEIGHT), WTITLE)
    window.framerate_limit = 60

    # Background
    bg_texture = sf.Texture.from_file("assets/images/background.png")
    background = sf.Sprite(bg_texture)

    # Create ball textures
    b_texture = []
    b_texture.append( sf.Texture.from_file("assets/bln/balon0.png") )
    b_texture.append( sf.Texture.from_file("assets/bln/balon1.png") )
    b_texture.append( sf.Texture.from_file("assets/bln/balon2.png") )
    b_texture.append( sf.Texture.from_file("assets/bln/balon3.png") )

    balls = []
    while window.is_open:
        for event in window.events:
            if type(event) is sf.CloseEvent:
                window.close()
        # Close
        if sf.Keyboard.is_key_pressed(sf.Keyboard.ESCAPE):
            window.close()
        # Move balloons
        for ball in balls:
            ball.position = ball.position.x, (ball.position.y + BALL_SPEED)
            if ball.position.y > WHEIGHT:
                balls.remove(ball)
                size -= 1
        # Create balloons
        if size < MAX_SIZE:
            ball = sf.CircleShape( rm.randint(20,60) )
            ball.texture = rm.choice(b_texture)
            ball.origin = 20, 20
            ball.position = rm.randint(40, WWIDTH-80), rm.randint(-300, 0)
            balls.append(ball)
            size += 1

        # Rendering
        window.clear(sf.Color.BLACK)
        window.draw(background)
        for ball in balls:
            window.draw(ball) 
        
        window.display()
 
if __name__ == '__main__':
    run()