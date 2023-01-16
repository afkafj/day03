# univ = 'inha university'
# print(univ.split('i'))
#
#
# print(univ[5:])
# print(univ[5:15])
# print(univ[-10:])
# print(univ[::2])
# print(univ[-3:])
# print(univ[5:-6])
# print(univ[-10:-6])
#
# print(len(univ))
#
#
# pokemon = ['피카츄', '꼬부기', '이상해', '파이리']
# pokemons_string = '%'.join(pokemon)
# print(pokemons_string)
#
# inha = 'a duck goes into a sea'
# print(inha.replace('a ', 'a famous '))
#
# subjects = ' ! python, data structure, database     !!!'
# print(subjects.strip('!'))
#
#
# print(subjects.find('data'), subjects.index('data'))
# print(subjects.rfind('data'))
# print(subjects.rindex('data'))
# print(subjects.count('data'))
# print(subjects.title())


song= '"when an eel grabs your arm, and it causes great harm, That s a moray"'

# idx=song.rfind('m')
# song.replace(song[idx], song[idx].upper())
# print(song.endswith('moray!'))

song_list = song.split()
print(song_list)
song_list[14] = song_list[14].title()
song_string = ''.join(song_list)
print(song_string)


# index = song.rfind('m')
# print(idx, song[idx].upper())
