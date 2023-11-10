# مش مطلو يخلص بسرعه المطلوب انك تقدر تعمل حاجه مش اكتر ده تعليمي  و خد وقتك فيه بلالش استعجال لو سمحت
from flet import *





class ItemsTask(UserControl):
    def __init__(self, textvalue):
        super().__init__()
        self.textvalue = textvalue
    
    def build(self):
        self.items_box = Container(margin=margin.only(bottom=2,),bgcolor=colors.GREEN_50,
                                content=Row(
                                    controls=[
                                        Text(self.textvalue, width=320),
                                        IconButton(icon=icons.DELETE)])
                            )
                        
        return self.items_box


# [+] Class main Pos App ---------------------------------------------------------------------------------------------------
class PosApp(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        #cont= Container(margin=20, padding=20, alignment=alignment.center, bgcolor=colors.BLUE_GREY_900, border_radius=border_radius.all(30))
        self.total_text = Text(value='0')
        self.items_task_layout = Column(scroll=ScrollMode.ALWAYS,on_scroll_interval=1, height=200)
        self.title_layout = Container(alignment=alignment.center, bgcolor=colors.BLUE_GREY_900, border_radius=border_radius.all(10),padding=10,
                                    content=Row(
                                        controls=[
                                            Text("KIDSAREA POS", expand=True,color=colors.WHITE, size=20, weight=FontWeight.BOLD, text_align='center'),
                                            ElevatedButton(text="LogOut", icon=icons.LOGOUT, on_click=self.LogOut_Func)]))
        self.barcode_text = TextField(label='Barcode')
        self.reset_layout = Container(border=border.all(2),
                                content=(Column(
                                    controls=[
                                        Container(padding=padding.only(left=10,right=10,bottom=10,top=10),border_radius=5
                                            ,content=Row(
                                                controls=[
                                                    self.barcode_text,
                                                    FloatingActionButton(icon=icons.SEARCH,on_click=self.items_add_layout)]),
                                                    ),
                                                self.items_task_layout
                                                ,Container(margin=10, padding=5,
                                                           content=(
                                                               Row(
                                                                        controls=[Text('Total    ',bgcolor=colors.BLUE_200, width=250, text_align='center'),self.total_text]
                                                                    )
                                                                            ))
                                            ])))
        
        


                                    
        
        self.content_layout = Row(controls=[self.reset_layout])
        self.main_layout = Column([self.title_layout,self.content_layout])
        return self.main_layout
    
    def items_add_layout(self,e):
        x=self.barcode_text.value
        if x == '':
            pass
        else:
            self.items_task_layout.controls.append(ItemsTask(x))
            self.update()
            self.barcode_text.value = ''
            self.update()
    def LogOut_Func(self,e):
        self.page.window_close()







# [+] Main Func To Run App --------------------------------------------------------------------------------------------------
def main(page: Page):
    page.title = 'POS'
    page.theme_mode = ThemeMode.LIGHT
    page.vertical_alignment = MainAxisAlignment.START
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    App = PosApp()
    page.add(App)
    page.update()



if __name__ == "__main__":
    app(target=main, view=FLET_APP)