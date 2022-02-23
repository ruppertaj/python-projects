'''
alien_0 = {'x_pos': 0, 'y_pos': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_pos']}")

#Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This is the fast alien
    x_increment = 3

# The new postion is the old position plus the increment
alien_0['x_pos'] = alien_0['x_pos'] + x_increment

print(f"New postion: {alien_0['x_pos']}")
'''

'''
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
'''

aliens = []

#Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

#show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")



