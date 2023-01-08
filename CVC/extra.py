from random import choice, randint


# //7 -- snakes
# //3 -- dino
# //10 -- lifts
def random_style():
    dino_list_id = []
    snake_list_id = []
    lift_list_id = []
    num1 = randint(91, 99)
    num2 = randint(75, 90)
    num3 = randint(50, 74)
    dino_list_id.append(num1)
    dino_list_id.append(num2)
    dino_list_id.append(num3)

    while len(snake_list_id) < 10:
        num = randint(2, 99)
        if num not in dino_list_id and num not in snake_list_id and num not in lift_list_id:
            snake_list_id.append(num)

    while len(lift_list_id) < 7:
        num = randint(2, 90)
        if num not in dino_list_id and num not in snake_list_id and num not in lift_list_id:
            lift_list_id.append(num)

    style_tag = """"""
    s = ''
    for id in dino_list_id:
        s += "#c" + str(id) + "{background-image:url(/static/images/dino2.gif)}\n"

    style_tag += s
    s = ''
    
    for id in snake_list_id:
        s += "#c" + str(id) + "{background-image:url(/static/images/snake.gif)}\n"

    style_tag += s
    s = ''

    for id in lift_list_id:
        s += "#c" + str(id) + "{background-image:url(/static/images/lift2.gif)}\n"

    style_tag += s

    snake_list_final = []
    for i in snake_list_id:
        id = "#c"+str(i)
        snake_list_final.append(id)
    snakes = ""
    for snake in snake_list_final:
        snakes += f"window.currnet_blue_pos == '{snake}' || "
    # print(snakes)


    lift_list_final = []
    for i in lift_list_id:
        id = "#c"+str(i)
        lift_list_final.append(id)
    lifts = ""
    for lift in lift_list_final:
        lifts += f"window.currnet_blue_pos == '{lift}' || "

    # print(lifts)


    dino_list_final = []
    for i in dino_list_id:
        id = "#c"+str(i)
        dino_list_final.append(id)
    dinos = ""
    for dino in dino_list_final:
        dinos += f"window.currnet_blue_pos == '{dino}' || "

    # print(dinos)



    snakes_red = ""
    for snake in snake_list_final:
        snakes_red += f"window.currnet_red_pos == '{snake}' || "
    # print(snakes_red)


    lifts_red = ""
    for lift in lift_list_final:
        lifts_red += f"window.currnet_red_pos == '{lift}' || "

    # print(lifts_red)


    dinos_red = ""
    for dino in dino_list_final:
        dinos_red += f"window.currnet_red_pos == '{dino}' || "

    # print(dinos_red)


    set_dino = ""
    for id in dino_list_final:
        set_dino += f"$('{id}').css('background-image','url(/static/images/dino2.gif)')\n"
        set_dino += f"$('{id}').css('color','transparent')\n"
    # print(set_dino)
    # print()

    set_lift = ""
    for id in lift_list_final:
        set_lift += f"$('{id}').css('background-image','url(/static/images/lift2.gif)')\n"
        set_lift += f"$('{id}').css('color','transparent')\n"
    
    # print(set_lift)
    # print()

    set_snake = ""
    for id in snake_list_final:
        set_snake += f"$('{id}').css('background-image','url(/static/images/snake.gif)')\n"
        set_snake += f"$('{id}').css('color','transparent')\n"

    # print(set_snake)
    # print()

    data = [style_tag , snakes[0:len(snakes)-3],lifts[0:len(lifts)-3],dinos[0:len(dinos)-3],snakes_red[0:len(snakes_red)-3],lifts_red[0:len(lifts_red)-3],dinos_red[0:len(dinos_red)-3],set_lift,set_snake,set_dino]

    return data


# random_style()

def hide_ids(l):
    hide_id = []
    for id in range(1,37):
        if id not in l:
            hide_id.append(id)


def horizental(data,num):
    
    if data[str(num)] == data[str(num+1)] and  data[str(num)] == data[str(num+2)] and data[str(num)] == data[str(num+3)] and  data[str(num)] != 'none':
        win = ''
        
        if 'bluefill.gif' in data[str(num)]:
            win = 'blue'    
            pos = [num,num+1,num+2,num+3]
            # hides = hide_ids(pos)
            
            res = [True,win,pos]
            return res
        elif 'redfill.gif' in data[str(num)]:
            win = 'red'
            pos = [num,num+1,num+2,num+3]
            res = [True,win,pos]
            return res
    else:
        return [False,'none']
         

def vertical(data,num):
    
    if data[str(num)] == data[str(num+6)] and  data[str(num)] == data[str(num+12)] and data[str(num)] == data[str(num+18)] and  data[str(num)] != 'none':
        win = ''
        if 'bluefill.gif' in data[str(num)]:
            win = 'blue'    
            pos = [num,num+6,num+12,num+18]
            res = [True,win,pos]
            return res
        elif 'redfill.gif' in data[str(num)]:
            win = 'red'
            pos = [num,num+6,num+12,num+18]
            res = [True,win,pos]
            return res
        
    else:
        return [False,'none']
        
         




def check_any4(data):
    required_horizental_postions = [1,2,3,7,8,9,13,14,15,19,20,21,25,26,27,31,32,33]
    required_vertical_postions = [1,7,13,2,8,14,3,9,15,4,10,16,5,11,17,16,12,18]
    
    for pos in required_horizental_postions:
        res = horizental(data, pos)
        if res[0] == True:
            return res
    for pos in required_vertical_postions:
        res = vertical(data, pos)
        if res[0] == True:
            return res
    return [False,'none']

        



    
