from manim import *

class MyCircle(Arc):
    def __init__(
        self,
        radius: float = None,
        color=RED,
        **kwargs,
    ):
        super().__init__(
            radius=radius,
            start_angle=0,
            angle=-TAU,
            color=color,
            **kwargs,
        )

class Algoritmos(Scene):
  def construct(self):
    title = Text("¿Qué tan rápido es un algoritmo?").move_to(2*UP)
    alg = Text("Algoritmo").to_edge(UL).scale(0.8)
    time = Text("Tiempo").to_edge(UL).scale(0.8)
    alg1=Text(" de Ordenamiento").scale(0.8).next_to(alg.get_right()+UP*0.01)
    alg2=Text(" de Busqueda").scale(0.8).next_to(alg.get_right()+UP*0.01)
    alg3=Text(" de Multiplicación").scale(0.8).next_to(alg.get_right()+UP*0.01)

    face = ImageMobject("face.png").scale(0.8).move_to(6*DOWN)

    a = Circle(color=RED,fill_opacity=1).scale(0.7).move_to(LEFT*5)
    b = Square(color=GREEN,fill_opacity=1).scale(0.7).move_to(LEFT*2.5)
    c = RegularPolygon(n=6,color=YELLOW,fill_opacity=1).scale(0.8)
    d = Triangle(color=BLUE,fill_opacity=1).scale(0.8).move_to(RIGHT*2.5)

    uno = Text("1").scale(0.5).move_to(a.get_center()).set_color(BLACK)
    a1 = Arrow(start=a.get_right(),end=b.get_left(),buff=0)

    dos = Text("2").scale(0.5).move_to(b.get_center()).set_color(BLACK)
    a2 = Arrow(start=b.get_right(),end=c.get_left(),buff=0)

    tres = Text("3").scale(0.5).move_to(c.get_center()).set_color(BLACK)
    a3 = Arrow(start=c.get_right(),end=d.get_left(),buff=0)

    cuatro = Text("4").scale(0.5).move_to(d.get_center()).set_color(BLACK)
    algorithm=VGroup(a,b,c,d)
    stuff=VGroup(uno,dos,tres,cuatro,a1,a2,a3)

    self.wait()
    self.play(Write(title),face.animate.shift(UP*5.5),run_time=3)
    self.play(FadeOut(title))

    self.play(FadeIn(alg),face.animate.to_edge(DR),run_time=3)
    self.play(FadeIn(algorithm),run_time=2)
    self.play(FadeIn(uno),FadeIn(dos),GrowArrow(a1),tun_time=3)
    self.play(FadeIn(tres),GrowArrow(a2),tun_time=3)
    self.play(FadeIn(cuatro),GrowArrow(a3),tun_time=3)
    self.play(FadeOut(stuff),FadeOut(face),FadeOut(algorithm),run_time=2)

    #Ordenamiento
    axes = NumberPlane(x_range=[0,6],y_range=[0,6],x_length=5,y_length=5)
    f1 = axes.get_graph(lambda x: 6,x_range=[0,1],color=BLUE_C)
    a1 = axes.get_area(graph=f1,x_range=[0,0.5],color=BLUE_C).shift(RIGHT*0.83)
    f2 = axes.get_graph(lambda x: 5,x_range=[0,2],color=BLUE_C)
    a2 = axes.get_area(graph=f2,x_range=[1,1.5],color=BLUE_C).shift(RIGHT*3.33)
    f3 = axes.get_graph(lambda x: 4,x_range=[0,3],color=BLUE_C)
    a3 = axes.get_area(graph=f3,x_range=[2,2.5],color=BLUE_C).shift(RIGHT*1.66)
    f4 = axes.get_graph(lambda x: 3,x_range=[0,4],color=BLUE_C)
    a4 = axes.get_area(graph=f4,x_range=[3,3.5],color=BLUE_C).shift(LEFT*0.83)
    f5 = axes.get_graph(lambda x: 2,x_range=[0,5],color=BLUE_C)
    a5 = axes.get_area(graph=f5,x_range=[4,4.5],color=BLUE_C).shift(LEFT*3.33)
    f6 = axes.get_graph(lambda x: 1,x_range=[0,6],color=BLUE_C)
    a6 = axes.get_area(graph=f6,x_range=[5,5.5],color=BLUE_C).shift(LEFT*1.66)
    stuff1=VGroup(a1,a2,a3,a4,a5,a6,axes)

    # self.add_sound("ExistenDif2.mp3")
    self.play(Write(alg1),DrawBorderThenFill(stuff1),run_time=2)
    self.play(a1.animate.shift(LEFT*0.83),
              a2.animate.shift(LEFT*3.33),
              a3.animate.shift(LEFT*1.66),
              a4.animate.shift(RIGHT*0.83),
              a5.animate.shift(RIGHT*3.33),
              a6.animate.shift(RIGHT*1.66),run_time=2)
    self.play(FadeOut(stuff1))

    # Busqueda
    cinco = Text("5").scale(0.5)
    seis = Text("6").scale(0.5)
    siete = Text("7").scale(0.5)

    r = Rectangle(width=7.0, height=1.0, grid_xstep=1.0).scale(1.5)
    datos = VGroup(uno,dos,tres,cuatro,cinco,seis,siete)

    lu=Circle(color=BLUE_A,fill_opacity=1).scale(0.8).move_to(RIGHT*3+UP*2)
    brd=Circle(color=GREY,stroke_width=15).scale(0.8).move_to(lu.get_center())
    aux = Line(start=lu.get_left(),end=lu.get_right())
    pa=Line(stroke_width=15).set_color(GREY).next_to(lu,RIGHT,buff=0)
    lupa = VGroup(pa,brd).rotate(-30*DEGREES).shift(LEFT*0.1+DOWN*0.5)

    path = Line(start=LEFT*4.5,end=RIGHT*4.5).rotate(180*DEGREES)
    path.points[1:2] += DOWN*1.5
    path.points[2:3] += UP*1.5
    path2 = Line(start=LEFT*4.5,end=RIGHT*4.5).rotate(180*DEGREES).shift(RIGHT*0.85+DOWN*0.3)
    path2.points[1:2] += DOWN*1.5
    path2.points[2:3] += UP*1.5

    datos.set_color(BLACK).scale(3)
    uno.move_to(r.get_center())
    dos.move_to(LEFT*3)
    tres.move_to(LEFT*1.5)
    cuatro.move_to(RIGHT*1.5)
    cinco.move_to(RIGHT*4.5)
    seis.move_to(LEFT*4.5)
    siete.move_to(RIGHT*3)

    stuff2=VGroup(lu,lupa,r)

    self.play(ReplacementTransform(alg1,alg2),FadeIn(r),FadeIn(lu),FadeIn(lupa))
    self.add(datos)
    self.add(lupa)
    self.play(lu.animate.move_to(RIGHT*4.5),lupa.animate.move_to(RIGHT*5.35+DOWN*0.3))
    self.play(MoveAlongPath(lu,path),MoveAlongPath(lupa,path2),run_time=2)
    self.play(FadeOut(stuff2),FadeOut(alg2))
    self.wait()

    #Operation
    line=Line(color=WHITE).set_strock(5).scale(2).move_to(UP*0.4)
    line2 = line.copy().move_to(DOWN*1.1)
    num0=MathTex(r"102").scale(1.5).move_to(UP*1.5)
    num=MathTex(r"\text{x}21").scale(1.5).move_to(UP*0.8)
    num1=MathTex(r"102").scale(1.5)
    num2=MathTex(r"204","00").scale(1.5).move_to(DOWN*0.7)
    num3=MathTex(r"2142","0").scale(1.5).move_to(DOWN*1.5)
    stuff3 = VGroup(line,line2,num0,num,num1,num2[0],num3[0])

    self.play(Write(alg3),FadeIn(num0),FadeIn(num),GrowFromEdge(line,edge=LEFT))
    self.play(Write(num1))
    self.play(Write(num2[0]))
    self.play(Write(num3[0]),GrowFromEdge(line2,edge=LEFT))
    self.play(FadeOut(stuff3),FadeOut(alg3))
    self.wait()

    # Juntos y Tiempo
    l1 = ArcBetweenPoints(start=LEFT*3+DOWN,end=RIGHT*3+DOWN)
    l2 = ArcBetweenPoints(start=RIGHT*3+DOWN,end=UP*2)
    l3 = ArcBetweenPoints(start=UP*2,end=LEFT*3+DOWN)
    
    re = Circle(color=WHITE,fill_opacity=1).scale(2)
    loj = Circle(color=BLUE_D,stroke_width=25).scale(2.1).move_to(re.get_center())
    center = Dot(color=BLACK).move_to(re.get_center()).scale(1.2)

    path = ArcBetweenPoints(start=DOWN*1.5,end=re.get_corner(DL)-DL,radius=-1.5,color=RED)
    d= Dot(DOWN*1.5,color=WHITE)
    path2 = MyCircle(radius=1.7,color=BLACK)
    d2= Dot(RIGHT*1.7,color=BLACK).scale(0.01)
    hrs = always_redraw(lambda:Arrow(start=re.get_center(),end=d,color=BLACK,buff=0))
    min = always_redraw(lambda:Arrow(start=re.get_center(),end=d2,color=BLACK,buff=0))
    
    ore = Arc(angle=PI,color=BLUE_D,fill_opacity=1).rotate(-45*DEGREES).move_to(loj.get_corner(UR)-UR*0.6)
    jas = Arc(angle=PI,color=BLUE_D,fill_opacity=1).rotate(45*DEGREES).move_to(loj.get_corner(UL)-UL*0.6)
    pa = RoundedRectangle(color=BLUE_D,fill_opacity=1).rotate(-40*DEGREES).move_to(loj.get_corner(DR)-DR*0.3).scale(0.2)
    tas = RoundedRectangle(color=BLUE_D,fill_opacity=1).rotate(40*DEGREES).move_to(loj.get_corner(DL)-DL*0.3).scale(0.2)
    
    adorno = VGroup(ore,jas,pa,tas,path2)
    reloj = VGroup(re,loj,min,hrs,center,adorno)

    self.play(stuff1.animate.scale(0.5).move_to(UP*2),run_time=2)
    self.play(stuff2.animate.scale(0.5).move_to(LEFT*3+DOWN),run_time=2)
    self.play(stuff3.animate.scale(0.7).move_to(RIGHT*3+DOWN),run_time=2)
    self.play(MoveAlongPath(stuff1,l3),MoveAlongPath(stuff2,l1),MoveAlongPath(stuff3,l2),run_time=2)
    self.play(MoveAlongPath(stuff1,l1),MoveAlongPath(stuff2,l2),MoveAlongPath(stuff3,l3),run_time=2)
    self.play(FadeOut(stuff1),FadeOut(stuff2),FadeOut(stuff3),run_time=2)
    self.play(FadeIn(reloj),ReplacementTransform(alg,time))
    self.play(MoveAlongPath(d,path),MoveAlongPath(d2,path2))

    stuff2.move_to(RIGHT*2+DOWN*1.5).set_color(RED)
    newstf2 = stuff2.copy().move_to(RIGHT*2+UP*1.5).set_color(GREEN)
    timer1=Circle(color=YELLOW,fill_opacity=1).move_to(LEFT*4+UP*1.5).scale(0.7)
    timer2=Circle(color=YELLOW,fill_opacity=1).move_to(LEFT*4+DOWN*1.5).scale(0.7)

    p1 = Text("¿?").move_to(LEFT*4+UP*1.5).scale(0.8).set_color(BLACK)
    p2 = p1.copy().move_to(LEFT*4+DOWN*1.5).set_color(BLACK)
    parche = Circle(color=BLACK,fill_opacity=1).scale(3).move_to(LEFT*4)

    self.remove(reloj)
    self.remove(d)
    self.play(reloj.copy().animate.scale(0.4).move_to(LEFT*4+UP*1.5).set_color(GREEN),
              reloj.copy().animate.scale(0.4).move_to(LEFT*4+DOWN*1.5).set_color(RED),
              FadeIn(newstf2),FadeIn(stuff2),run_time=2)
    anims = [Create(timer1),Create(timer2,rate_func=rate_functions.ease_out_sine)]
    self.play(AnimationGroup(*anims,lag_ratio=0.3),run_time=4)
    self.wait()
    self.play(FadeIn(p1),FadeIn(p2),run_time=3)
    self.play(FadeOut(p1),FadeOut(p2),FadeOut(timer1),FadeOut(timer2),
              FadeOut(stuff2),FadeOut(newstf2),FadeOut(time),FadeIn(parche))
    self.wait(2)

