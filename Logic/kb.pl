start:-
    write("Hello World"),
    nl,
    write("This is my first KB"),
    nl.

cls :- write("\33\[2J").

female("Mary").
female("Sandra").
female("Juliet").
female("Lisa").
male("Peter").
male("Bob").
male("Paul").
male("Drew").

/*parent of Y is X*/
parent("Bob", "Mary"). 
parent("Bob", "Peter").
parent("Juliet", "Drew").
parent("Juliet", "Paul").
parent("Peter", "Lisa").

father(X,Y):- male(Y), parent(X,Y), /*male Y AND parent of Y is X*/
    write("A father is a male parent").
mother(X,Y):- female(Y), parent(X,Y), /*female Y AND parent of Y is X*/
    write("A mother is a female parent").

get_grandchild(X):- /*parent of Y is X AND parent of Z is Y, therefore Z is grandchild of X*/
    parent(Y,X),
    parent(Z,Y),
    format("~w is grandchild of ~w.~n", [Z,X]).
