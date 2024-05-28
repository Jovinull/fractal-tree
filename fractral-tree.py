import turtle
import random

def draw_branch(branch_length, t, pen_size):
    if branch_length > 5:
        # Define a cor baseada no comprimento do galho
        if branch_length < 20:
            # Cor aleatória para folhas
            t.color(random.choice(["green", "darkgreen", "red", "orange"]))
            t.pensize(pen_size / 2)
        else:
            # Gradiente no tronco
            t.color((0.55 * branch_length / 100, 0.27 * branch_length / 100, 0.07))
            t.pensize(pen_size)
        
        t.forward(branch_length)
        
        # Variedade aleatória para um aspecto mais natural
        angle = random.randint(15, 30)
        length_factor = random.uniform(0.6, 0.8)

        # Desenha a perna direita
        t.right(angle)
        draw_branch(branch_length * length_factor, t, pen_size * 0.7)
        
        # Volta à posição inicial
        t.left(2 * angle)
        
        # Desenha a perna esquerda
        draw_branch(branch_length * length_factor, t, pen_size * 0.7)
        
        # Volta à posição inicial
        t.right(angle)
        t.backward(branch_length)
        
        # Se o comprimento do galho for pequeno, desenha uma folha
        if branch_length < 20:
            t.color(random.choice(["green", "darkgreen", "red", "orange"]))
            t.begin_fill()
            t.circle(3)
            t.end_fill()
            
            # Adiciona frutos ocasionalmente
            if random.random() > 0.7:
                t.color("red")
                t.begin_fill()
                t.circle(3)
                t.end_fill()

def draw_star(x, y, size, t):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
        t.forward(size)
        t.right(144)
    t.end_fill()

def draw_grass(t):
    t.color("green")
    t.pensize(3)
    for _ in range(30):
        t.penup()
        x = random.randint(-300, 300)
        y = random.randint(-300, -200)
        t.goto(x, y)
        t.pendown()
        t.forward(random.randint(10, 20))

def draw_moon(t):
    t.penup()
    t.goto(200, 200)
    t.pendown()
    t.color("lightyellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()

def draw_fairy(x, y, t):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(2)
    t.end_fill()

def draw_firefly(t):
    t.color("yellow")
    t.penup()
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(1)
    t.end_fill()

def draw_cloud(x, y, t):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    for i in range(3):
        t.penup()
        t.goto(x + 20 * i, y)
        t.pendown()
        t.begin_fill()
        t.circle(20)
        t.end_fill()

def draw_root(t):
    t.color("saddlebrown")
    t.pensize(3)
    for _ in range(5):
        t.penup()
        x = random.randint(-50, 50)
        y = random.randint(-250, -200)
        t.goto(x, y)
        t.pendown()
        t.forward(random.randint(10, 20))

def draw_mushroom(t):
    t.color("red")
    t.penup()
    x = random.randint(-100, 100)
    y = random.randint(-250, -230)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.color("white")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for _ in range(5):
        t.forward(4)
        t.right(72)
        t.forward(4)
        t.right(72)
    t.end_fill()

def main():
    # Configuração inicial
    window = turtle.Screen()
    window.bgcolor("midnightblue")
    
    # Criação da tartaruga
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(0)
    
    # Adiciona estrelas no céu
    for _ in range(20):
        x = random.randint(-300, 300)
        y = random.randint(100, 300)
        size = random.randint(5, 10)
        draw_star(x, y, size, t)
    
    # Adiciona a lua
    draw_moon(t)
    
    # Adiciona nuvens no céu
    for _ in range(5):
        x = random.randint(-300, 300)
        y = random.randint(150, 250)
        draw_cloud(x, y, t)
    
    # Adiciona grama na base
    draw_grass(t)
    
    # Adiciona raízes
    draw_root(t)
    
    # Adiciona cogumelos
    for _ in range(10):
        draw_mushroom(t)
    
    # Posiciona a tartaruga
    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.left(90)
    t.color("saddlebrown")
    
    # Inicia a recursão para desenhar a árvore
    draw_branch(100, t, 10)
    
    # Adiciona fadas brilhantes
    for _ in range(10):
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        draw_fairy(x, y, t)
    
    # Adiciona vagalumes
    for _ in range(20):
        draw_firefly(t)
    
    # Fecha a janela ao clicar
    window.exitonclick()

if __name__ == "__main__":
    main()
