married(avr,sara). % ���� ������ ������
married(yit,rivka).
married(yaak,lea).
parent(avr,yit).
parent(yit,yaak).
parent(yaak,reuven). % ��� ����� �- 12 ������
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


% Section 1 - ����� ��
father(X,Y):-parent(X,Y),male(X).

% Section 3 - ����� ��
son(X,Y):-parent(Y,X),male(X).

% Section 9 - ����� ����� ����/����� (sibling)
diff(X,Y):-not(X=Y).
% 
% Section 8 - ����� ����
grand_daugther(X,Y):-female(X), parent(Z,X), parent(Y,Z).