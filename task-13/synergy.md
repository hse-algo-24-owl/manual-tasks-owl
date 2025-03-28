# Задание №13
# Задача о рюкзаке (Knapsack problem). Генетический алгоритм. Вариант 1.
## Условия задачи
Решить задачу о рюкзаке с применением генетического алгоритма, с учетом следующих требований:
   - Придумать условия задачи с количеством предметов не менее 7.
   - Численность популяции не менее 4 особей, в скрещивании участвует половина популяции. 
   - Для скрещивания выбираются сильнейшие особи, скрещивание – одноточечное.
   - До выполнения алгоритма сформулировать стратегию применения оператора мутации.
   - Сформировать не менее 3 поколений, не считая первоначального.


|    **Вес**    |  2   |  3   |  4   |  5   |  6   |  7   |  8   |
|:-------------:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| **Стоимость** |  8   |  7   |  6   |  5   |  4   |  3   |  2   |

Ограничение по весу: 15

Пусть мутация будет применяться к любому гену, то есть любой ген может менять своё значение на противоположное. 
Если стоимость двух особей одинакова, то для скрещивания выбирается любая из них.
Для нового поколения отбираются сильнейшие особи из прошлого поколения (те, которые учавствовали в скрещивании) и особи, полувшиеся после скрещивания.

#### Поколение 1
|         |     |     |     |     |     |     |     | **S**|
|:--------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:----:|
| **x_1** |  1  |  1  |  1  |  1  |  0  |  0  |  0  |**26**|
| **x_2** |  1  |  0  |  0  |  1  |  0  |  1  |  0  |**16**|
| **x_3** |  0  |  0  |  0  |  0  |  0  |  1  |  1  |  5   |
| **x_4** |  0  |  0  |  1  |  1  |  1  |  0  |  0  |  15  |

#### Поколение 2
|         |     |     |     |     |     |     |     | **S**|
|:--------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:----:|
| **x_1** |  1  |  1  |  1  |  1  |  0  |  0  |  0  |**26**|
| **x_2** |  1  |  0  |  0  |  1  |  0  |  1  |  0  |  16  |
| **x_5** |  0  |  1  |  1  |  0  |  0  |  1  |  0  |**16**|
| **x_6** |  1  |  0  |  0  |  1  |  0  |  0  |  0  |  13  |

#### Поколение 3
|         |     |     |     |     |     |     |     | **S**|
|:--------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:----:|
| **x_1** |  1  |  1  |  1  |  1  |  0  |  0  |  0  |**26**|
| **x_5** |  0  |  1  |  1  |  0  |  0  |  1  |  0  |  16  |
| **x_7** |  1  |  1  |  0  |  0  |  0  |  1  |  0  |**18**|
| **x_8** |  0  |  1  |  1  |  1  |  0  |  0  |  0  |  18  |

#### Поколение 4
|         |     |     |     |     |     |     |     | **S**|
|:--------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:----:|
| **x_1** |  1  |  1  |  1  |  1  |  0  |  0  |  0  |  26  |
| **x_7** |  1  |  1  |  0  |  0  |  0  |  1  |  0  |  18  |
| **x_9** |  1  |  1  |  1  |  0  |  0  |  0  |  0  |  21  |
| **x_10**|  1  |  1  |  0  |  1  |  0  |  0  |  0  |  20  |

#### Скрещивания

#### 1 Скрещивание: **x_1** и **x_2**:

 |         |           |     |     |           |     |     |     |**Вес**|**Мутация**|**S**|
 |:-------:|:---------:|:---:|:---:|:---------:|:---:|:---:|:---:|:-----:|:---------:|:---:|
 | **x_1** |  1        |  1  |  1  |  1        |  0  |  0  |  0  |       |           |     |
 | **x_2** |  1        |  0  |  0  |  1        |  0  |  1  |  0  |       |           |     |
 | **x_5** |1(станет 0)|  1  |  1  |1(станет 0)|  0  |  1  |  0  |22 > 15| Да        | 16  |
 | **x_6** |  1        |  0  |  0  |  1        |  0  |  0  |  0  | 7 < 15| Нет       | 13  |

#### 2 Скрещивание: **x_1** и **x_5**:

 |         |     |     |           |     |     |     |     |**Вес**|**Мутация**|**S**|
 |:-------:|:---:|:---:|:---------:|:---:|:---:|:---:|:---:|:-----:|:---------:|:---:|
 | **x_1** |  1  |  1  |  1        |  1  |  0  |  0  |  0  |       |           |     |
 | **x_5** |  0  |  1  |  1        |  0  |  0  |  1  |  0  |       |           |     |
 | **x_7** | 1   |  1  |1(станет 0)|  0  |  0  |  1  |  0  |16 > 15| Да        | 18  |
 | **x_8** |  0  |  1  |  1        |  1  |  0  |  0  |  0  |12 < 15| Нет       | 18  |

#### 3 Скрещивание: **x_1** и **x_7**:

 |         |     |     |     |     |     |           |     |**Вес**|**Мутация**|**S**|
 |:-------:|:---:|:---:|:---:|:---:|:---:|:---------:|:---:|:-----:|:---------:|:---:|
 | **x_1** |  1  |  1  |  1  |  1  |  0  |  0        |  0  |       |           |     |
 | **x_7** |  1  |  1  |  0  |  0  |  0  |  1        |  0  |       |           |     |
 | **x_9** |  1  |  1  |  1  |  0  |  0  |1(станет 0)|  0  |16 > 15| Да        | 21  |
 | **x_10**|  1  |  1  |  0  |  1  |  0  |0          |  0  |10 < 15| Нет       | 20  |

#### Ответ

Лидер 4-го поколения особь **x_1**, берем предметы 1, 2, 3, 4 (111100), стоимость = 26, вес = 14, свободное место = 1.
