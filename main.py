
import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.widget import Widget 



class Calculator(BoxLayout):

	def backward(self, express):
		if express:
			self.display.text = express[:-1]

	def calculate(self, express):
		if not express: return

		try:
			self.display.text = str(eval(express))
		except Exception:
			self.display.text = 'error'




class CalculatorApp(App):
	title = 'calculator'
	icon = 'number13.png'

	def build(self):
		return Calculator()

	def on_pause(self):
		return True




if __name__ in ('__main__', '__android__'):
	CalculatorApp().run()