import turtle
import math

screen = turtle.Screen()
player = turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.pensize(10)


def listen():
    x1 = screen.textinput("set coordinate", "set x1's value")
    y1 = screen.textinput("set coordinate", "set y1's value")
    x2 = screen.textinput("set coordinate", "set x2's value")
    y2 = screen.textinput("set coordinate", "set y2's value")
    string_coordinate = [x1, y1, x2, y2]
    # input으로 입력받으면, string이라서, float으로 바꿉니다.
    result = map(float, string_coordinate) 
    return result


def main():
    x1, y1, x2, y2 = listen()
    print("x1, y1, x2, y2 = " , x1, y1, x2, y2)
    player.penup()
    player.goto((x1,y1))
    player.pendown()
    player.goto((x2,y2))
    screen.mainloop()
    result = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    print("distance is", result)
    return result
    
main()
