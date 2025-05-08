% name: yosef hiefetz
% ID: 216175398

%1
grade(sara,97).
grade(rivka,88).    
grade(naama,67).
grade(rachel,81).    

% Helper predicate to collect grades into a list
collect_grades(Grades) :-
    findall(grade(ID, G), grade(ID, G), Grades).

% Helper predicate to sort grades
sort_grades(Grades, SortedGrades) :-
    sort(2, @>=, Grades, SortedGrades).

% Main predicate
milga(Num, FinalGrade, SelectedGrades) :-
    collect_grades(Grades),
    sort_grades(Grades, SortedGrades),
    length(Prefix, Num),
    append(Prefix, _, SortedGrades),
    last(Prefix, grade(_, FinalGrade)),
    SelectedGrades = Prefix.

% 2
allDivs(Num, Divs) :-
    divisors(Num, Num, Divs).

divisors(0, _, []).

divisors(I, Num, [I|Rest]) :-
    I > 0,
    0 is Num mod I,  % Check if I is a divisor of Num
    I1 is I - 1,
    divisors(I1, Num, Rest).

divisors(I, Num, Rest) :-
    I > 0,
    I1 is I - 1,
    divisors(I1, Num, Rest).

% 3
% Helper predicate to count occurrences of each element in the list
count_elements(L, CountList) :-
    findall((E, C), (member(E, L), count_occurrences(E, L, C)), AllCounts),
    sort(AllCounts, CountList).

% Helper predicate to count the occurrences of an element in the list
count_occurrences(E, L, Count) :-
    include(=(E), L, Filtered),
    length(Filtered, Count).

% Helper predicate to find the element with the maximum count
max_count([(_, C)], C).
max_count([(_, C)|T], MaxC) :-
    max_count(T, C1),
    MaxC is max(C, C1).

% Helper predicate to find the element with the minimum count
min_count([(_, C)], C).
min_count([(_, C)|T], MinC) :-
    min_count(T, C1),
    MinC is min(C, C1).

% Main predicate to find the most and least recurring members
max_min(L, X, Y) :-
    count_elements(L, CountList),
    max_count(CountList, MaxCount),
    min_count(CountList, MinCount),
    member((X, MaxCount), CountList),
    member((Y, MinCount), CountList).

% 4
% The query is solve(member(X, [1, 2]))..

% We start with: solve(member(X, [1, 2])).

% This matches the third rule solve(A) :- clause(A, C), solve(C). with A = member(X, [1, 2]).

% Clause lookup:

% clause(member(X, [1, 2]), C) tries to match the head member(X, [1, 2]) with the clauses of member/2.
% The first clause of member/2 is member(X, [X | T])..

% Attempt to match: member(X, [1, 2]) with member(X, [X | T]).

% Matching member(X, [X | T]) with member(X, [1, 2]) gives:
% X = 1
% T = [2]
% Success: C = true (because the body of the clause is true implicitly).

% We now have solve(true).

% This matches the first rule: solve(true) :- !. which succeeds.

% Output:

% X = 1
% ; (backtracking to find more solutions).

% Backtrack to step 2 and find more clauses for member(X, [1, 2]).

% The second clause of member/2 is member(X, [Y | T]) :- member(X, T)..

% Attempt to match: member(X, [1, 2]) with member(X, [Y | T]).

% Matching member(X, [Y | T]) with member(X, [1, 2]) gives:
% Y = 1
% T = [2]
% Success: We get C = member(X, [2]).

% We now have solve(member(X, [2])).

% Re-enter the third rule solve(A) :- clause(A, C), solve(C) with A = member(X, [2]).

% Clause lookup:

% clause(member(X, [2]), C) tries to match the head member(X, [2]) with the clauses of member/2.
% The first clause of member/2 is member(X, [X | T])..

% Attempt to match: member(X, [2]) with member(X, [X | T]).

% Matching member(X, [X | T]) with member(X, [2]) gives:
% X = 2
% T = []
% Success: C = true (because the body of the clause is true implicitly).

% We now have solve(true).

% This matches the first rule: solve(true) :- !. which succeeds.

% Output:

% X = 2
% ; (backtracking to find more solutions).

% Backtrack to step 8 and find more clauses for member(X, [2]).

% The second clause of member/2 is member(X, [Y | T]) :- member(X, T)..

% Attempt to match: member(X, [2]) with member(X, [Y | T]).

% Matching member(X, [Y | T]) with member(X, [2]) gives:
% Y = 2
% T = []
% Success: We get C = member(X, []).

% We now have solve(member(X, [])).

% Re-enter the third rule solve(A) :- clause(A, C), solve(C) with A = member(X, []).

% Clause lookup:

% clause(member(X, []), C) tries to match the head member(X, []) with the clauses of member/2.
% No matching clause for member(X, []).

% Failure: No more solutions.

% Summary of Outputs
% X = 1
% X = 2
% The final output would be the values of X as 1 and 2, corresponding to the successful solutions found during the dry run.