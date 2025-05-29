import re
import pygame
import random
import hungry_games_classes as hgc

# Initialize pygame
pygame.init()

# Constants
GRID_SIZE = 128
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
SCREEN_COL = (53, 94, 59)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hungry Games Simulation")
clock = pygame.time.Clock()

class Grid:
    MAX_OBJECT = 999

    def __init__(self, row, col):
        self.coordinate = (row, col)
        self.game_sprites = [None] * Grid.MAX_OBJECT
        self.rect = pygame.Rect(col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE)

    def get_coordinate(self):
        return self.coordinate

    def add_game_sprite(self, sprite):
        index = self.get_index_for_next_game_sprite()
        if index != -1:
            self.game_sprites[index] = sprite

    def remove_game_sprite(self, sprite):
        if sprite in self.game_sprites:
            index = self.game_sprites.index(sprite)
            self.game_sprites[index] = None

    def replace_game_sprite(self, new_sprite, old_sprite):
        if old_sprite in self.game_sprites:
            index = self.game_sprites.index(old_sprite)
            self.game_sprites[index] = new_sprite

    def get_index_for_next_game_sprite(self):
        for i in range(len(self.game_sprites)):
            
            if self.game_sprites[i] is None:
                return i
        return -1

    def reposition_all_game_sprites(self):
        for i in range(len(self.game_sprites)):
            sprite = self.game_sprites[i]
            if sprite is not None:
                sprite.position = self.get_position_for_game_sprite_at_index(i)

    def get_position_for_game_sprite_at_index(self, index):
        GRID_MAP = [
            [4, 8, 9, 2],
            [10, 0, 6, 11],
            [12, 7, 1, 13],
            [3, 14, 15, 5]
        ]

        # If index is within GRID_MAP, use predefined positions
        for i in range(len(GRID_MAP)):
            for j in range(len(GRID_MAP[i])):
                if GRID_MAP[i][j] == index:
                    subRow, subCol = i, j
                    subColWidth = GRID_SIZE / len(GRID_MAP[0])
                    subRowHeight = GRID_SIZE / len(GRID_MAP)

                    x = self.rect.x + (subCol + 0.5) * subColWidth
                    y = self.rect.y + (subRow + 0.5) * subRowHeight
                    return (x, y)

        # If index is >= 16, position extra sprites within the same grid cell
        #print(f"Warning: Index {index} exceeds GRID_MAP limits. Adjusting position.")

        # Define a small 3x3 grid inside the larger grid cell for extra sprites
        sub_grid_size = 3
        sub_col = (index - 16) % sub_grid_size
        sub_row = (index - 16) // sub_grid_size

        max_extra_sprites = sub_grid_size * sub_grid_size  # Limit per grid cell
        if sub_row >= sub_grid_size:  # Prevent too many sprites in one cell
            sub_row = sub_grid_size - 1
            sub_col = sub_grid_size - 1  # Stack at the last position

        # Calculate position within the current grid cell
        subCellWidth = GRID_SIZE / sub_grid_size
        subCellHeight = GRID_SIZE / sub_grid_size

        x = self.rect.x + (sub_col + 0.5) * subCellWidth
        y = self.rect.y + (sub_row + 0.5) * subCellHeight

        return (x, y)

    def search_for_game_sprite(self, game_object):
        for sprite in self.game_sprites:
            if sprite is not None and sprite.get_id() == game_object.get_id():
                return sprite

        for sprite in self.game_sprites:
            if sprite is not None and sprite.get_game_object().get_name() == game_object.get_name() and sprite.get_game_object().get_id() == -1:
                return sprite

        return None

    def get_next_sprite_position(self):
        index = self.get_index_for_next_game_sprite()
        if index == -1:
            print(f"Warning: No available space in grid {self.coordinate} for new sprite.")
            return None  # Return None instead of causing a crash

        return self.get_position_for_game_sprite_at_index(index)

    def draw(self, screen):
        pygame.draw.rect(screen, GRAY, self.rect, 1)  # Draw grid outline
        for sprite in self.game_sprites:
            if sprite is not None:
                sprite.draw(screen)

