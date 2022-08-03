# 3-1
years_list = [1985, 1986, 1987, 1988, 1989, 1990]
# 3-2
years_list[3]
# 3-3
years_list[len(years_list) - 1] 
# 3-4
things = ['mozzarella', 'cinderella', 'salmonella']
# 3-5
things[0].title()
things[1].title()
things[2].title()
things
# 3-6
things[0].upper()
# 3-7
things.remove('salmonella')
things
# 3-8
surprise = ['Groucho', 'Chico', 'Harpo']
# 3-9
surprise[2] = surprise[2].lower()
surprise.sort(reverse=True)
surprise[0] = surprise[0].title()
# 3-10
e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
# 3-11
e2f.get('walrus')
# 3-12
f2e = {v: k for k, v in e2f.items()}
# 3-13
f2e['chien']
# 3-14
set(e2f.keys())
# 3-15
life = {
    'animals': {'cats': ['Henri', 'Grumpy', 'Lucy'], 'octopi': {}, 'emus': {}},
    'plants': {},
    'other': {}
}
# 3-16
life.keys()
# 3-17
life.get('animals').keys()
# 3-18
life.get('animals').get('cats')