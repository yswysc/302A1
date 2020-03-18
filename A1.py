#A1Q1#

def calculate(a,b):
    print(a+b, a-b, a*b, a/b, a**b, a%b)

#END A1Q1#

#A1Q2#

def sumHypotenuses(triangles):
    '''
	# Your code goes here
    n = 0
    for i in triangles:
        n += (i[0]**2 + i[1]**2)**0.5
    return n
	'''
	return sum((t[0]**2+t[1]**2)**0.5 for t in triangles)

#END A1Q2#

#A1Q3#

def charmSnakes(charm_ratings, time_for_charming):
    for i in charm_ratings:
        n, a, b = 0, 0, 1
        while n < i:
            a, b = b, a+b
            n+=1
        if a > time_for_charming:
            print("Failed to charm the snakes...")
            return
    print("Successfully charmed the snakes!")

#END A1Q3#

#A1Q4#

class Person():
    def __init__(self, name, age, height, weight, gender):
        if not isinstance(age, int):
            raise TypeError('Age must be an int')
        if not isinstance(height, float):
            raise TypeError('Height must be a float')
        if not isinstance(weight, float):
            raise TypeError('Weight must be a float')
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender
        self.initials = name[0] + '.' + name[name.rfind(' ')+1]

class Manager(Person):
    def __init__(self, name, age, height, weight, gender):
        Person.__init__(self, name, age, height, weight, gender)
        self.employees = list()

    def addEmployee(self, Employee):
        self.employees.append(Employee)

class Employee(Person):
    def __init__(self, name, age, height, weight, gender):
        Person.__init__(self, name, age, height, weight, gender)
        self.manager = ""

    def setManager(self, Manager):
        self.manager = Manager.name

#END A1Q4#

#A1Q5#

def encode(msg):
    l_msg = list(msg)
    n = 0
    for i in l_msg:
        if (ord(i) >= 69 and ord(i) <= 90) or (ord(i) >= 101 and ord(i) <= 122):
            l_msg[n] = chr(ord(i) - 4)
        elif (ord(i) >= 65 and ord(i) <= 68) or (ord(i) >= 97 and ord(i) <= 100):
            l_msg[n] = chr(ord(i) + 22)
        n += 1
    msg = ''.join(l_msg)
    return msg

#END A1Q5#