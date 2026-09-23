+####TUPLE###
YOU CAN IDENTIFY TUPLE BY PARANTHESIS().
TUPLE()
####COMMA IS MANDATORY IF WE MISS THEN IT CONSIDER AS WHAT TYPE OF DATA WE PASSED)
TUPLE IS OREDERD DATA TYPE.(THAT MEANS SEQUENCE CANT CHANGE).
IT ACCEPT DUPLICATE ELEMENTS.
TUPLE IS IMMUTABLE IN NATURE.
IN TUPLE DATA TYPE BOUNDRY CONDITION IS NOT MANDATORY.BUT COMMA IS COMPULSORY.
IN TUPLE DATA TYPE EACH ELEMENT IS SEPARATED BY COMMA.
TUPLE IS COMBINATION OF HOMOGENOUS AND HETEROGENEOUS ELEMENT.
HOMOGENEOUS=SAME TYPE OF DATA.
EX.X=(1,2,3,4)
HETEROGENEOUS=DIFFERENT TYPE OF DATA.
EX.X=(11,12,True,"$")

####HOW TO CREATE EMPTY TUPLE###
   1. A=()
    type(A)
    <class 'tuple'>
   2. a=tuple()
    type(a)
    <class 'tuple'>
##in tuple data type there are only two methods.
    1.count() 2.index()
    dir(tuple) to know how many methods are present in tuple.
####tuple is immutable because we cant change the original object.
    s=(10,20,"hello",[1,2,3])
    s[2]
    'hello'
    s[2].upper()
    'HELLO'
     s
###(10, 20, 'hello', [1, 2, 3])here the original object has not change.
TO DO MODIFICATION IN TUPLE WE TAKE HELP OF LIST .WE HAVE TO PASS HETEROGENEOUS
ELEMENT THE WE CAN PERFORM OPERATIONS.
t=(34,["abc","walmart","python"],600,{67,909})
t[1]
['abc', 'walmart', 'python']
t[1][1]
'walmart'
t[1][1]=100
a  
E=(100,67,"abc","python","walmart","instagram")
E[-3]
E




