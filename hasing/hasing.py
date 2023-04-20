class ProbHash:
    def __init__(self, cap):
        self.hashtable = cap * [None]
        self.n = cap

    def hash(self, mykey):
        return mykey%self.n
    
    def rehash(self, hashkey):
        pos1 = self.hash(hashkey)
        while self.hashtable[pos1] != None:
            pos1 += 1
        return pos1
    
    def insertData(self, student_obj):
        result = self.rehash(student_obj.id)
        print("Insert", student_obj.id, "at index", result)
        self.hashtable[result] = student_obj
        
    def searchData(self, key):
        for i in self.hashtable:
            if i != None and i.id == key:
                print("Found", key, "at index", self.hashtable.index(i))
                return self.hashtable[self.hashtable.index(i)]
        print(key, "does not exist.")


class Student:
    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa

    def getId(self):
        return self.id
    
    def getName(self):
        return self.name

    def getGpa(self):
        return self.gpa

    def printDetails(self):
        print("ID:", self.id, "\nName:", self.name, "\nGPA:", self.gpa)

s1 = Student(65070001, "Sandee Boonmak", 3.05)
s2 = Student(65070077, "Somsak Jaidee", 2.78)
s3 = Student(65070021, "Somsri Jaiyai", 3.44)
s4 = Student(65070042, "Sommai Meeboon", 2.89)
myHash = ProbHash(20)
myHash.insertData(s1)
myHash.insertData(s2)
myHash.insertData(s3)
myHash.insertData(s4)
print("-------------------------")
myHash.searchData(65070077).printDetails()
print("-------------------------")
myHash.searchData(65070021).printDetails()
print("-------------------------")
myHash.searchData(65070042).printDetails()
print("-------------------------")
myHash.searchData(65070032)
print("-------------------------")