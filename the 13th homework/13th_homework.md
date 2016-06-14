# The 13th homework

## Exercise List:

- 5.3 Use the symmetry of the capacitor problem(Figure5.6) to write a program that obtains the result by calculating the potential in only half of one quadrant of the x-y plane.

- 5.7 Write two programs to solve the capcacitor problem of Figure 5.6 and Figure 5.7, one using the Jacobi method and one using the SOR algorithm. For a fixed accuracy(as set by the convergence test) compare the number of iterations, N<sub>iter</sub>, that each slgorithm requires as a function of the number of grid elements, L. Show that for the Jacobi method N<sub>iter</sub> ~ L<sup>2</sup>, while with SOR N<sub>iter</sub> ~ L.

## Solutions:

### 5.3
- Here is the [**code**](code/problem5.3.py) of exercise 5.3.
- Here are two figures below that are exactly the same as the ones in the testbook. The former is a 3D view and the latter is a top-down view. We can see in the figure what is like that is in only one quadrant because all quadrants are here.

    <img src="img/5.3_1.png" width = "400" height = "400" alt="Problem5.3_1" align=center />
    <img src="img/5.3_2.png" width = "400" height = "400" alt="Problem5.3_2" align=center />

### 5.7
- Here is the [**code**](code/problem5.7.py) of exercise 5.7. 
- I didn't investigate the relationship between N<sub>iter</sub> and L or L<sup>2</sup>. However, I did compare the two different methods in some way. Here are 8 figures below, the left stand for the Jacobi method while the right stand for the SOR algorithm. Each row with a growing number of iterations that respectively are 10,50,500,5000. We can easily find the SOR algorithm is more optimizing comparing with the Jacobi method. However, the two methods become almost the same when N<sub>iter</sub> become bigger enough.

    <img src="img/5.7_1.png" width = "400" height = "400" alt="Problem5.7_1" align=center />
    <img src="img/5.7_2.png" width = "400" height = "400" alt="Problem5.7_2" align=center />
    
    <img src="img/5.7_3.png" width = "400" height = "400" alt="Problem5.7_3" align=center />
    <img src="img/5.7_4.png" width = "400" height = "400" alt="Problem5.7_4" align=center />
    
    <img src="img/5.7_5.png" width = "400" height = "400" alt="Problem5.7_5" align=center />
    <img src="img/5.7_6.png" width = "400" height = "400" alt="Problem5.7_6" align=center />
    
    <img src="img/5.7_7.png" width = "400" height = "400" alt="Problem5.7_7" align=center />
    <img src="img/5.7_8.png" width = "400" height = "400" alt="Problem5.7_8" align=center />
