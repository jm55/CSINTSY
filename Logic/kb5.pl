say_hi :-
	loop(start).
	
loop(stop) :- 
	write("Goodbye!").
	
loop(X) :-
	write('What is your name? '),
	read(Name), nl,
	format('Hi, ~w!~n', [Name]),
	loop(Name).