from big_ol_pile_of_manim_imports import *

class Info(Scene):
	def construct(self):
		self.add_sound("sinfo1")
		title = TextMobject("\\textit{Informaci\\'on}")
		self.play(Write(title), run_time = 3)
		self.wait()
		self.play(
                title.to_corner, UL,
                run_time=2,
                path_arc=0 #Sustituir 0 por otro valor, -np.pi
            )
		bit = TextMobject("bit")
		bit2 = TextMobject("bit")
		bd = TextMobject("binary digit")
		self.play(FadeIn(bit))
		self.wait()
		self.play(ReplacementTransform(bit,bd))
		self.wait()
		self.play(ReplacementTransform(bd,bit2))
		self.wait()
		self.play(FadeOut(bit2))
		c = Circle()
		l = Line(UP, DOWN)
		evento0 = TextMobject("Incertidumbre\\\\de un evento").scale(.7)
		evento1 = TextMobject("Cae sol o\\\\cae aguila").scale(.7)
		evento2 = TextMobject("Cae sol").scale(.7)
		evento0.move_to(UP*2+RIGHT*3)
		evento1.move_to(LEFT*2+UP)
		evento2.move_to(LEFT*2+UP)
		self.play(FadeIn(evento0), ShowCreation(c))
		self.wait()
		flecha = Arrow(evento0.get_bottom(), c.get_right(), buff = 0.2)
		self.play(GrowArrow(flecha))
		self.play(ShowCreation(l))
		self.wait()
		d1 = Dot().move_to(RIGHT*3+DOWN*2)
		d2 = Dot().move_to(RIGHT*3)
		d3 = Dot().move_to(RIGHT*3+UP*2)
		l2 = Line(d1.get_top(),d2.get_bottom())
		lc = Line(d1.get_top(),d3.get_bottom())
		l2.set_stroke(None,35)
		lc.set_stroke(None,35)
		question = TextMobject("Preguntas").rotate(PI/2).move_to(RIGHT*2.5+DOWN).scale(.7)
		info = TextMobject("Informaci\\'on").move_to(RIGHT*3.5+UP*0.2).scale(.7)
		self.play(FadeOut(l))
		self.play(
                evento0.move_to, LEFT+UP*2,
                flecha.move_to, 2*LEFT+UP*0.9,
                c.move_to, 4*LEFT,
                FadeIn(question),
                ShowCreation(l2),
                FadeIn(info),
                run_time=3,
                path_arc=0 #Sustituir 0 por otro valor, -np.pi
            )
		self.play(
				ReplacementTransform(l2,lc),
				info.move_to, RIGHT*3.5+UP*2.2,
				run_time=2.5
			)
		self.add_sound("sinfo2")
		coin = Dot().set_color(YELLOW).scale(13).move_to(4*LEFT)
		info1 = TextMobject("Cantidad de Informaci\\'on =", " 0").scale(0.7)
		info2 = TextMobject("1").scale(0.7)
		info1.move_to(RIGHT*3)
		info2.move_to(RIGHT*5.2)
		self.play(
				FadeOut(question),
				FadeOut(lc),
				FadeOut(info),
				FadeOut(evento0),
				FadeOut(flecha),
        		run_time=2
			)
		self.play(
				FadeIn(info1[0]),
				ReplacementTransform(c,coin),
				run_time = 2
				)
		self.wait()
		self.play(
                FadeIn(evento1),
                FadeIn(info1[1]),
                run_time=4,
            )
		self.wait(5)
		self.play(
                ReplacementTransform(evento1,evento2),
                ReplacementTransform(info1[1],info2),
                run_time=4,
            )
		self.wait(6)
		evento3 = TextMobject("Evento arbitrario").scale(0.7)
		evento3.move_to(UP*2)
		self.wait()
		self.add_sound("sinfo3")
		self.play(
                ReplacementTransform(evento2,evento3),
                FadeOut(coin),
                FadeOut(info1),
                FadeOut(info2),
                run_time=4,
                path_arc=0 #Sustituir 0 por otro valor, -np.pi
            )
		self.wait(6)
		t1 = TextMobject("La informaci\\'on de un evento depende \\'unica y continuamente de su probabilidad.").scale(0.7).move_to(UP)
		t2 = TextMobject("La informaci\\'on de la uni\\'on de dos eventos independientes es la suma de sus informaciones individuales.").scale(0.7)
		t3 = TextMobject("La informaci\\'on de un evento con probabilidad de $50\\%$ es exactamente $1$ bit.").scale(0.7).move_to(DOWN)
		self.play(FadeIn(t1))
		self.wait(4)
		self.play(FadeIn(t2))
		self.wait(5)
		self.play(FadeIn(t3))
		self.wait(4)
		self.add_sound("sinfo4")
		self.play(FadeOut(t1),FadeOut(t2),FadeOut(t3),FadeOut(evento3), run_time = 4)
		formula = TexMobject("I(x)"," = -\\log_2(\\mathbb{P}(x))").scale(0.9)
		self.play(FadeIn(formula[0]))
		self.wait(3)
		self.play(FadeIn(formula[1]))
		self.wait(5)
		self.play(
				FadeOut(title),
				FadeOut(formula)
			)
		self.wait()
