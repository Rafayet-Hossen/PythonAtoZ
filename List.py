#            0          1       2     3
people = ['Rafayet','Sojib','Bithy','Mike']
#this will give me Bithy because list index starts form 0
print(people[2])
people.append('Jim')

#list slicing
#line 9 and line 10 code are return same output one is positive and other with negative index
print(people[2:4])
print(people[-3:-1])

print(people.count('Rafayet'))
for person in people:
    print(person)