class Analisis(MovingCameraScene):
  def construct(self):
    self.camera.frame.save_state()
    plane = NumberPlane(x_range=[-8,8], y_range=[-5,5],x_length=16,y_length=10)
    title = Text("Análisis Matemático").scale(0.8).to_edge(UL)

    code = '''from manim import Scene, Square
    class SquareToCircle(Scene):
      def construct(self):
        square = Square()
        circle = Circle()
        self.play(Create(square))
        self.play(Transform(square, circle))
        self.wait()'''
    rendered_code = Code(code=code, tab_width=2, background="window",
                            language="Python", font="Monospace")

    codigo2 = '''
    include <iostream>

    int main(){

      int n
      int suma = 0;
      for(int i = 0; i < n; i++){
        suma = suma + 1
      }

      return 0;
    }
    '''
    rendered_code2 = Code(code=codigo2, tab_width=4,background_stroke_color=BLACK,
                         background="rectangle",language="c++", font="Monospace")
    
    v = ValueTracker(0)
    tick_dot = Dot(color=RED_D).scale(2)
    tick_aux = Tex(" ``1 Tick\"").next_to(tick_dot,UP,buff=0.5)
    tick_frac= MathTex(r" 1 \text{tick}=\frac{1}{4x10^6}\text{seg} ").scale(1.5)
    pc = ImageMobject("PC.png").move_to(LEFT*3.5).scale(0.5)
    arrow = Arrow(start=pc.get_right(),end=LEFT*0.5,buff=0.1)
    ghz = MathTex(r"4x10^6 \text{ de ticks por segundo}").next_to(arrow,RIGHT,buff=0.3)

    tick_text = Tex("Ticks: ")
    tick_value = always_redraw(lambda: DecimalNumber(num_decimal_places=0)
                               .set_value(v.get_value())
                               .next_to(tick_text,RIGHT,buff=0.1))
    tick_n = Tex("Ticks: n").to_edge(UR)
    tick_fn = Tex("Ticks: f(n)").scale(2)
    tick = VGroup(tick_text, tick_value).to_edge(UR)

    path1 = Arc(angle=-PI).rotate(90*DEGREES).scale(0.2).move_to(RIGHT*3.6+DOWN*0.3)
    path2 = Arc(angle=-PI).rotate(90*DEGREES).scale(0.2).move_to(RIGHT*3.6+DOWN*0.7)
    path3 = Arc(angle=PI).rotate(-90*DEGREES).scale(0.4).move_to(RIGHT*3.7+DOWN*0.5)
    path = VGroup(path1,path2,path3)

    a1 = Arrow(color=RED).rotate(180*DEGREES).move_to(RIGHT*1.5).scale(0.9)
    a2 = Arrow(color=GREEN).rotate(180*DEGREES).move_to(RIGHT*1.5+DOWN*0.3).scale(0.9)
    a3 = Arrow(color=PURPLE).rotate(180*DEGREES).move_to(RIGHT*3+DOWN*0.61).scale(0.9)
    a4 = Arrow(color=YELLOW).rotate(180*DEGREES).move_to(RIGHT*5.3+DOWN*0.95).scale(0.9)
    a5 = Arrow(color=BLUE).rotate(180*DEGREES).move_to(RIGHT*0.4+DOWN*1.25).scale(0.9)
    anims = [GrowArrow(a1),GrowArrow(a2),GrowArrow(a3),GrowArrow(a4),GrowArrow(a5)]

    # 1
    # self.add(plane)
    self.play(FadeIn(title))
    self.play(Write(tick_aux),run_time=2)
    self.play(Create(tick_dot),run_time=2)
    self.play(FadeOut(tick_dot),FadeOut(tick_aux))
    self.play(FadeIn(pc),GrowArrow(arrow))
    self.play(Write(ghz),run_time=2)
    self.play(FadeOut(pc),FadeOut(arrow),FadeOut(ghz))
    self.play(Write(tick_frac),run_time=2)
    self.play(FadeOut(tick_frac))
    self.wait()
    # 2
    self.play(FadeIn(rendered_code),FadeIn(tick))
    self.play(AnimationGroup(*anims,lag_ratio=0.5),run_time=3)
    self.play(ReplacementTransform(a1,tick_value),v.animate.set_value(1))
    self.play(ReplacementTransform(a2,tick_value),v.animate.set_value(2))
    self.play(ReplacementTransform(a3,tick_value),v.animate.set_value(3))
    self.play(ReplacementTransform(a4,tick_value),v.animate.set_value(4))
    self.play(ReplacementTransform(a5,tick_value),v.animate.set_value(5))
    self.play(FadeOut(rendered_code),v.animate.set_value(0))
    self.wait()

    self.play(FadeIn(rendered_code2),tick_dot.animate.move_to(RIGHT*3.6+DOWN*0.1))
    self.play(self.camera.frame.animate.scale(0.6).move_to(RIGHT*0.5+DOWN*0.5))
    # ,tick_dot.animate.set_color(BLUE_D)
    # ,tick_dot.animate.set_color(RED_D)
    for i in range(1,6):
      self.play(MoveAlongPath(tick_dot,path1),run_time=0.2)
      self.play(MoveAlongPath(tick_dot,path2),run_time=0.2)
      self.play(MoveAlongPath(tick_dot,path3),run_time=0.2)
    self.play(Restore(self.camera.frame))
    self.play(ReplacementTransform(tick,tick_n))
    self.play(FadeOut(rendered_code2),FadeOut(tick_dot),run_time=2)
    self.play(ReplacementTransform(tick_n,tick_fn),run_time=2)
    self.play(FadeOut(tick_fn),FadeOut(title))
    self.wait()

