from big_ol_pile_of_manim_imports import *

class Entro(Scene):
	def construct(self):
		self.add_sound("entro1")
		title = TextMobject("\\textit{Entrop\\'ia}")
		self.play(Write(title), run_time = 3)
		self.wait()
		self.play(
                title.to_corner, UL,
                run_time=2,
                path_arc=0 #Sustituir 0 por otro valor, -np.pi
            )
		info = TextMobject("Informaci\\'on").scale(0.7)
		info.move_to(LEFT*2+UP)
		ent = TextMobject("Entrop\\'ia").scale(0.7)
		ent.move_to(LEFT*2+DOWN)
		flecha1 = Arrow(LEFT, RIGHT, buff = 0.2)
		flecha1.next_to(info)
		flecha2 = Arrow(LEFT, RIGHT, buff = 0.2)
		flecha2.next_to(ent)
		sor1 = TextMobject("Sorpresa de un evento").scale(0.7)
		sor1.next_to(flecha1)
		sor2 = TextMobject("Sorpresa promedio de\\\\una variable aleatoria").scale(0.7)
		sor2.next_to(flecha2)
		formula1 = TexMobject("I(X)"," = -","\\log_2(\\mathbb{P}(X = x)",")").scale(0.8)
		formula1.move_to(UP*3)
		formula2 = TexMobject("H(X) = \\mathbb{E}(","I(X)",") = -\\sum_x\\mathbb{P}(X = x)","\\log_2(\\mathbb{P}(X = x)",")").scale(0.8)
		formula2.move_to(DOWN)
		self.play(FadeIn(info), FadeIn(ent))
		self.wait()
		self.play(GrowArrow(flecha1),run_time = 2)
		self.wait()
		self.play(FadeIn(sor1))
		self.wait()
		self.play(GrowArrow(flecha2))
		self.play(FadeIn(sor2))
		self.wait(2)
		self.add_sound("entro2")
		self.play(
			FadeOut(flecha1),
			FadeOut(flecha2),
			FadeOut(sor1),
			FadeOut(sor2),
			ReplacementTransform(info,formula1),
			ReplacementTransform(ent,formula2[0:1]),
			FadeIn(formula2[2]),
			FadeIn(formula2[4]),
			run_time = 3
			)
		self.wait(4)
		self.play(
			ReplacementTransform(formula1[0].copy(),formula2[1]),
			ReplacementTransform(formula1[2].copy(),formula2[3]),
			run_time = 3
			)
		self.wait(11)
		self.add_sound("entro3")
		self.play(
			formula2.move_to,UP*2.5,
			FadeOut(formula1),
			run_time = 3
			)
		self.wait()
		br1 = Dot().scale(5).set_color(RED).move_to(LEFT*6.3)
		br2 = Dot().scale(5).set_color(RED).move_to(LEFT*5.3)
		br3 = Dot().scale(5).set_color(RED).move_to(LEFT*4.3)
		br4 = Dot().scale(5).set_color(RED).move_to(LEFT*3.3)
		self.play(
			FadeInFromDown(br1),
			FadeInFromDown(br2),
			FadeInFromDown(br3),
			FadeInFromDown(br4),
			run_time = 3,
			)
		self.wait()
		br5 = Dot().scale(5).set_color(RED).move_to(LEFT*1.5)
		br6 = Dot().scale(5).set_color(RED).move_to(LEFT*.5)
		br7 = Dot().scale(5).set_color(RED).move_to(RIGHT*.5)
		ba1 = Dot().scale(5).set_color(BLUE).move_to(RIGHT*1.5)
		self.play(
			FadeInFromDown(br5),
			FadeInFromDown(br6),
			FadeInFromDown(br7),
			FadeInFromDown(ba1),
			run_time = 3,
			)
		self.wait()
		br8 = Dot().scale(5).set_color(RED).move_to(RIGHT*3.3)
		br9 = Dot().scale(5).set_color(RED).move_to(RIGHT*4.3)
		ba2 = Dot().scale(5).set_color(BLUE).move_to(RIGHT*5.3)
		ba3 = Dot().scale(5).set_color(BLUE).move_to(RIGHT*6.3)
		self.play(
			FadeInFromDown(br8),
			FadeInFromDown(br9),
			FadeInFromDown(ba2),
			FadeInFromDown(ba3),
			run_time = 3,
			)
		self.add_sound("entro4")
		self.wait(6)
		pinf = TextMobject("Poca Informaci\\'on").scale(0.7).move_to(LEFT*4.8+DOWN)
		minf = TextMobject("Media Informaci\\'on").scale(0.7).move_to(DOWN)
		ainf = TextMobject("Alta Informaci\\'on").scale(0.7).move_to(RIGHT*4.9+DOWN)
		self.play(br3.move_to,UP+LEFT*4.3, run_time = 1)
		self.play(br3.move_to,LEFT*4.3, run_time = 1)
		self.wait()
		self.play(FadeIn(pinf))
		self.wait(2)
		self.play(br6.move_to,UP+LEFT*.5, run_time = 1)
		self.play(br6.move_to,LEFT*.5, ba1.move_to,UP+RIGHT*1.5, run_time = 1)
		self.play(ba1.move_to,RIGHT*1.5, FadeIn(minf), run_time = 1)
		self.play(br8.move_to,UP+RIGHT*3.3, run_time = 1)
		self.play(br8.move_to,RIGHT*3.3, ba2.move_to,UP+RIGHT*5.3, run_time = 1)
		self.play(ba2.move_to,RIGHT*5.3, br9.move_to,UP+RIGHT*4.3, FadeIn(ainf), run_time = 1)
		self.play(br9.move_to,RIGHT*4.3, ba3.move_to,UP+RIGHT*6.3, run_time = 1)
		self.play(ba3.move_to,RIGHT*6.3, run_time = 1)
		self.add_sound("entro5")
		self.wait()
		self.play(
				FadeOut(br1),
				FadeOut(br2),
				FadeOut(br3),
				FadeOut(br4),
				FadeOut(br8),
				FadeOut(br9),
				FadeOut(ba2),
				FadeOut(ba3),
				FadeOut(pinf),
				FadeOut(minf),
				FadeOut(ainf),
				br5.move_to, LEFT*5.3,
				br6.move_to, LEFT*4.3,
				br7.move_to, LEFT*3.3,
				ba1.move_to, LEFT*2.3,
				run_time = 4
			)
		self.wait()
		self.play(
				br6.copy().move_to, RIGHT*.5,
				run_time = 2,
				path_arc = 2
			)
		self.play(
				br5.copy().move_to, RIGHT*1.5,
				run_time = 2,
				path_arc = -2
			)
		self.play(
				br6.copy().move_to, RIGHT*2.5,
				run_time = 2,
				path_arc = 2
			)
		self.play(
				ba1.copy().move_to, RIGHT*3.5,
				run_time = 2,
				path_arc = -2
			)
		self.add_sound("entro6")
		self.wait()
		aux = Line(br5.get_left(), br7.get_right())
		key1 = Brace(aux, DOWN, buff = SMALL_BUFF).move_to(RIGHT*1.5+DOWN*.5)
		key2 = Brace(ba1, DOWN, buff = SMALL_BUFF).move_to(RIGHT*3.5+DOWN*.5)
		e1 = TextMobject("Baja Entrop\\'ia").scale(.7).move_to(LEFT*4.8+DOWN)
		e2 = TextMobject("Media Entrop\\'ia").scale(.7).move_to(DOWN)
		e3 = TextMobject("Alta Entrop\\'ia").scale(.7).move_to(RIGHT*4.9+DOWN)
		p1 = TexMobject("\\frac{3}{4}").scale(.7).next_to(key1, DOWN)
		p2 = TexMobject("\\frac{1}{4}").scale(.7).next_to(key2, DOWN)
		r2 = TexMobject("-\\frac{3}{4}\\log_2(\\frac{3}{4})-\\frac{1}{4}\\log_2(\\frac{1}{4}) = 0.81").scale(.7).move_to(UP+RIGHT*2)
		r1 = TexMobject("-\\frac{4}{4}\\log_2(\\frac{4}{4}) = 0").scale(.7).move_to(UP+RIGHT*2)
		r3 = TexMobject("-\\frac{2}{4}\\log_2(\\frac{2}{4})-\\frac{2}{4}\\log_2(\\frac{2}{4}) = 1").scale(.7).move_to(UP+RIGHT*2)
		self.play(GrowFromCenter(key1), FadeIn(p1), run_time = 2)
		self.wait(2)
		self.play(GrowFromCenter(key2), FadeIn(p2))
		self.wait(3)
		self.play(Write(r2), run_time = 3)
		self.wait(2)
		br4.move_to(LEFT*2.3)
		ba2.move_to(LEFT*3.3)
		self.play(
				FadeOut(key1),
				FadeOut(key2),
				FadeOut(p1),
				FadeOut(p2),
				FadeOut(ba1),
				FadeIn(br4),
			)
		self.play(
				br4.copy().move_to,RIGHT*3.5,
				ReplacementTransform(r2,r1),
				run_time = 2
			)
		self.wait()
		self.play(
				FadeOut(br4),
				FadeIn(ba1),
				FadeIn(ba2),
				ba1.copy().move_to,RIGHT*3.5,
				ba2.copy().move_to,RIGHT*2.5,
				ReplacementTransform(r1,r3),
				run_time = 2
			)
		self.wait()
		aux2 = Dot().scale(6).set_color(BLACK).move_to(RIGHT*3.5)
		aux3 = Dot().scale(6).set_color(BLACK).move_to(RIGHT*2.5)
		aux4 = Dot().scale(6).set_color(BLACK).move_to(RIGHT*.5)
		aux5 = Dot().scale(6).set_color(BLACK).move_to(RIGHT*1.5)
		self.play(
				FadeIn(aux2),
				FadeIn(aux3),
				br4.move_to,LEFT*3.3,
				ba2.move_to,RIGHT*5.3,
				br5.move_to,LEFT*1.5,
				br6.move_to,LEFT*.5,
				br7.move_to,RIGHT*.5,
				ba1.move_to,RIGHT*1.5,
				FadeIn(br1),
				FadeIn(br2),
				FadeIn(br3),
				FadeIn(br8),
				FadeIn(br9),
				FadeIn(ba3),
				FadeOut(r3),
				FadeIn(e1),
				FadeIn(e2),
				FadeIn(e3),
				run_time = 2
			)
		self.wait()
		self.play(
				FadeIn(aux4),
				FadeIn(aux5),
				FadeOut(title),
				FadeOut(formula2),
				FadeOut(br1),
				FadeOut(br2),
				FadeOut(br3),
				FadeOut(br4),
				FadeOut(br5),
				FadeOut(br6),
				FadeOut(br7),
				FadeOut(br8),
				FadeOut(br9),
				FadeOut(ba1),
				FadeOut(ba2),
				FadeOut(ba3),
				FadeOut(e1),
				FadeOut(e2),
				FadeOut(e3),
				run_time = 2
			)
		self.wait()