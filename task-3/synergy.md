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

## Найти маршруты, начинающиеся в вершине $C$ и заканчивающиеся в вершине $B$

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

Так как $\ a_n = b_n \$, то:

$$
\begin{align*}
b_n = b_{n-1} + b_{n-1} + c_{n-1} = 2b_{n-1} + c_{n-1}
\end{align*}
$$


Выризим $c_{n}$ из первого уравнения:


$$
\begin{align*}
c_n = c_{n-1} = a_n - a_{n-1} - b_{n-1} = b_n - b_{n-1} - b_{n-1} = b_n - 2b_{n-1}
\end{align*}
$$

$$
\begin{align*}
c_{n-1} = b_{n-1} - 2b_{n-2}
\end{align*}
$$

Подставим $с_{n-1}$ в $b_{n}$:

$$
\begin{align*}
b_n = 2b_{n-1} + b_{n-1} - 2b_{n-2}
\end{align*}
$$

$$
\begin{align*}
b_n = 3b_{n-1} - 2b_{n-2}
\end{align*}
$$

Теперь найдем характеристическое уравнение для $\ b_n \$:

$$
\begin{align*}
t^2 - 3t + 2 = 0
\end{align*}
$$

Решим характеристическое уравнение:

$$
\begin{align*}
t_1 = 1, \quad t_2 = 2
\end{align*}
$$

Так как $t_1 \neq t_2$ общее решение будет:

$$
\begin{align*}
b_n = C_1 \cdot 1^n + C_2 \cdot 2^n
\end{align*}
$$

Используем начальные условия $b_{1} = 1$  и  $b_{2} = 3$:

$$
\begin{cases}
1 = C_1 \cdot 1 + C_2 \cdot 2 \\
3 = C_1 \cdot 1 + C_2 \cdot 2^2
\end{cases}
$$


Решим систему уравнений:

$$
\begin{cases}
C_1 = -1 \\
C_2 = 1
\end{cases}
$$

Таким образом, рекуррентное соотношение для $b_{n}$ будет:

$$
\begin{align*}
b_n = -1 \cdot 1^n + 1 \cdot 2^n = 2^n - 1
\end{align*}
$$

Проверка:

$$
\begin{aligned}
& n = 1, \quad b_{1} = 1 \\
& n = 2, \quad b_{2} = 3 \\
& n = 3, \quad b_{3} = 7
\end{aligned}
$$
