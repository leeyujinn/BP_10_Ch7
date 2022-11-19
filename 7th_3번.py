# 3. 함수 f(x)=x^2+1을 계산하는 함수를 작성하고 이 함수를 이용하여 화면에 f(x)를 그려보자.
import turtle  # turtle 라이브러리 불러오기
t = turtle.Turtle()  # 변수 t에 turtle.Turtle()을 선언
t.shape("turtle")  # turtle 도형 불러오기
t.speed(0)  # 속도를 0으로 함


def f(x):  # f(x)로 함수 선언
    return x**2+1  # x**2+1의 결과값을 반환


t.goto(200, 0)  # (200,0)으로 이동
t.goto(0, 0)  # (0,0)으로 이동
t.goto(0, 200)  # (0,200)으로 이동
t.goto(0, 0)  # (0,0)으로 이동

for x in range(150):  # 변수 x를 150번 반복
    t.goto(x, int(0.01*f(x)))  # (x,int(0.01*f(x)))로 이동

t._screen.exitonclick()  # 마우스로 클릭해야 화면이 종료됨
