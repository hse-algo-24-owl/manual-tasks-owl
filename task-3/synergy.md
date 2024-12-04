# Маршруты Вариант 4

Допустимые маршруты:

$$
\begin{aligned}
& - A \rightarrow A \\
& - A \rightarrow B \\
& - B \rightarrow A \\
& - B \rightarrow B \\
& - C \rightarrow A \\
& - C \rightarrow C \\
& - C \rightarrow B
\end{aligned}
$$

## Найти маршруты, начинающиеся в варианте $C$ и заканчивающиеся в варианте $B$

| $n$ | Маршруты                      | Кол-во |
| :---: | :----------------------------: | :---: |
| 1    | $C \rightarrow B$             | 1     |
| 2    | $C \rightarrow C \rightarrow B$ | 3     |
|      | $C \rightarrow A \rightarrow B$ |       |
|      | $C \rightarrow B \rightarrow B$ |       |
| 3    | $C \rightarrow C \rightarrow C \rightarrow B$ |  7    |
|      | $C \rightarrow C \rightarrow B \rightarrow B$ |       |
|      | $C \rightarrow B \rightarrow B \rightarrow B$ |       |
|      | $C \rightarrow C \rightarrow A \rightarrow B$ |       |
|      | $C \rightarrow A \rightarrow A \rightarrow B$ |       |
|      | $C \rightarrow A \rightarrow B \rightarrow B$ |       |
|      | $C \rightarrow B \rightarrow A \rightarrow B$ |       |

## Граф маршрутов

![Граф маршрутов](https://i.ibb.co/9hNmvXZ/2024-12-04-160028.png)

## Формулы

Пусть:
- $a_{n}$ — количество маршрутов, заканчивающихся в вершине $A$
- $b_{n}$ — количество маршрутов, заканчивающихся в вершине $B$
- $c_{n}$ — количество маршрутов, заканчивающихся в вершине $C$

Система уравнений:

$$
\begin{cases}
a_{n} = a_{n-1} + b_{n-1} + c_{n-1} \\
b_{n} = a_{n-1} + b_{n-1} + c_{n-1} \\
c_{n} = c_{n-1}
\end{cases}
$$


Из третьего уравнения $c_{n} = c_{n-1}$. Это означает, что $c_{n}$ остается постоянным и равным начальному значению $c_{0} = 1$.

$$
\begin{aligned}
& c_{n} = 1 \\
& \begin{cases}
a_{n} = a_{n-1} + b_{n-1} + 1 \\
b_{n} = a_{n-1} + b_{n-1} + 1
\end{cases}
\end{aligned}
$$

Так как $a_{n} = b_{n}$, то:

$$
b_{n} = b_{n-1} + b_{n-1} + 1 \\
b_{n} = 2b_{n-1} + 1
$$

Характеристическое уравнение:

Однородное равнение:

$$
\begin{aligned}
& r^{n} = 2r^{n-1} \\
& r = 2 \\
& b_{n}^{(g)} = C \cdot 2^{n}
\end{aligned}
$$

Частное решение:

$$
\begin{aligned}
& b_{n}^{(ch)} = A \text{ (константа)} \\
& A = 2A + 1 \\
& A = -1
\end{aligned}
$$

Общее решение:

$$
b_{n} = C \cdot 2^{n} - 1
$$

Подставим начальное условие $b_{1} = 1$:

$$
\begin{aligned}
& 1 = C \cdot 2^{1} - 1 \\
& C = 1
\end{aligned}
$$

Таким образом:

$$
b_{n} = 2^{n} - 1
$$

Проверка:

$$
\begin{aligned}
& n = 1, \quad b_{1} = 1 \\
& n = 2, \quad b_{2} = 3 \\
& n = 3, \quad b_{3} = 7
\end{aligned}
$$
