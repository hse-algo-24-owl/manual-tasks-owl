## Вариант 2:
### Пропускная способность дуг сети:

|          Дуги          | sa | sc | sd | ab | cb | dc | bt | ct | dt |
|:----------------------:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Пропускная способность | 6  | 4  | 8  | 4  | 5  | 2  | 9  | 3  | 5  |

## Решение

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
### Анализ разрезов

|   V1    |  V2     |         Max         |
|:-------:|:-------:|:-------------------:|
|    S    |  ABCDT  |         18          |
|   SA    |  BCDT   |         16          |
|   SB    |  ACDT   |         27          |
|   SC    |  ABDT   |         20          |
|   SD    |  ABCT   |         17          |
|   SAB   |   CDT   |         21          |
|   SAC   |   BDT   |         12          |
|   SAD   |   CBT   |$$\color{green}{15}$$|
|   SBC   |   ADT   |         29          |
|   SBD   |   ACT   |         36          |
|   SCD   |   ABT   |         19          |
|  SABC   |   DT    |         18          |
|  SABD   |   CT    |         20          |
|  SBCD   |   AT    |         26          |
|  SACD   |   BT    |$$\color{green}{15}$$|
|  SACBD  |    T    |         17          |

### Остаточная сеть

```mermaid
graph LR
    t-->|9|b
    t-->|3|c
    t-->|5|d
    b-->|4|a
    b-->|5|c
    c-->|4|s
    c-->|2|d
    d-->|8|s
    a-->|6|s
```

### берём tcds min 2

```mermaid
graph LR
    s-->|0.6|a
    s-->|0.4|c
    s-->|2.8|d
    a-->|0.4|b
    c-->|0.5|b
    d-->|2.2|c
    b-->|0.9|t
    c-->|2.3|t
    d-->|0.5|t
```

```mermaid
graph LR
    t-->|9|b
    t-->|1|c
    t-->|5|d
    b-->|4|a
    b-->|5|c
    c-->|4|s
    d-->|6|s
    a-->|6|s
```

### tbas min 4

```mermaid
graph LR
    s-->|4.6|a
    s-->|0.4|c
    s-->|2.8|d
    a-->|4.4|b
    c-->|0.5|b
    d-->|2.2|c
    b-->|4.9|t
    c-->|2.3|t
    d-->|0.5|t
```

```mermaid
graph LR
    t-->|9|b
    t-->|1|c
    t-->|5|d
    b-->|5|c
    c-->|4|s
    d-->|6|s
    a-->|2|s
```

### tbs min 4

```mermaid
graph LR
    s-->|4.6|a
    s-->|4.4|c
    s-->|2.8|d
    a-->|4.4|b
    c-->|0.5|b
    d-->|2.2|c
    b-->|4.9|t
    c-->|2.3|t
    d-->|0.5|t
```

```mermaid
graph LR
    t-->|1|b
    t-->|1|c
    t-->|5|d
    b-->|1|c
    d-->|6|s
    a-->|2|s
```

### tds min 5

```mermaid
graph LR
    s-->|4.6|a
    s-->|4.4|c
    s-->|=7.8|d
    a-->|4.4|b
    c-->|4.5|b
    d-->|2.2|c
    b-->|8.9|t
    c-->|2.3|t
    d-->|5.5|t
```

## Результат
4 + 4 + 7 = 15