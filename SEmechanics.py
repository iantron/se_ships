# Effectiveness of atmospheric thrusters as percent.
def e_atmospheric(r, R, A, H):
    e = 1 - ( ( r-R ) / ( R*0.7*H*A) )
    if e > 1 : e=1
    elif e < 0 : e=0
    return(e)

def acceleration_gravity(r, g, Rmin, Rmax):
    if Rmax < r: a = g * (Rmax/r)**7
    elif Rmin <= r <= Rmax: a = g
    else: a = g * (r/Rmin)
    return(a)