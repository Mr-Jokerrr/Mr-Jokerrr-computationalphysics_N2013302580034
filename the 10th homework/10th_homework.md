# The 10<sup>th</sup> homework

## Exercise List:

- 3.26 Continue the previous problem, and construct the phase-space plots as in Figure3.16 and 3.17 in the different regimes.

- 3.29 Explore the intermittency route to chaos for r>=163 in more detail. Begin by calculating z as a function of time for different values of r. Try r=163, and several larger values up to r=165 or so. For the larger values of r you should observe chaotic "hiccups".

## Solutions:

### 3.26 
- Here is the [**code**](code/problem3.26.py) of exercise 3.26. Below are three figure during the run time of the program. The first is the same as Figure3.16, we can find it just like two intertwined spirals which is a symbol of chaos.

  <img src="img/3.26_0.png" width = "400" height = "400" alt="Problem1.3" align=center />

  And the next two figure shows a evolution of the former figure with r increasing.

  <img src="img/3.26_1.png" width = "400" height = "400" alt="Problem1.3" align=center />
  <img src="img/3.26_2.png" width = "400" height = "400" alt="Problem1.3" align=center />

  So it can be easily find out that the increaing of r is a fundamental factor for chaos.

### 3.29
- Here is the [**code**](code/problem3.29.py) of exercise 3.29.The three figures below respectively shows the Lorenz variable z as a function of time, for high values of r. And approximately 163.8 seems to be a boundary between chaos and order. The fist figure is also seen in the textbook.

  <img src="img/3.29_0.png" width = "400" height = "400" alt="Problem1.3" align=center />

  And the following two figures are of two values of r that are near 163.8.

  <img src="img/3.29_1.png" width = "400" height = "400" alt="Problem1.3" align=center />
  <img src="img/3.29_2.png" width = "400" height = "400" alt="Problem1.3" align=center />
 
  So we can see from the figures, the bigger r goes the more unpredictable z goes. The "hiccups" will become more and the averange time between these hiccups will be less.
