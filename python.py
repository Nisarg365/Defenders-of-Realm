# A simple Tower Defense game in Python

import random
import time

class Enemy:
    def __init__(self, health, speed):
        self.health = health
        self.speed = speed

class Tower:
    def __init__(self, damage, range_radius):
        self.damage = damage
        self.range_radius = range_radius

class Game:
    def __init__(self):
        self.base_health = 100
        self.gold = 100
        self.enemies = []
        self.towers = []
        self.wave = 1
    
    def spawn_enemies(self):
        print(f"\nWave {self.wave} incoming!")
        num_enemies = 5 + self.wave  # Increase number of enemies with each wave
        for _ in range(num_enemies):
            health = 10 + (self.wave * 2)  # Stronger enemies each wave
            speed = random.choice([1, 2, 3])  # Random speed for variety
            self.enemies.append(Enemy(health, speed))

    def place_tower(self):
        if self.gold >= 50:
            self.gold -= 50
            new_tower = Tower(damage=10, range_radius=3)
            self.towers.append(new_tower)
            print(f"New tower placed! You have {len(self.towers)} towers.")
        else:
            print("Not enough gold to place a tower.")
    
    def attack_enemies(self):
        if not self.towers:
            return
        
        for tower in self.towers:
            if self.enemies:
                target = self.enemies[0]  # Simplified: tower attacks first enemy in the list
                target.health -= tower.damage
                if target.health <= 0:
                    self.enemies.pop(0)  # Enemy is defeated
                    self.gold += 20  # Reward for defeating enemy
                    print("Enemy defeated! +20 Gold.")
            else:
                break  # No more enemies to attack

    def enemy_attack(self):
        # Enemies move and attack the base
        enemies_reaching_base = [enemy for enemy in self.enemies if enemy.speed > 2]  # Simplification: fast enemies get through
        self.base_health -= len(enemies_reaching_base) * 10  # Each enemy deals 10 damage to the base
        print(f"{len(enemies_reaching_base)} enemies reached the base! Base health now at {self.base_health}.")
        self.enemies = [enemy for enemy in self.enemies if enemy.speed <= 2]  # Remove the ones that reached the base
    
    def start_wave(self):
        self.spawn_enemies()
        while self.enemies and self.base_health > 0:
            self.attack_enemies()
            self.enemy_attack()
            time.sleep(1)  # Simulate time between attacks
        
        if self.base_health <= 0:
            print("Game over! Your base has been destroyed.")
        elif not self.enemies:
            print(f"Wave {self.wave} cleared! Prepare for the next wave.")
            self.wave += 1

# Start the game
def start_game():
    game = Game()
    while game.base_health > 0:
        print("\n--- Menu ---")
        print(f"Gold: {game.gold}, Towers: {len(game.towers)}, Base Health: {game.base_health}")
        print("1. Place Tower (Cost: 50 Gold)")
        print("2. Start Next Wave")
        choice = input("Choose an action: ")

        if choice == '1':
            game.place_tower()
        elif choice == '2':
            game.start_wave()

start_game()
