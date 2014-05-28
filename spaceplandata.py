## Data for the Space Planning Algorithm
def data():
    employees = {};
    employees[0] = {'preferences': [1, .5, -.25], 'name': 'Nick'}
    employees[1] = {'preferences': [1, .4, -1], 'name': 'Jen'}
    employees[2] = {'preferences': [-1, .5, -1], 'name': 'Michelle'}
    employees[3] = {'preferences': [1, 0, -1], 'name': 'Fritz'}
    employees[4] = {'preferences': [1, -1, -.75], 'name': 'Freddie'}
    employees[5] = {'preferences': [1, .9, 0], 'name': 'Augusto'}
    employees[6] = {'preferences': [1, .5, -1], 'name': 'Marc'}
    employees[7] = {'preferences': [1, .4, 0], 'name': 'Owen'}
    employees[8] = {'preferences': [1, 1, -1], 'name': 'Vivian'}
    employees[9] = {'preferences': [1, .6, -.5], 'name': 'Scott'}
    employees[10] = {'preferences': [1, 1, 0], 'name': 'Julia'}
    employees[11] = {'preferences': [1, .5, -.5], 'name': 'Alex'}
    employees[12] = {'preferences': [1, .5, -.5], 'name': 'Ryan'}
    employees[13] = {'preferences': [1, 1, -1], 'name': 'Tom'}
    employees[14] = {'preferences': [1, .8, -.1], 'name': 'Rohan'}
    employees[15] = {'preferences': [1, .75, 0.75], 'name': 'Sam'}
    employees[16] = {'preferences': [-1, .5, 0], 'name': 'Connie'}
    employees[17] = {'preferences': [-1, .5, 0], 'name': 'Katherine'}
    employees[18] = {'preferences': [1, 1, 0], 'name': 'Jocelyn'}

    desks = {}
    desks[0] = {
        'location': [0.2, 0.15],
        'individualScore': 1,
        'lightScore': .3,
        'loudnessScore': .7
    }
    desks[1] = {
        'location': [0.25, 0.19],
        'individualScore': 1,
        'lightScore': .3,
        'loudnessScore': .6
    }
    desks[2] = {
        'location': [0.32, 0.19],
        'individualScore': 1,
        'lightScore': .3,
        'loudnessScore': .6
    }
    desks[3] = {
        'location': [0.38, 0.19],
        'individualScore': 1,
        'lightScore': .3,
        'loudnessScore': .5
    }
    desks[4] = {
        'location': [0.45, 0.15],
        'individualScore': 1,
        'lightScore': .3,
        'loudnessScore': .4
    }
    desks[5] = {
        'location': [0.38, 0.12],
        'individualScore': 1,
        'lightScore': .3,
        'loudnessScore': .5
    }
    desks[6] = {
        'location': [0.32, 0.12],
        'individualScore': 1,
        'lightScore': .3,
        'loudnessScore': .6
    }
    desks[7] = {
        'location': [0.25, 0.12],
        'individualScore': 1,
        'lightScore': .3,
        'loudnessScore': .6
    }
    desks[8] = {
        'location': [0.53, 0.1],
        'individualScore': 1,
        'lightScore': .2,
        'loudnessScore': .3
    }
    desks[9] = {
        'location': [0.53, 0.17],
        'individualScore': 1,
        'lightScore': .2,
        'loudnessScore': .3
    }
    desks[10] = {
        'location': [0.53, 0.25],
        'individualScore': 1,
        'lightScore': .2,
        'loudnessScore': .3
    }
    desks[11] = {
        'location': [0.28, .35],
        'individualScore': 1,
        'lightScore': .7,
        'loudnessScore': .5
    }
    desks[12] = {
        'location': [0.34, .35],
        'individualScore': 1,
        'lightScore': .7,
        'loudnessScore': .5
    }
    desks[13] = {
        'location': [0.41, .35],
        'individualScore': 1,
        'lightScore': .7,
        'loudnessScore': .5
    }
    desks[14] = {
        'location': [0.48, .31],
        'individualScore': 1,
        'lightScore': .7,
        'loudnessScore': .6
    }
    desks[15] = {
        'location': [0.41, 0.27],
        'individualScore': 1,
        'lightScore': .5,
        'loudnessScore': .5
    }
    desks[16] = {
        'location': [0.34, 0.27],
        'individualScore': 1,
        'lightScore': .5,
        'loudnessScore': .5
    }
    desks[17] = {
        'location': [0.28, 0.27],
        'individualScore': 1,
        'lightScore': .5,
        'loudnessScore': .5
    }
    desks[18] = {
        'location': [0.45, 0.44],
        'individualScore': 1,
        'lightScore': .9,
        'loudnessScore': .7
    }
    desks[19] = {
        'location': [0.45, 0.51],
        'individualScore': 1,
        'lightScore': .9,
        'loudnessScore': .7
    }
    desks[20] = {
        'location': [0.51, 0.51],
        'individualScore': 1,
        'lightScore': .8,
        'loudnessScore': .8
    }
    desks[21] = {
        'location': [0.51, 0.44],
        'individualScore': 1,
        'lightScore': .8,
        'loudnessScore': .8
    }
    desks[22] = {
        'location': [0.19, 0.92],
        'individualScore': -1,
        'lightScore': .6,
        'loudnessScore': .5
    }
    desks[23] = {
        'location': [0.28, 0.92],
        'individualScore': -1,
        'lightScore': .6,
        'loudnessScore': .5
    }
    desks[24] = {
        'location': [0.38, 0.92],
        'individualScore': -1,
        'lightScore': .6,
        'loudnessScore': .4
    }
    desks[25] = {
        'location': [0.42, 0.85],
        'individualScore': -1,
        'lightScore': .7,
        'loudnessScore': .4
    }
    desks[26] = {
        'location': [0.33, 0.85],
        'individualScore': -1,
        'lightScore': .7,
        'loudnessScore': .5
    }
    desks[27] = {
        'location': [0.23, 0.85],
        'individualScore': -1,
        'lightScore': .7,
        'loudnessScore': .5
    }
    desks[28] = {
        'location': [0.58, 0.95],
        'individualScore': 1,
        'lightScore': .7,
        'loudnessScore': .1
    }
    desks[29] = {
        'location': [0.58, 0.90],
        'individualScore': 1,
        'lightScore': .7,
        'loudnessScore': .2
    }
    desks[30] = {
        'location': [0.58, 0.85],
        'individualScore': 1,
        'lightScore': .3,
        'loudnessScore': .3
    }
    desks[31] = {
        'location': [0.58, 0.80],
        'individualScore': 1,
        'lightScore': .3,
        'loudnessScore': .4
    }
    return [employees, desks];