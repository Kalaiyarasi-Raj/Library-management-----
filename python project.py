class library:
    def inputs(self):
        self.sno=int(input("Enter the S.no:"))
        self.name=str(input("Enter the name:"))
        self.author=str(input("Enter the author:"))
        self.quantity=int(input("Enter the quantity:"))
        self.input=[self.sno,self.name,self.author,self.quantity]

        
class management(library):
        def __init__(self):
            self.books=[]
            self.count=0
            self.borrowed_books=[]
            self.details=["s.no","Name","author",'quantity']
                
        def add(self,d):
            ii=1
            while(ii<=2):
                library.inputs(self)
                d={}
                for i,j in zip(self.details,self.input):
                    d[i]=j
                self.books.append(d)
                ii+=1
        def display(self):
            print(self.books)
        def filter(self,a):
            a=int(input("Enter_Sno: "))
            for i in self.books:
                if a == i["s.no"]:
                    print(i)
        def barrow(self,b):
            b=int(input("Enter_Sno: "))
            for i in self.books:
                if b == i["s.no"]:
                        no=int(input("No of Books: "))
                        if no>0 and no<=i["quantity"]:
                            i["quantity"]=i["quantity"]-no
                            print(i)
                
                            
                        

s=management()
c=1
a=0
b=0
while c!=0:
    c=int(input("Enter the number to 1 to Add or 2 to Display or 3 to Filter or 4 to Borrow: "))
    if c == 1:
        s1=library
        s.add(s1)
    elif c == 2:
        s.display()
    elif c == 3:
        s.filter(a)
    elif c == 4:
        s.barrow(b)
          
          



