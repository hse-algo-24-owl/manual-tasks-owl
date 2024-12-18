# Задание №2
## Вычисление ленточного определителя (трехдиагональной матрицы) - вариант 1
#### Постановка задачи:
Дана трехдиагональная матрица порядка *n = 11* :

$$    
A =     
\begin{pmatrix}    
6 & -3 & 0 & \cdots & 0 & 0 \\    
9 & 6 & -3 & \cdots & 0 & 0 \\    
0 & 9 & 6 & \cdots & 0 & 0 \\    
\vdots  & \vdots & \vdots & \ddots & \vdots & \vdots  \\    
0 & 0 & 0 & \cdots & 6 & -3 \\    
0 & 0 & 0 & \cdots & 9 & 6     
\end{pmatrix}    
$$

Для решения задачи требуется:  
1. Вывести рекуррентное соотношение для предложенной матрицы.  
2. Составить и решить характеристическое уравнение.  
3. Вывести формулу общего решения.  
4. Рассчитать на основе полученной формулы значение определителя матрицы порядка *n* = 10.


---


### 1. Выведем рекуррентное соотношение:

Для матрицы

$$    
A =     
 \begin{pmatrix}    
  a & b & 0 & \cdots & 0 & 0 \\    
  c & a & b & \cdots & 0 & 0 \\    
  0 & c & a & \cdots & 0 & 0 \\    
  \vdots  & \vdots & \vdots & \ddots & \vdots & \vdots  \\    
  0 & 0 & 0 & \cdots & a & b \\    
  0 & 0 & 0 & \cdots & c & a     
 \end{pmatrix}    
$$

Будем искать определитель по первой строке. Т.к. первая строка состоит из элементов *a* и *b*, a остальные нули, нам потребуется произвести вычисления только для первых двух элементов строки матрицы.

∆<sub>n</sub> = *а* &middot; *А<sub>1 1</sub>* + *b* &middot; *А<sub>1 2</sub>*

1. a:

Вычислим *алгебраическое дополнение*

*А<sub>1 1</sub>* = (-1)<sup>1+1</sup> &middot; ∆*M<sub>1 1</sub>*

где *M<sub>1 1</sub>* - минор элемента *а*, получаемый вычеркиванием 1 строки и 1 столбца матрицы *A*

Рассмотрим минор: минором является матрица той же структуры, что и изначальная, только на порядок ниже (n - 1) ⇒ ∆*M<sub>1 1</sub>* = ∆<sub>n -1</sub>

Таким образом получаем:

$$
a \cdot A_{1 1} = a \cdot ∆_{n - 1}
$$

2. b:

Вычислим *алгебраическое дополнение*

*А<sub>1 2</sub>* = (-1)<sup>1+2</sup> &middot; ∆*M<sub>1 2</sub>*

Минор будет выглядеть следующим образом:

$$    
M_{1 2} =     
 \begin{pmatrix}        
  c  & b & \cdots & 0 & 0 \\    
  0  & a & \cdots & 0 & 0 \\    
  \vdots  & \vdots & \ddots & \vdots & \vdots  \\    
  0  & 0 & \cdots & a & b \\    
  0  & 0 & \cdots & c & a     
 \end{pmatrix}    
$$

Раскладывая определитель по строкам (столбцам) мы должны выполнить вычисления для каждого ненулевого элемента выбранной строки (столбца)

Заметим, что первый столбец *M<sub>1 2</sub>*  по первому столбцу имеет всего 1 элемент *с*. Следовательно, будем раскладывать определитель по первому столбцу.

Обратим внимание, что после вычеркивания 1 столбца и 1 строки минора мы получили первоначальную матрицу порядка *n-2*.

Получаем:

∆*M<sub>1 2</sub>* = с &middot; ∆<sub>n - 2</sub>

Объединим все результаты:

$$
\begin{cases}
A_{1 2} = (-1)^{1+2} \cdot ∆ M_{1 2};\\
∆ M_{1 2} = c \cdot ∆_{n - 2}.
\end{cases}
$$
$$
↓
$$
$$
A_{1 2} = (-1)^{1+2} \cdot c \cdot ∆_{n - 2}
$$
$$
↓
$$
$$
b \cdot A_{1 2}= b \cdot (-1) \cdot c \cdot ∆_{n - 2}
$$
#### Итоговая формула для поиска определителя порядка *n* :

