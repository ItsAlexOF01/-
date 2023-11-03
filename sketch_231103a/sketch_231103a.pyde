x=15
y=15




def setup():
    size(500,500)
def draw():
    background(64,198,203)
    global x
    ellipse(x,x,50,50)
    x=x+10
    if x == 500:
        x=x-500
   
        
        
