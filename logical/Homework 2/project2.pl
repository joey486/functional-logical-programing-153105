%ID - 216175398
%name - joey heifetz

%my_reverse
%Base:
my_reverse([],[]).

% Recursive call:
my_reverse([H|T1],R):- my_reverse(T1,T2), 
			       append(T2,[H],R).

%----------------------------------------------------------------
%my_prefix
% Base:
my_prefix([], _).

% Recursive call:
my_prefix([X|XS], [X|YS]) :-
    my_prefix(XS, YS).

%----------------------------------------------------------------
%my_member
% Base case: X is the first element of the list.
my_member(X, [X|_]).

% Recursive case: Check if X is a member of the tail of the list.
my_member(X, [_|T]) :-
    my_member(X, T).

%----------------------------------------------------------------
%my_member2
my_member2(X, L) :-
    select(X, L, L1),
    my_member(X, L1).

%----------------------------------------------------------------
%my_palindrome
my_palindrome(L) :-
    reverse(L, L, []).

reverse([], L, L).
reverse([H|T], L, Acc) :-
    reverse(T, L, [H|Acc]).


%----------------------------------------------------------------
%my_sorted
my_sorted([]).
my_sorted([_]).
my_sorted([X,Y|Rest]) :-
    X =< Y,
    my_sorted([Y|Rest]).

%----------------------------------------------------------------
%my_insert
my_insert(X, [], [X]).
my_insert(X, [H|T], [X,H|T]) :- X =< H.
my_insert(X, [H|T], [H|Z]) :-
    X > H,
    my_insert(X, T, Z).
