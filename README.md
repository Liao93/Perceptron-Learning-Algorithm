# Perceptron-Learning-Algorithm

## Environment
  - Python 3.7.1
  - numpy 1.19.2
  - matplotlib 3.3.2

## The format of input.txt
  x1 x2 y
  
  x1 x2 y
  
  x1 x2 y
  
  .
  
  .
  
  .
  
## Algorithm
  - Initialize W by zero.
  - If find any Xn such that sign(W ‧ Xn) != sign(Yn), then update W = W + Yn*Xn.
  - If no more mistakes, return the last W.
  - To avoid infinite loop, I set the maximum number of loops of 100.
  
  
## Demo
  - w0: -1.0
  - w1: 40.3
  - w2: 30.400000000000006
  ---
  ![demo1](./img/pla_at1.png)
  ![demo2](./img/pla_at2.png)
  ![demo3](./img/pla_at3.png)
  ![demo4](./img/pla_at4.png)
  
  - The points with shape of 'o' should be classified to 'yes', otherwise, 'no'
  - The points with color of blue are predicted to 'yes' by the perceptron, and the red ones are predicted to 'no'.
 
