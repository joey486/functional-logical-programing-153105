% id: 216175398
% name: joey heifetz

%----------------------------------------------------------------
% Help functions

% Convert a single character to a number
char_to_number(Char, Number) :-
    char_type(Char, digit),                       % Ensure Char is a digit
    char_code('0', ZeroCode),                     % Get the ASCII code for '0'
    char_code(Char, CharCode),                    % Get the ASCII code for the character
    Number is CharCode - ZeroCode.                % Calculate the numerical value of the character

% Find the sum of a list of characters
sumList([], 0).                                   % Base case: The sum of an empty list is 0

sumList([H|T], Sum) :-
    char_to_number(H, Digit),                     % Convert H to a number
    sumList(T, SumTail),                          % Recursively find the sum of the tail
    Sum is Digit + SumTail.                       % Sum up the values

% Calculate the sum of a regular list
sumlist([], 0).                                   % Base case: The sum of an empty list is 0

sumlist([H|T], Sum) :-                            % Recursive case: The sum of a list with head H and tail T
    sumlist(T, RestSum),                          % Recursively find the sum of the tail
    Sum is H + RestSum.                           % Add the head to the sum of the tail

% Search for an element in a list
search(X, [X|_]).                                 % Base case: X is the first element of the list

search(X, [_|T]) :-                               % Recursive case: Check if X is a member of the tail of the list
    search(X, T).
%----------------------------------------------------------------

%----------------------------------------------------------------
% scum(N, Res)
% Calculate the sum of all integers from 0 to N (inclusive)

scum(0, 0).                                       % Base case: The sum of integers up to 0 is 0

scum(N, Res) :- 
    N > 0,                                        % Ensure N is positive
    N1 is N - 1,                                  % Decrease N by 1
    scum(N1, Res1),                               % Recursively calculate the sum up to N-1
    Res is Res1 + N.                              % Add N to the result
%----------------------------------------------------------------

%----------------------------------------------------------------
% sumDigits(Num, Sum)
% Calculate the sum of the digits of a number represented as a string

sumDigits("", 0).                                 % Base case: The sum of the digits of an empty string is 0

sumDigits(Num, Sum) :-
    atom_chars(Num, List),                        % Convert the number to a list of characters
    sumList(List, Sum).                           % Calculate the sum of the list of characters
%----------------------------------------------------------------

%----------------------------------------------------------------
% split(N, Res)
% Split a number represented as a string into a list of digits

split(N, Res) :-
    atom_chars(N, CharList),                      % Convert the number to a list of characters
    maplist(char_to_number, CharList, Res).       % Convert each character to its corresponding number
%----------------------------------------------------------------

%----------------------------------------------------------------
% create(List, N)
% Create a number from a list of digits

create([], 0).                                    % Base case: The number created from an empty list is 0

create([H|List], N) :- 
    create(List, N1),                             % Recursively create a number from the tail
    N is N1 * 10 + H.                             % Combine the head with the rest of the number
%----------------------------------------------------------------

%----------------------------------------------------------------
% reverse(List, Res)
% Reverse a number represented as a string

reverse(List, Res) :- 
    split(List, Tmp),                             % Split the number into a list of digits
    create(Tmp, Res).                             % Create a number from the reversed list
%----------------------------------------------------------------

%----------------------------------------------------------------
% intersection(L1, L2, Z)
% Find the intersection of two lists

intersection([], _, []).                          % Base case: The intersection of an empty list with any list is empty

intersection([H|T], L2, [H|Z]) :-                 % Case 1: H is in L2, include H in the result
    search(H, L2),                                % Check if H is in L2
    intersection(T, L2, Z).                       % Recursively find the intersection of the tail of L1 with L2

intersection([H|T], L2, Z) :-                     % Case 2: H is not in L2, do not include H in the result
    \+ search(H, L2),                             % Check if H is not in L2
    intersection(T, L2, Z).                       % Recursively find the intersection of the tail of L1 with L2
%----------------------------------------------------------------

%----------------------------------------------------------------
% minus(L1, L2, Z)
% Find the difference between two lists (elements in L1 but not in L2)

minus([], _, []).                                 % Base case: The difference of an empty list with any list is empty

minus([H|T], L2, Z) :-  
    search(H, L2),                                % If H is in L2,
    minus(T, L2, Z).                              % Skip H and continue with the tail of L1

minus([H|T], L2, [H|Z]) :-  
    \+ search(H, L2),                             % If H is not in L2,
    minus(T, L2, Z).                              % Include H in the result and continue with the tail of L1
%----------------------------------------------------------------

last_three([X, Y, Z], X, Y, Z).


last_three([_|Tail], X, Y, Z) :-
    last_three(Tail, X, Y, Z).


% this recurtion is a tail recurtion, beause the recursive call
% is the last step 

%----------------------------------------------------------------
% union(L1, L2, L3) - not tail recursion

union([], L2, L2).                                % Base case: The union of an empty list with any list is empty
 
union([H|T], L2, [H|Z]) :-
    \+ search(H, L2),                            % If H is not in L2,
    union(T, L2, Z).                             % Include H in the result and continue with the tail of L1

union([H|T], L2, Z) :-
    member(H, L2),
    union(T, L2, Z).

% union(L1, L2, Z) - tail recurstion

union_acc([], L2, Acc, Result) :-
    append(Acc, L2, Result).

union_acc([H|T], L2, Acc, Result) :-
    \+ member(H, L2), !,                            % green exlimation mark. just for optimasion
    union_acc(T, L2, [H|Acc], Result).

union_acc([H|T], L2, Acc, Result) :-
    union_acc(T, L2, Acc, Result).

% Wrapper predicate that 
tail_union(L1, L2, Result) :-
    union_acc(L1, L2, [], Result).

%----------------------------------------------------------------
% kuku(L1, L2) - not tail recursion

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


% kuku(L1, L2) - tail recursion

kuku_acc([], L2, Acc, Result) :-
    append(Acc, L2, Result).

kuku_acc([H|T], L2, Acc, Result) :-
    \+ member(H, L2), !,
    kuku_acc(T, L2, [H|Acc], Result).
    
kuku_acc([H|T], L2, Acc, Result) :-
    kuku_acc(T, L2, Acc, Result).
    
% Wrapper predicate that

tail_kuku(L1, L2, Result) :-
    kuku_acc(L1, L2, [], Result).

%----------------------------------------------------------------