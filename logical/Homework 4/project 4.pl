% Name: Joey Heifetz

%----------------------------------------------------------------
% Helper functions:

% min/3: Determines the minimum of two numbers.
min(X, Y, Min) :- X =< Y, Min is X.
min(X, Y, Min) :- X > Y, Min is Y.

% max/3: Determines the maximum of two numbers.
max(X, Y, Max) :- X =< Y, Max is Y.
max(X, Y, Max) :- X > Y, Max is X.

% green_min/3: Determines the minimum of two numbers using a green cut.
green_min(X, Y, Min) :- X =< Y, Min is X, !.
green_min(X, Y, Min) :- X > Y, Min is Y, !.

% green_max/3: Determines the maximum of two numbers using a green cut.
green_max(X, Y, Max) :- X =< Y, Max is Y, !.
green_max(X, Y, Max) :- X > Y, Max is X, !.

% search/2: Search for an element in a list.
search(X, [X|_]).                                 % Base case: X is the first element of the list
search(X, [_|T]) :-                               % Recursive case: Check if X is a member of the tail of the list
    search(X, T).

%----------------------------------------------------------------
% 1

% min_max/4: Determines the minimum and maximum of two numbers without using cuts.
min_max(X, Y, Min, Max) :-
    min(X, Y, Min),
    max(X, Y, Max).

% green_min_max/4: Determines the minimum and maximum of two numbers using green cuts.
green_min_max(X, Y, Min, Max) :-
    green_min(X, Y, Min),
    green_max(X, Y, Max).

% red_min_max/4: Determines the minimum and maximum of two numbers using red cuts.
red_min_max(X, Y, Min, Max) :-
    X =< Y,    
    !,         
    Min = X,   
    Max = Y.  

red_min_max(X, Y, Min, Max) :-
    X > Y,     
    !,         
    Min = Y,   
    Max = X.   

% 2

% buy(X, Y): Predicate with various cuts to demonstrate different cut behaviors.
% buy(X,Y):-! , car(Y),! ,price(Y,Z),! , Z<1000, ! .  % !1 - red, !2 - green, !3 - green, !4 - Unnecessary
% car(alpha):-! .                                     % !5 - Unnecessary
% car(subaru):-! .                                    % !6 - Unnecessary
% price(alpha,1100):-! .                              % !7 - red
% price(subaru,990):-! .                              % !8 - red

% 3
% Base case: If either list is empty, the result is an empty list.
intersection_help([], _, []).
intersection_help(_, [], []).

% Recursive case: If the head of the first list is a member of the second list,
% include it in the result and proceed with the tails of both lists.
intersection_help([H|T], L2, [H|Common]) :-
    member(H, L2),
    intersection_help(T, L2, Common).

% Recursive case: If the head of the first list is not a member of the second list,
% skip it and proceed with the tail of the first list.
intersection_help([H|T], L2, Common) :-
    \+ member(H, L2),
    intersection_help(T, L2, Common).

% Check the result and write a message if the list is empty.
check([], _) :-
    write('no').
check(H, H) :-
    H \= [].

% intersection/3: Predicate which combines the helper and check predicates to find the intersection of two lists.
intersection(L1, L2, Common) :-
    intersection_help(L1, L2, Common),
    check(Common, Res).

% 4
% Predicate to count occurrences of a string in a list.

string_count([], 0, _).

string_count([H|T], Num, String) :-
    H == String,
    !,
    string_count(T, Num1, String),
    Num is Num1 + 1.

string_count([H|T], Num, String) :-
    H \= String,
    string_count(T, Num, String).

% rgbsort/2: Predicate to count RGB strings in a list and return the counts.
rgbsort(L, [R1, G1, B1]) :-
    string_count(L, G1, "green"),
    string_count(L, R1, "red"),
    string_count(L, B1, "blue").

% 5

% flatten/2: Predicate to flatten a list containing atoms and sub-lists.

% Base case: The flattened version of an empty list is an empty list.
flatten([], []).

% Recursive case: If the head is a list, flatten it and the tail, then append the results.
flatten([H|T], FlatList) :-
    is_list(H),
    flatten(H, FlatH),
    flatten(T, FlatT),
    append(FlatH, FlatT, FlatList).

% Recursive case: If the head is not a list, add it to the result of flattening the tail.
flatten([H|T], [H|FlatT]) :-
    \+ is_list(H),
    flatten(T, FlatT).
