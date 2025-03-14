### Вариант 6:
Транспортная задача

Два завода имеют производительность 8 и 8, а два складских помещения имеют вместимость 7 и 9. Матрица затрат на перевозку одной единицы товара (строки – это заводы, столбцы – это склады) имеет вид:

$$
 \begin{pmatrix}    
  8 & 6 \\ 
  4 & 5 \\ 
 \end{pmatrix} 
$$

Требуется:

1. Найти стоимость перевозки с первого завода на первый склад 7 единиц товара на второй склад 1 единицу, со второго завода на второй склад 8 единиц товара;
2. Используя алгоритм поиска максимального потока минимальной стоимости, скорректировать указанный выше вариант перевозки товаров, так чтобы объём перевозимых товаров не изменился, а стоимость их перевозки стала минимальной.

### Шаг 1. Посчитаем стоимость перевозки товара

Затраты на перевозку одного товара с первого завода на первый склад – **8**. 
Затраты на перевозку одного товара с первого завода на второй склад – **6**. 
Затраты на перевозку одного товара со второго завода на второй склад – **4**.

$$8*7+6*1+4*8=94$$

### Шаг 2. Построим транспортную сеть

 завод 1 – а
 завод 2 – b
 склад 1 – 1
 склад 2 – 2 
 
 Построим транспортную сеть и укажем локальные потоки и пропускные способности дуг.

Завод a имеет производительность **8**, завод b имеет производительность **8**, склад 1 имеет вместимость **7**, склад 2 имеет вместимость **9**.

``` mermaid
graph LR
    S-->|8, 8|a
    S-->|8, 8|b
    a-->|7, 7|1
    a-->|1, 9|2
    b-->|0, 7|1
    b-->|8, 9|2
    1-->|7, 7|t
    2-->|9, 9|t
```
#### Строим остаточную сеть

``` mermaid
graph LR
    S-->|8|a
    S-->|8|b
    a-->|7|1
    a-->|1|2
    2-.->|8|a
    1-.->|7|b
    2-.->|1|b
    b-->|8|2
    1-->|7|t
    2-->|9|t
```

Для каждого ребра остаточной сети укажем стоимость транспортировки единицы потока.

``` mermaid
graph LR
    S-->|-0|a
    S-->|-0|b
    a-->|-8|1
    a-->|-6|2
    2-.->|+6|a
    1-.->|+4|b
    2-.->|+5|b
    b-->|-5|2
    1-->|-0|t
    2-->|-0|t
```
### Шаг 3. Поиск цикла отрицательной стоимости

В остаточной сети найден ориентированный цикл отрицательной стоимости a -> 1 -> b -> 2 -> a (- 8 + 4 - 5 + 6 = -3)

min вес ребра в указанном цикле в графе остаточной сети = 7

Удалим найденный цикл - уменьшим на 7 вес всех ребер, входящих в цикл.

``` mermaid
graph LR
    S-->|8|a
    S-->|8|b
    1-.->|7|a
    a-->|8|2
    2-.->|1|a
    b-->|7|1
    2-.->|8|b
    b-->|1|2
    1-->|7|t
    2-->|9|t
```

Скорректируем остаточную сеть с указанием стоимости транспортировки единицы потока.

``` mermaid
graph LR
    S-->|-0|a
    S-->|-0|b
    1-.->|+8|a
    a-->|-6|2
    2-.->|+6|a
    b-->|-4|1
    2-.->|+5|b
    b-->|-5|2
    1-->|-0|t
    2-->|-0|t
```

В остаточной сети отсутствуют циклы отрицательной стоимости, следовательно, стоимость потока минимальна.

``` mermaid
graph LR
    S-->|8, 8|a
    S-->|8, 8|b
    a-->|0, 7|1
    a-->|8, 9|2
    b-->|7, 7|1
    b-->|1, 9|2
    1-->|7, 7|t
    2-->|9, 9|t
```

### Шаг 4. Рассчитаем текущую стоимость

$$a-->2 = 8 * 6 = 48$$
$$b-->1 = 7 * 4 = 28$$
$$b-->2 = 1 * 5 = 5$$
sum = 48 + 28 + 5 = 81

### Ответ

1. Изначальная стоимость - 94
2. Стоимость после корректировки - 81. 
	1 завод -> 2 склад - 8 ед.
	2 завод -> 1 склад - 7 ед.
	2 завод -> 2 склад - 1 ед.
