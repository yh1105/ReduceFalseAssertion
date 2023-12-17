
def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
    planet_names = ("Mercury", "Venus", "Earth", "Mars", "Jupyter", "Saturn", "Uranus", "Neptune")
    if planet1 not in planet_names or planet2 not in planet_names or planet1 == planet2:
        return ()
    planet1_index = planet_names.index(planet1)
    planet2_index = planet_names.index(planet2)
    if planet1_index < planet2_index:
        return (planet_names[planet1_index + 1: planet2_index])
    else:
        return (planet_names[planet2_index + 1 : planet1_index])
assert bf('Saturn', 'Neptune') == ('Uranus',)
assert bf('Venus', 'Earth') == ()
assert bf('Earth', 'Venus') == ()
assert bf('Venus', 'Mars') == ('Earth',)
assert bf('Jupiter', 'Neptune') == ('Saturn', 'Uranus')
assert bf('', 'Mars') == ()
assert bf('Mercury', 'Jupiter') == ('Venus', 'Earth', 'Mars')
assert bf('Earth', 'Garbage') == ()
assert bf('Pluto', 'Saturn') == ()
assert bf('Venus', 'Venus') == ()
assert bf('neptune', 'mercury') == ()
assert bf('neptune', 'neptune') == ()
assert bf('pluto', 'earth') == ()
assert bf('Mercury', 'Mars') == ('Venus', 'Earth')
assert bf('Mercury', 'Mercury') == ()
assert bf('Zeus', 'Saturn') == ()
assert bf('Saturn', 'Zeus') == ()
assert bf('Pluto', 'Neptune') == ()
assert bf('Neptune', 'Pluto') == ()
assert bf('Neptune', 'Mercury') == ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus')
assert bf('Earth', 'Jupiter') == ('Mars',)
assert bf('Earth', 'Mars') == ()
assert bf('Earth', 'Neptune') == ('Mars', 'Jupiter', 'Saturn', 'Uranus')
assert bf('Pluto', 'Pluto') == ()
assert bf('Ares', 'Pluto') == ()
assert bf('Pluto', 'Venus') == ()
assert bf('Mars', 'Mars') == ()
assert bf('Sun', 'Jupiter') == ()
assert bf('Venus', 'Mercury') == ()
assert bf('Venus', 'Neptune') == ('Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus')
assert bf('Earth', 'Earth') == ()
assert bf('', '') == ()
assert bf('Mars', 'Jupiter') == ()
assert bf('', 'Uranus') == ()
assert bf('Mercury', 'Vega') == ()
assert (bf('mars', 'venus') == ())
assert bf('Neptune', 'Neptune') == ()
assert bf('Mercury', 'Pluto') == ()
assert bf('Pluto', 'Mercury') == ()
assert bf('Jupiter', 'Jupiter') == ()
assert bf('Saturn', 'Jupiter') == ()
assert bf('Jupiter', 'Pluto') == ()
assert bf('Pluto', 'Mars') == ()
assert bf('Venus', 'Jupiter') == ('Earth', 'Mars')
assert bf('Pippo', 'Pluto') == ()
assert bf('Mars', 'Earth') == ()
assert bf('Uranus', 'Saturn') == ()
assert bf('Uranus', 'Uranus') == ()
assert bf('Mercury', 'Venus') == ()
assert bf('earth', 'Mercury') == ()
assert bf('Neptune', 'Saturn') == ('Uranus',)
assert bf('Earth', 'not a planet') == ()
assert bf('not a planet', 'Earth') == ()
assert bf('not a planet', 'not a planet') == ()
assert bf('Jupiter', 'Uranus') == ('Saturn',)
assert bf('Jupiter', 'Saturn') == ()
assert bf('Earths', 'Mars') == ()
assert bf('Neptune', '') == ()
assert bf('Mercury', 'Mercury') == tuple()
assert bf('Earth', 'Venus') == tuple()
assert bf('Jupiter', 'Sun') == ()
assert bf('Jupiter', 'EARTH') == ()
assert bf('Uranus', 'Mars') == ('Jupiter', 'Saturn')
assert bf('Mars', 'Neptune') == ('Jupiter', 'Saturn', 'Uranus')
assert bf('Mars', 'Uranus') == ('Jupiter', 'Saturn')
assert bf('Earth', 'Uranus') == ('Mars', 'Jupiter', 'Saturn')
assert bf('Earth', 'Jupiter') == ('Mars', )
assert bf('Jupiter', 'Uranus') == ('Saturn', )
assert bf('Saturn', 'Neptune') == ('Uranus', )
assert bf('Saturn', 'Pluto') == ()
assert bf('Mercury', 'Saturn') == ('Venus', 'Earth', 'Mars', 'Jupiter')
assert bf('mars', 'mars') == ()
assert bf('uranus', 'mars') == ()
assert bf('uranus', 'earth') == ()
assert bf('jupiter', 'earth') == ()
assert bf('Uranus', 'Jupiter') == ('Saturn',)
assert bf('Pluto', 'Jupiter') == ()
assert bf('Pluto', 'Sun') == ()
assert bf('Sun', 'Pluto') == ()
assert bf('Mercury', 'Neptune') == ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus')
assert bf('earth', 'mercury') == ()
assert bf('pluto', 'Mars') == ()
assert bf('Earth', 'Earth') == (), 'Wrong Answer'
assert bf('Mars', 'Saturn') == ('Jupiter',), 'Wrong Answer'
assert bf('Earth', 'Mars') == (), 'Wrong Answer'
assert bf('Mars', 'Earth') == (), 'Wrong Answer'
assert bf('Jupiter', 'Saturn') == (), 'Wrong Answer'
assert bf('Mercury', 'Jupiter') == ('Venus', 'Earth', 'Mars'), 'Wrong Answer'
assert bf('', 'Mercury') == (), 'Wrong Answer'
assert bf('Mars', '') == (), 'Wrong Answer'
assert bf('Sun', 'Earth') == ()
assert bf('Jupiter', 'Mars') == ()
assert bf('Earth', 'Luna') == ()
assert bf('Luna', 'Venus') == ()
assert bf('Venus', 'Pluto') == ()
assert bf('Foo', 'Pluto') == ()
assert bf('Earth', 'Pluto') == ()
assert bf('Saturn', 'Saturn') == ()
assert bf('Saturn', 'pluto') == ()
assert bf(' ', ' ') == ()
assert bf('mars', 'venus') == ()
assert bf('Jupiter', 'Uranus') == ('Saturn',), 'Test 2'
assert bf('Jupiter', 'Mars') == (), 'Test 3'
assert bf('Mercury', 'Earth') == ('Venus',), 'Test 4'
assert bf('Mars', 'Earth') == (), 'Test 6'
assert bf('', 'Uranus') == (), 'Test 7'
assert bf('Venus', '') == (), 'Test 8'
assert bf('', '') == (), 'Test 9'
assert bf('Eart', 'Saturn') == ()
assert bf('Earth', 'Satur') == ()
assert bf('XX', 'Mars') == ()
assert bf('Mars', 'XX') == ()
assert bf('Mars', '') == ()
assert bf(1, 'Mars') == ()
assert bf('Mars', 1) == ()
assert bf(1, 2) == ()
assert bf('Jupiter', 'Moon') == ()
assert bf('Jupiter', 'jupiter') == ()
assert bf('Mars', 'not a planet') == ()
assert bf('not a planet', 'Mars') == ()
assert bf('Mercury', 'Earth') == ('Venus',)
assert bf('Venus', 'Saturn') == ('Earth', 'Mars', 'Jupiter')
assert bf('Asteroid', 'Mars') == ()
assert bf('Mercury', 'Uranus') == ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn')
assert bf('', 'Venus') == ()
assert bf('Venus', '') == ()
assert bf('Neptune', 'Uranus') == tuple()
assert bf('Neptune', 'xxxx') == tuple()
assert bf('xxxx', 'Neptune') == tuple()
assert bf('Unknown', 'Earth') == ()
assert bf('Earth', 'Unknown') == ()
assert bf('haha', 'haha') == ()
assert bf('Krypton', 'Uranus') == ()
assert bf('Uranus', 'Krypton') == ()
assert bf('X', 'Y') == ()
assert bf('Earth', 'earth') == ()
assert bf('Venus', 'A') == ()
assert bf('A', 'Venus') == ()
assert bf('A', 'B') == ()
assert bf('A', 'A') == ()
assert bf('Uranus', 'Neptune') == ()
assert bf('Earth', 'Mercury') == ('Venus',)
assert bf('', 'Neptune') == ()
assert bf('bla', 'Neptune') == ()
assert bf('Earth', 'bla') == ()
assert bf('bla', 'bla') == ()
assert bf('Q', 'Earth') == ()
assert bf('Pluto', 'Earth') == ()
assert bf('planet1', 'planet2') == ()
