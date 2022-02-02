

def save_dict(dictionary, name, path = ''):
    '''
    Save a dictionary as a csv file with name 'name'.
    Input:
        dictionary: (dict)
        name: (string) name of file to save
        path: (string) path which where the dictionary will be saved, default is '', in this case it will be save in current directory.
    Output:
        -
    '''
    import csv
    path_name = path +'/'+ name
    w = csv.writer(open(path_name + '.csv', "w"))
    for key, val in dictionary.items():
        w.writerow([key, val])
