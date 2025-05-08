% id: 216175398


married(avr,sara). 
married(yit,rivka).
married(yaak,lea).
parent(avr,yit).
parent(yit,yaak).
parent(yaak,reuven). 
parent(yaak,shimon).
parent(yaak,joseph).
parent(yaak,levi).
parent(yaak,yehuda).
parent(yaak,dina).
parent(yehuda,zerach).
parent(yehuda,peretz).
parent(levi,kehat).
parent(levi,gershon).
parent(levi,merari).
parent(sara,shimon).
parent(sara,joseph).
male(avr).
male(yit).
male(yaak).
male(levi).
male(yehuda).
male(zerach).
male(peretz).
male(kehat).
male(gershon).
male(merari).
male(reuven).
male(shimon).
female(sara).
female(rivka). 
female(lea).
female(dina).


% Section 1 - 
father(X,Y):-parent(X,Y),male(X).

% Section 3 - 
son(X,Y):-parent(Y,X),male(X).

% Section 9 -  (sibling)
diff(X,Y):-not(X=Y).
% 
% Section 8 - ����� ����
grand_daugther(X,Y):-female(X), parent(Z,X), parent(Y,Z).

% section 2 - mother
mother(X,Y):-parent(X,Y),female(X).
 % section 4 - daughter
daughter(X,Y) :- female(X),parent(Y,X).
% section 5 - grandfather
grand_father(X,Y) :- male(X),parent(X,Z),parent(Z,Y).

% section 6 - grandmother
grand_mother(X,Y) :- female(X),parent(X,Z),parent(Z,Y).

% section 7 - grandson
grandson(X,Y) :- male(X),parent(Y,Z),parent(Z,X).

% Section 10 - sibiling
sibling(X,Y) :- parent(Z,X),parent(Z,Y),dif(X,Y).

% Section 11 - uncle
uncle(X,Y) :- parent(W,Y),sibling(Z,W),married(Z,X).

% Section 12 - cusin
cusin(X,Y) :- parent(Z,X),mother(W,Y),sibling(Z,W),male(Y).

% Section 13 - sibling in law
sibling_In_Law(X,Y) :- male(X),married(Z,X),sibling(Z,Y),male(Y).
sibling_In_Law(X,Y) :- male(X),sibling(X,Z),female(Z),married(Z,Y).
sibling_In_Law(X,Y) :- male(X),married(X,Z),sibling(Z,W),female(W),married(W,Y).
sibling_In_Law(X,Y) :- female(X),married(Z,X),sibling(Z,Y),male(Y).
sibling_In_Law(X,Y) :- female(X),sibling(X,Z),female(Z),married(Z,Y).
sibling_In_Law(X,Y) :- male(X),married(X,Z),sibling(Z,W),female(W),married(W,Y).

% Section 14 - niece
niece(X,Y) :- female(X),parent(Z,X),sibling(Z,Y).

% Section 15 - second degree cousin
second_Degree_Cousins(X,Y) :- parent(Z,X),parent(W,Y),cusin(Z,W).