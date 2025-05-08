% Base case: An empty list transforms into an empty list
kuku([], []).

% Recursive case: If the head is a list, apply the transformation recursively
kuku([H|T], [HZ|TZ]) :-
    is_list(H), !,
    kuku(H, HZ),
    kuku(T, TZ).

% Recursive case: If the head is not a list, transform the head and continue with the tail
kuku([H|T], [[H, H2]|TZ]) :-
    \+ is_list(H),
    H2 is 2 * H,
    kuku(T, TZ).
