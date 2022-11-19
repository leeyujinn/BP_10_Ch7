# 4. 터틀 그래픽에서 거북이를 움직이지 않고 선을 긋는 함수 draw_line()을 정의하고 이것을 이용하여 다음과 같은 거미줄과 같은 모양을 그려보자. 거북이는 항상 중앙에 위치한다.
import turtle  # turtle 라이브러리 불러오기
t = turtle.Turtle()  # 변수 t에 turtle.Turtle()을 선언
t.shape("turtle")  # turtle 도형 가져오기
t.speed(0)  # 속도를 0으로 함


def draw_line():  # draw_line으로 함수를 선언
    t.forward(100)  # 앞으로 100만큼 전진
    t.backward(100)  # 뒤로 100만큼 이동


for x in range(12):  # 변수 x를 12번 반복
    t.right(30)  # 오른쪽으로 30도 회전
    draw_line()  # 선을 그림

t._screen.exitonclick()  # 마우스로 클릭해야 화면이 종료됨