class Intuitivo(Scene):
  def construct(self):
    plane = NumberPlane(x_range=[-8,8], y_range=[-5,5],x_length=16,y_length=10)
    title =  Text("Big O")

    r = Rectangle(width=7.0, height=1.0, grid_xstep=1.0).scale(1.5)

    uno = Tex("1").move_to(LEFT*4.5).scale(1.5)
    dos = Tex("2").move_to(LEFT*3).scale(1.5)
    tres = Tex("3").move_to(LEFT*1.5).scale(1.5)
    cuatro = Tex("4").move_to(RIGHT*1.5).scale(1.5)
    cinco = Tex("5").scale(1.5)
    seis = Tex("6").move_to(RIGHT*3).scale(1.5)
    siete = Tex("7").move_to(RIGHT*4.5).scale(1.5)

    anim = [FadeIn(uno),FadeIn(dos),FadeIn(tres),FadeIn(cinco),FadeIn(cuatro),
            FadeIn(seis),FadeIn(siete)]
    c1 =  Text("\"Buen Caso\"").next_to(r,UP)
    stuff = VGroup(uno,dos,tres,cuatro,cinco,seis,siete,r,c1)

    path1 = ArcBetweenPoints(start=cuatro.get_center(),end=cinco.get_center(),angle=PI)
    path2 = ArcBetweenPoints(start=cinco.get_center(),end=cuatro.get_center(),angle=PI)

    r1 = Rectangle(width=7.0, height=1.0, grid_xstep=1.0).scale(1.5)

    n1 = Tex("1").move_to(LEFT*3).scale(1.5)
    n2 = Tex("2").move_to(LEFT*4.5).scale(1.5)
    n3 = Tex("3").move_to(RIGHT*4.5).scale(1.5)
    n4 = Tex("4").move_to(RIGHT*1.5).scale(1.5)
    n5 = Tex("5").scale(1.5)
    n6 = Tex("6").move_to(RIGHT*3).scale(1.5)
    n7 = Tex("7").move_to(LEFT*1.5).scale(1.5)
    
    p1 = ArcBetweenPoints(start=uno.get_center(),end=dos.get_center(),angle=PI)
    p2 = ArcBetweenPoints(start=dos.get_center(),end=uno.get_center(),angle=PI)
    p3 = ArcBetweenPoints(start=tres.get_center(),end=siete.get_center(),angle=PI)
    p4 = ArcBetweenPoints(start=siete.get_center(),end=tres.get_center(),angle=PI)

    anim1 = [MoveAlongPath(n2,p1),MoveAlongPath(n1,p2),
             MoveAlongPath(n4,path1),MoveAlongPath(n5,path2),
             MoveAlongPath(n7,p3),MoveAlongPath(n3,p4),]

    c2 =  Text("\"Peor Caso\"").next_to(r,UP).shift(LEFT*15)
    time =  Tex("T(n) = O(f(n))").next_to(r,DOWN)
    stuff1 = VGroup(n1,n2,n3,n4,n5,n6,n7,r1).move_to(LEFT*15)

    a = Circle(color=RED,fill_opacity=1).scale(0.7).move_to(LEFT*4)
    b = Square(color=GREEN,fill_opacity=1).scale(0.7).move_to(LEFT*1.5)
    c = RegularPolygon(n=6,color=YELLOW,fill_opacity=1).scale(0.8).move_to(RIGHT)
    d = Triangle(color=BLUE,fill_opacity=1).scale(0.8).move_to(RIGHT*3.5)

    a1 = Arrow(start=a.get_right(),end=b.get_left(),buff=0)
    a2 = Arrow(start=b.get_right(),end=c.get_left(),buff=0)
    a3 = Arrow(start=c.get_right(),end=d.get_left(),buff=0)
    algorithm=VGroup(a,b,c,d,a1,a2,a3)
    name = Text("Algoritmo").next_to(algorithm,UP)
    
    t1 = MathTex(r"T(n) = n^2").move_to(LEFT*5.5)
    case1 =  Text("Caso 1").next_to(t1,DOWN).scale(0.7)
    v1 = VGroup(case1,t1)
    
    t2 = MathTex(r"T(n) = \log(n)").move_to(LEFT*2)
    case2 =  Text("Caso 2").next_to(t2,DOWN).scale(0.7)
    v2 = VGroup(case2,t2)
    
    t3 = MathTex(r"T(n) = \sqrt{n}").move_to(RIGHT*2)
    case3 =  Text("Caso 3").next_to(t3,DOWN).scale(0.7)
    v3 = VGroup(case3,t3)
    
    t4 = MathTex(r"T(n) = \log(n)").move_to(RIGHT*5.5)
    case4 =  Text("Caso 4").next_to(t4,DOWN).scale(0.7)
    v4 = VGroup(case4,t4)

    anim2 = [FadeIn(v1),FadeIn(v2),FadeIn(v3),FadeIn(v4)]

    mejor_a = Rectangle(width=12, height=0.5, color = BLACK,fill_color = color_gradient((GREEN, RED), 2), fill_opacity = 1).move_to(DOWN*1.5)
    mejor = Tex(r"Menos timepo = Mejor").set_color(BLACK).move_to(mejor_a.get_center())
    t1 = Triangle(color = GREEN,fill_opacity=1).rotate(30*DEGREES).scale(0.5).move_to(RIGHT*6.35+DOWN*1.5)
    peor_a = Rectangle(width=12, height=0.5, color = BLACK,fill_color = color_gradient((GREEN, RED), 2), fill_opacity = 1).move_to(DOWN*2.5)
    peor = Tex(r"M\'as timepo = Peor").set_color(BLACK).move_to(peor_a.get_center())
    t2 = Triangle(color = RED,fill_opacity=1).rotate(-30*DEGREES).scale(0.5).move_to(LEFT*6.35+DOWN*2.5)

    # self.add(plane)
    self.play(Write(title),run_time=2)
    self.play(title.animate.scale(0.8).to_edge(UL))
    self.play(Create(r),Write(c1),run_time=2)
    self.play(AnimationGroup(*anim,lag_ratio=0.5),run_time=3)
    self.play(MoveAlongPath(cuatro,path1),MoveAlongPath(cinco,path2),run_time=2)
    self.play(stuff.animate.shift(RIGHT*15),stuff1.animate.shift(RIGHT*15),c2.animate.shift(RIGHT*15),run_time=2)
    self.play(AnimationGroup(*anim1,lag_ratio=0.3),run_time=3)
    self.play(Write(time),run_time=2)
    self.play(Wiggle(time),Wiggle(stuff1))
    self.play(FadeOut(stuff1),FadeOut(time),FadeOut(c2))
    #
    self.play(Create(algorithm),Write(name),run_time=3)
    self.play(algorithm.animate.scale(0.8).shift(UP*2),name.animate.scale(0.8).shift(UP*2))
    self.play(AnimationGroup(*anim2,lag_ratio=0.3),run_time=2)
    self.play(GrowFromEdge(mejor_a,LEFT))
    self.play(Write(mejor),Create(t1))
    self.play(GrowFromEdge(peor_a,RIGHT))
    self.play(Write(peor),Create(t2))
    self.play(FadeOut(peor),
              FadeOut(mejor),
              FadeOut(algorithm),
              FadeOut(t1),
              FadeOut(t2),
              FadeOut(peor_a),
              FadeOut(mejor_a),
              FadeOut(name),
              FadeOut(v1),
              FadeOut(v2),
              FadeOut(v3))
    self.play(v4.animate.shift(LEFT*5.5+UP).scale(1.5))
    re4 = SurroundingRectangle(v4,color=YELLOW)
    t4_O = MathTex(r"T(n) = O(\log(n))").scale(1.2).move_to(re4.get_center())
    self.play(Create(re4),run_time=2)
    self.play(ReplacementTransform(v4,t4_O),run_time=2)
    self.play(FadeOut(re4,t4_O,case4),FadeOut(title))
    self.wait()

