# 2. 6각형을 그리는 draw_hexa() 함수를 작성하고 이 함수를 호출하여서 다음과 같은 벌집 모양을 화면에 그려보자.
import turtle  # turtle 라이브러리 불러오기
t = turtle.Turtle()  # 변수 t에 turtle.Turtle()를 선언
t.shape("turtle")  # turtle 모양 불러오기
t.speed(0)  # 속도를 0으로 함


def hexagon():  # hexagon으로 함수 선언
    for i in range(6):  # 변수 i를 6번 반복
        turtle.forward(100)  # 앞으로 100만큼 전진
        turtle.left(360/6)  # 왼쪽으로


for i in range(6):  # 변수 i를 6번 반복
    hexagon()  # 육각형을 출력
    turtle.forward(100)  # 앞으로 100만큼 전진
    turtle.right(60)  # 오른쪽으로 60도 회전

t._screen.exitonclick()  # 마우스로 클릭해야 화면이 종료됨
