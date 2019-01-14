---
title: "PERCEPTRON TUTORIAL"
---

# perceptron

> 다수의 신호를 입력으로 받아 하나의 신호를 출력합니다.
> <br/>1이나 0 두 가지 값을 가질 수 있습니다. 1은 신호가 흐른다, 0은 신호가 흐르지 않는다의 의미를 가집니다.<br/>
> 아래 수식은 입력으로 2개의 신호를 받은 퍼셉트론의 수식입니다.<br/><br/>
> x<sub>1</sub>, x<sub>2</sub> : 입력신호<br/>
> w<sub>1</sub>, w<sub>2</sub> : 가중치<br/>
> <a href="https://www.codecogs.com/eqnedit.php?latex=y&space;=&space;\left\{\begin{matrix}&space;0\,&space;(w_{1}x_{1}&space;&plus;&space;w_{2}x_{2}&space;\leq&space;\Theta&space;)&space;\\&space;1&space;(w_{1}x_{1}&space;&plus;&space;w_{2}x_{2}&space;>&space;\Theta&space;)&space;\end{matrix}\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?y&space;=&space;\left\{\begin{matrix}&space;0\,&space;(w_{1}x_{1}&space;&plus;&space;w_{2}x_{2}&space;\leq&space;\Theta&space;)&space;\\&space;1&space;(w_{1}x_{1}&space;&plus;&space;w_{2}x_{2}&space;>&space;\Theta&space;)&space;\end{matrix}\right." title="y = \left\{\begin{matrix} 0\, (w_{1}x_{1} + w_{2}x_{2} \leq \Theta ) \\ 1 (w_{1}x_{1} + w_{2}x_{2} > \Theta ) \end{matrix}\right." /></a><br/><br/>
> 입력신호가 뉴런에 보내질 때는 각각 고유한 가중치가 곱해집니다. 뉴런에서 보내온 신호의 총합이 정해진 한계를 넘어설 때만 1을 출력합니다. 그 한계를 임계값이라 하며 <a href="https://www.codecogs.com/eqnedit.php?latex=\Theta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\Theta" title="\Theta" /></a> 기호로 나타냅니다.<br/><br/>
> 가중치는 그 값이 클수록 강한 신호를 흘려보냅니다.

### 가중치와 편향 도입

>앞서 구현한 AND 게이트는 알기 쉽지만 앞으로를 생각해서 다른 방식으로 수정하고자 합니다.
<a href="https://www.codecogs.com/eqnedit.php?latex=y&space;=&space;\left\{\begin{matrix}&space;0\,&space;(b&space;&plus;&space;w_{1}x_{1}&space;&plus;&space;w_{2}x_{2}&space;\leq&space;0&space;)&space;\\&space;1&space;(b&space;&plus;&space;w_{1}x_{1}&space;&plus;&space;w_{2}x_{2}&space;>&space;0&space;)&space;\end{matrix}\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?y&space;=&space;\left\{\begin{matrix}&space;0\,&space;(b&space;&plus;&space;w_{1}x_{1}&space;&plus;&space;w_{2}x_{2}&space;\leq&space;0&space;)&space;\\&space;1&space;(b&space;&plus;&space;w_{1}x_{1}&space;&plus;&space;w_{2}x_{2}&space;>&space;0&space;)&space;\end{matrix}\right." title="y = \left\{\begin{matrix} 0\, (b + w_{1}x_{1} + w_{2}x_{2} \leq 0 ) \\ 1 (b + w_{1}x_{1} + w_{2}x_{2} > 0 ) \end{matrix}\right." /></a>
<br/>
퍼셉트론은 입력신호에 가중치를 곱한 값과 편향을 합하여, 그 값이 0을 넘으면 1을 출력, 그렇지 않으면 0을 출력합니다.
<br/>
편향은 가중치 w<sub>1</sub>, w<sub>2</sub> 와 기능이 다르다는 사실에 주의합시다. 구체적으로 말하면 w<sub>1</sub>과 w<sub>2</sub>는 각 입력 신호가 결과에 주는 영향력(중요도)을 조절하는 매개변수고, **편향**은 뉴런이 얼마나 쉽게 활성화(결과로 1을 출력) 하느냐를 조정하는 매개변수 입니다. 예를 들어 b가 -0.1 이면 각 입력 신호에 가중치를 곱한 값들의 합이 0.1을 초과할 때만 뉴런이 활성화합니다. 반면 b가 -20.0이면 각 입력 신호에 가중치를 곱한 값들의 합이 20.0을 넘지 않으면 뉴런은 활성화하지 않습니다. 이처럼 편향의 값은 뉴런이 얼마나 쉽게 활성화되는지를 결정합니다.



 출처 : Deep Learning from Scratch ( 밑바닥부터 시작하는 딥러닝 ) 










