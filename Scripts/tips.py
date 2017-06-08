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

