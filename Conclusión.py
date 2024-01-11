from big_ol_pile_of_manim_imports import *

class Conclu(Scene):
	def construct(self):
		self.add_sound("conclusión")
		title = TextMobject("\\textit{Recapitulaci\\'on}")
		self.play(FadeIn(title))
		self.play(
                title.to_corner, UL,
                run_time=2,
                path_arc=0 #Sustituir 0 por otro valor, -np.pi
            )
		t1 = TextMobject("La Teor\\'ia de la Informaci\\'on").scale(.8).move_to(UP*0.5)
		theory = ImageMobject("theory").move_to(RIGHT*0.7+DOWN*0.5).scale(0.6)
		shannon = ImageMobject("shannon").scale(0.7).move_to(LEFT*.7+DOWN*0.5)

		t2 = TextMobject("Informaci\\'on").scale(.8).move_to(RIGHT*3.5+UP*2)
		bit = TextMobject("bit").move_to(RIGHT*4.4+UP).scale(.7)
		coin = Dot().set_color(YELLOW).scale(4).move_to(RIGHT*3.3+UP)
		line = Line(coin.get_top(), coin.get_bottom()).set_color(BLACK)

		t3 = TextMobject("Entrop\\'ia").scale(.8).move_to(LEFT*5.5+DOWN)
		br1 = Dot().scale(2).set_color(RED).move_to(LEFT*6+DOWN*2)
		br2 = Dot().scale(2).set_color(RED).move_to(LEFT*5.5+DOWN*2)
		br3 = Dot().scale(2).set_color(RED).move_to(LEFT*5+DOWN*2)
		ba1 = Dot().scale(2).set_color(BLUE).move_to(LEFT*4.5+DOWN*2)
		uno = TextMobject("Matem\\'aticas").scale(.5).move_to(DOWN*1.5+LEFT*2.5)
		dos = TextMobject("Computaci\\'on").scale(.5).move_to(DOWN*2+LEFT*2.45)
		tres = TextMobject("F\\'isica").scale(.5).move_to(DOWN*2.5+LEFT*2.85)
		d1 = Dot().next_to(uno, LEFT)
		d2 = Dot().next_to(dos, LEFT)
		d3 = Dot().next_to(tres, LEFT)

		t4 = TextMobject("Comunicaci\\'on").scale(.8).move_to(LEFT*5+UP*2)
		s1 = Rectangle().scale(0.1).move_to(LEFT*6+UP*1.5).set_color(YELLOW)
		s2 = Rectangle().scale(0.1).move_to(LEFT*5+UP*1.5).set_color(YELLOW)
		s3 = Rectangle().scale(0.1).move_to(LEFT*4+UP*1.5).set_color(YELLOW)
		s4 = Rectangle().scale(0.1).move_to(LEFT*3+UP*1.5).set_color(YELLOW)
		s5 = Rectangle().scale(0.1).move_to(LEFT*2+UP*1.5).set_color(YELLOW)
		s0 = Rectangle().scale(0.1).move_to(LEFT*4+UP*.5).set_color(YELLOW)
		a1 = Line(s1.get_right(),s2.get_left()).set_color(RED)
		a2 = Line(s2.get_right(),s3.get_left()).set_color(RED)
		a3 = Line(s3.get_right(),s4.get_left()).set_color(RED)
		a4 = Line(s4.get_right(),s5.get_left()).set_color(RED)
		a0 = Line(s0.get_top(),s3.get_bottom()).set_color(RED)

		t5 = TextMobject("Problema Cl\\'asico").scale(.8).move_to(RIGHT*4+DOWN)
		b1 = ImageMobject("balanza1").scale(0.3).move_to(RIGHT*4+DOWN*2)
		b2 = ImageMobject("balanza2").scale(0.3).move_to(RIGHT*4+DOWN*2.6)

		self.play(FadeIn(t1), FadeIn(theory), FadeIn(shannon))
		self.wait()

		self.play(FadeIn(t2))
		self.wait()
		self.play(FadeIn(bit), FadeIn(coin), ShowCreation(line), run_time = 2)
		self.wait()

		self.play(FadeIn(t3), FadeInFrom(br1, DOWN), FadeInFrom(br2, DOWN), FadeInFrom(br3, DOWN), FadeInFrom(ba1, DOWN))
		self.wait()

		self.play(FadeIn(t4), FadeIn(s1), FadeIn(s2), FadeIn(s3), FadeIn(s4), FadeIn(s5), FadeIn(s0))
		self.play(ShowCreation(a1), ShowCreation(a2), ShowCreation(a3), ShowCreation(a4), ShowCreation(a0), buff = 0.3)
		self.wait()

		self.play(FadeIn(d1), FadeIn(uno))
		self.play(FadeIn(d2), FadeIn(dos))
		self.play(FadeIn(d3), FadeIn(tres))
		self.wait(2)

		self.play(FadeIn(t5), FadeIn(b1), FadeIn(b2))
		self.wait(2)

		self.play(
				FadeOut(title),
				FadeOut(theory),
				FadeOut(shannon),
				FadeOut(t2),
				FadeOut(bit),
				FadeOut(coin),
				FadeOut(line),
				FadeOut(t3),
				FadeOut(br1),
				FadeOut(br2),
				FadeOut(br3),
				FadeOut(ba1),
				FadeOut(t4),
				FadeOut(s1),
				FadeOut(s2),
				FadeOut(s3),
				FadeOut(s4),
				FadeOut(s5),
				FadeOut(s0),
				FadeOut(a1),
				FadeOut(a2),
				FadeOut(a4),
				FadeOut(a3),
				FadeOut(a0),
				FadeOut(d1),
				FadeOut(d2),
				FadeOut(d3),
				FadeOut(uno),
				FadeOut(dos),
				FadeOut(tres),
				FadeOut(t5),
				FadeOut(b1),
				FadeOut(b2),
				run_time = 2
			)
		bye = TextMobject("Gracias:D")
		self.play(ReplacementTransform(t1, bye))
		self.wait(2)