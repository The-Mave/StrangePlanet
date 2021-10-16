import pygame


def Player(self, name, age, x, y):
    self.name = "Nome do jogador"
    self.age = "19"
    self.x, self.y = (100,100)
    self.vel = 150 #velocidade do joagdor
    self.health = 100 #vida do jogador
    
    self.inventory = [] #esse sera o inventario do jogador, onde os itens serao armazenados 
    self.weapon = 'ID DO ITEM' #ARMA DO JOGADOR

    self.helmet = 'ID DO ITEM' # CAPACETE (IMPLEMENTADO NO FUTURO)
    self.chestplate = 'ID DO ITEM' # ARMADURA (IMPLEMENTADO NO FUTURO)
    self.legs = 'ID DO ITEM' # CALÇAS (IMPLEMENTADO NO FUTURO)
    self.shoes = 'ID DO ITEM' # PÉS (IMPLEMENTADO NO FUTURO)
    
    self.vision = 300 #campo de visao, quanto mais tarde ele devera diminuir
