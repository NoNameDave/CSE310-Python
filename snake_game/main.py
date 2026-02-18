"""
Snake Game (Arcade)
- Graphics: snake + food + score
- Input: arrow keys / WASD
- Moveable objects: snake moves, food relocates
- Levels/Difficulty: speed increases as score increases
"""

import random
import arcade

# -----------------------------
# Constants
# -----------------------------
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Snake (Arcade)"

GRID_SIZE = 20  # each snake segment is GRID_SIZE x GRID_SIZE

START_SPEED_TICKS = 10  # lower = faster; we will reduce as difficulty increases
MIN_SPEED_TICKS = 3

SNAKE_COLOR = arcade.color.GREEN
FOOD_COLOR = arcade.color.RED
TEXT_COLOR = arcade.color.WHITE
BG_COLOR = arcade.color.BLACK


def snap_to_grid(value: int) -> int:
    """Snap a pixel value to the nearest grid coordinate."""
    return (value // GRID_SIZE) * GRID_SIZE


def draw_rect_centered(cx: float, cy: float, w: float, h: float, color):
    """
    Draw a filled rectangle using center coordinates.
    Arcade 3.x removed draw_rectangle_filled, so we convert center -> (left,bottom,width,height).
    """
    arcade.draw_lbwh_rectangle_filled(cx - w / 2, cy - h / 2, w, h, color)


class SnakeGame(arcade.Window):
    """Main game window class."""

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(BG_COLOR)

        # Game state
        self.game_started = False
        self.game_over = False

        # Snake data
        self.snake = []  # list of (x, y) tuples
        self.direction = (1, 0)  # moving right initially (dx, dy)
        self.pending_direction = (1, 0)

        # Food
        self.food = (0, 0)

        # Score + difficulty
        self.score = 0
        self.level = 1
        self.speed_ticks = START_SPEED_TICKS
        self.tick_counter = 0

    def setup(self):
        """Set up / reset the game to the initial state."""
        self.game_started = False
        self.game_over = False

        self.score = 0
        self.level = 1
        self.speed_ticks = START_SPEED_TICKS
        self.tick_counter = 0

        # Start snake in the center with 3 segments
        start_x = snap_to_grid(SCREEN_WIDTH // 2)
        start_y = snap_to_grid(SCREEN_HEIGHT // 2)
        self.snake = [
            (start_x, start_y),
            (start_x - GRID_SIZE, start_y),
            (start_x - 2 * GRID_SIZE, start_y),
        ]
        self.direction = (1, 0)
        self.pending_direction = (1, 0)

        self.spawn_food()

    def spawn_food(self):
        """Place food randomly on the grid, avoiding the snake body."""
        while True:
            x = random.randrange(0, SCREEN_WIDTH, GRID_SIZE)
            y = random.randrange(0, SCREEN_HEIGHT, GRID_SIZE)
            if (x, y) not in self.snake:
                self.food = (x, y)
                return

    def calculate_difficulty(self):
        """
        Update level and speed based on score.
        Example: level increases every 5 points.
        Speed increases by lowering ticks between moves.
        """
        new_level = 1 + (self.score // 5)
        if new_level != self.level:
            self.level = new_level

        # Speed: every level makes snake faster, but cap it
        self.speed_ticks = max(MIN_SPEED_TICKS, START_SPEED_TICKS - (self.level - 1))

    def on_draw(self):
        """Render the screen."""
        self.clear()

        # Start screen
        if not self.game_started and not self.game_over:
            arcade.draw_text(
                "SNAKE",
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2 + 40,
                TEXT_COLOR,
                font_size=48,
                anchor_x="center",
            )
            arcade.draw_text(
                "Press ENTER to start",
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2 - 10,
                TEXT_COLOR,
                font_size=18,
                anchor_x="center",
            )
            arcade.draw_text(
                "Move: Arrow Keys or WASD",
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2 - 40,
                TEXT_COLOR,
                font_size=14,
                anchor_x="center",
            )
            return

        # Game over screen
        if self.game_over:
            arcade.draw_text(
                "GAME OVER",
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2 + 30,
                arcade.color.ORANGE_RED,
                font_size=40,
                anchor_x="center",
            )
            arcade.draw_text(
                f"Final Score: {self.score} | Level: {self.level}",
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2 - 10,
                TEXT_COLOR,
                font_size=18,
                anchor_x="center",
            )
            arcade.draw_text(
                "Press R to restart",
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2 - 45,
                TEXT_COLOR,
                font_size=14,
                anchor_x="center",
            )
            return

        # Draw food
        fx, fy = self.food
        draw_rect_centered(
            fx + GRID_SIZE / 2, fy + GRID_SIZE / 2, GRID_SIZE, GRID_SIZE, FOOD_COLOR
        )

        # Draw snake
        for i, (x, y) in enumerate(self.snake):
            color = SNAKE_COLOR if i == 0 else arcade.color.DARK_GREEN
            draw_rect_centered(
                x + GRID_SIZE / 2, y + GRID_SIZE / 2, GRID_SIZE, GRID_SIZE, color
            )

        # UI text
        arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT - 25, TEXT_COLOR, 14)
        arcade.draw_text(f"Level: {self.level}", 120, SCREEN_HEIGHT - 25, TEXT_COLOR, 14)
        arcade.draw_text(
            f"Speed: {START_SPEED_TICKS - self.speed_ticks + 1}",
            220,
            SCREEN_HEIGHT - 25,
            TEXT_COLOR,
            14,
        )

    def on_update(self, delta_time: float):
        """Game logic runs here."""
        if not self.game_started or self.game_over:
            return

        self.tick_counter += 1
        if self.tick_counter < self.speed_ticks:
            return  # wait until it's time to move
        self.tick_counter = 0

        # Apply direction change (prevents instant reverse)
        self.direction = self.pending_direction

        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx * GRID_SIZE, head_y + dy * GRID_SIZE)

        # Wall collision
        if (
            new_head[0] < 0
            or new_head[0] >= SCREEN_WIDTH
            or new_head[1] < 0
            or new_head[1] >= SCREEN_HEIGHT
        ):
            self.game_over = True
            return

        # Self collision
        if new_head in self.snake:
            self.game_over = True
            return

        # Move snake
        self.snake.insert(0, new_head)

        # Food collision
        if new_head == self.food:
            self.score += 1
            self.spawn_food()
            self.calculate_difficulty()
            # Do NOT pop tail: snake grows
        else:
            # Remove tail to maintain length
            self.snake.pop()

    def on_key_press(self, symbol: int, modifiers: int):
        """Handle keyboard input."""
        if symbol == arcade.key.ENTER and not self.game_started and not self.game_over:
            self.game_started = True
            return

        if symbol == arcade.key.R and self.game_over:
            self.setup()
            return

        if not self.game_started or self.game_over:
            return

        # Determine new direction
        new_dir = None
        if symbol in (arcade.key.UP, arcade.key.W):
            new_dir = (0, 1)
        elif symbol in (arcade.key.DOWN, arcade.key.S):
            new_dir = (0, -1)
        elif symbol in (arcade.key.LEFT, arcade.key.A):
            new_dir = (-1, 0)
        elif symbol in (arcade.key.RIGHT, arcade.key.D):
            new_dir = (1, 0)

        if new_dir is None:
            return

        # Prevent 180° turns
        current_dx, current_dy = self.direction
        new_dx, new_dy = new_dir
        if (current_dx + new_dx == 0) and (current_dy + new_dy == 0):
            return

        self.pending_direction = new_dir


def main():
    """Program entry point."""
    window = SnakeGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()