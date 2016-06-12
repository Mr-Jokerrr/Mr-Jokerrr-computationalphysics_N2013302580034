# The 12th homework

## Exercise List:

- 4.16 Carry out a true three-body simulation in which the motions of Earth, Jupiter, and the Sun are all calculated. Since all three bodies are now in motion, it is useful to take the center of mass of the three-body system as the origin, rather than the position of Sun. We also suggest that you give Sun an initial velocity which makes the total momentum of the system exactly zero. Study the motion of Earth with different initial conditions. Alse, try increasing the mass of Jupiter to 10, 100, and 1000 times its true mass.

- 4.18 Investigate how close an asteroid must be to the precise gap resonance in order to be effectively "in" the gap. That is, study the effective width of the resonance in Figure4.14. Do this by performing the calculation of Figure4.15 for several asteroids whose orbits are near that of asteroid number 2. Calculate how much the orbit is "smeared out" as a function of the initial orbital radius.

- 4.20 Our results for the divergence of two trajectories θ<sub>1</sub>(t) and θ<sub>2</sub>(t) in the chaotic regime, shown on the right in Figure4.19, are complicated by the way we dealt with the angle θ. In Figure4.19 we followed the practice employed in Chapter 3 and restricted θ to the range -π to +π, since angles outside this range are equivalent to angles within it. However, when during the course of a calculation the angle passes out of this range and is then "reset", this shows up in the results for ∆θ as a discontinuous jump. Repeat the calculation of ∆θ as in Figure4.17, but do not restrict the value of θ. This should remove the large jumpsin ∆θ in Figure4.19, but the smaller and more frequent dips will remain. What is the origin of these dips?

## Solutions:

### 4.16
- Here is the [**code**](code/problem4.16.py) of exercise 4.16. Here the yellow ball represents the Sun while the blue one represents Earth and the red one represents Jupiter.
- To show the results clearly, I've made 4 gif figures below. The 4 gifs are with different coefficients. The first is with a coefficient that represent the  true mass of Jupiter while the following 3s respectively are 10, 100, 1000 times its true mass. We can easily find the differences between the 4 figures. With Jupiter's mass growing bigger, the motion of the three planets become unstable. And even when the mass of Jupiter went to 1000 times its true mass, Earth flew away and the Sun and Jupiter became a two-body system.

    <img src="img/4.16_1.gif" width = "400" height = "400" alt="Problem4.16_1" align=center />
    <img src="img/4.16_2.gif" width = "400" height = "400" alt="Problem4.16_2" align=center />
  
    <img src="img/4.16_3.gif" width = "400" height = "400" alt="Problem4.16_3" align=center />
    <img src="img/4.16_4.gif" width = "400" height = "400" alt="Problem4.16_4" align=center />

### 4.18
- Here is the [**code**](code/problem4.18.py) of exercise 4.18. 
- I just show the exact figure as the testbook did. And the right figure was enlargered. And the first two figures and the last two figures lasted different times.

    <img src="img/4.18_1.png" width = "400" height = "400" alt="Problem4.18_1" align=center />
    <img src="img/4.18_2.png" width = "400" height = "400" alt="Problem4.18_2" align=center />
  
    <img src="img/4.18_3.png" width = "400" height = "400" alt="Problem4.18_3" align=center />
    <img src="img/4.18_4.png" width = "400" height = "400" alt="Problem4.18_4" align=center />

### 4.20
- Here is the [**code**](code/problem4.20.py) of exercise 4.20.  
- When I was doing this exercise, some problem went into my work that is My figures are not just exactly the same as the examples in testbook. Maybe the step that the author chose wasn't 0.0001. So the figures may not look the same(Here I didn't give the figures I made comparing with the examples in the testbook). However, here is what I get using my code with step of 0.0001.

    <img src="img/4.20.png" width = "400" height = "400" alt="Problem4.20" align=center />
