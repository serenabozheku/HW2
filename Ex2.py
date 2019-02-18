from statistics import mean
st_dict = {
    'dict_one': {
        'name': 'Serena Bozheku',
        'grades': [99.94, 95.00, 79.58, 85.50, 97.79] 
        },
    'dict_two': {
        'name': 'Iris Dyrmishi',
        'grades': [98.35, 76.30, 71.43, 94.43, 68.98]
    },
    'dict_three': {
        'name':'Fami Fatmusha',
        'grades': [67.98, 76.76, 45.32, 75.87, 100.00]
    }
}

for st in st_dict:
    print(st_dict[st]['name'],' has an average grade of {}'.format(mean(st_dict[st]['grades'])))
