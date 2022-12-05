
# calculator app 3
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window


Window.size = (500,700)

Builder.load_string("""
<MyLayout>
    BoxLayout:
		orientation: 'vertical'
		size: root.width,root.height

		TextInput:
			id: calc_input
			text: '0'
			halign: 'right'
			font_size: 65
			size_hint: (1, .15)

		GridLayout:
			cols: 4
			rows: 5
            
            Button:
				size_hint:(.2,.2)
				font_size: 32
				text: '**'
				on_press: root.math_sign('**')

			Button:
				size_hint:(.2,.2)
				font_size: 32
				text: 'C'
				on_press: root.clear()

			Button:
				id: clear
				size_hint:(.2,.2)
				font_size: 32
				text: u'\u00AB'
				on_press: root.remove()

			Button:
				size_hint:(.2,.2)
				font_size: 32
				text: '/'
				on_press: root.math_sign('/')

			Button:
				size_hint:(.2,.2)
				font_size: 32
				text: '7'
				background_color:(157/255,157/255,157/255,1)
				on_press: root.button_press(7)

			Button:
				size_hint:(.2,.2)
				font_size: 32
				text: '8'
				background_color:(157/255,157/255,157/255,1)
				on_press: root.button_press(8)

			Button:
				size_hint:(.2,.2)
				font_size: 32
				text: '9'
				background_color:(157/255,157/255,157/255,1)
				on_press: root.button_press(9) 

			Button:
				size_hint:(.2,.2)
				font_size: 32
				text: '*'
				on_press: root.math_sign('*')			
			Button:
			    size_hint:(.2,.2)
				font_size: 32
				text: '4'
				background_color:(157/255,157/255,157/255,1)
				on_press: root.button_press(4)
						
			Button:
				size_hint:(.2,.2)
				font_size: 32
				text: '5'
				background_color:(157/255,157/255,157/255,1)	
                on_press: root.button_press(5)

			Button:
				size_hint:(.2,.2)
				font_size: 32
				text: '6'
				background_color:(157/255,157/255,157/255,1)   
                on_press: root.button_press(6)

			Button:
				size_hint:(.2,.2)
				font_size: 32
				text: '-'
				on_press: root.math_sign('-')

			Button:
				size_hint:(.2,.2)
				font_size: 32
				text: '1'
			    background_color:(157/255,157/255,157/255,1)	
                on_press: root.button_press(1)

			Button:
				size_hint:(.2,.2)
				font_size: 32
				text: '2'
				background_color:(157/255,157/255,157/255,1)   
                on_press: root.button_press(2)

			Button:
				size_hint:(.2,.2)
				font_size: 32
				text: '3'
				background_color:(157/255,157/255,157/255,1)
				on_press: root.button_press(3)	   

			Button:
				size_hint:(.2,.2)
				font_size: 32
				text: '+'
				on_press: root.math_sign('+')

			Button:
				size_hint:(.2,.2)
				font_size: 32
				text: '+/-'
				background_color:(157/255,157/255,157/255,1)
				on_press: root.pos_neg()
						
			Button:
				size_hint:(.2,.2)
				font_size: 32
				text: '0'
			    background_color:(157/255,157/255,157/255,1)
                on_press: root.button_press(0)

			Button:
				size_hint:(.2,.2)
				font_size: 32
				text: '.'
				background_color:(157/255,157/255,157/255,1)
				on_press: root.dot()

			Button:
				size_hint:(.2,.2)
				font_size: 32
				text: '='
				on_press: root.equals()			   
    """)

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text ='0'
        
    def remove(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior
    
    def pos_neg(self):
        prior = self.ids.calc_input.text
        
        if '-' in prior:
            self.ids.calc_input.text = f'{prior.replace("-","")}'
        else:
            self.ids.calc_input.text = f'-{prior}'
        
        
    def button_press(self,button):
        prior = self.ids.calc_input.text
        
        if 'Error' in prior:
            prior = ''
        
        if prior == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
            
        else:
            self.ids.calc_input.text = f'{prior}{button}'
            
    def dot(self):
        prior = self.ids.calc_input.text
        num_list = prior.split('+')
        
        if '+' in prior and "." not in num_list[:-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior
        
        elif '.' in prior:
            pass
        else: 
           prior = f'{prior}.'
           self.ids.calc_input.text = prior
        
        
    def math_sign(self,sign):
        prior = self.ids.calc_input.text 
        self.ids.calc_input.text = f'{prior}{sign}'     
        
    def equals(self):
        prior = self.ids.calc_input.text 
        try:
            answer = eval(prior)
            prior = self.ids.calc_input.text = str(answer)
        except:
             prior = self.ids.calc_input.text = 'Error'
        
        '''
       # if "+" in prior:
            num_list = prior.split('+')
            answer = 0
            for number in num_list:
                answer = answer + float(number)
                
            self.ids.calc_input.text = str(answer)
       '''
class CalculatorApp(App):
    def build(self):
	        return MyLayout()
     
if __name__ == '__main__':
    CalculatorApp().run()
    
    