$$
∆_n = a \cdot ∆_{n - 1} - b \cdot c \cdot ∆_{n - 2}
$$

В нашем случае:

$$    
A =     
 \begin{pmatrix}    
  6 & -3 & 0 & \cdots & 0 & 0 \\    
  9 & 6 & -3 & \cdots & 0 & 0 \\    
  0 & 9 & 6 & \cdots & 0 & 0 \\    
  \vdots  & \vdots & \vdots & \ddots & \vdots & \vdots  \\    
  0 & 0 & 0 & \cdots & 6 & -3 \\    
  0 & 0 & 0 & \cdots & 9 & 6     
 \end{pmatrix}    
$$

 а = 6, b = -3, c = 9;

Подставляем в общую формулу и получаем рекуррентное соотношение:

### ∆<sub>n</sub> = 6 &middot; ∆<sub>n-1</sub> + 27 &middot; ∆<sub>n-2</sub>
### 2. Составим и решим характеристическое уравнение
λ<sup>n</sup> = 6 &middot; λ<sup>n-1</sup> + 27 &middot; λ<sup>n-2</sup> | :λ<sup>n-2</sup>

λ<sup>2</sup> = 6λ + 27

λ<sup>2</sup> - 6λ - 27 = 0

Решаем квадратное уравнение и получаем корни:

$$
\begin{cases}
λ_1 = -3;\\
λ_2 = 9.
\end{cases}
$$

Сравниваем значения λ<sub>2</sub> и λ<sub>2</sub>: -3 ≠ 9
### 3. Вывод общей формулы поиска определителя *n<sub>го</sub>* порядка
В общем случае выражение выглядит следующим образом:
∆<sub>n</sub> = С<sub>1</sub> &middot; λ<sup>n</sup><sub>1</sub> + С<sub>2</sub> &middot; λ<sup>n</sup><sub>2</sub>

Коэффициенты С<sub>1</sub> и С<sub>2</sub> пока что не известны. Подставим найденные  значения λ<sub>2</sub> и λ<sub>2</sub> и получаем систему уравнение:

∆<sub>n</sub> = С<sub>1</sub> &middot; (-3)<sup>n</sup> + С<sub>2</sub> &middot; 9<sup>n</sup>

#### Поиск коэффициентов С<sub>1</sub> и С<sub>2</sub>:

Рассчитаем определители первого и второго порядка:

∆<sub>1</sub> = а = 6;

∆<sub>2</sub> = a<sup>2</sup> -  b &middot; c = 36 + 27 = 63.

После того как ∆<sub>1</sub> и ∆ <sub> 2</sub> стали известны, можем составить систему уравнений:

$$
\begin{cases}
6 = C_1 \cdot (-3)^1 + C_2 \cdot 9^1; \\
63 = C_1 \cdot (-3)^2 + C_2 \cdot 9^2. \\
\end{cases}
$$

Преобразуем и решим систему:

$$
\begin{cases}
6 = C_1 \cdot -3 + C_2 \cdot 9; \\
63 = C_1 \cdot 9 + C_2 \cdot 81. \\
\end{cases}
$$

Из 1<sub>го</sub> выражения:

$$
C_1 = \frac{6 - C_2 \cdot 9}{-3}
$$

$$
63 = 9 \cdot\frac{6 - C_2 \cdot 9}{-3} + C_2\cdot81
$$

Решив уравнение получаем  

$$
C_2 = 0,75
$$

Подставляем значение в формулу С<sub>1</sub>:

$$
C_1 = \frac{6 - 0,75 \cdot 9}{-3} = \frac{6 - 6,75}{-3} = \frac{-0,75}{-3} = 0,25
$$

#### Итого получаем формулу определителя n<sub>го</sub> порядка:

$$
∆_n = 0,25 \cdot (-3)^n + 0,75 \cdot 9^n
$$

### 4. Рассчет определителя 10<sub>го</sub> порядка
Произведем рассчеты при *n* = 11:

$$
∆_{11} = 0,25 \cdot (-3)^{11} + 0,75 \cdot 9^{11}
$$

$$
∆_{11} = - 3^{11} + 4^{11}
$$

$$
∆_{11} = 23535750420
$$



# Ответ

### ∆<sub>11</sub> = 23535750420
