import pygame
from pygame.locals import *

from Modules.Gui.GUI_button import *
from Modules.Gui.GUI_form_container_level import *
from Modules.Gui.GUI_slider import *
from Modules.Gui.GUI_textbox import *
from Modules.Gui.GUI_label import *
from Modules.Gui.GUI_form import *
from Modules.Gui.GUI_button_image import *
from Modules.Gui.GUI_form_menu_score import *
from Modules.Levels.DriverLevels import *


    
class FormMenuPause(Form):
    def __init__(self, screen, x,y,w,h,color_background, color_border, active, path_image=""):
        super().__init__(screen, x,y,w,h,color_background, color_border, active)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image, (w,h))
        self._slave = aux_image
        self.flag_play = True

        # self.volumen = 0.2
        # pygame.mixer.init()
        # pygame.mixer.music.load("Modules\Assets\Music\Vengeance (Loopable).wav")
        # pygame.mixer.music.set_volume(self.volumen)
        # pygame.mixer.music.play(-1)

        # self.btn_play_music = Button_Image(self._slave, 
        #                                 x, 
        #                                 y, 
        #                                 300, 
        #                                 75, 
        #                                 50, 
        #                                 50,
        #                                 "Modules\Assets\Images\Menu\sound-on.png",
        #                                 self.btn_play_click, 
        #                                 "")

        # self.slider_volumen = Slider(self._slave, 
        #                                     x, 
        #                                     y, 
        #                                     200, 
        #                                     30, 
        #                                     200, 
        #                                     15, 
        #                                     self.volumen, 
        #                                     EColors.BLACK.value, 
        #                                     EColors.WHITE.value)
        
        # porcentaje_volumen = f"{self.volumen * 100}%"
        # self.label_volumen = Label(self._slave, 
        #                                     100, 
        #                                     10, 
        #                                     50, 
        #                                     50, 
        #                                     porcentaje_volumen, 
        #                                     "Comic Sans MS", 
        #                                     20, 
        #                                     EColors.WHITE.value,
        #                                     "Modules\Assets\Images\Menu\porcentaje.png")
        
        self._btn_home = Button_Image(screen=self._slave,
                            master_x = self._x,
                            master_y= self._y,
                            x = self._w - 50,
                            y = self._h - 50,
                            w= 30,
                            h= 30,
                            onclick= self.btn_home_click,
                            onclick_param= "",
                            path_image= "Modules\Assets\Images\Menu\home.png")
        
        self._btn_pause = Button_Image(screen = self._slave, 
                        master_x = self._x,
                        master_y= self._y,
                        x = self._w - 150,
                        y = self._h - 50,
                        w = 200,
                        h = 80,
                        onclick = self.btn_pause_click,
                        onclick_param = "",
                        path_image = "Modules\Assets\Images\Menu\\table.png") 
        
        # self.lista_widgets.append(self.label_volumen)
        # self.lista_widgets.append(self.slider_volumen)
        # self.lista_widgets.append(self.btn_play_music)
        self.lista_widgets.append(self._btn_home)
        self.lista_widgets.append(self._btn_pause)
    
    def render(self):
        self._slave.fill(self._color_background)

    # def update_volumen(self, lista_eventos):
    #     self.volumen = self.slider_volumen.value
    #     self.label_volumen.update(lista_eventos)
    #     self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
    #     pygame.mixer.music.set_volume(self.volumen)

    def btn_play_click(self, param):
        if self.flag_play:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

        self.flag_play = not self.flag_play


    def update(self, events):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(events)
            self.draw() 
            # self.update_volumen(events) 
        else:
            self.hijo.update(events)

    def btn_home_click(self, param):
        self.end_dialog()
    
    def btn_pause_click(self, param):
        self.end_dialog()