import sys 



class Term:
    def __init__(self):
        # renkler
        self.default_color = "\033[37m"
        self.red = "\033[31m"
        self.yellow = "\033[33m"
        self.green="\033[32m"
        self.okay_emoji="✅"

    def error(self, error):
        print(self.red + "error : " + error + self.default_color)
    def critic_error(self, error):
        print(self.red + "critic error : " + error + self.default_color)
        sys.exit(0)
    def task_info(self,task_info):
        print(self.yellow,"task:",task_info,self.default_color)
    def warning(self, warning):
        print(self.yellow + "warning: " + warning + self.default_color)
    def işlem_başarılı(self):
        print(self.okay_emoji,self.green," The process was successful. ",self.default_color)
    
    
class hello_screen(Term):
        def __init__(self,ascii_art,explanation):
            super().__init__()
            self.ascii = ascii_art
            self.explanation = explanation



        def cemo(self):
            print(self.red + self.ascii + self.default_color)
            print(self.yellow + self.explanation + self.default_color)
