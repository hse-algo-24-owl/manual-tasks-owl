## Вариант 2:
### Пропускная способность дуг сети:

|          Дуги          | sa | sc | sd | ab | cb | dc | bt | ct | dt |
|:----------------------:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Пропускная способность | 6  | 4  | 8  | 4  | 5  | 2  | 9  | 3  | 5  |

## Решение
### 1. Построим сеть с источником **s**, стоком **t** и указанными пропускными способностями дуг.
```mermaid
graph LR
    s-->|6|a
    s-->|4|c
    s-->|8|d
    a-->|4|b
    c-->|5|b
    d-->|2|c
    b-->|9|t
    c-->|3|t
    d-->|5|t
```
### Остаточная сеть. Локальный поток равен нулю => необходимо вынести обратную дугу с весом равным пропускной способности. 

```mermaid
graph RL
    a-.->|6|s
    c-.->|4|s
    d-.->|8|s
    b-.->|4|a
    b-.->|5|c
    c-.->|2|d
    t-.->|9|b
    t-.->|3|c
    t-.->|5|d
```

## Анализ разрезов
Найдем Минимальную пропускную способность сети, используя 16 разных разрезов сети.
|    V1   |    V2   |         Max         |
|:-------:|:-------:|:-------------------:|
|    S    |  ABCDT  |         18          |
|   SA    |  BCDT   |         16          |
|   SB    |  ACDT   |         27          |
|   SC    |  ABDT   |         22          |
|   SD    |  ABCT   |         17          |
|   SAB   |   CDT   |         21          |
|   SAC   |   BDT   |         20          |
|   SAD   |   CBT   |$$\color{green}{15}$$|
|   SBC   |   ADT   |         26          |
|   SBD   |   ACT   |         26          |
|   SCD   |   ABT   |         19          |
|  SABC   |   DT    |         20          |
|  SABD   |   CT    |         20          |
|  SBCD   |   AT    |         23          |
|  SACD   |   BT    |         17          |
|  SACBD  |    T    |         17          |

### Результаты анализа:
Минимальная пропускная способность сети - 15. Пока запомним это число.

### 2. В остаточной сети найден увеличивающий путь t->c->d->s, минимальная пропускная способность на дугах пути - 2.

Уменьшим вес дуг на этом пути на минимальную пропускную способность на пути. Дуги с нулевым весом удалим из осчтаточной сети.
```mermaid
graph RL
    t-.->|9|b
    t-.->|1|c
    t-.->|5|d
    b-.->|4|a
    b-.->|5|c
    c-.->|4|s
    d-.->|6|s
    a-.->|6|s

    s-->|2|d
    d-->|2|c
    c-->|2|t
```

Отразим изменения и на исходной сети.
```mermaid
graph LR
    s-->|"(0, 6)"|a
    s-->|"(0, 4)"|c
    s-->|"(2, 8)"|d
    a-->|"(0, 4)"|b
    c-->|"(0, 5)"|b
    d-->|"(2, 2)"|c
    b-->|"(0, 9)"|t
    c-->|"(2, 3)"|t
    d-->|"(0, 5)"|t
```

### 3. В остаточной сети найден ещё один увеличивающий путь t->b->a->s , минимальная пропускная способность на дугах пути - 4.

Уменьшим вес дуг на этом пути на минимальную пропускную способность на пути. Дуги с нулевым весом удалим из осчтаточной сети.
```mermaid
graph RL
    t-.->|5|b
    t-.->|1|c
    t-.->|5|d
    b-.->|5|c
    c-.->|4|s
    d-.->|6|s
    a-.->|2|s

    s-->|2|d
    d-->|2|c
    c-->|2|t

    s-->|4|a
    a-->|4|b
    b-->|4|t
```

Отразим изменения и на исходной сети.
```mermaid
graph LR
    s-->|"(4, 6)"|a
    s-->|"(0, 4)"|c
    s-->|"(2, 8)"|d
    a-->|"(4, 4)"|b
    c-->|"(0, 5)"|b
    d-->|"(2, 2)"|c
    b-->|"(4, 9)"|t
    c-->|"(2, 3)"|t
    d-->|"(0, 5)"|t
```

### 4. В остаточной сети найден увеличивающий путь t->b->c->s , минимальная пропускная способность на дугах пути - 4.

Уменьшим вес дуг на этом пути на минимальную пропускную способность на пути. Дуги с нулевым весом удалим из осчтаточной сети.
```mermaid
graph RL
    t-.->|1|b
    t-.->|1|c
    t-.->|5|d
    b-.->|1|c
    d-.->|6|s
    a-.->|2|s

    s-->|2|d
    d-->|2|c
    c-->|2|t

    s-->|4|a
    a-->|4|b
    b-->|8|t

    s-->|4|c
    c-->|4|b
```

Отразим изменения и на исходной сети.
```mermaid
graph LR
    s-->|"(4, 6)"|a
    s-->|"(4, 4)"|c
    s-->|"(2, 8)"|d
    a-->|"(4, 4)"|b
    c-->|"(4, 5)"|b
    d-->|"(2, 2)"|c
    b-->|"(8, 9)"|t
    c-->|"(2, 3)"|t
    d-->|"(0, 5)"|t
```

### 5. В остаточной сети найден увеличивающий путь t->d->s , минимальная пропускная способность на дугах пути - 5.

Уменьшим вес дуг на этом пути на минимальную пропускную способность на пути. Дуги с нулевым весом удалим из осчтаточной сети.
```mermaid
graph RL
    t-.->|1|b
    t-.->|1|c
    b-.->|1|c
    d-.->|1|s
    a-.->|2|s

    s-->|7|d
    d-->|2|c
    c-->|2|t

    s-->|4|a
    a-->|4|b
    b-->|8|t

    s-->|4|c
    c-->|4|b

    d-->|5|t
```

Отразим изменения и на исходной сети.
```mermaid
graph LR
    s-->|"(4, 6)"|a
    s-->|"(4, 4)"|c
    s-->|"(7, 8)"|d
    a-->|"(4, 4)"|b
    c-->|"(4, 5)"|b
    d-->|"(2, 2)"|c
    b-->|"(8, 9)"|t
    c-->|"(2, 3)"|t
    d-->|"(5, 5)"|t
```

### 6. Продолжим поиск увеличивающего пути в остаточной сети
В остаточной сети больше нет увеличивающих путей, найденный поток величиной 15 (2 + 4 + 4 + 5 = 15) является максимальным в данной сети. Он совпадает с найденной ранее Минимальной пропускной способностью сети.

## Результат
Максимальный поток равен 15, он реализуется этими локальными потоками:
```mermaid
graph LR
    s-->|"(4, 6)"|a
    s-->|"(4, 4)"|c
    s-->|"(7, 8)"|d
    a-->|"(4, 4)"|b
    c-->|"(4, 5)"|b
    d-->|"(2, 2)"|c
    b-->|"(8, 9)"|t
    c-->|"(2, 3)"|t
    d-->|"(5, 5)"|t
```