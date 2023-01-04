from random import choice , randint


        # //20 -- gold
        # //30 -- black
        # //20 -- red
def random_style():
    final_style = """"""
    base_list = []
    for i in range(2,100):
        base_list.append(i)
    
    for i in range(20):
        num = choice(base_list)
        base_list.remove(num)
        id = "#c"+str(num)
        border = 'gold'
        s = id+"{border:7px outset gold}\n"
        final_style +=s
    
    for i in range(30):
        num = choice(base_list)
        base_list.remove(num)
        id = "#c"+str(num)
        border = 'gold'
        s = id+"{border:7px outset black}\n"
        final_style +=s
    
    for i in range(30):
        num = choice(base_list)
        base_list.remove(num)
        id = "#c"+str(num)
        border = 'gold'
        s = id+"{border:7px outset red}\n"
        final_style +=s
    
    return final_style