from big_ol_pile_of_manim_imports import *

class Inicio(Scene):
	def construct(self):
		title1 = TextMobject("La Teor\\'ia de la Informaci\\'on").move_to(UP)
		title = TextMobject("\\textit{La Teor\\'ia de la Informaci\\'on}")
		datos = TextMobject("\\'Eric Iv\\'an Hern\\'andez Palacios\\\\Luis Osvaldo Cerna Copado\\\\17 Abril 2021").move_to(DOWN).scale(0.9)
		self.play(FadeIn(title1), FadeIn(datos))
		self.wait(3)
		self.add_sound("introducción")
		self.play(FadeOut(datos),ReplacementTransform(title1,title), run_time = 2)
		self.play(
                title.to_corner, UL,
                run_time=2,
                path_arc=0 #Sustituir 0 por otro valor, -np.pi
            )
		self.wait()
		uno = TextMobject("Probabilidad").scale(.7).move_to(LEFT*1.73+UP)
		dos = TextMobject("Computaci\\'on").scale(.7).move_to(RIGHT*1.73+UP)
		tres = TextMobject("F\\'isica").scale(.7).move_to(2*DOWN)
		sc1 = Line(uno.get_center(),tres.get_center())
		sc1.points[1:3] += LEFT*.86+DOWN*.5
		sc2 = Line(tres.get_center(),dos.get_center())
		sc2.points[1:3] += RIGHT*.86+DOWN*.5
		sc3 = Line(dos.get_center(),uno.get_center())
		sc3.points[1:3] += UP
		#self.play(ShowCreation(sc1),ShowCreation(sc2),ShowCreation(sc3))
		self.play(GrowFromCenter(uno))
		self.play(GrowFromCenter(dos))
		self.play(GrowFromCenter(tres))
		self.wait()
		self.play(
				MoveAlongPath(uno,sc1),
				MoveAlongPath(dos,sc3),
				MoveAlongPath(tres,sc2),
				run_time = 3
			)
		self.play(
				FadeOut(uno),
				FadeOut(dos),
				FadeOut(tres)
			)
		inf = TextMobject("Informaci\\'on").scale(.7).move_to(LEFT*3)
		des = TextMobject("Desorden").scale(.7)
		com = TextMobject("Compresi\\'on").scale(.7).move_to(RIGHT*3)
		a1 = Arrow(RIGHT, LEFT).next_to(inf,RIGHT).set_color(GREEN)
		a2 = Arrow(LEFT, RIGHT).next_to(inf,RIGHT).set_color(RED)
		l = Line(inf.get_left(), inf.get_right()).next_to(inf,DOWN).set_color(YELLOW)
		l2 = Line(des.get_left(), des.get_right()).next_to(des,DOWN).set_color(YELLOW)
		l3 = Line(com.get_left(), com.get_right()).next_to(com,DOWN).set_color(YELLOW)
		self.play(FadeIn(inf), GrowArrow(a1))
		self.play(FadeOut(a1), GrowArrow(a2))
		self.wait()
		self.play(FadeOut(a2))
		self.wait()
		self.play(ShowCreation(l))
		self.play(FadeIn(des), ReplacementTransform(l,l2))
		self.wait(.5)
		self.play(FadeIn(com), ReplacementTransform(l2,l3))
		self.wait()
		self.play(FadeOut(l3))
		self.wait()
		self.play(
				FadeOut(inf),
				FadeOut(des),
				FadeOut(com),
				run_time = 3
			)
		theory = ImageMobject("theory").move_to(RIGHT*3).scale(2)
		shannon = ImageMobject("shannon").scale(2.5).move_to(LEFT*3)
		name1 = TextMobject("Claude Shannon").scale(0.7).next_to(shannon,DOWN)
		name2 = TextMobject("1948","- La Teoria Matem\\'atica\\\\de la Comunicaci\\'on").scale(0.7).next_to(theory,DOWN)
		name3 = TextMobject("1948","---","- A Mathematical Theory\\\\ of Communication").scale(0.7).next_to(theory,DOWN)
		self.wait(3)
		self.play(FadeIn(theory), run_time = 2)
		self.wait()
		self.play(FadeIn(name2[0]))
		self.wait(2)
		self.play(FadeIn(shannon), FadeIn(name1))
		self.wait()
		self.play(FadeIn(name3[2]))
		self.wait(1)
		self.play(ReplacementTransform(name3[2], name2[1]), run_time = 2)
		self.wait(11)
		self.play(
				FadeOut(theory),
				FadeOut(shannon),
				FadeOut(name1),
				FadeOut(name2),
				run_time = 2
			)
		self.add_sound("jaja")
		defin = TextMobject("A continuaci\\'on...").scale(0.7)
		self.play(FadeInFrom(defin, LEFT),run_time = 2)
		self.wait(5)
		self.play(FadeOut(defin),FadeOut(title))
		self.wait()