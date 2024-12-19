## Задание 5
### Задача о разделении процессоров - вариант 10
<style>


    
@keyframes funnyJump {
  0% {
    transform: translateY(0) scale(1);
    opacity: 0;
  }
  25% {
    transform: translateY(-20px) scale(1.2);
  }
  50% {
    transform: translateY(0) scale(1);
  }
  75% {
    transform: translateY(-10px) scale(1.1);
  }
  100% {
    transform: translateY(0) scale(1);
    opacity: 1;
  }
}

@keyframes funnySpin {
  0% {
    transform: rotate(0deg);
  }
  50% {
    transform: rotate(360deg);
  }
  100% {
    transform: rotate(720deg);
  }
}

@keyframes gradientAnimation {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

body {
  animation: gradientAnimation 2s ease infinite, funnyJump 2s ease-out, funnySpin 3s  ease-in-out;
  background-image: linear-gradient(to right bottom, #e66fb3, #cb73bc, #af77bf, #9379bd, #7a7ab6, #6379af, #4e76a4, #3e7398, #276f8a, #16697a, #136369, #1a5c58);
  background-size: 400% 400%;
  animation: 
  height: 100vh;
  margin: 0;
}

body {
  
}

h1 {
  animation: funnyJump 1s ease-out, funnySpin 2s  ease-in-out;
}

p {
  animation: funnyJump 1.5s ease-out, funnySpin 1.5s  ease-in-out;
}
</style>

    
</style>



<hr>
Имеется 4 независимых задания: 
<center>

|  A  |  B  |  C  |  D  |
|:---:|:---:|:---:|:---:|
|  20 |  14 |  7 |   7 |

</center>

И 2 исполнителя:
<center>

| Исполнители         |  1  |  2  |
|:-------------------|:---:|:---:|
| Производительность (p)  |  3  |  1  |

</center>

Требуется составить минимально возмножное раписание и предоставить в виде диаграммы Ганта.
<hr>
Для начала посчитаем минимальное время, за которое можно выполнить все задания:

$$  
t_{min} = \frac {20+14+7+7}{3+1}  =  12
$$  


Требуемое расписание должно занимать 12 у.е. времени.
<hr>
Будем пользоваться сдледующим алгоритмом: будем определять приоритеты заданий, и будем назначать исполнителей на задания в соответсвии с приоритетами. Далее будем составлять уравнения и искать мимнимальное время, когда какие-либо задания сравняются. Приведя все задания к равному состоянию, распределим их равномерно среди исполнителей на оставшееся время.
<hr>
Момент времени
<div style = 'position:absolute; margin-top: -2.5em; margin-left: 8.9em'>

$$
t = 0:
$$

</div>

<br>

Расставим приоритеты для каждой из задачи: 

<center>

|  A  |  B  |  C  |  D  |
|:---:|:---:|:---:|:---:|
|  20 |  14 |  7 |   7 |
|  I  |  II  |  III  |  III  |
|  <div style="margin-top:-1.3em"> $$ p_{1} $$  </div>  |  <div style="margin-top:-1.3em">  $$ p_{2} $$  </div>|  

</center>

Составим уравнения.

<div style = 'position:absolute; margin-top: -1.7em; '>

$$ A = B: $$

</div>

$$ 
20 - 3t = 14 - t
\\
2t = 6
\\
t = 3 
$$

<div style = 'position:absolute; margin-top: -1.7em; '>

$$ B = C: $$

</div>

$$ 
14 - t = 7
\\
t = 7
$$

Можно заметить, что минимальное время, через которое произойдёт выравнивание работ – 3. Поэтому отправиляем исполнителей 1 и 2 на задачи A и B соответственно на 3 у. е. времени.
<hr>
Момент времени
<div style = 'position:absolute; margin-top: -2.5em; margin-left: 8.9em'>

$$
t = 3:
$$

</div>

<br>

Расставим приоритеты для каждой из задачи: 

<center>

|  A  |  B  |  C  |  D  |
|:---:|:---:|:---:|:---:|
|  11 |  11 |  7 |   7 |
|  I  |  I  |  II  |  II  |

<div style="margin-top:-1.3em; margin-left: -3.5em "> 

$$ (p_{1}p_{2})'/2 $$  

</div>

</center>
Оба исполниеля будут работать на первом приоритете, выполняя задачи A и B.
<br>
Составим уравнениe.

<div style = 'position:absolute; margin-top: -0.5em; '>

$$ AB = CD: $$

</div>

$$
11 - ((3 + 1)/2)t = 7
\\
11 - 2t = 7
\\
2t = 4
\\
t = 2
$$

Минимальное время, через которое произойдёт выравнивание работ – 2. Поэтому отправиляем исполнителей 1 и 2 на задачи A и B на 2 у. е. времени.
<hr>
Момент времени
<div style = 'position:absolute; margin-top: -2.5em; margin-left: 8.9em'>

$$
t = 5:
$$

</div>

<br>

Расставим приоритеты для каждой из задачи: 

<center>

|  A  |  B  |  C  |  D  |
|:---:|:---:|:---:|:---:|
|  7 |  7 |  7 |   7 |
|  I  |  I  |  I  |  I  |


</center>

Можно заметить, что все задачи сравнялись. Поэтому далее просто распределяем все задачи равномерно на оставшееся время – 7 у. е. времени.

Диаграмма Ганта:

```mermaid
gantt
    title Диаграмма Ганта для задачи
    dateFormat DD HH:mm
    axisFormat %H:%M
    Начало выполнения работ : milestone, m1, 01 00:00, 0h
    A = B : milestone, m1, 01 03:00, 0h
    A=B=C=D : milestone, m1, 01 05:00, 0h
    section Исполнитель 1
    A         :a1, 01 00:00, 3h
    A         :a2, after a1, 1h
    B         :a3, after a2, 1h
    A         :a4, after a3, 105m
    B         :a5, after a4, 105m
    C         :a6, after a5, 105m
    D         :a7, after a6, 105m
    section Исполнитель 2
    B         :b1, 01 00:00, 3h
    B         :b2, after b1, 1h
    A         :b3, after b2, 1h
    B         :b4, after b3, 105m
    C         :b5, after b4, 105m
    D         :b6, after b5, 105m
    A         :b7, after b6, 105m
    Окончание выполнения работ : milestone, m2, 01 12:00, 0h


```