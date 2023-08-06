# Maintain common settings for the game state

class Settings:
    def __init__(self, width, height):
        # Display
        self.screen_width = width
        self.screen_height = height
        
        # Timer
        self.total_game_time = 0

        # Enemy Settings
        self.max_enemies = 5  # The maximum number of enemies to create
        self.enemy_timer = 0
        self.enemy_interval = 1000 # 1000 milliseconds = 1 second

        # Fire Rate
        self.fire_timer = 0
        self.fire_interval = 1000  # 1000 milliseconds = 1 second

        # Pause Flag
        self.paused = False
        self.pause_cooldown = 500  # Cooldown period in milliseconds
        self.last_pause_time = 0  # Time when the last key was pressed

        #Score Counter
        self.score = 0

        #Game Over Condition
        self.game_over_condition = False