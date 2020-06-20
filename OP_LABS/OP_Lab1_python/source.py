import os

dir = os.path.relpath('resources_folder')
files = ['premier_league1.csv', 'premier_league2.csv']


def add_teams_to_array(dir, files):
    teams_points = []
    for file in files:
        with open(f"{dir}/{file}") as f:
            first_line = True

            for line in f:
                if first_line:
                    first_line = False
                    continue

                array = line.split(',')
                team = [array[0], 0]

                for i in range(1, len(array)):
                    if array[i][0] > array[i][2]:
                        team[1] += 3
                    elif array[i][0] == array[i][2]:
                        team[1] += 1

                teams_points.append(team)
    return teams_points


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][1] < arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def writing_into_file(teams_points):
    with open('results.csv', 'w') as res:
        for team in teams_points:
            res.write(f"{team[0]},{team[1]}\n")

teams_points = add_teams_to_array(dir, files)
teams_points = bubble_sort(teams_points)
writing_into_file(teams_points)