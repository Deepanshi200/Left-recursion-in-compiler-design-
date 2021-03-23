#Removal of  Left-recursion-in-compiler-design-
Program to find left recursion in compiler design 
Please use | symbol to separate the production rules
The production rules separated with "|" are considered as one whole so please enter the number of productions according

SAMPLE INPUT 

Enter the NUMBER productions 2
A=ABd|Aa|a
B=Be|b


SAMPLE OUTPUT
****#######*******************************
LEFT RECURSION IN: 
A=ABd
A=Aa
 
REMOVAL
A=aA'|
A'=BdA'|eps
A'=aA'|eps
 
****#######*******************************
LEFT RECURSION IN: 
B=Be
 
REMOVAL
B=bB'|
B'=eB'|eps
 
****#######*******************************
FINAL GRAMMAR
A=aA'|
A'=BdA'|eps
A'=aA'|eps
B=bB'|
B'=eB'|eps
Deepanshis-MacBook-Pro:desktop deepanshisrivastava$ 