class Graficas(Scene):
  def construct(self):
    # self.camera.background_color = "#15303E"

    square = RoundedRectangle(height=2.5,width=2.5,fill_opacity=1,color=GREY).scale(2.5).shift(DOWN*0.5)
    rectangle = RoundedRectangle(height=2.5,width=7,fill_opacity=1,color=GREY).scale(2.5).shift(DOWN*0.5)
    # square = Square(fill_opacity=1,color=GREY).scale(2.5).shift(DOWN*0.5)

    formal = Text("Formal").scale(0.65).to_edge(UL)
    definicion = MathTex(r"f(n)","=O(g(n))\Leftrightarrow","\exists c>0",
                         ",n_0>0:\\forall n>n_0",",f(n)\leq cg(n)"
                         ).scale(0.7).move_to(UP*3)

    BigO1 = ImageMobject("BigO1.png").scale(0.8).move_to(DOWN*0.5)
    BigO2 = ImageMobject("BigO2.png").scale(0.8).move_to(DOWN*0.5)
    BigO3 = ImageMobject("BigO3.png").scale(0.8).move_to(DOWN*0.5)
    BigO4 = ImageMobject("BigO4.png").scale(0.8).move_to(DOWN*0.5)
    BigO5 = ImageMobject("BigO5.png").scale(0.8).move_to(DOWN*0.5)
  
    BigOmega = ImageMobject("BigOmega.png").scale(0.65).move_to(DOWN*0.5)
    BigTheta = ImageMobject("BigTheta.png").scale(0.65).move_to(DOWN*0.5)
  
    comercial = Text("Estructuras de Datos y Algoritmos").scale(0.8).move_to(UP*3.3)

    self.play(FadeIn(formal),run_time=2)
    self.play(FadeIn(square),FadeIn(BigO1),FadeIn(definicion[0]),run_time=2)
    self.wait(2)
    self.play(ReplacementTransform(BigO1,BigO2),FadeIn(definicion[1]),run_time=2)
    self.wait()
    self.play(ReplacementTransform(BigO2,BigO3),FadeIn(definicion[2]),run_time=2)
    self.wait()
    self.play(ReplacementTransform(BigO3,BigO4),FadeIn(definicion[3]),run_time=2)
    self.wait(3)
    self.play(ReplacementTransform(BigO4,BigO5),FadeIn(definicion[4]),run_time=2)
    self.wait(5)
    self.play(Wiggle(BigO5))
    self.wait()
    self.play(FadeOut(definicion),run_time=2)
    self.play(Transform(square,rectangle),
              BigOmega.animate.shift(LEFT*4.5),BigTheta.animate.shift(RIGHT*4.5),
              FadeOut(formal),BigO5.animate.scale(0.8),run_time=5)
    self.wait()
    self.play(FadeIn(comercial),run_time=2)
    self.play(FadeOut(comercial),FadeOut(square),run_time=2)
    self.wait()

