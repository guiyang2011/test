if x is None:
    print x

if x is not None:
    print x

if not x:
    print 'not found'

urlsInList = ['microsoft.com', 'microsoft.cn']

urlsInSet = {'microsoft.com', 'microsoft.cn'} # set is faster than list

url = 'microsoft.com'
url in urlsInList  # returns true

word = "Python"
letter = 't'
letter in word # returns true

if url in urls:
    print('this url is taken')

all(urlsInSet) # test if all values are true

any(urlsInSet) # test if any of the values is true

# for is effectively foreach
for i in [0,1,2,3,4,5,6,7]:
    print i

for i in range(8):
    print i

# loop through characters in word
word = 'Python'
for letter in word:
    print letter

# over lines in file
with open('file.ext') as file:
    for line in file:
        print repr(line)

# over stream of all regex matches
for match in re.finditer(pattern, string):
    if match:
        print (match.string)

# over files and directories
for root, dirs, files in os.walk("d:\temp"):
    print dirs

# over infinite stream of numbers
for num in itertools.count():
    if num%2 == 0:
        print (num)

# loop if need indices
for i, url in enumerate(urls):
    print (i, ':', url)

people = ['dcramer', 'iulianm', 'giacomo', 'rafaelgu', 'talpa', 'katynski', 'zahariao']
tasks = ['Drills',  'SEA SE10',  'DUB Ops meeting',  'StandUps reporting',  'StandUps',  'DevSup-TOS Collaboration']
# just use zip(), which creates list of tuples containing i-th elements
for person, task in zip(people, tasks):
    print(person, ' is the new owner of ', task)

# as it was the case with xrange(), zip() has iterator version too - izip() - it consumes less memory and is faster
for  person, task in izip(people, tasks):
    print person, 'is the new owner of', task

for entry in sorted(urlsInList):
    print (entry)

# loop in sorted but reversed order
for person in sorted(ticket.work_log, reverse=True):
    print entry

def find(seq, target):
    for i, value in enumerate(seq):
        if value == target
             break
    else: # no_break
        return -1
    return i

def find(seq, target):
    # None is more pythonic than -1 for 'not found'
    found = None
    for i, value in enumerate(seq):
        if value == target
             found = i
             break
    return found

def evens(stream):
    result = []
    for y in stream:
        if y % 2 == 0:
            result.append(y)
    return result

def evens(stream):
    result = [y for y in stream if not y%2]
    return result

# and use it like below
for x in evens(nums):
    do_something()

# the function defined above can be generator (generators are lazy):
def evens(stream):
    for y in stream:
        if y % 2 == 0:
            yield y

# abstract and generate
def interesting_lines(file):
    for line in file:
        line = line.strip()
        if line.startswith('#'):
            continue
        if not line:
            continue
        yield line

with open('config.ini') as file:
    for line in interesting_lines(file):
        do_something(line)

def square(x):
    return x**2

lambda x:x**2

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print filter(lambda x: x % 3 == 0, foo)
#returns [18, 9, 24, 12, 27]
 
print map(lambda x: x * 2 + 10, foo)
#returns [14, 46, 28, 54, 44, 58, 26, 34, 64]
 
print reduce(lambda x, y: x + y, foo)
#returns 139

def compare_length(work_log_1, work_log_2):
    if len(work_log_1) < len(work_log_2):
        return -1
    if len(work_log_1) > len(work_log_2):
        return 1
    return 0

print sorted(work_logs, cmp=compare_length)

