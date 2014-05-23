## Data for the Space Planning Algorithm
def data():
    employees = {};
    employees['Nick']       =  0
    employees['Jen']        =  1
    employees['Michelle']   =  2
    employees['Fritz']      =  3
    employees['Freddie']    =  4
    employees['Augusto']    =  5
    employees['Marc']       =  6
    employees['Owen']       =  7
    employees['Vivian']     =  8
    employees['Scott']      =  9
    employees['Julia']      =  10
    employees['Alex']       =  11
    employees['Ryan']       =  12
    employees['Tom']        =  13
    employees['Rohan']      =  14
    employees['Sam']        =  15
    employees['Connie']     =  16
    employees['Katherine']  =  17
    desks = {}
    desks[0] = {
        'location': [0.2, 0.15],
        'individualScore': 1,
        'teamScore': 0,
        'lightScore': .3,
        'loudnessScore': .7
    }
    desks[1] = {
        'location': [0.25, 0.19],
        'individualScore': 1,
        'teamScore': 0,
        'lightScore': .3,
        'loudnessScore': .6
    }
    desks[2] = {
        'location': [0.32, 0.19],
        'individualScore': 1,
        'teamScore': 0,
        'lightScore': .3,
        'loudnessScore': .6
    }
    desks[3] = {
        'location': [0.38, 0.19],
        'individualScore': 1,
        'teamScore': 0,
        'lightScore': .3,
        'loudnessScore': .5
    }
    desks[4] = {
        'location': [0.45, 0.15],
        'individualScore': 1,
        'teamScore': 0,
        'lightScore': .3,
        'loudnessScore': .4
    }
    desks[5] = {
        'location': [0.38, 0.12],
        'individualScore': 1,
        'teamScore': 0,
        'lightScore': .3,
        'loudnessScore': .5
    }
    desks[6] = {
        'location': [0.32, 0.12],
        'individualScore': 1,
        'teamScore': 0,
        'lightScore': .3,
        'loudnessScore': .6
    }
    desks[7] = {
        'location': [0.25, 0.12],
        'individualScore': 1,
        'teamScore': 0,
        'lightScore': .3,
        'loudnessScore': .6
    }
    desks[8] = {
        'location': [0.53, 0.1],
        'individualScore': 1,
        'teamScore': 0,
        'lightScore': .2,
        'loudnessScore': .3
    }
    desks[9] = {
        'location': [0.53, 0.17],
        'individualScore': 1,
        'teamScore': 0,
        'lightScore': .2,
        'loudnessScore': .3
    }
    desks[10] = {
        'location': [0.53, 0.25],
        'individualScore': 1,
        'teamScore': 0,
        'lightScore': .2,
        'loudnessScore': .3
    }
    desks[11] = {
        'location': [0.28, .35],
        'individualScore': 1,
        'teamScore': 0,
        'lightScore': .7,
        'loudnessScore': .5
    }
    desks[12] = {
        'location': [0.34, .35],
        'individualScore': 1,
        'teamScore': 0,
        'lightScore': .7,
        'loudnessScore': .5
    }
    desks[13] = {
        'location': [0.41, .35],
        'individualScore': 1,
        'teamScore': 0,
        'lightScore': .7,
        'loudnessScore': .5
    }
    desks[14] = {
        'location': [0.48, .31],
        'individualScore': 1,
        'teamScore': 0,
        'lightScore': .7,
        'loudnessScore': .6
    }
    desks[15] = {
        'location': [0.41, 0.27],
        'individualScore': 1,
        'teamScore': 0,
        'lightScore': .5,
        'loudnessScore': .5
    }
    desks[16] = {
        'location': [0.34, 0.27],
        'individualScore': 1,
        'teamScore': 0,
        'lightScore': .5,
        'loudnessScore': .5
    }
    desks[17] = {
        'location': [0.28, 0.27],
        'individualScore': 1,
        'teamScore': 0,
        'lightScore': .5,
        'loudnessScore': .5
    }
    desks[18] = {
        'location': [0.45, 0.44],
        'individualScore': 1,
        'teamScore': 0,
        'lightScore': .9,
        'loudnessScore': .7
    }
    desks[19] = {
        'location': [0.45, 0.51],
        'individualScore': 1,
        'teamScore': 0,
        'lightScore': .9,
        'loudnessScore': .7
    }
    desks[20] = {
        'location': [0.51, 0.51],
        'individualScore': 1,
        'teamScore': 0,
        'lightScore': .8,
        'loudnessScore': .8
    }
    desks[21] = {
        'location': [0.51, 0.44],
        'individualScore': 1,
        'teamScore': 0,
        'lightScore': .8,
        'loudnessScore': .8
    }
    desks[22] = {
        'location': [0.19, 0.92],
        'individualScore': -1,
        'teamScore': 0,
        'lightScore': .6,
        'loudnessScore': .5
    }
    desks[23] = {
        'location': [0.28, 0.92],
        'individualScore': -1,
        'teamScore': 0,
        'lightScore': .6,
        'loudnessScore': .5
    }
    desks[24] = {
        'location': [0.38, 0.92],
        'individualScore': -1,
        'teamScore': 0,
        'lightScore': .6,
        'loudnessScore': .4
    }
    desks[25] = {
        'location': [0.42, 0.85],
        'individualScore': -1,
        'teamScore': 0,
        'lightScore': .7,
        'loudnessScore': .4
    }
    desks[25] = {
        'location': [0.33, 0.85],
        'individualScore': -1,
        'teamScore': 0,
        'lightScore': .7,
        'loudnessScore': .5
    }
    desks[25] = {
        'location': [0.23, 0.85],
        'individualScore': -1,
        'teamScore': 0,
        'lightScore': .7,
        'loudnessScore': .5
    }
    desks[26] = {
        'location': [0.58, 0.95],
        'individualScore': 1,
        'teamScore': 0,
        'lightScore': .3,
        'loudnessScore': .1
    }
    desks[27] = {
        'location': [0.58, 0.90],
        'individualScore': 1,
        'teamScore': 0,
        'lightScore': .3,
        'loudnessScore': .2
    }
    desks[28] = {
        'location': [0.58, 0.85],
        'individualScore': 1,
        'teamScore': 0,
        'lightScore': .3,
        'loudnessScore': .3
    }
    desks[29] = {
        'location': [0.58, 0.80],
        'individualScore': 1,
        'teamScore': 0,
        'lightScore': .3,
        'loudnessScore': .4
    }
    return [employees, desks];