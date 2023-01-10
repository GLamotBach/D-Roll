from random import randrange
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window
from settings import button_font_size, prompt_font_size, score_font_size, score_font_size_s

class DRollApp(App):
    def build(self):
        Window.clearcolor = "#17030c"
        self.window = GridLayout()
        self.window.cols = 3

        self.number_of_dice = 1
        self.dice_sides = 20
        # String containing the amount of dices to be rolled
        self.dice_amount = ""
        # String containing the selected dice
        self.dice_display = f"{self.dice_amount}d{self.dice_sides}"

        # Add widgets here
        # Head
        self.score_prompt = Label(text="Score", font_size=prompt_font_size, color='#e6dbe1')
        self.window.add_widget(self.score_prompt)
        self.window.add_widget(Image(source="logo.jpg"))
        self.dice_prompt = Label(text="Dices", font_size=prompt_font_size, color='#e6dbe1')
        self.window.add_widget(self.dice_prompt)
        # Displaying roll score
        self.prompt = Label(text="", font_size=score_font_size, color='#e6dbe1', bold=True)
        self.window.add_widget(self.prompt)
        # Buttons - Roll
        self.button_roll = Button(text="ROLL!",
                                  font_size=button_font_size,
                                  bold=True,
                                  color='#17030c',
                                  background_color="#db9236",
                                  background_normal="")
        self.button_roll.bind(on_press=lambda x: self.roll(self.dice_sides, self.number_of_dice))
        self.window.add_widget(self.button_roll)
        # Displaying chosen dice
        self.chosen = Label(text=self.dice_display, font_size=score_font_size, color='#e6dbe1', bold=True)
        self.window.add_widget(self.chosen)
        # Buttons - Quantity
        # 1
        self.button_1 = Button(text="1",
                               font_size=button_font_size,
                               color="#17030c",
                               background_color="#e6dbe1",
                               background_normal="")
        self.button_1.bind(on_press=lambda x: self.amount_select(1))
        self.window.add_widget(self.button_1)
        # 2
        self.button_2 = Button(text="2",
                               font_size=button_font_size,
                               color="#17030c",
                               background_color="#e6dbe1",
                               background_normal="")
        self.button_2.bind(on_press=lambda x: self.amount_select(2))
        self.window.add_widget(self.button_2)
        # 3
        self.button_3 = Button(text="3",
                               font_size=button_font_size,
                               color="#17030c",
                               background_color="#e6dbe1",
                               background_normal="")
        self.button_3.bind(on_press=lambda x: self.amount_select(3))
        self.window.add_widget(self.button_3)
        # 4
        self.button_4 = Button(text="4",
                               font_size=button_font_size,
                               color="#17030c",
                               background_color="#e6dbe1",
                               background_normal="")
        self.button_4.bind(on_press=lambda x: self.amount_select(4))
        self.window.add_widget(self.button_4)
        # 5
        self.button_5 = Button(text="5",
                               font_size=button_font_size,
                               color="#17030c",
                               background_color="#e6dbe1",
                               background_normal="")
        self.button_5.bind(on_press=lambda x: self.amount_select(5))
        self.window.add_widget(self.button_5)
        # 6
        self.button_6 = Button(text="6",
                               font_size=button_font_size,
                               color="#17030c",
                               background_color="#e6dbe1",
                               background_normal="")
        self.button_6.bind(on_press=lambda x: self.amount_select(6))
        self.window.add_widget(self.button_6)
        # 7
        self.button_7 = Button(text="7",
                               font_size=button_font_size,
                               color="#17030c",
                               background_color="#e6dbe1",
                               background_normal="")
        self.button_7.bind(on_press=lambda x: self.amount_select(7))
        self.window.add_widget(self.button_7)
        # 8
        self.button_8 = Button(text="8",
                               font_size=button_font_size,
                               color="#17030c",
                               background_color="#e6dbe1",
                               background_normal="")
        self.button_8.bind(on_press=lambda x: self.amount_select(8))
        self.window.add_widget(self.button_8)
        # 9
        self.button_9 = Button(text="9",
                               font_size=button_font_size,
                               color="#17030c",
                               background_color="#e6dbe1",
                               background_normal="")
        self.button_9.bind(on_press=lambda x: self.amount_select(9))
        self.window.add_widget(self.button_9)
        # Placeholder
        self.placeholder_1 = Label(text="")
        self.window.add_widget(self.placeholder_1)
        # 0
        self.button_0 = Button(text="0",
                               font_size=button_font_size,
                               color="#17030c",
                               background_color="#e6dbe1",
                               background_normal="")
        self.button_0.bind(on_press=lambda x: self.amount_select(0))
        self.window.add_widget(self.button_0)
        # C
        self.button_c = Button(text="C",
                               font_size=button_font_size,
                               color="#17030c",
                               background_color="#db9236",
                               background_normal="")
        self.button_c.bind(on_press=lambda x: self.clear_amount())
        self.window.add_widget(self.button_c)
        # Buttons - Dice
        # d4
        self.button_d4 = Button(text="d4",
                                font_size=button_font_size,
                                color="#17030c",
                                background_color="#bd8574",
                                background_normal="")
        self.button_d4.bind(on_press=lambda x: self.dice_pick(4))
        self.window.add_widget(self.button_d4)
        # d6
        self.button_d6 = Button(text="d6",
                                font_size=button_font_size,
                                color="#17030c",
                                background_color="#bd8574",
                                background_normal="")
        self.button_d6.bind(on_press=lambda x: self.dice_pick(6))
        self.window.add_widget(self.button_d6)
        # d8
        self.button_d8 = Button(text="d8",
                                font_size=button_font_size,
                                color="#17030c",
                                background_color="#bd8574",
                                background_normal="")
        self.button_d8.bind(on_press=lambda x: self.dice_pick(8))
        self.window.add_widget(self.button_d8)
        # d10
        self.button_d10 = Button(text="d10",
                                 font_size=button_font_size,
                                 color="#17030c",
                                 background_color="#bd8574",
                                 background_normal="")
        self.button_d10.bind(on_press=lambda x: self.dice_pick(10))
        self.window.add_widget(self.button_d10)
        # d12
        self.button_d12 = Button(text="d12",
                                 font_size=button_font_size,
                                 color="#17030c",
                                 background_color="#bd8574",
                                 background_normal="")
        self.button_d12.bind(on_press=lambda x: self.dice_pick(12))
        self.window.add_widget(self.button_d12)
        # d20
        self.button_d20 = Button(text="d20",
                                 font_size=button_font_size,
                                 color="#17030c",
                                 background_color="#bd8574",
                                 background_normal="")
        self.button_d20.bind(on_press=lambda x: self.dice_pick(20))
        self.window.add_widget(self.button_d20)
        # d20 - Disadvantage
        self.button_dis = Button(text="DIS",
                                 font_size=button_font_size,
                                 color="#e6dbe1",
                                 background_color="#7d545c",
                                 background_normal="")
        self.button_dis.bind(on_press=lambda x: self.roll_disadvantage())
        self.window.add_widget(self.button_dis)
        # d100
        self.button_d100 = Button(text="d100",
                                  font_size=button_font_size,
                                  color="#e6dbe1",
                                  background_color="#7d545c",
                                  background_normal="")
        self.button_d100.bind(on_press=lambda x: self.roll_percentile())
        self.window.add_widget(self.button_d100)
        # d20 - Advantage
        self.button_adv = Button(text='ADV',
                                 font_size=button_font_size,
                                 color="#e6dbe1",
                                 background_color="#7d545c",
                                 background_normal="")
        self.button_adv.bind(on_press=lambda x: self.roll_advantage())
        self.window.add_widget(self.button_adv)

        return self.window

    def refresh_labels(self):
        """Refreshing the content of label widgets"""
        self.dice_display = f"{self.dice_amount}d{self.dice_sides}"
        self.chosen.text = self.dice_display

    def amount_select(self, a):
        """Calculator style chosing the ammount of dice"""
        self.dice_amount = self.dice_amount + str(a)
        self.number_of_dice = int(self.dice_amount)
        self.refresh_labels()

    def clear_amount(self):
        """Clearing the dice amount in window and setting it to default value of 1"""
        self.dice_amount = ""
        self.number_of_dice = 1
        self.refresh_labels()

    def dice_pick(self, d):
        """Chosing a dice to roll"""
        self.dice_sides = d
        self.refresh_labels()

    def roll(self, d, n):
        """Rolling n-amount of d-sided dice"""
        score = 0
        for r in range(n):
            score += randrange(1, d+1)
        self.prompt.font_size = score_font_size
        self.prompt.text = str(score)

    def roll_advantage(self):
        """Rolling a advantage d20 roll"""
        first_roll = randrange(1, 21)
        second_roll = randrange(1, 21)
        self.prompt.font_size = score_font_size_s
        if second_roll > first_roll:
            self.prompt.text = f"[{second_roll}] {first_roll}"
        else:
            self.prompt.text = f"[{first_roll}] {second_roll}"

    def roll_disadvantage(self):
        """Rolling a disadvantage d20 roll"""
        first_roll = randrange(1, 21)
        second_roll = randrange(1, 21)
        self.prompt.font_size = score_font_size_s
        if second_roll < first_roll:
            self.prompt.text = f"[{second_roll}] {first_roll}"
        else:
            self.prompt.text = f"[{first_roll}] {second_roll}"

    def roll_percentile(self):
        """Rolling a percentile dice"""
        self.prompt.text = str(randrange(1, 101))


if __name__ == '__main__':
    DRollApp().run()


