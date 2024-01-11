from big_ol_pile_of_manim_imports import *

class Teo(Scene):
	def construct(self):
		self.add_sound("teo1")
		title = TextMobject("\\textit{Primer Teorema de Shannon}")
		self.play(FadeIn(title))
		self.play(
                title.to_corner, UL,
                run_time=3,
                path_arc=0
            )
		e = TexMobject("\\varepsilon>0").move_to(LEFT*4+UP).scale(0.7)
		c1 = TexMobject("010110").move_to(LEFT+UP).scale(0.7)
		c2 = TexMobject("100101").move_to(LEFT+UP).scale(0.7)
		c3 = TexMobject("101011").move_to(LEFT+UP).scale(0.7)
		a1 = Arrow(e,c3)
		va = TextMobject("n variables aleatorias").scale(0.7).move_to(RIGHT*2+UP)
		h = TexMobject("H(X) = h").scale(0.7).next_to(va, DOWN)
		r = TexMobject("n(h+\\varepsilon)").scale(0.7).move_to(DOWN)
		r1 = TexMobject("n(h)").scale(0.7).move_to(LEFT*2+DOWN)
		s = SurroundingRectangle(r, buff = SMALL_BUFF)
		bits = TextMobject("bits").scale(0.7).next_to(s)
		p1 = TexMobject("\\mathbb{P}").scale(.7).move_to(DOWN+RIGHT)
		n = TexMobject("n").scale(.7).next_to(p1, DOWN)
		u = TexMobject("1").scale(.7).move_to(DOWN+RIGHT*2)
		a2 = Arrow(p1,u)
		inf = TexMobject("\\infty").scale(0.7).next_to(n,RIGHT, buff = 0.8)
		a3 = Arrow(n, inf)


		self.play(FadeIn(e))
		self.play(GrowArrow(a1))
		self.play(FadeIn(c1))
		self.play(ReplacementTransform(c1,c2))
		self.play(ReplacementTransform(c2,c3))
		self.play(FadeIn(va))
		self.wait(2)
		self.play(FadeIn(h))
		self.wait()
		self.play(FadeIn(r))
		self.play(ShowCreation(s), FadeIn(bits))
		self.wait()
		self.play(r.move_to, LEFT*2+DOWN, s.move_to, LEFT*2+DOWN, FadeOut(bits))
		self.play(FadeIn(p1))
		self.play(GrowArrow(a2), FadeIn(u))
		self.play(FadeIn(n))
		self.play(GrowArrow(a3), FadeIn(inf))
		self.wait()
		self.play(FadeOut(a3), FadeOut(inf), FadeOut(n), run_time = 2)
		self.play(ReplacementTransform(r,r1))
		self.play(GrowArrow(a2))
		self.wait(2)
		self.add_sound("teo2")
		self.wait(4)
		self.play(
				FadeOut(title),
				FadeOut(a2),
				FadeOut(e),
				FadeOut(va),
				FadeOut(h),
				FadeOut(s),
				FadeOut(r1),
				FadeOut(u),
				FadeOut(p1),
				FadeOut(a1),
				FadeOut(c3),
				run_time = 2
			)
		self.wait()

