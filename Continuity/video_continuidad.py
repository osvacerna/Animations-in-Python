from manim import *

class Lapiz(Scene):
  def construct(self):
    '''
    plane = NumberPlane(x_range=[-8,8], y_range=[-5,5],x_length=16,y_length=10).set_color(BLACK)
    self.add(plane)
    '''

    a = Rectangle(color=YELLOW_D, fill_color=YELLOW_D, fill_opacity=1, height=1, width=0.2)
    b = Arc(angle = PI,color=PINK, fill_color=PINK, fill_opacity=1).set_width(0.2).move_to(UP*0.56)
    c = Triangle(color=YELLOW_A, fill_color=YELLOW_D, fill_opacity=1)
    c.rotate(60*DEGREES).scale(0.1).move_to(DOWN*0.6)
    lapiz = VGroup(a,b,c)
    # lapiz.rotate(-25*DEGREES)

    title = Text('¿Sabes qué es una función continua?')
    t1 = Text('Sentido Clásico').scale(0.6).to_edge(UL)

    axes = Axes(x_range=[0,9], y_range=[0,5],x_length=9,y_length=5)
    axes.add_coordinates()
    graph = axes.get_graph(lambda x: x**0.5, x_range=[0,9])
    graph_aux = axes.get_graph(lambda x: x**0.5+0.8, x_range=[0,9])
    graph_aux.set_color(BLACK)

    g1 = axes.get_graph(lambda x: x**0.5, x_range=[0,4])
    g2 = axes.get_graph(lambda x: x**0.5+1, x_range=[4,9])
    d1 = Circle(color=WHITE, fill_color=BLACK, fill_opacity=1).scale(0.05).move_to(LEFT*0.5+DOWN*0.5)
    d2 = Dot().scale(0.7).move_to(LEFT*0.5+UP*0.5).set_color(WHITE)
    g1_aux = axes.get_graph(lambda x: x**0.5+0.8, x_range=[0,4]).set_color(BLACK)
    g2_aux = axes.get_graph(lambda x: x**0.5+1.8, x_range=[4,9]).set_color(BLACK)
    l = Line(start=LEFT*0.5,end=RIGHT*0.5,path_arc=-PI/2)
    l.rotate(PI/2).move_to(LEFT*0.6+UP*0.8).set_color(BLACK)
    
    self.play(Write(title))
    self.wait(2)
    self.play(FadeOut(title))
    self.play(FadeIn(t1))
    self.play(DrawBorderThenFill(axes), run_time=3)
    self.play(Create(graph),MoveAlongPath(lapiz,graph_aux), run_time=4)
    self.play(FadeOut(graph),FadeOut(lapiz))
    self.play(FadeIn(g1),FadeIn(d1),FadeIn(g2),FadeIn(d2))
    self.play(MoveAlongPath(lapiz,g1_aux), run_time=2)
    # self.play(Create(g1),MoveAlongPath(lapiz,g1_aux), run_time=2)
    self.play(MoveAlongPath(lapiz,l), run_time=2)
    # self.play(Create(g2),MoveAlongPath(lapiz,g2_aux), run_time=2)
    self.play(MoveAlongPath(lapiz,g2_aux), run_time=2)
    self.wait()
    self.play(FadeOut(g1),FadeOut(g2),FadeOut(lapiz),FadeOut(t1),
              FadeOut(d1),FadeOut(d2))
    self.wait(2) #Quitar al pegar videos (?

%%manim -ql -v WARNING ParticulaPersona
config.media_width = "50%"

