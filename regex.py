#!/usr/bin/env python
import re

pattern1 = 'ab(c|d|)$'
assert     re.match(pattern1, 'ab')
assert     re.match(pattern1, 'abc')
assert     re.match(pattern1, 'abd')
assert not re.match(pattern1, 'abcd')
assert not re.match(pattern1, 'abe')

regex1 = re.compile('''
    ab         # match "ab" characters
    (?P<optional_group>  # create "char" group, so that we can extract data
    (c|d|)        # match any character
    )          # end of group
    $          # match to the end the string
''', re.VERBOSE)

assert     regex1.match('ab').groupdict() == {'optional_group': ''}
assert     regex1.match('abc').groupdict() == {'optional_group': 'c'}
assert     regex1.match('abd').groupdict() == {'optional_group': 'd'}

pattern2='^\d{3}\D?\d{3}\D?\d{3}$'

assert     re.match(pattern2, '123 456 789')
assert     re.match(pattern2, '678 543 970')
assert     re.match(pattern2, '987654321')  # grouping digits is optional
assert     re.match(pattern2, '123-456-789')  # you can separate groups by space or dash (or not separate it at all)
assert not re.match(pattern2, '12 345 678') # there must be exactly 9 digits
assert not re.match(pattern2, '12345678')  
assert not re.match(pattern2, '1234567890')
assert not re.match(pattern2, '12 3456 789')  # grouping matters (3 digits in each group)

regex2 = re.compile('''
    ^ #from the start
    (?P<group1>  # create group, so that we can extract data
    \d{3}        # match 3 digits
    )          # end of group
    \D?          # optional non-digit
    (?P<group2>  # create group, so that we can extract data
    \d{3}        # match 3 digits
    )          # end of group
    \D?          # optional non-digit
    (?P<group3>  # create group, so that we can extract data
    \d{3}        # match 3 digits
    )          # end of group
    \D?          # optional non-digit
    $           #from end
''', re.VERBOSE)

assert     regex2.match('123 456 789').groupdict() == {'group1': '123', 'group2': '456', 'group3': '789'}
assert     regex2.match('987654321').groupdict() == {'group1': '987', 'group2': '654', 'group3': '321'}

pattern3='^(\+\d{1,2}\D?)?\d{3}\D?\d{3}\D?\d{3}$'

assert     re.match(pattern3, '123 456 789')
assert     re.match(pattern3, '678 543 970')
assert     re.match(pattern3, '123456789')
assert     re.match(pattern3, '123-456-789')
assert     re.match(pattern3, '+48 123 456 789')
assert     re.match(pattern3, '+48 123456789')
assert     re.match(pattern3, '+48123456789')
assert     re.match(pattern3, '+1 345 111 222')
assert not re.match(pattern3, ' 345 111 222')
assert not re.match(pattern3, '12 456 789')  # there must be exactly 9 digits (plus optional country prefix)
assert not re.match(pattern3, '12345678')
assert not re.match(pattern3, '1234567890')
assert not re.match(pattern3, '12 3456 789')  # grouping matters (3 digits in each group)
assert not re.match(pattern3, '+489 123 456 789')  # one or two digits allowed after plus
assert not re.match(pattern3, '48 123 456 789')  # if country prefix is present, it must be prepended by plus
assert not re.match(pattern3, '+123 456 789')  # if plus is present, country prefix is required


#pattern3='^(\+\d{1,2}\D?)?\d{3}\D?\d{3}\D?\d{3}$'

regex3 = re.compile('''
    ^ #from the start
    \+? #catch plus
    ( #group prefix
        (?P<prefix>\d{1,2})?  #catch prefix
    )
    \D?
    (?P<group1>  # create group, so that we can extract data
    \d{3}        # match 3 digits
    )          # end of group
    \D?          # optional non-digit
    (?P<group2>  # create group, so that we can extract data
    \d{3}        # match 3 digits
    )          # end of group
    \D?          # optional non-digit
    (?P<group3>  # create group, so that we can extract data
    \d{3}        # match 3 digits
    )          # end of group
    \D?          # optional non-digit
    $           #from end
''', re.VERBOSE)

assert     regex3.match('123456789').groupdict() == {'prefix': None, 'group1': '123', 'group2': '456', 'group3': '789'}
assert     regex3.match('+1 345 111 222').groupdict() == {'prefix': '1', 'group1': '345', 'group2': '111', 'group3': '222'}

pattern4='^[^@]+@{1}\w+\.{1}\w+$'

assert     re.match(pattern4, 'john@smith.com')
assert     re.match(pattern4, 'john.smith@gmail.com')
assert     re.match(pattern4, 'j.o.h.n@smith.com')
assert     re.match(pattern4, 'j.o.h.n+smith@smith.com')
assert     re.match(pattern4, 'j.o.h.n+smi+th@smith.com')
assert not re.match(pattern4, 'jo@hn@smith.com')
assert not re.match(pattern4, 'jo@hn@com')
assert not re.match(pattern4, 'jo@hn@sm.ith.com')

#pattern4='^[^@]+@{1}\w+\.{1}\w+$'
regex4 = re.compile('''
    ^ #from the start
    (?P<username>[^\+@]+
        \+*
        (?P<tag>[^@]+)?
        )
    @{1} # @
    (?P<host>
    (?P<subdomain>\w+)
    \.{1} #kropka
    (?P<domain>\w*))  #domain 
    $           #from end
''', re.VERBOSE)

#print regex4.match('john@smith.com').groupdict() 
assert     regex4.match('john@smith.com').groupdict() == {'username': 'john', 'tag': None, 'host': 'smith.com', 'domain': 'com', 'subdomain': 'smith'}
#print regex4.match('j.o.h.n+tag@smith.com').groupdict()
assert     regex4.match('j.o.h.n+tag@smith.com').groupdict() == {'username': 'j.o.h.n+tag', 'tag': 'tag', 'host': 'smith.com', 'domain': 'com', 'subdomain': 'smith'}
assert     regex4.match('j.o.h.n+ta+g@smith.com').groupdict() == {'username': 'j.o.h.n+ta+g', 'tag': 'ta+g', 'host': 'smith.com', 'domain': 'com', 'subdomain': 'smith'}

pattern5='^\D{3} (Jan|Oct|Dec|) [0-3][0-9] \d{2}:\d{2}:\d{2}$'

assert     re.match(pattern5, 'Sun Oct 14 13:47:03')
assert     re.match(pattern5, 'Mon Dec 14 13:47:03')
assert not re.match(pattern5, 'Sun Oct 14 13:47:3')
assert not re.match(pattern5, 'Sun Aaa 14 13:47:03')
assert not re.match(pattern5, 'Sun Oct 40 13:47:03')

regex5 = re.compile('''
    ^ #from the start
    (?P<day_of_week>\D{3})\ 
    (?P<month>(Jan|Oct|Dec|))\ 
    (?P<day>[0-3][0-9])\ 
    (?P<hour>\d{2}):
    (?P<minute>\d{2}):
    (?P<second>\d{2})
    $           #from end
''', re.VERBOSE)
assert     regex5.match('Sun Oct 14 13:47:03').groupdict() == {'day_of_week': 'Sun', 'month': 'Oct', 'day': '14', 'hour': '13', 'minute': '47', 'second': '03'}