class PP(Scene):
	def construct(self):
		title = TextMobject("\\textit{Problema Pr\\'actico}")
		self.play(FadeIn(title))
		self.play(
                title.to_corner, DL,
                run_time=3,
                path_arc=0
            )
		self.add_sound("pp1")
		m1 = Dot().scale(3).set_color(YELLOW).move_to(RIGHT*0.5)
		m2 = Dot().scale(3).set_color(YELLOW).move_to(RIGHT*1.5)
		m3 = Dot().scale(3).set_color(YELLOW).move_to(RIGHT*2.5)
		m4 = Dot().scale(3).set_color(YELLOW).move_to(RIGHT*3.5)
		m5 = Dot().scale(3).set_color(YELLOW).move_to(RIGHT*4.5)
		m6 = Dot().scale(3).set_color(YELLOW).move_to(RIGHT*5.5)
		m7 = Dot().scale(3).set_color(YELLOW).move_to(LEFT*0.5)
		m8 = Dot().scale(3).set_color(YELLOW).move_to(LEFT*1.5)
		m9 = Dot().scale(3).set_color(YELLOW).move_to(LEFT*2.5)
		m10 = Dot().scale(3).set_color(YELLOW).move_to(LEFT*3.5)
		m11 = Dot().scale(3).set_color(YELLOW).move_to(LEFT*4.5)
		m12 = Dot().scale(3).set_color(YELLOW).move_to(LEFT*5.5)

		self.play(FadeIn(m1),FadeIn(m2),FadeIn(m3),FadeIn(m4),FadeIn(m5),FadeIn(m6),
				FadeIn(m7),FadeIn(m8),FadeIn(m9),FadeIn(m10),FadeIn(m11),FadeIn(m12), run_time = 2)
		self.play(m4.set_color, PURPLE, m4.move_to, RIGHT*3.5+UP)
		self.wait()
		self.play(m4.set_color, YELLOW, m4.move_to, RIGHT*3.5)
		self.wait()
		self.play(
				m1.move_to, RIGHT*0.5+UP*3,
				m2.move_to, RIGHT*1.5+UP*3,
				m3.move_to, RIGHT*2.5+UP*3,
				m4.move_to, RIGHT*3.5+UP*3, #falsa
				m5.move_to, RIGHT*4.5+UP*3,
				m6.move_to, RIGHT*5.5+UP*3,
				m7.move_to, LEFT*0.5+UP*3,
				m8.move_to, LEFT*1.5+UP*3,
				m9.move_to, LEFT*2.5+UP*3,
				m10.move_to, LEFT*3.5+UP*3,
				m11.move_to, LEFT*4.5+UP*3,
				m12.move_to, LEFT*5.5+UP*3,
				run_time = 5
				)
		b1 = ImageMobject("balanza1").scale(0.5)
		b2 = ImageMobject("balanza2").scale(0.5).move_to(DOWN)
		self.play(FadeIn(b1), FadeIn(b2))
		self.wait(11)
		self.add_sound("pp2")
		self.play(m8.move_to, LEFT*2+UP, run_time = 2)
		self.play(m2.move_to, RIGHT*2+UP)
		self.play(m2.move_to, RIGHT*1.5+UP*3, m3.move_to, RIGHT*2+UP)
		self.play(m3.move_to, RIGHT*2.5+UP*3, m4.move_to, RIGHT*2+UP)
		self.play(m4.move_to, RIGHT*3.5+UP*3, m5.move_to, RIGHT*2+UP)
		self.play(m5.move_to, RIGHT*4.5+UP*3)
		self.play(m8.move_to, LEFT*1.5+UP*3)
		self.wait()
		aprox = TexMobject("59/12\\approx 4.92").scale(.7).move_to(RIGHT*3+UP)
		self.play(FadeIn(aprox), run_time = 2)
		self.wait(2)
		self.play(FadeOut(aprox))
		self.wait(3)
		self.play(b1.move_to,LEFT*2, b2.move_to,LEFT*2+DOWN, run_time = 2)
		g = TextMobject("Algoritmo Greedy").move_to(RIGHT*3).scale(.7)
		e = TextMobject("Entrop\\'ia").next_to(g, DOWN).scale(.7)
		self.play(FadeIn(g))
		self.wait(4)
		self.play(FadeIn(e))
		self.wait(2)
		self.play(FadeOut(g), FadeOut(e))
		self.add_sound("pp3")
		l1 = Line(m4.get_right(), m1.get_left())
		l2 = Line(m6.get_right(), m1.get_left())
		key1 = Brace(l1, DOWN, buff = 0.5)
		key2 = Brace(l2, DOWN, buff = 0.5)
		k1 = TexMobject("1\\leq k \\leq 6").scale(.7).next_to(key2, DOWN)
		k = TextMobject("k = 4").scale(.7).next_to(key1, DOWN)
		p1 = TexMobject("\\frac{k}{12}").scale(.7).move_to(RIGHT*3)
		p2 = TexMobject("1-\\frac{2k}{12}").scale(.7).move_to(RIGHT*3)
		self.wait(3)
		self.play(GrowFromCenter(key2), FadeIn(k1), run_time = 2)
		self.wait(5)
		self.play(b1.rotate, 0.20, run_time = 2)
		self.play(FadeIn(p1))
		self.wait()
		self.play(b1.rotate, -0.40, run_time = 2)
		self.wait()
		self.play(b1.rotate, 0.20, b1.move_to, LEFT*2, ReplacementTransform(p1,p2), run_time = 2)
		self.wait(3)
		self.play(ReplacementTransform(key2,key1), ReplacementTransform(k1, k), FadeOut(p2), run_time = 2)
		self.wait()
		e1 = TexMobject("\\log_2(3)\\approx 1.58").scale(.7).move_to(RIGHT*3+DOWN)
		e2 = TexMobject("-3/4\\log_2(3/8)-1/4\\log_2(1/4)\\approx 1.56").scale(.7).move_to(RIGHT*3+DOWN)
		self.play(FadeIn(e1))
		self.wait(3)
		self.play(FadeOut(e1))
		self.wait()
		self.add_sound("pp4")
		self.wait(3)
		self.play(
				FadeOut(m1),
				FadeOut(m2),
				FadeOut(m3),
				FadeOut(m4),
				FadeOut(m7),
				FadeOut(m9),
				FadeOut(m10),
				FadeOut(m8),
				FadeOut(key1),
				FadeOut(k),
				run_time = 3
			)
		self.wait(2)
		self.play(
				m11.move_to, LEFT*4+UP, m6.move_to, UP, run_time = 2
			)
		self.wait(3)
		self.play(FadeOut(m11), FadeOut(m6))
		self.wait(3)
		self.play(
				m5.move_to, LEFT*4+UP, m12.move_to, UP, run_time = 2
			)
		self.wait(3)
		self.play(FadeOut(m12), m5.set_color, PURPLE)
		self.wait(5)
		self.add_sound("pp5")
		self.play(
				b1.rotate, 0.20,
				FadeIn(key1),
				FadeIn(k),
				m1.move_to, RIGHT*0.5+UP*3,
				m2.move_to, RIGHT*1.5+UP*3,
				m3.move_to, RIGHT*2.5+UP*3,
				m4.move_to, RIGHT*3.5+UP*3, m5.set_color, YELLOW, #falsa
				m5.move_to, RIGHT*4.5+UP*3,
				m6.move_to, RIGHT*5.5+UP*3,
				m7.move_to, LEFT*0.5+UP*3,
				m8.move_to, LEFT*1.5+UP*3,
				m9.move_to, LEFT*2.5+UP*3,
				m10.move_to, LEFT*3.5+UP*3,
				m11.move_to, LEFT*4.5+UP*3,
				m12.move_to, LEFT*5.5+UP*3,
				run_time = 5
				)
		self.wait(4)
		self.play(
				b1.rotate, -.20, b1.move_to, LEFT*2,
				FadeOut(m7),
				FadeOut(m8),
				FadeOut(m5),
				FadeOut(m6),
				FadeOut(key1),
				FadeOut(k),
				run_time = 2
			)
		self.wait(6)
		self.play(
				b1.rotate, 0.20,
				m4.move_to, LEFT*4+UP, m3.move_to, LEFT*3+UP, m9.move_to, UP, run_time = 2
			)
		self.wait(2)
		self.play(FadeIn(e2))
		self.play(
				FadeOut(m12),
				FadeOut(m11),
				FadeOut(m10),
				FadeOut(m1),
				FadeOut(m2),
				FadeOut(m9),
				m3.move_to, UP,
				run_time = 2
			)
		self.wait()
		self.play(
				FadeOut(m3),
				m4.set_color, PURPLE,
				run_time = 2
			)
		self.play(
				FadeOut(m4),
				b1.rotate, -.20, b1.move_to, LEFT*2,
			)
		self.wait(14)
		self.add_sound("pp6")
		self.play(
				FadeIn(e),
				FadeOut(e2),
			)
		self.wait(15)
		self.play(
				FadeOut(title),
				FadeOut(b1),
				FadeOut(b2),
				FadeOut(e),
			)
		self.wait(2)