class ParticulaPersona(Scene):
  def construct(self):
    plane = NumberPlane(x_range=[-8,8], y_range=[-5,5],x_length=16,y_length=10)
    t1 = Text('Sentido Clásico').scale(0.6).to_edge(UL)

    o1 = Ellipse(width=2.0, height=4.0, color=RED).rotate(45*DEGREES)
    o2 = Ellipse(width=2.0, height=4.0, color=RED).rotate(90*DEGREES)
    o3 = Ellipse(width=2.0, height=4.0, color=RED).rotate(135*DEGREES)
    o4 = Ellipse(width=2.0, height=4.0, color=RED).rotate(180*DEGREES)
    o5 = Ellipse(width=2.0, height=4.0, color=RED).rotate(225*DEGREES)
    c=Dot(color = RED).scale(3)

    particula = VGroup(o1,o2,o3,o4,o5,c).scale(0.4).move_to(LEFT*4.5+UP)
    persona = ImageMobject("person1.png").scale(0.5).move_to(LEFT*4.5+DOWN*0.5)

    axes = Axes(x_range=[0,9], y_range=[0,5],x_length=9,y_length=5)
    g1 = axes.get_graph(lambda x: np.sin(x)+3.5, x_range=[0,9])
    g2 = axes.get_graph(lambda x: np.absolute(x-4.5)/2.25 , x_range=[0,9])

    formal = Tex(r"Para todo $\epsilon>0$, existe $\delta>0$ tal que\\si $|x-p|<\delta$, entonces $|f(x)-f(p)|<\epsilon$").to_edge(UP)
    distancia = Tex(r"$d(f(x),f(p)) = |f(x)-f(p)|,d(x,p)=|x-p|$")

    p1 = Text('A').scale(1.5).next_to(axes,LEFT,buff=0.5)
    p2 = Text('B').scale(1.5).next_to(axes,RIGHT,buff=0.5)

    self.add(t1)
    self.play(Create(particula),FadeIn(persona),run_time=3)
    self.play(FadeIn(p1))
    self.play(Create(g1),Create(g2),run_time=3)
    self.play(FadeIn(p2))
    self.play(MoveAlongPath(particula,g1),run_time=3)
    self.play(MoveAlongPath(persona,g2),run_time=3)
    self.play(FadeOut(particula),FadeOut(persona),FadeOut(p1),
              FadeOut(g1),FadeOut(g2),FadeOut(t1),FadeOut(p2))
    self.wait(2)

class Preformal(Scene):
  def construct(self):
    plane = NumberPlane(x_range=[-8,8], y_range=[-5,5],x_length=16,y_length=10).set_color(BLUE)
    # self.add(plane)

    title = Text('¿Como caracterizar una función continua?').scale(0.8)
    t1 = Text("Definición Formal").scale(0.6).to_edge(UL)

    axes = Axes(x_range=[0,9], y_range=[0,5],x_length=9,y_length=5).scale(0.8)
    g1 = axes.get_graph(lambda x: np.cos(x)+2.75,x_range=[0,9])

    distancia = Tex(r"$d(f(x),f(p)) =$","$|f(x)-f(p)|$",",$d(x,p)=|x-p|$")
    d = Tex(r"$d(f(x),f(p)) =$","$f(x)$","$-$","$f(p)$").scale(1.5)

    p = Dot().set_color(RED)
    space1 = Tex(r"$(\quad p \quad )$").move_to(DOWN*2.3)
    space2 = Tex(r"$(\quad f(p) \quad)$").rotate(90*DEGREES).move_to(LEFT*4)
    space = VGroup(space1,space2)

    title2 = Text('¿A qué nos referimos con pequeña?').scale(0.8)

    self.play(Write(title))
    self.wait()
    self.play(FadeOut(title))
    self.play(Write(t1))
    self.play(Create(g1),Create(axes),run_time=3)
    self.play(FadeIn(space1),FadeIn(p))
    self.play(FadeIn(space2))
    self.play(space2.animate.scale(0.5),run_time=2)
    self.play(space1.animate.scale(0.5),run_time=2)
    self.wait()
    self.play(FadeOut(axes),FadeOut(g1),FadeOut(p),
              ReplacementTransform(space,d), run_time=3)
    self.play(d[1].animate.scale(1.3))
    self.play(d[3].animate.scale(0.7))
    self.play(ReplacementTransform(d,distancia))
    self.wait()
    self.play(FadeOut(distancia),FadeOut(t1))
    self.play(Write(title2))
    self.wait()
    self.play(FadeOut(title2),FadeIn(t1))

    distancia[1].move_to(LEFT*1.5)
    a = Arrow().next_to(distancia[1],RIGHT)
    cero = Tex(r"$0$").next_to(a,RIGHT)
    aux = Tex(r"$|f(x)-f(p)|<$","$\epsilon$")

    vt = ValueTracker(1)

    data = MathTex(r"\epsilon =").to_edge(UR, buff = 2)
    data_aux = always_redraw(
        lambda: DecimalNumber(num_decimal_places=2)
        .set_value(vt.get_value()).scale(0.8).next_to(data,RIGHT,buff= 0.1))
    data_aux2 = always_redraw(
        lambda: DecimalNumber(num_decimal_places=2)
        .set_value(vt.get_value()).scale(0.8).next_to(aux[0],RIGHT,buff= 0.1))

    self.play(FadeIn(distancia[1]))
    self.play(GrowArrow(a),run_time=2)
    self.play(FadeIn(cero))
    self.play(FadeOut(cero,a),ReplacementTransform(distancia[1],aux),run_time=2)
    self.play(FadeIn(data,data_aux),ReplacementTransform(aux[1],data_aux2))
    self.play(vt.animate.set_value(0.01),run_time = 3)
    self.play(FadeOut(aux,data_aux,data_aux2,data))
    self.wait()