class GameSprite:
    tribute_id = 1

    def __init__(self, game_object):
        self.game_object = game_object
        try:
            self.image = pygame.image.load("resources/" + GameSprite.get_sprite_name(game_object))
        except pygame.error as e:
            print(f"Error loading image: {e}")
            self.image = pygame.Surface((GRID_SIZE, GRID_SIZE))
            self.image.fill((255, 0, 0))  # Fill with red color to indicate missing image
        self.rect = self.image.get_rect()
        self.position = (0, 0)
        self.hp_bar_sprite = None

        if isinstance(self.game_object, hgc.LivingThing):
            self.show_hp_bar()

    def get_id(self):
        return self.game_object.get_id()

    def get_game_object(self):
        return self.game_object

    @staticmethod
    def get_sprite_name(game_object):
        if isinstance(game_object, hgc.Food) and "meat" in game_object.get_name():
            return "meat.png"
        elif isinstance(game_object, hgc.Tribute):
            sprite_name = "ai" + str(GameSprite.tribute_id) + ".png"
            GameSprite.tribute_id += 1
            if GameSprite.tribute_id > 8:
                GameSprite.tribute_id = 1
            return sprite_name
        return game_object.get_name().lower().replace(' ', '_') + ".png"

    def show_hp_bar(self):
        self.hp_bar_sprite = pygame.Surface((self.rect.width, 5))
        self.hp_bar_sprite.fill((255, 0, 0))
        self.hp_bar_rect = self.hp_bar_sprite.get_rect()
        self.hp_bar_rect.topleft = (self.rect.x, self.rect.y - 10)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.hp_bar_sprite is not None:
            screen.blit(self.hp_bar_sprite, self.hp_bar_rect)

    def update_position(self, position):
        self.position = position
        self.rect.center = position
        if self.hp_bar_sprite is not None:
            self.hp_bar_rect.topleft = (self.rect.x, self.rect.y - 10)


