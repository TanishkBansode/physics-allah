def workdone(force, displacement):
    return print(f"Workdone = {force * displacement}")


##################################################
# When displacement is in the direction of force #
##################################################

# Eg
force1 = 5#N
displacement1 = 2#m
workdone(force1, displacement1)

#########################################
# When work is 90degree (zero workdone) #
#########################################

# Eg
force2 = 5#N
displacement2 = 0#N coz straight up

workdone(force2, displacement2)

#########################################
# When work is opposite(negative)       #
#########################################

# Eg (when drawing water out of well)
force3 = -5 #N 
displacement3 = 2 #m

workdone(force3, displacement3)

######################################################
# When work is against gravity like lifting luggage  #
######################################################

def workdone1(mass, gravity, displacement):
    return print(f"Workdone = {mass*gravtiy*displacement}")

mass = 15#kg
displacement4 = 1.5#m

workdone1(mass=15, gravity=9.8, displacement=displacement4)


###############################################################
# When object is in motion like a ball falling from a ground. #
###############################################################

def workdone2(mass, final_velocity, initial_velocity):
	return print(f"Workdone = {0.5 * mass * ((final_velocity ** 2) - (initial_velocity ** 2))}")

mass = 15#kg
fv = 10#m/s
fi = 5#m/s
workdone2(mass, fv, fi)