def get_horizontal_line_to_graph(axes, function, x, width, color):
  result = VGroup()
  line = DashedLine(
      start=axes.c2p(0,function.underlying_function(x)),
      end=axes.c2p(x,function.underlying_function(x)),
      stroke_width=width,
      stroke_color=color
  )
  dot = Dot().set_color(color).move_to(axes.c2p(x,function.underlying_function(x)))
  dot.set_color(BLACK).scale(0.8) #Personalizado
  result.add(line,dot)
  return result

def get_vertical_line_to_graph(axes, function, x, width, color):
  result = VGroup()
  line = DashedLine(
      start=axes.c2p(x,0),
      end=axes.c2p(x,function.underlying_function(x)),
      stroke_width=width,
      stroke_color=color
  )
  dot = Dot().set_color(color).move_to(axes.c2p(x,function.underlying_function(x)))
  dot.set_color(BLACK).scale(0.8) #Personalizado
  result.add(line,dot)
  return result

class Formal(Scene):
  def construct(self):
    # self.camera.background_color = "#15303E"
    '''
    plane = NumberPlane(x_range=[-8,8], y_range=[-5,5],x_length=16,y_length=10).set_color(BLACK)
    self.add(plane)
    '''

    t1 = Text("Definición Formal").scale(0.6).to_edge(UL)
    # formal = MathTex(r"\forall \epsilon>0, \exists \delta>0, |x-p|<\delta \Rightarrow |f(x)-f(p)|<\epsilon")
    formal = Tex(r"Para todo $\epsilon>0$, existe $\delta>0$ tal que\\si $|x-p|<\delta$, entonces $|f(x)-f(p)|<\epsilon$")
    f = MathTex(r"f(x) = \left(\frac{x}{4}\right)^2").to_edge(UR)

    j = ValueTracker(5)
    k = ValueTracker(7)

    axes = Axes(x_range=[0,9], y_range=[0,5],x_length=9,y_length=5).add_coordinates()
    axes_new = Axes(x_range=[0,9], y_range=[0,5],x_length=9,y_length=5)

    lab1 = Tex(r"x").move_to(DOWN*3+RIGHT*5)
    lab2 = Tex(r"f(x)").move_to(UP*2+LEFT*5.5)
    labels = VGroup(lab1,lab2)

    g1 = axes.get_graph(lambda x: (x/4)**2, x_range=[0,8])
    graph = always_redraw(
        lambda: axes.get_graph(
            lambda x: (x/4)**2, x_range=[0,k.get_value()]
        ))

    hl_c = get_horizontal_line_to_graph(axes=axes_new,function=graph,x=6,width=4,color=BLUE_D)
    vl_c = get_vertical_line_to_graph(axes=axes_new,function=graph,x=6,width=4,color=RED_E)
    lab5 = Tex(r"p").next_to(vl_c,DOWN,buff=0.2).scale(0.8)
    lab6 = Tex(r"f(p)").next_to(hl_c,LEFT,buff=0.2).scale(0.8)
    punto = VGroup(lab5,lab6,hl_c,vl_c)
    dot = Dot().move_to(axes.c2p(6,graph.underlying_function(6))).set_color(BLACK).scale(0.8)

    mhl_l = always_redraw(
        lambda: get_horizontal_line_to_graph(
            axes=axes_new,function=graph,x=k.get_value(),width=4,color=BLUE_D
        ))
    mvl_l = always_redraw(
        lambda: get_vertical_line_to_graph(
            axes=axes_new,function=graph,x=k.get_value(),width=4,color=RED_E
        ))
    lab3 = Tex(r"p+","0.5").next_to(mvl_l,DOWN,buff=0.1).scale(0.8)
    lab4 = Tex(r"f(p+","0.5",")").next_to(mhl_l,LEFT,buff=0.1).scale(0.8)

    mhl_r = always_redraw(
        lambda: get_horizontal_line_to_graph(
            axes=axes_new,function=graph,x=j.get_value(),width=4,color=BLUE_D
        ))
    mvl_r = always_redraw(
        lambda: get_vertical_line_to_graph(
            axes=axes_new,function=graph,x=j.get_value(),width=4,color=RED_E
        ))
    lab7 = Tex(r"p-","0.5").next_to(mvl_r,DOWN,buff=0.1).scale(0.8)
    lab8 = Tex(r"f(p-","0.5",")").next_to(mhl_r,LEFT,buff=0.1).scale(0.8)

    rangos = VGroup(mhl_l,mhl_r,mvl_l,mvl_r)

    lab7_aux = always_redraw(
        lambda: DecimalNumber(num_decimal_places=1)
        .set_value(k.get_value()-6).scale(0.8).move_to(lab7[1].get_center()))
    lab3_aux = always_redraw(
        lambda: DecimalNumber(num_decimal_places=1)
        .set_value(k.get_value()-6).scale(0.8).move_to(lab3[1].get_center()))
    delta = VGroup(lab3_aux,lab7_aux)

    lab8_aux = always_redraw(
        lambda: DecimalNumber(num_decimal_places=1)
        .set_value(k.get_value()-6).scale(0.8).move_to(lab8[1].get_center()))
    lab4_aux = always_redraw(
        lambda: DecimalNumber(num_decimal_places=1)
        .set_value(k.get_value()-6).scale(0.8).move_to(lab4[1].get_center()))
    epsilon = VGroup(lab4_aux,lab8_aux)

    brace1 = BraceBetweenPoints(axes.c2p(5,0),axes.c2p(6,0))
    e = brace1.get_text("$\epsilon$")
    e.add_updater(lambda x : x.next_to(brace1,DOWN))
    brace2 = BraceBetweenPoints(axes.c2p(0,graph.underlying_function(6)),axes.c2p(0,graph.underlying_function(5)))
    d = brace2.get_text("$\delta$")
    d.add_updater(lambda x : x.next_to(brace2,LEFT,buff= 0.1))

    brace1_aux = BraceBetweenPoints(axes.c2p(6,0),axes.c2p(7,0))
    brace2_aux = BraceBetweenPoints(axes.c2p(0,graph.underlying_function(6)+0.6875),axes.c2p(0,graph.underlying_function(6)))
    brace = VGroup(brace1_aux,brace2_aux)

    data = MathTex(r"\epsilon =").next_to(f,DOWN, buff = 2)
    data_aux = always_redraw(
        lambda: DecimalNumber(num_decimal_places=1)
        .set_value(k.get_value()-6).scale(0.8).next_to(data,RIGHT,buff= 0.1))

    self.add(axes)
    self.play(FadeIn(t1))
    self.play(Create(g1), Write(f), run_time=3)
    self.play(Write(labels))
    self.play(Transform(axes,axes_new))
    self.play(FadeIn(punto),run_time=2)
    self.play(FadeIn(rangos),FadeIn(epsilon),FadeIn(delta),
              FadeIn(lab7[0]),FadeIn(lab8[0]),FadeIn(lab8[2]),
              FadeIn(lab3[0]),FadeIn(lab4[0]),FadeIn(lab4[2]),
              run_time=2)
    self.play(FadeOut(epsilon),FadeOut(delta),
              FadeOut(lab7[0]),FadeOut(lab8[0]),FadeOut(lab8[2]),
              FadeOut(lab3[0]),FadeOut(lab4[0]),FadeOut(lab4[2]),
              FadeOut(lab5),FadeOut(lab6)
              )
    self.play(GrowFromCenter(brace1),GrowFromCenter(brace2),FadeIn(e),FadeIn(d), run_time=2)
    self.play(ReplacementTransform(brace1,brace1_aux),ReplacementTransform(brace2,brace2_aux),run_time=3)
    self.play(Transform(brace,data),FadeIn(data_aux),FadeOut(e),FadeOut(d),run_time=3)
    self.play(FadeIn(epsilon),FadeIn(delta),
              FadeIn(lab7[0]),FadeIn(lab8[0]),FadeIn(lab8[2]),
              FadeIn(lab3[0]),FadeIn(lab4[0]),FadeIn(lab4[2]),
              FadeIn(lab5),FadeIn(lab6),
              run_time=3)
    self.play(FadeOut(hl_c),FadeOut(vl_c),FadeIn(dot))
    self.wait()
    self.play(k.animate.set_value(6),j.animate.set_value(6), run_time = 5, rate_func=linear)
    self.wait(2) #Quitar al pegar videos (?