print sorted(work_logs, cmp=lambda x, y: cmp(len(x), len(y))

print sorted(work_logs, key=len)

print sorted(work_logs, key=lambda log: log.start_date)

# using them is what separates the newbies from the pythonistas. Use iter() to make one from an object:
ipeople = iter(people)

blocks = []
    for block in iter(partial(f.read, 32), ''):
    blocks.append(block)

# x is a tuple
x = ('What', 'can', 'I', 'do', 'for', 'you', '?')
 
# unpack the tuple
(a, b, c, d, e, f, g) = x


# and even swapping works in atomic way:
e, f = f, e

# Fibonacci
x, y = 0, 1
x, y = y, x + y

# wlcm = ' '.join([a, b, c, d, e, f, g])
print wlcm

print ', '.join(urls)

choices = {'fqdn': 'polishmypython.com', 'port': 80, 'protocol': 'http'}
# because new line character is a string too:
string = '\n'.join("For {0} I choose {1}".format(k, v) for k, v in choices.iteritems())
print string

# use this, and forget about closing
with open('somefile.txt') as f:
    data = f.read()
# or:
with get_mysql_connection() as conn:
    conn.execute("SELECT * FROM users WHERE lunch LIKE "%whoopie pie%";)

# Decorators factor-out reusable logic

# because functions can: define functions, take functions as arguments, and return functions:
def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped
 
def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

# now we can use above as decorators:
@makebold
@makeitalic
def hello():
    return "hello world"
 
print hello()
#returns <b><i>hello world</i></b>

@exponential_backoff(retries=5)
def gimmie_my_ticket(ticket_id):
    return fluxo.getTicketById(ticket_id)
# definition of exponential_backoff decorator lives in BenderLibCore package as a class

#Comprehension
print sum([i**2 for i in xrange(10)])
# Generator
print sum(i**2 for i in xrange(10))

pinged = [ping_this_url(url) for url in urls if not_yet_pinged(url)]
# Comprehension can also create sets and dictionaries:
>>> {key:value for key,value in (('a',1),('b',2),('c',3))}
{'a': 1, 'c': 3, 'b': 2}
>>> {x*2 for x in range(10)}
set([0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

urls[start:end] # items start through end-1
urls[start:]    # items start through the rest of the array
urls[:end]      # items from the beginning through end-1
urls[:]         # a copy of the whole array
urls[-1]    	# last item in the array
urls[-2:]   	# last two items in the array
urls[:-2]   	# everything except the last two items

choices = {'fqdn': 'polishmypython.com', 'port': '80', 'protocol': 'http'}
# by default you get keys:
for k in d:
    print k

# if you are messing with live dictionary you better use its copy:
for k in d.keys():       # creates a list of dictionary keys in background
    if k.startswith('p'):
        del d[k] * mutation

for k, v in d.items():
    print k, '-->', v

# make dictionary out of two lists:
keys = ['fqdn', 'protocol', 'port']
values = ['polishmypython.com', 'http', '80']
# use itertools.izip() - iterator version of zip() and make dictionary ouf of it:
d = dict(izip(keys, values)) # lives in _itertools_ module
# remember enumerate? it returns "enumerate" object, which you can turn to dictionary the same way:
d = dict(enumerate(values))
 
# returns:
{0: 'polish-my-python.amazon.com', 1: 'http', 2: '80'}

and now using get() - yes, second parameter is a default value used if first isn't found
d = {}
for host in ticketing_hosts:
    d[host] = d.get(host, 0) + 1     #get, if not, use default, increment
# you could use defaultdict factory from collections module
# it because it _defaults_ to zero (don't you know)
d = defaultdict(int)
for host in ticketing_hosts:
    d[host] += 1
 
# returns:
defaultdict(<type 'int'>, {'hostname123': 1, 'hostname234': 2, 'hostname234': 3})
 
# needs conversion for some use cases:
dict(d)

xens = ['xen1.iad.blah', 'xen2.dub.blah', 'xen3.dub.blah', 'xen4.pdx.blah', 'xen5.pdx.blah', 'xen6.pdx.blah']
d = {}
for xen in xens:
    key = xen[5:8]
    d.setdefault(key, []).append(xen)    #checks, defaults, appends

d = defaultdict(list)
for xen in xens:
    key = xen[5:8]
    d[key].append(xen)

# all above return:
{'dub': ['xen2.dub.blah', 'xen3.dub.blah'], 
 'iad': ['xen1.iad.blah'],
 'pdx': ['xen4.pdx.blah', 'xen5.pdx.blah', 'xen6.pdx.blah']}

 dupes = [1,2,3,4,5,1,2,3,1,2]
set(dupes)
# returns: set([1, 2, 3, 4, 5])

s1 = set([1,2,3,4,5])
s2 = set([4,5,6,7,8])
intersection:
s1 & s2
# returns: set([4, 5])
union:
s1 | s2
# returns: set([1,2,3,4,5,6,7,8])
sets also have a comprehension in >2.7. Just think of them as a key-only dict:
subnets = {ip.rsplit('.', 1)[0] for ip in ['1.1.1.1', '1.1.2.1', '1.1.1.2', '1.3.1.2', '1.3.1.1']}
# returns: set(['1.1.1', '1.1.2', '1.3.1'])

import unittest
import mymodule
 
class TestSomething(unittest.TestCase):
 
    def setUp(self):
        # instantiate, build mocks etc.
        self.x = mymodule.myClass()
 
    def tearDown(self):
        # close resources, restore mocks etc.
 
    def test_method_with_valid_inputs(self):
        result = self.x.add(5, 6)
        self.assertEqual(result, 11)
 
if __name__ == '__main__':
    unittest.main(verbosity=2)

import mymodule
import nose
from nose.tools import *
 
def setup_func():
    # mocks and stuff
 
def teardown_func():
    # kill mocks etc.
 
# this decorates function with contents of setup() and teardown() functions
@with_setup(setup_func, teardown_func) 
def test_some_class_functionality():
    x = myClass()
    result = x.add(5, 6)
    assert result == 11
 
# this is optional as nose will discover tests
if __name__ == '__main__':
    nose.main()

import mymodule
import py.test
 
def test_some_method_fails():
    py.test.raises(ValueError, my_method, 'arguments')
 
def test_some_method_fails():
    with py.test.raises(ValueError):
        my_method('arguments')
 
def test_sonme_method_succeed():
    assert my_method('argument') == 42
 
    result = my_method('xxx')
    assert hasattr(result, 'yyy')

import unittest
import mock
import yourmodule
 
class TestWithMock(unittest.TestCase):
 
    # this setup method preserves through the whole class - pretty useful, but use with care
    def setUp(self):
 
        # we need to replace class of FluxoClient used in yourmodule with a Mock. We use patch
        # here so that the change to your module can be undone at the end of the test (as tests
        # should always be isolated from each other
        patcher = mock.patch('yourmodule.fluxo.FluxoClient')
        mock_fluxo_class = patcher.start()
 
        # Use a unittest feature to clean up after ourselves -- this is in Python 2.7+/3.2+ and 
        # the unittest2 module for earlier Pythons. Pytest has request.addfinalizer to do the
        # same thing.
        self.addCleanup(patcher.stop)
 
        # return value of class it its instance
        self.mock_fluxo = mock_fluxo_class.return_value
 
        # now let's mock a method of our mocked instance, and its return value (yes, the ticket can be mocked too)
        self.mock_fluxo.getTicketById.return_value = mock_ticket
 
        # now, let's create an instance of yourmodule (the one that uses external library - Fluxo, that we mocked already)
        self.yourObject = yourmodule.yourClass()
 
    # here we finally check if your method is using the external library method like it should
    def test_your_method_calls_fluxo_correctly(self):
        self.yourObject.your_method('123')
        self.mock_fluxo.getTicketById.assert_called_once_with('123')

