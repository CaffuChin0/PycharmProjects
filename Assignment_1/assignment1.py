"""
Replace the contents of this module docstring with your own details
Name: Hsu Ming-wei
Date started:11/8/2020
GitHub URL: https://github.com/JCUS-CP1404/assignment-1-travel-tracker-CaffuChin0
"""

class Elem:
    def __init__(self, name, country, priority, visited):
        self.name = name
        self.country = country
        self.priority = priority
        self.visited = visited

    def __repr__(self):
        return f"{self.name}\t in {self.country}\t priority {self.priority}"

    def to_raw(self):
        return f'{self.name},{self.country},{self.priority},{"v" if self.visited else "n"}\n'


def get_input(items):
    ans = input(f'{items}: ').strip()
    while len(ans) == 0:
        print('Input can not be blank')
        ans = input(f'{items}: ').strip()
    return ans


def get_priority(items):
    ans = input(f'{items}: ').strip()
    while True:
        if len(ans) == 0:
            print('Invalid input; enter a valid number')
        elif int(ans) <= 0:
            print('Number must be > 0')
        else:
            break
        ans = input(f'{items}: ').strip()
    return int(ans)


def main():
    print("Travel Tracker 1.0 - by name")

    data = get_data('places.csv')
    print(f'{len(data)} places loaded from places.csv')
    while True:
        choosemenu = menu()
        if choosemenu == "l":
            show_data(data)
        elif choosemenu == "a":
            name = get_input('Name')
            country = get_input('Country')
            priority = get_priority('Priority')
            visited = False
            d = Elem(name, country, priority, visited)
            data.insert(0, d)
            print(f'{d.name} in {d.country} (priority {d.priority}) added to Travel Tracker')
        elif choosemenu == 'm':
            show_data(data)
            print('Enter the number of a place to mark as visited')

            def get_place():
                places = input()
                while True:
                    if not places.isdigit():
                        print('Invalid input; enter a valid number')
                    elif int(places) <= 0:
                        print('Number must be > 0')
                    elif int(places) > len(data):
                        print('Invalid place number')
                    else:
                        break
                    places = input()
                return int(places)

            places = get_place()
            if data[places - 1].visited:
                print('That place is already visited')
            else:
                print(f'{data[places - 1].name} in {data[places - 1].country} visited!')
                data[places - 1].visited = True
        elif choosemenu == 'q':
            save_data(data,save_path='places.csv')
            print(f'{len(data)} places saved to places.csv')
            print('Have a nice day :)')
            break
        else:
            print('Invalid menu choice')


def show_data(data):
    not_visited = 0
    for index, d in enumerate(data):
        if not d.visited:
            print('*', end='')
            not_visited += 1
        print(f'{index + 1}. {d}')
    print(
        (f'{len(data)} places. ') + (
            'No places left to visit. Why not add a new place?' if not_visited == 0 else f'You still want to visit {not_visited} places.'))


def menu():
    print("Menu:")
    print("L - List places")
    print("A - Add new place")
    print("M - Mark a place as visited")
    print("Q - Quit")
    choice = input().lower()
    return choice


def get_data(filename):
    ans = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if len(line):
                name, country, priority, visited = line.split(',')
                priority = int(priority)
                visited = (visited == 'v')
                ans.append(Elem(name, country, priority, visited))
    return ans


def save_data(data, save_path='places.csv'):
    with open(save_path, 'w') as f:
        for d in data:
            f.writelines(f'{d.to_raw()}')


if __name__ == '__main__':
    main()
