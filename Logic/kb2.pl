/*Assume bigger(X,Y)*/
bigger(elephant, horse). /*X is bigger than Y*/
bigger(horse, donkey). /*X is bigger than Y*/
bigger(donkey, dog). /*X is bigger than Y*/
bigger(donkey, monkey). /*X is bigger than Y*/

is_bigger(X,Y):- bigger(X,Y). /*True if X,Y matches knowledge*/
is_bigger(X,Y):- bigger(X,Z), is_bigger(Z,Y). /*True if X,Z matches knowledge AND Z,Y matches knowledge*/