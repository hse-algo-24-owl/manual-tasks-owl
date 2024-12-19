# Решение

Рассчитаем минимально необходимое время:

$$
T_{min} = \frac {35+22+13+10} {3+1} = 20
$$

Расставим приоритеты заданиям и назначим работников в соответствии с приоритетами:

| Процесс          | A     | B     | C     | D     |
| ---------------- | ----- | ----- | ----- | ----- |
| Оставшееся время | 35    | 22    | 13    | 10    |
| Приоритет        | I     | II    | III   | IV    |
| Работник         | P1 = 3| P2 = 1|   -   |   -   |

Рассчитаем время, когда сравняются приоритеты, это произойдет в 1 из 2 следующих моментов:

$$
35 - 3t_1 = 22 - t_1 \\
или \\
22 - t_2 = 13
$$

Упрощаем выражения и получаем:

$$
t_1 = 6.5 \\
t_2 = 9
$$

Поскольку момент 1 наступит раньше, то берем его.  Рассчитаем оставшееся время для заданий A и B:

$$
A: 35 - 3 \cdot 6.5 = 15.5 \\
B: 22 - 1 \cdot 6.5 = 15.5
$$

Составляем новую таблицу:

| Процесс          | A     | B     | C     | D     |
| ---------------- | ----- | ----- | ----- | ----- |
| Оставшееся время | 15.5  | 15.5  | 13    | 10    |
| Приоритет        |  I    |  I    |  II   |  III  |
| Работник         |P1,  P2|P1,  P2|   -   |   -   |

Рассчитаем минимально необходимое время:

$$
T_{min} = \frac {15.5+15.5+13+10} {3+1} = 13.5
$$

Поскольку у заданий A, B равный приоритет, то мы назначаем на них всех работников. Поскольку работники P1 и P2 не могут выполнять одновременно 2 задания вместе, то будем их постоянно чередовать.

Общая производительность для этих двух заданий будет равна:

$$
P_{2} = \frac{3+1}{2} = 2
$$

где 2 - число выполняемых заданий

Определим время, когда у задач изменятся приоритеты, это произойдет когда оставшаяся длительность процессов А и В сраняется с С:

$$
15.5 - 2t = 13
$$

Получаем:

$$
t = 1.25
$$

Рассчитаем оставшееся время:

$$
A, B : 15.5 - 2 \cdot 1.25 = 13
$$

Составляем новую таблицу:

| Процесс          | A     | B     | C     | D     |
| ---------------- | ----- | ----- | ----- | ----- |
| Оставшееся время | 13    | 13    | 13    | 10    |
| Приоритет        |  I    |  I    |  I    |  II   |
| Работник         |P1, P2 |P1, P2 |P1, P2 |   -   |

Рассчитаем минимально необходимое время:

$$
T_{min} = \frac {13+13+13+10} {3+1} = 12.25
$$

Поскольку у заданий A, B и С равный приоритет, то мы назначаем на них всех работников. Поскольку работники P1 и P2 не могут выполнять одновременно 3 задания вместе, то будем их постоянно чередовать.

Общая производительность для этих двух заданий будет равна:

$$
P_{2} = \frac{3+1}{3} = \frac{4}{3}
$$

где 3 - число выполняемых заданий

Определим время, когда у задач изменятся приоритеты, это произойдет когда оставшаяся длительность процессов А и В сраняется с С:

$$
13 - \frac{4}{3}t = 10
$$

Получаем:

$$
t = 2.25
$$

Рассчитаем оставшееся время:

$$
A,B,C : 13 - \frac{4}{3} \cdot 2.25 = 10
$$

Составляем новую таблицу:

| Процесс          | A     | B     | C     | D     |
| ---------------- | ----- | ----- | ----- | ----- |
| Оставшееся время | 10    | 10    | 10    | 10    |
| Приоритет        |  I    |  I    |  I    |  I    |
| Работник         |P1, P2 |P1, P2 |P1, P2 |P1, P2 |

Поскольку у всех заданий равный приоритет, то мы назначаем на них всех работников. Сами задания закончатся одновременно:

$$
10 - \frac{3+1}{4}t = 0 \\
t = 10
$$

Необходимо поделить кол-во оставшегося времени на кол-во заданий, чтобы получить время, потраченное каждым отдельным работником на каждое отдельное задание. Получаем: 

$$
10 : 4 = 2.5
$$

Тогда диаграмма Ганта будет выглядеть следующим образом (время в таблице обозначает момент завершения работы процессора в задаче): 

| работник\момент смены задачи | 6.5 | 7.125 | 7.75 | 8.5 | 9.25 | 10 | 12.5 | 15 | 17.5 | 20 |
|-----------------------------|------|-------|------|-----|------|----|-------|----|------|----|
| p1                          | A    | A     | B    | A   | B    | C  | A     | B  | C    | D  |
| p2                          | B    | B     | A    | B   | C    | A  | B     | C  | D    | A  |
