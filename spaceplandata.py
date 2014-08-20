## Data for the Space Planning Algorithm
def data():
    employees = {}
    employees['Jen']        = addEmployee(.70,  .4,  -.5, .67, .60)
    employees['Nick']       = addEmployee(.25,   0,  -.5,  .4, .50)
    employees['Fritz']      = addEmployee( -1,   1,   -1, -.5, .40)
    employees['Augusto']    = addEmployee(.75,  .2,    0,  .5, .25)
    employees['Owen']       = addEmployee(.50, .91,    0,   0, .80)
    employees['Vivian']     = addEmployee(.50,   1,    1,  .3, .30)
    employees['Scott']      = addEmployee(.40,   0,  -.5,  .2, .65)
    employees['Julia']      = addEmployee( .5,  .5,    0,  .9, .60)
    employees['Jocelyn']    = addEmployee(  0,   1,    0,  .8, .80)
    employees['Ryan']       = addEmployee(  1,   1,    0, .25,   0)
    employees['Tom']        = addEmployee(  0,  .5,   -1,  .7, .70)
    employees['Rohan']      = addEmployee(  0,  .8,  -.1, .25, .70)
    employees['Autumn']     = addEmployee(.25,   1,    0,  .7, .40)
    employees['Eric']       = addEmployee(  0,  .3,  -.5, .25, .80)
    employees['Kate']       = addEmployee(.25,   1,  -.8,  .5, .70)
    employees['Katie']      = addEmployee(.25, -.4,    0,  .2, .50)
    employees['Daishi']     = addEmployee(.25,  .4,  -.2,  .3, .80)
    employees['Chris']      = addEmployee(.25,   1,   -1,  .5, .60)
    employees['Morgan']     = addEmployee(  0,   1,  -.8,  .8, .60)
    employees['Turner']     = addEmployee(.25,  .3,  -.4,  .4, .60)
    employees['Andrew']     = addEmployee(.25,   1,  -.8,  .3, .60)
    employees['Teddy']      = addEmployee(.25,  .5, -.25, .25, .70)
    employees['Aki']        = addEmployee(1,     0,  -.5,  .5,  .6)
    employees['AE2']        = addEmployee(1,     0,  -.5,  .5,  .6)
    employees['BD']         = addEmployee(1,     0,  -.5,  .5,  .6)
    employees['ENG1']       = addEmployee(1,     0,  -.5,  .5,  .6)
    employees['ENG2']       = addEmployee(1,     0,  -.5,  .5,  .6)
    employees['PD']         = addEmployee(1,     0,  -.5,  .5,  .6)

    desks = {}
    teams = [['Fritz', 'Augusto', 'Owen', 'Daishi', 'Andrew', 'Teddy'], # BE
             ['Rohan', 'Turner', 'AE2', 'BD'], # App Eng
             ['Owen', 'Rohan', 'ENG1'], # API
             ['Scott', 'Jocelyn', 'Kate', 'Chris', 'Katie', 'ENG2'], # Metro
             ['Vivian', 'Morgan', 'Chris', 'Ryan'], # Product
             ['Nick', 'Jen', 'Tom', 'Andrew'], # Leadership
             ['Eric', 'Ryan', 'Julia', 'Jen', 'Aki', 'PD', 'Scott'], # Maker Tools
             ['Autumn', 'Tom', 'Ryan'] # Office Administration
            ]

    desks[0]  = addDesk([.18, .91], .0, .0, .5)
    desks[1]  = addDesk([.24, .91], .2, .0, .3)
    desks[2]  = addDesk([.35, .91], .2, .2, .5)
    desks[3]  = addDesk([.42, .91], .2, .5, .3)
    desks[4]  = addDesk([.18, .86], .5, .3, .6)
    desks[5]  = addDesk([.24, .86], .5, .3, .6)
    desks[6]  = addDesk([.35, .86], .5, .4, .6)
    desks[7]  = addDesk([.42, .86], .4, .5, .4)
    desks[8]  = addDesk([.45, .75], .7, .5, .5)
    desks[9]  = addDesk([.51, .75], .5, .6, .3)
    desks[10] = addDesk([.45, .66], .7, .5, .5)
    desks[11] = addDesk([.51, .66], .5, .4, .3)
    desks[12] = addDesk([.49, .78], .7, .6, .5)
    desks[13] = addDesk([.45, .54], .6, .5, .6)
    desks[14] = addDesk([.51, .54], .4, .4, .3)
    desks[15] = addDesk([.45, .46], .5, .5, .6)
    desks[16] = addDesk([.51, .46], .4, .4, .2)
    desks[17] = addDesk([.26, .32], .6, .7, .5)
    desks[18] = addDesk([.35, .32], .6, .7, .7)
    desks[19] = addDesk([.40, .32], .6, .7, .5)
    desks[20] = addDesk([.10, .25], .4, .7, .4)
    desks[21] = addDesk([.26, .27], .3, .8, .4)
    desks[22] = addDesk([.35, .27], .3, .8, .4)
    desks[23] = addDesk([.40, .27], .4, .8, .5)
    desks[24] = addDesk([.55, .24], .5, .8, .5)
    desks[25] = addDesk([.55, .17], .6, .8, .4)
    desks[26] = addDesk([.55, .11], .6, .8, .2)
    desks[27] = addDesk([.48, .40], .4, .4, .3)
    desks[28] = addDesk([.10, .20], .3, .6, .4)

    return [employees, desks, teams]

def addEmployee(team, sunlight, noise, heatScore, atDeskLikelihood):
    return {
    'preferences': {
        'individualScore': 1, 'lightScore': sunlight, 'loudnessScore': noise, 'heatScore': heatScore
        },
    'atDeskLikelihood': atDeskLikelihood
    }

def addDesk(location, lightScore, loudnessScore, heatScore):
    return {
    'location': location,
    'preferences': {
        'lightScore': lightScore, 'loudnessScore': loudnessScore, 'heatScore': heatScore
        }
    }
