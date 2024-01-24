# HW06

## Watch
1. National Instruments
2. PREEMPT_RT is the name of the patchset hosted at the Linux Foundation to implement a priority scheduler and other supporting real-time mechanisms
3. When a system has to run both time-critical and non time-critical tasks
4. Driver stacks are shared between RT tasks and non-RT tasks
5. Time between an event to occur until the relevant real-time task executes
6. Cyclictest measures the lantencies of real-time systems.
7. The deltas with and without preept_rt
8. Dispatch latency is the time between the harware event firing and the thread waking up. Scheduling latency is the time between the relevant thread being woken up and the CPU executing that task
9. Mainline refers to new, up to date kernels
10. Non-critical IRQ must be finished for External event to be able to run
11. External event can start and finish before the non critical IRQ finishes running

## PREEMPT_RT
Make sure that gnuplot and xdg-open are installed

in hw06/rt:

heavy load RT data is stored in rt_load.hist

no load RT data is stored in rt_noload.hist

heavy load no RT data is stored in nort_load.hist

no load no RT data is stored in nort_noload.hist

run the following command to generate the histogram: gnuplot hist_load.plt

run the following command to display the image: xdg-open cyclictest.png

# hw06 grading

| Points      | Description | |
| ----------- | ----------- |-|
|  2/2 | Project 
|  5/5 | Questions
|  4/4 | PREEMPT_RT
|  2/2 | Plots to 500 us
|  5/5 | Plots - Heavy/Light load
|  2/2 | Extras
| 20/20 | **Total**

*My comments are in italics. --may*

 | *Mainline is the main kernel tree.*