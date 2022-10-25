import config 

settings = config.Settings()
janela = settings.janela()
class Snake:
    def __init__(self, choise, color, font, size):
        self.choise = choise
        self.color = color
        self.font = font
        self.dize = size
        self.posicao = [100, 50]
        self.fruit_position = [config.random.randrange(1, (self.tamanhox//10)) * 10,
                  config.random.randrange(1, (self.tamanhoy//10)) * 10]
        self.fruit_spawn = True
        self.direcao = "RIGHT"
        self.mudar_direcao = self.direcao
    def score(self):
        self.font_score = config.pygame.font.SysFont(self.font, self.size)
        self.surface_score = self.font_score.render("Score: " + str(self.score), True, self.color)
        self.rect_score = self.surface_score.get_rect()
        return janela.blit(self.surface_score, self.rect_score)
