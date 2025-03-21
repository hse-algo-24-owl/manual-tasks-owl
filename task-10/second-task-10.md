# Задание №10. Команда Second.
### Постановка задачи:
1. Дана сеть (взвешенный ориентированный граф) с источником s и стоком t.
2. Для каждой дуги определена пропускная способность и стоимость транспортировки.
3. Необходимо найти для указанной сети максимальный поток минимальной стоимости. 

## Вариант 5:
#### Пропускная способность дуг сети p(e) и стоимость транспортировки  единицы потока c(e):

| Дуги                      | sa | sb | ac | ba | bc | bd | cd | dt |
|:--------------------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Пропускная способность    | 3  | 10 | 4  | 1  | 3  | 10 | 8  | 12 |
| Стоимость транспортировки | 1  | 1  | 1  | 2  | 3  | 5  | 1  | 1  |

## Этап 1: Построим сеть с источником *s*, стоком *t* и указанными пропускными способностями дуг.

```mermaid
graph LR
    s-->|3|a
    s-->|10|b
    a-->|4|c
    b-->|1|a
    b-->|3|c
    b-->|10|d
    c-->|8|d
    d-->|12|t
```

Укажем начальный поток величиной 10 s -> b -> d -> t. Построим соответствующую остаточную сеть.

```mermaid
graph RL
    s-->|10|b
    b-->|10|d
    d-->|10|t
    t-.->|2|d
    a-.->|3|s
    c-.->|4|a
    a-.->|1|b
    c-.->|3|b
    d-.->|8|c
```

## Этап 2: Проведем поиск увеличивающего пути в остаточной сети

В остаточной сети найден увеличивающий путь t -> d -> c -> a -> s. Минимальный вес дуг на этом пути равен 2.

Уменьшим вес дуг на найденном пути, дуги для которых вес стал нулевым удалим из остаточной сети.

```mermaid
graph RL
    s-->|10|b
    b-->|10|d
    d-->|12|t
    c-->|2|d
    d-.->|6|c
    a-->|2|c
    c-.->|2|a
    s-->|2|a
    a-.->|1|s
    a-.->|1|b
    c-.->|3|b
```

## Этап 3. Продолжим поиск увеличивающего пути в остаточной сети

В остаточной сети не найдено увеличивающих путей, следовательно, алгоритм завершил работу и найденный поток величиной 12 является максимальным для данной сети.

```mermaid
graph LR
    s-->|2,3|a
    s-->|10,10|b
    a-->|2,4|c
    b-->|0,1|a
    b-->|0,3|c
    b-->|10,10|d
    c-->|2,8|d
    d-->|12,12|t
```

## Этап 4. Рассчитаем стоимость полученного максимального потока.

| Дуги                                          | sa | sb | ac | ba | bc | bd | cd | dt | Итого  |
|:----------------------------------------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:------:|
| Пропускная способность p(e)                   | 3  | 10 | 4  | 1  | 3  | 10 | 8  | 12 |        |
| Локальный поток f(e)                          | 2  | 10 | 2  | 0  | 0  | 10 | 2  | 12 |        |
| Стоимость транспортировки единицы потока c(e) | 1  | 1  | 1  | 2  | 3  | 5  | 1  | 1  |        |
| Суммарная стоимость f(e)*c(e)                 | 2  | 10 | 2  | 0  | 0  | 50 | 2  | 12 | **78** |

Стоимость полученного потока составляет 78. 

## Этап 5. Попробуем уменьшить стоимость потока для чего построим остаточную сеть

Для каждого ребра остаточной сети укажем стоимость транспортировки единицы потока.

```mermaid
graph LR
    s-->|-1|a
    a-.->|+1|s
    s-->|-1|b
    b-->|-5|d
    d-->|-1|t
    a-->|-1|c
    c-.->|+1|a
    c-->|-1|d
    d-.->|+1|c
    a-.->|+2|b
    c-.->|+3|b
```

В остаточной сети найден ориентированный цикл отрицательной стоимости s -> b -> d -> c -> a -> s (- 1 - 5 + 1 + 1 + 1 = -3)

Минимальный вес ребра в цикле 1 - это неиспользованный резерв рёбер s -> a.

Удалим найденный цикл - уменьшим на 1 вес всех ребер, входящих в цикл.

