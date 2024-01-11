from big_ol_pile_of_manim_imports import *

class Esquema(Scene):
	def construct(self):
		self.add_sound("sesquema")
		title = TextMobject("\\textit{Sistema de comunicaci\\'on}")
		self.play(FadeIn(title), run_time = 3)
		self.wait()
		self.play(
                title.to_corner, UL,
                run_time=3,
                path_arc=0 #Sustituir 0 por otro valor, -np.pi
            )
		uno = TextMobject("Fuente de \\\\ informaci\\'on")
		uno.scale(.6)
		self.play(FadeIn(uno))
		self.wait(.5)
		self.play(
                uno.move_to, 6*LEFT,
                run_time=2,
                path_arc=0 #Sustituir 0 por otro valor, -np.pi
            )
		self.wait(.5)
		marco1 = SurroundingRectangle(uno, buff = 0.5*SMALL_BUFF)
		self.play(ShowCreation(marco1))
		self.wait()
		flecha1 = Arrow(LEFT,RIGHT)
		flecha1.set_color(RED)
		flecha1.scale(.8)
		flecha1.next_to(uno,RIGHT,buff = .3)
		self.play(GrowArrow(flecha1))
		self.wait()
		dos = TextMobject("Transmisor")
		dos.scale(.6)
		dos.next_to(flecha1)
		self.play(FadeIn(dos))
		self.wait(4.5)
		flecha2 = Arrow(LEFT,RIGHT)
		flecha2.set_color(RED)
		flecha2.scale(.8)
		flecha2.next_to(dos,RIGHT,buff = .3)
		self.play(GrowArrow(flecha2))
		self.wait()
		tres = TextMobject("Canal")
		tres.scale(.6)
		tres.next_to(flecha2)
		self.play(FadeIn(tres))
		self.wait(5)
		cero = TextMobject("Ruido")
		cero.scale(.6)
		cero.next_to(tres, DOWN)
		cero.move_to(2*DOWN+.1*RIGHT)
		self.play(FadeIn(cero))
		self.wait()
		flecha0 = Arrow(DOWN, UP)
		flecha0.set_color(RED)
		flecha0.scale(.8)
		flecha0.next_to(cero, UP, buff = .3)
		self.play(GrowArrow(flecha0))
		self.wait()
		flecha3 = Arrow(LEFT,RIGHT)
		flecha3.set_color(RED)
		flecha3.scale(.8)
		flecha3.next_to(tres,RIGHT,buff = .3)
		self.play(GrowArrow(flecha3))
		self.wait(.5)
		cuatro = TextMobject("Receptor")
		cuatro.scale(.6)
		cuatro.next_to(flecha3)
		self.play(FadeIn(cuatro))
		self.wait(4.5)
		flecha4 = Arrow(LEFT,RIGHT)
		flecha4.set_color(RED)
		flecha4.scale(.8)
		flecha4.next_to(cuatro,RIGHT,buff = .3)
		self.play(GrowArrow(flecha4))
		self.wait()
		cinco = TextMobject("Destinatario")
		cinco.scale(.6)
		cinco.next_to(flecha4)
		self.play(FadeIn(cinco))
		self.wait()
		marco2 = SurroundingRectangle(cinco, buff = SMALL_BUFF)
		self.play(ShowCreation(marco2))
		self.wait(2)
		self.play(
				FadeOut(title),
				FadeOut(flecha0),
				FadeOut(flecha1),
				FadeOut(flecha2),
				FadeOut(flecha3),
				FadeOut(flecha4),
				FadeOut(uno),
				FadeOut(dos),
				FadeOut(tres),
				FadeOut(cuatro),
				FadeOut(cinco),
				FadeOut(cero),
				FadeOut(marco1),
				FadeOut(marco2),
			)
		self.wait()