class GameReplayLayer:
    def __init__(self, map_size):
        self.grids = []
        self.map_states = None
        self.game_events = None
        self.turn_id = None
        self.event_id = None
        self.replay_finish_callback = None

        self.create_grids(map_size)

    def create_grids(self, map_size):
        for i in range(map_size):
            row = []
            for j in range(map_size):
                grid = Grid(i, j)
                row.append(grid)
            self.grids.append(row)

    def replay(self, game_events, map_states, callback=None, start_turn=0, start_event=0):
        self.game_events = game_events
        self.map_states = map_states
        self.replay_finish_callback = callback
        self.turn_id = start_turn - 1
        self.replay_next_turn(start_event)

    def replay_next_turn(self, start_event=0):
        self.turn_id += 1
        if self.turn_id >= len(self.game_events):
            if self.replay_finish_callback:
                self.replay_finish_callback()
            return

        print("Time " + str(self.turn_id + 1) + ":")
        self.load_new_game_objects()
        self.event_id = start_event - 1
        self.replay_next_event()

    def load_new_game_objects(self):
        map_state = self.map_states[self.turn_id]
        for row in map_state:
            for place in row:
                grid = self.get_grid_from_place(place)
                for game_object in place.get_objects():
                    if grid.search_for_game_sprite(game_object) is None:
                        self.load_game_object(game_object, grid)
        #self.reposition_all_game_objects()

    def load_game_object(self, game_object, grid):
        sprite = GameSprite(game_object)
        grid.add_game_sprite(sprite)
        sprite.update_position(grid.get_next_sprite_position())

    def reposition_all_game_objects(self):
        for row in self.grids:
            for grid in row:
                grid.reposition_all_game_sprites()

    def replay_next_event(self):
        self.event_id += 1
        if self.event_id >= len(self.game_events[self.turn_id]):
            print()
            self.replay_next_turn()
            return

        event = self.game_events[self.turn_id][self.event_id]

        hgc.GAME_LOGGER.print_event(event[0], *event[1:])

        if self.should_replay_event(event):
            self.replay_event(event)
        else:
            self.replay_next_event()

    @staticmethod
    def should_replay_event(event):
        return event[0] in ['MOVE', 'ATTACK', 'TOOK', 'KILLED', 'SPAWNED', 'ATE']

    def replay_event(self, event):
        handlers = {
            'MOVE': self.replay_move_event,
            'TOOK': self.replay_take_event,
            'ATTACK': self.replay_attack_event,
            'KILLED': self.replay_dead_event,
            'SPAWNED': self.replay_spawn_event,
            'ATE': self.replay_eat_event
        }

        if event[0] in handlers:
            handlers[event[0]](event)
        else:
            print("Unknown event: " + event[0])

    def replay_move_event(self, event):
        from_grid = self.get_grid_from_place(event[2])
        sprite = from_grid.search_for_game_sprite(event[1])
        to_grid = self.get_grid_from_place(event[3])

        # Remove grid updates here.
        self.animate_move_event(sprite, to_grid)

    def get_grid_from_place(self, place):
        place_name = place.get_name()
        tokens = re.sub("[(),]", "", place_name).split(" ")
        row = int(tokens[0]) - 1
        col = int(tokens[1]) - 1
        return self.grids[row][col]

    def animate_move_event(self, sprite, to_grid):
        target_position = to_grid.get_next_sprite_position()
        def on_animation_complete():
            from_grid = self.get_grid_from_place(sprite.get_game_object().get_place())
            from_grid.remove_game_sprite(sprite)
            to_grid.add_game_sprite(sprite)
            self.replay_next_event()
        self.animate_sprite(sprite, target_position, on_animation_complete)

    def replay_take_event(self, event):
        grid = self.get_grid_from_place(event[1].get_place())
        taking_sprite = grid.search_for_game_sprite(event[1])
        taken_sprite = grid.search_for_game_sprite(event[2])

        self.animate_take_event(taking_sprite, taken_sprite, grid)

    def animate_take_event(self, taking_sprite, taken_sprite, grid):
        self.animate_sprite(taken_sprite, taking_sprite.position, lambda: self.handle_take_animation_end(taken_sprite, grid))

    def handle_take_animation_end(self, taken_sprite, grid):
        grid.remove_game_sprite(taken_sprite)
        self.replay_next_event()

    def replay_attack_event(self, event):
        attacking_grid = self.get_grid_from_place(event[1].get_place())
        attacking_sprite = attacking_grid.search_for_game_sprite(event[1])
        attacked_grid = self.get_grid_from_place(event[2].get_place())
        attacked_sprite = attacked_grid.search_for_game_sprite(event[2])
        new_hp = max(0, event[2].get_health() - event[3])

        self.animate_attack_event(attacking_sprite, attacked_sprite, new_hp)

    def animate_attack_event(self, attacking_sprite, attacked_sprite, new_hp):
        self.animate_sprite(attacking_sprite, attacked_sprite.position, lambda: self.animate_target_flinch(attacked_sprite, new_hp))

    def animate_target_flinch(self, attacked_sprite, new_hp):
        self.shake_sprite(attacked_sprite, lambda: self.update_target_hp(attacked_sprite, new_hp))

    def update_target_hp(self, attacked_sprite, new_hp):
        scale_x = (max(5, new_hp) if new_hp else 0) / 100
        attacked_sprite.hp_bar_sprite = pygame.transform.scale(attacked_sprite.hp_bar_sprite, (int(attacked_sprite.rect.width * scale_x), 5))
        self.replay_next_event()

    def replay_dead_event(self, event):
        grid = self.get_grid_from_place(event[1].get_place())
        dead_sprite = grid.search_for_game_sprite(event[2])
        self.animate_dead_event(dead_sprite, grid)

    def animate_dead_event(self, dead_sprite, grid):
        self.fade_out_sprite(dead_sprite, lambda: self.handle_dead_animation_end(dead_sprite, grid))

    def handle_dead_animation_end(self, dead_sprite, grid):
        if isinstance(dead_sprite.get_game_object(), hgc.Animal):
            if self.turn_id + 1 < len(self.game_events):
                self.forward_load_animal_meat(self.map_states[self.turn_id + 1], dead_sprite, grid)
        else:
            grid.remove_game_sprite(dead_sprite)
        self.replay_next_event()

    def forward_load_animal_meat(self, map_state, dead_sprite, grid):
        row, col = grid.get_coordinate()
        place = map_state[row][col]
        find_meat = False
        for game_object in place.get_objects():
            if isinstance(game_object, hgc.Food) and dead_sprite.get_game_object().get_name() in game_object.get_name() and "meat" in game_object.get_name():
                meat = game_object
                find_meat = True
                break

        if not find_meat:
            dead_object = dead_sprite.get_game_object()
            meat = hgc.Food(dead_object.get_name() + " meat", dead_object.get_food_value())
            meat._id = -1

        meat_sprite = GameSprite(meat)
        meat_sprite.position = dead_sprite.position

        grid.replace_game_sprite(meat_sprite, dead_sprite)

    def replay_spawn_event(self, event):
        grid = self.get_grid_from_place(event[1].get_place())
        sprite = GameSprite(event[1])

        sprite.position = grid.get_next_sprite_position()
        grid.add_game_sprite(sprite)

        self.animate_spawn_event(sprite)

    def animate_spawn_event(self, spawned_sprite):
        self.fade_in_sprite(spawned_sprite, self.replay_next_event)

    def replay_eat_event(self, event):
        grid = self.get_grid_from_place(event[1].get_place())
        sprite = grid.search_for_game_sprite(event[1])
        new_hp = min(100, event[1].get_health() + event[2].get_food_value())
        self.animate_eat_event(sprite, new_hp)

    def animate_eat_event(self, sprite, new_hp):
        scale_x = new_hp / 100
        sprite.hp_bar_sprite = pygame.transform.scale(sprite.hp_bar_sprite, (int(sprite.rect.width * scale_x), 5))
        self.replay_next_event()

    def animate_sprite(self, sprite, target_position, callback):
        start_position = sprite.position
        distance = (target_position[0] - start_position[0], target_position[1] - start_position[1])
        steps = 30
        step_size = (distance[0] / steps, distance[1] / steps)

        def update():
            nonlocal steps
            if steps > 0:
                sprite.update_position((sprite.position[0] + step_size[0], sprite.position[1] + step_size[1]))
                steps -= 1
                return True
            else:
                callback()
                return False

        self.animations.append(update)

    def shake_sprite(self, sprite, callback):
        start_position = sprite.position
        steps = 10
        shake_distance = 5

        def update():
            nonlocal steps
            if steps > 0:
                sprite.update_position((start_position[0] + random.randint(-shake_distance, shake_distance),
                                       start_position[1] + random.randint(-shake_distance, shake_distance)))
                steps -= 1
                return True
            else:
                sprite.update_position(start_position)
                callback()
                return False

        self.animations.append(update)

    def fade_out_sprite(self, sprite, callback):
        alpha = 255
        steps = 30
        step_size = alpha / steps

        def update():
            nonlocal alpha, steps
            if steps > 0:
                alpha -= step_size
                sprite.image.set_alpha(int(alpha))
                steps -= 1
                return True
            else:
                callback()
                return False

        self.animations.append(update)

    def fade_in_sprite(self, sprite, callback):
        alpha = 0
        steps = 30
        step_size = 255 / steps

        def update():
            nonlocal alpha, steps
            if steps > 0:
                alpha += step_size
                sprite.image.set_alpha(int(alpha))
                steps -= 1
                return True
            else:
                callback()
                return False

        self.animations.append(update)

    def draw(self, screen):
        for row in self.grids:
            for grid in row:
                grid.draw(screen)

    def update(self):
        for animation in self.animations:
            if not animation():
                self.animations.remove(animation)


def animate_game_logger_events(grid_size, callback=None):
    animate_game_events(grid_size, hgc.GAME_LOGGER.events, hgc.GAME_LOGGER.map_states, callback)

def animate_game_events(grid_size, game_events, map_states, callback=None):
    screen = pygame.display.set_mode((grid_size * GRID_SIZE, grid_size * GRID_SIZE))
    game_replay_layer = GameReplayLayer(grid_size)
    game_replay_layer.animations = []

    converted_game_events = []
    for i in range(1, len(game_events)):
        converted_game_events.append(game_events[i])

    game_replay_layer.replay(converted_game_events, map_states, callback)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_replay_layer.update()
        screen.fill(SCREEN_COL)
        game_replay_layer.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)