```mermaid
graph LR
    s-->|3|a
    s-->|9|b
    b-.->|1|s
    b-->|9|d
    d-.->|1|b
    d-->|12|t
    a-->|3|c
    c-.->|1|a
    c-->|3|d
    d-.->|5|c
    a-.->|1|b
    c-.->|3|b
```

## Этап 6: Проведем повторный поиск цикла отрицательной стоимости в остаточной сети

Скорректируем остаточную сеть с указанием стоимости транспортировки единицы потока.

```mermaid
graph LR
    s-->|-1|a
    s-->|-1|b
    b-.->|+1|s
    b-->|-5|d
    d-.->|+5|b
    d-->|-1|t
    a-->|-1|c
    c-.->|+1|a
    c-->|-1|d
    d-.->|+1|c
    a-.->|+2|b
    c-.->|+3|b
```

В остаточной сети найден ориентированный цикл отрицательной стоимости b -> d -> c -> b (- 5 + 1 + 3 = -1)

Минимальный вес ребра в цикле 1 - это неиспользованный резерв рёбер b -> d.

Удалим найденный цикл - уменьшим на 1 вес всех ребер, входящих в цикл.

```mermaid
graph LR
    s-->|3|a
    s-->|9|b
    b-.->|1|s
    a-.->|1|b
    d-->|12|t
    a-->|3|c
    c-.->|1|a
    b-->|8|d
    d-.->|2|b
    c-->|2|d
    d-.->|6|c
    b-->|1|c
    c-.->|2|b
```

## Этап 7: Проведем повторный поиск цикла отрицательной стоимости в остаточной сети

Скорректируем остаточную сеть с указанием стоимости транспортировки единицы потока.

```mermaid
graph LR
    s-->|-1|a
    s-->|-1|b
    b-.->|+1|s
    a-.->|+1|b
    d-->|-1|t
    a-->|-1|c
    c-.->|+1|a
    b-->|-5|d
    d-.->|+5|b
    c-->|-1|d
    d-.->|+1|c
    b-->|-3|c
    c-.->|+3|b
```

В остаточной сети найден ориентированный цикл отрицательной стоимости a -> b -> c -> a (+ 1 - 3 + 1 = -1)

Минимальный вес ребра в цикле 1 - это неиспользованный резерв рёбер b -> a и a -> c.

Удалим найденный цикл - уменьшим на 1 вес всех ребер, входящих в цикл.

```mermaid
graph LR
    s-->|3|a
    s-->|9|b
    b-.->|1|s
    d-->|12|t
    b-->|8|d
    d-.->|2|b
    c-->|2|d
    d-.->|6|c
    b-->|1|a
    a-->|3|c
    c-.->|1|a
    c-.->|3|b
```

## Этап 8: Проведем повторный поиск цикла отрицательной стоимости в остаточной сети

Скорректируем остаточную сеть с указанием стоимости транспортировки единицы потока.

```mermaid
graph LR
    s-->|-1|a
    s-->|-1|b
    b-.->|+1|s
    d-->|-1|t
    b-->|-5|d
    d-.->|+5|b
    c-->|-1|d
    d-.->|+1|c
    b-->|-2|a
    a-->|-1|c
    c-.->|+1|a
    c-.->|+3|b
```

В остаточной сети отсутствуют циклы отрицательной стоимости, следовательно, стоимость потока минимальна.

## Этап 9: Рассчитаем стоимость полученного максимального потока

| Дуги                                          | sa | sb | ac | ba | bc | bd | cd | dt | Итого  |
|:----------------------------------------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:------:|
| Пропускная способность p(e)                   | 3  | 10 | 4  | 1  | 3  | 10 | 8  | 12 |        |
| Локальный поток f(e)                          | 3  | 9  | 3  | 1  | 0  | 8  | 2  | 12 |        |
| Стоимость транспортировки единицы потока c(e) | 1  | 1  | 1  | 2  | 3  | 5  | 1  | 1  |        |
| Суммарная стоимость f(e)*c(e)                 | 3  | 9  | 3  | 2  | 0  | 40 | 2  | 12 | **71** |

Стоимость полученного потока составляет 71.

## Ответ:

Максимальный поток в сети равен 12, минимальная стоимость потока 71, она реализуется следующим локальными потоками:

```mermaid
graph LR
    s-->|3,3|a
    s-->|9,10|b
    a-->|3,4|c
    b-->|0,1|a
    b-->|0,3|c
    b-->|9,10|d
    c-->|3,8|d
    d-->|12,12|t
```