class Final(Scene):
  def construct(self):
    circle = Circle(stroke_width = 12, stroke_color = YELLOW_E,
    fill_color = WHITE,fill_opacity = 1)
    circle.set_width(4)

    semi1 = Arc(angle = PI, stroke_width = 12, stroke_color = BLUE_E,
    fill_color = WHITE,fill_opacity = 1).set_width(4).move_to(UP*1)

    title = Tex(r"Departamento \\ de matem\'aticas").set_color(BLUE_E).set_height(1)
    title.move_to(circle.get_center())
    title.add_updater(lambda x : x.move_to(circle.get_center()))

    rectangulo = Rectangle(stroke_width = 6, stroke_color = WHITE,
    fill_color = BLUE_E, fill_opacity = 1, width = 8, height = 3).shift(DOWN*2+RIGHT*2.5)

    fb = Rectangle(stroke_width = 1, stroke_color = BLUE_D,
    fill_color = BLUE_D, fill_opacity = 1, width = 0.8, height = 0.8).shift(DOWN*1.5+LEFT*0.5)
    f = Tex("f").set_color(WHITE).set_height(0.8).move_to(fb.get_center())

    yt = Rectangle(stroke_width = 1, stroke_color = RED_C,
    fill_color = RED_C, fill_opacity = 1, width = 0.8, height = 0.8).shift(DOWN*2.5+LEFT*0.5)
    t = Triangle(stroke_color = WHITE, fill_color = WHITE, fill_opacity = 1)
    t.scale(0.2).rotate(30*DEGREES).move_to(yt.get_center())

    link1 = Tex(r"Difusion UG - Universidad de Guanajuato").set_color(WHITE).scale(0.6).next_to(yt, buff = 0.3)
    link2 = Tex(r"/Difusi\'onUG").set_color(WHITE).scale(1).next_to(fb, buff = 0.3)

    self.play(FadeIn(circle, semi1))
    self.play(Write(title))
    self.play(semi1.animate.shift(UP*1.5+LEFT*4.5), circle.animate.shift(UP*1.5+LEFT*4.5), run_time=2)
    self.play(FadeIn(rectangulo), FadeIn(fb), Write(f), FadeIn(yt), FadeIn(t))
    self.play(Write(link1), Write(link2))
    self.wait(3)
    self.play(FadeOut(circle),FadeOut(semi1),FadeOut(rectangulo),FadeOut(fb),FadeOut(yt),FadeOut(t),FadeOut(f),FadeOut(link1),FadeOut(link2),FadeOut(title))
    self.wait()