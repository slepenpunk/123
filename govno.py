#Programm "Who are your Daddy?"
couple = {'Мешок': ['Батя с говном', 'Дед с говном'], 'Слепень': ['Батя алкаш', 'Дед крутой чел']}
guess = None

while guess != '0':
    print(
        '''
        0 - Exit
        1 - View existing names
        2 - Find out a couple
        3 - Add couple
        4 - Change couple
        5 - Delete couple
        '''
    )
    guess = input('Your choice: ')
    if guess == '0':
        print('See you soon!')
        break
    elif guess == '1':
        for name in couple.keys():
            print(name)
    elif guess == '2':
        name = input('Enter a name to find out the relatives: ').capitalize()
        if name in couple:
            print('Relatives', name, '-', couple[name][0])
        else:
            print('There is no such name!')
    elif guess == '3':
        add_name = input('Enter a new name which you want to add: ').capitalize()
        if add_name not in couple:
            add_relatives = input('Enter relatives: ').capitalize()
            couple[add_name] = add_relatives
        else:
            print('Such a name already exists!')
    elif guess == '4':
        change_name = input('Enter name you want a change: ').capitalize()
        if change_name in couple:
            new_name = input('Enter new name: ')
            new_relative = input('Enter relative: ').capitalize()
            del couple[change_name]
            couple[new_name] = new_relative
        else:
            print('There is no such name!')
    elif guess == '5':
        del_couple = input('Enter name you want to delete: ').capitalize()
        if del_couple in couple:
            del couple[del_couple]
        else:
            print('There is no such couple!')
    elif guess == '6':
        second = input('Enter name to find out him grandfather: ').capitalize()
        if second in couple:
            print('Grandfather', second, 'is a -', couple[second][1])












