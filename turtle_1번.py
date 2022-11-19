# 1. 눈사람을 그리는 함수를 작성하고 이 함수를 여러 번 호출하여서 랜덤한 위치에 눈사람을 그리는 프로그램을 작성하라. 아래 실행 결과와 최대한 비슷하게 작성해보자.
import turtle  # turtle 라이브러리 불러오기
t = turtle.Turtle()  # 변수 t에 turtle.Turtle()를 선언
t.shape("turtle")  # turtle 도형 가져오기
t.color("black", "white")  # 선:검은색, 채우기:흰색으로 지정
s = turtle.Screen()  # 변수 s에 turtle.Screen()을 선언
s.bgcolor('skyblue')  # 배경색을 하늘색으로 지정


def draw_snowman(x, y):
    t.up()  # 펜 올리기
    t.goto(x, y)  # (x,y)로 이동
    t.down()  # 펜 내리기
    t.begin_fill()  # 도형을 색칠할 준비
    t.circle(20)  # 반지름이 20인 원을 그림
    t.end_fill()  # 그린 도형에 색칠하기
    t.goto(x, y-25)  # (x,y-25)로 이동
    t.setheading(135)  # 거북이가 바라보는 방향을 135도로 함
    t.forward(50)  # 앞으로 50만큼 전진
    t.backward(50)  # 뒤로 50만큼 이동

    t.setheading(30)  # 거북이가 바라보는 방향을 30도로 함
    t.forward(50)  # 앞으로 50만큼 전진
    t.backward(50)  # 뒤로 50만큼 이동
    t.setheading(0)  # 거북이가 바라보는 방향을 0도로 함

    t.begin_fill()  # 도형을 색칠할 준비
    t.circle(15)  # 반지름이 15인 원을 그림
    t.end_fill()  # 그린 도형에 색칠하기
    t.goto(x, y-70)  # (x,y-70)으로 이동
    t.begin_fill()  # 도형을 색칠할 준비
    t.circle(30)  # 반지름이 30인 원을 그림
    t.end_fill()  # 그린 도형에 색칠하기


draw_snowman(0, 0)  # x,y에 0,0을 대입
draw_snowman(100, 0)  # x,y에 100,0을 대입
draw_snowman(200, 0)  # x,y에 200,0을 대입

t._screen.exitonclick()  # 마우스를 클릭해야 화면이 종료됨
