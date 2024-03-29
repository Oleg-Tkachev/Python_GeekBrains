# Программу на языке Prolog для вычисления суммы элементов списка. 
# На вход подаётся целочисленный массив.
# На выходе - сумма элементов массива.

sum_list([], 0).

sum_list([Head|Tail], Sum) :-
    sum_list(Tail, TailSum),  % вычисляем сумму остатка списка
    Sum is Head + TailSum.    % вычисляем сумму элементов списка

% Пример использования:
?- sum_list([1, 2, 3, 4, 5], Sum).
Sum = 15.