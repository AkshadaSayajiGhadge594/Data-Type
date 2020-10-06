print("---------Demonstration of Data Type----------");

no=None;
print(no);
print(type(no));
print(id(no));
print("")

no=11;
print(no);
print(type(no));
print(id(no));
print("");

# Numeric data type contain different subtype as int,float,boolean,complex
no=11
print(no)
print(type(no));

no=3.14
print(no)
print(type(no));

no=6+3j;
print(no);
print(type(no));

no=True	
print(no)		# in python boolean Value is True And False
print(type(no));
print("")

#we can convert variable from one data type to another data type (typecasting)
print("Typecasting :")
no=11;
no=float(no);
print(no);

print(type(no))
print(id(no))
print("")

a=5;
b=6;
no=complex(a,b);
print(no);
print(type(no));
print(id(no));
print("")

## SEQUENCE there are different data type List,tuple,set,String,Range
print("sequence data type =>")

ListEx=[10,20,30,40];
print(ListEx);
print(type(ListEx));

SetEx={10,20,30,40};
print(SetEx);
print(type(SetEx));

TupleEx=(10,20,30,40);
print(TupleEx);
print(type(TupleEx));

name="Akshada"
print(name);
print(type(name));
print("");

ex=list(range(1,10))
print(ex)
print(type(ex))
print("")

ex=list(range(10))
print(ex)
print(type(ex))
print("")

ex=list(range(1,20,2))
print(ex)
print(type(ex))
print("")

# Dictionary contain Keys and values
print("DICTIONARY =>")
languages={"C":"Richie","C++":"Strostrup","Java":"Gosling","Python":"Rossum"}
print(languages);
print(type(languages));
print("")

print(languages.keys());

print(languages.values());

print(languages["Python"])

