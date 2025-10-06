import pygame
import sys
import random
import time  # Añadir esta importación

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla (ahora con dimensiones iniciales)
INITIAL_WIDTH, INITIAL_HEIGHT = 1200, 700
screen = pygame.display.set_mode((INITIAL_WIDTH, INITIAL_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Jeopardy Game")

# Variables globales para dimensiones actuales
WIDTH, HEIGHT = INITIAL_WIDTH, INITIAL_HEIGHT

# Colores
BLUE_DARK = (13, 71, 161)
BLUE_MEDIUM = (21, 101, 192)
BLUE_LIGHT = (30, 136, 229)
GOLD = (255, 215, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (244, 67, 54)
GREEN = (76, 175, 80)
ORANGE = (255, 152, 0)
PURPLE = (156, 39, 176)
TEAL = (0, 150, 136)
PINK = (233, 30, 99)
YELLOW = (255, 235, 59)
GRAY = (128, 128, 128)

# CONFIGURACIÓN DE TAMAÑOS (PARÁMETROS MODIFICABLES)
SIZE_CONFIG = {
    # Espaciado general
    "margin_factor": 0.01,  # 1% del tamaño de la pantalla
    "min_margin": 5,
    # Tablero
    "board_top_margin": 100,  # Espacio superior para el título
    "board_bottom_margin": 200,  # Espacio inferior para puntuaciones
    # Categorías
    "category_height_factor": 0.20,  # 8% de la altura disponible
    "min_category_height": 40,
    "max_category_lines": 3,
    # Preguntas
    "question_height_factor": 0.30,  # 12% de la altura disponible
    "min_question_height": 60,
    # Puntuaciones de equipos
    "score_section_height_factor": 0.1,  # 10% de la altura
    "min_score_section_height": 80,
    "score_margin_factor": 0.005,  # 0.5% para espacio entre scores
    # Ventana de pregunta modal
    "modal_width_factor": 0.50,  # 50% del ancho de pantalla (aumentado de 40%)
    "modal_height_factor": 0.50,  # 50% de la altura de pantalla (aumentado de 40%)
    "modal_max_lines": 8,  # Más líneas permitidas
    "modal_vertical_padding": 0.10,  # 10% de padding vertical
    # Botones
    "button_min_width": 80,
    "button_min_height": 30,
}

# Fuentes (se inicializarán dinámicamente)
title_font = None
category_font = None
value_font = None
modal_font = None
button_font = None
score_font = None
team_font = None  # Fuente para nombres de equipos (sin negrita)
team_bold_font = None  # NUEVA: Fuente para nombres de equipos en negrita
turn_font = None


# Función para inicializar fuentes según el tamaño actual
def initialize_fonts():
    global title_font, category_font, value_font, modal_font, button_font, score_font, team_font, team_bold_font, turn_font

    # Calcular tamaños de fuente basados en la altura de la ventana
    base_size = HEIGHT // 20

    # Asegurar que todos los tamaños sean enteros usando int() o //
    title_font = pygame.font.SysFont("Arial", max(int(base_size), 30), bold=True)
    category_font = pygame.font.SysFont(
        "Arial", max(int(base_size // 1.8), 16), bold=True
    )
    value_font = pygame.font.SysFont("Arial", max(int(base_size // 1.2), 20), bold=True)
    modal_font = pygame.font.SysFont(
        "Arial", max(int(base_size // 1.3), 20)
    )  # Fuente ligeramente más grande
    button_font = pygame.font.SysFont("Arial", max(int(base_size // 1.8), 16))
    score_font = pygame.font.SysFont("Arial", max(int(base_size // 1.2), 20), bold=True)
    team_font = pygame.font.SysFont("Arial", max(int(base_size // 2.2), 14))
    team_bold_font = pygame.font.SysFont("Arial", max(int(base_size // 2.2), 14), bold=True)  # NUEVA: Fuente en negrita
    turn_font = pygame.font.SysFont("Arial", max(int(base_size // 2.2), 14), bold=True)


# Inicializar fuentes por primera vez
initialize_fonts()

# Datos del juego
categories = [
    "Fundamentos de modelos",
    "Triple helice",
    "Cuadruple helice",
    "Quintuple helice",
    "Clusters",
    "Fundamentos de Clusters",
]
question_values = [200, 400, 600, 800, 1000]

# Preguntas y respuestas (igual que antes)
questions_data = {
    "Fundamentos de modelos": [
        {
            "question": "¿Qué es un sistema de innovación?",
            "answer": "Conjunto de instituciones, actores y relaciones que facilitan la generación y aplicación de conocimiento.",
        },
        {
            "question": "¿Qué supera el concepto de sistemas de innovación?",
            "answer": "Al modelo lineal de innovación",
        },
        {
            "question": "Elemento clave para la formación de clusters según el marco teórico.",
            "answer": "La proximidad geográfica y social.",
        },
        {
            "question": "¿Qué tipo de instituciones surgen de la interacción entre actores en los sistemas de innovación?",
            "answer": "Instituciones híbridas.",
        },
        {
            "question": "¿Por qué se dice que la innovación es un proceso no lineal?",
            "answer": "Porque involucra interacciones dinámicas y retroalimentación entre múltiples actores",
        },
    ],
    "Triple helice": [
        {
            "question": "Nombra los tres actores del modelo de Triple Hélice.",
            "answer": "Universidad, industria, gobierno.",
        },
        {
            "question": "¿Quiénes propusieron originalmente el modelo de Triple Hélice?",
            "answer": "Etzkowitz y Leydesdorff",
        },
        {
            "question": "Menciona un ejemplo de institución híbrida en este modelo",
            "answer": "Parques científicos / Oficinas de transferencia tecnológica.",
        },
        {
            "question": "¿Qué papel juega la universidad en la Triple Hélice?",
            "answer": "Aporta conocimiento y capital humano",
        },
        {
            "question": "¿En qué programa de la Unión Europea se aplica el modelo de Triple Hélice?",
            "answer": "Horizonte 2020",
        },
    ],
    "Cuadruple helice": [
        {
            "question": "¿Qué actor se añade en el modelo de Cuádruple Hélice?", 
            "answer": "La sociedad civil"
            },
        {
            "question": "Menciona una ventaja de incluir a la sociedad civil en la innovación.", 
            "answer": "Mayor legitimidad y aceptación social."
            },
        {
            "question": "¿Qué tipo de innovación promueve la Cuádruple Hélice?", 
            "answer": "Innovación social / orientada a la demanda."
            },
        {
            "question": "¿En qué proyecto participa la sociedad civil y en donde?",
            "answer": "Proyecto Smart Citizen en Barcelona.",
        },
        {
            "question": "¿Cuál es una limitación del modelo de Cuádruple Hélice?",
            "answer": "Mayor complejidad en la coordinación entre actores.",
        },
    ],
    "Quintuple helice": [
        {
            "question": "¿Qué actor se incorpora en el modelo de Quíntuple Hélice?", 
            "answer": "El medio ambiente."
            },
        {
            "question": "¿Qué desafíos globales busca enfrentar este modelo?", 
            "answer": "Cambio climático, pérdida de biodiversidad, transición a economías verdes"
            },
        {
            "question": "Menciona un mecanismo para implementar la Quíntuple Hélice.",
            "answer": "Mesas de diálogo / Proyectos colaborativos / Plataformas digitales.",
        },
        {
            "question": "¿Qué papel juega el gobierno en este modelo?",
            "answer": "Diseñar políticas y regular a favor del desarrollo sostenible.",
        },
        {
            "question": "Da un ejemplo internacional donde se aplique este modelo y en que lugar.",
            "answer": "Eco-innovación en Europa / Alianzas para los ODS",
        },
    ],
    "Clusters": [
        {
            "question": "¿Qué es un cluster?",
            "answer": "Concentración geográfica de empresas e instituciones interconectadas.",
        },
        {
            "question": "Nombra el cluster tecnológico más famoso de Estados Unidos.",
            "answer": "Silicon Valley",
        },
        {
            "question": "Menciona un cluster especializado en biotecnología",
            "answer": "Boston",
        },
        {
            "question": "¿Qué autor definió el concepto moderno de cluster?",
            "answer": "Michael Porter",
        },
        {
            "question": "¿Cuáles son las tres vías de impacto que señaló Porter para los clusters?",
            "answer": "Incremento de la productividad, dirección y velocidad de la innovación, y creación de nuevas empresas",
        },
    ],
    "Fundamentos de Clusters": [
        {
            "question": "¿Quién introdujo la idea original de distritos industriales?",
            "answer": "Alfred Marshall.",
        },
        {
            "question": "¿Qué concepto económico se asocia con la concentración espacial de empresas?",
            "answer": "Economías de aglomeración.",
        },
        {
            "question": "Menciona un factor crítico para el éxito de un cluster según Porter.",
            "answer": "Demanda sofisticada / Rivalidad empresarial / Industrias de soporte",
        },
        {
            "question": "¿Qué institución internacional enfatiza la integración de clusters en cadenas de valor sostenibles?",
            "answer": "UNIDO",
        },
        {
            "question": "Según Big Think (2024), ¿de qué depende la innovación en un cluster?",
            "answer": "De la interacción social, cultural y académica, no del \"genio solitario\"",
        },
    ],
}

# Lista de nombres de equipos
team_names = [
    "Aurora",
    "Dodgers",
    "Wachiturros",
    "Boots",
    "Lobas",
    "Acme",
    "Galacticos",
]

# Seleccionar 7 equipos al azar (todos los nombres disponibles)
selected_teams = random.sample(team_names, 7)

# Estado del juego
team_scores = [0] * 7
team_colors = [BLUE_DARK, BLUE_MEDIUM, GREEN, ORANGE, PURPLE, TEAL, PINK]
current_turn = 0
used_questions = {}
current_question = None
current_question_value = 0
current_category_index = -1
current_value_index = -1
show_answer = False
game_state = "board"
show_menu = False
assigning_points = False  # Nuevo estado para asignación manual de puntos

# Variables para el temporizador
question_start_time = 0
timer_duration = 30  # 30 segundos
timer_active = False
time_expired = False  # Nueva variable para controlar si el tiempo ha expirado

# Dimensiones del tablero (se calcularán dinámicamente)
CATEGORY_HEIGHT = None
QUESTION_HEIGHT = None
MARGIN = None
BOARD_WIDTH = None
SCORE_SECTION_HEIGHT = None


# Función para calcular dimensiones dinámicas usando la configuración
def calculate_dimensions():
    global CATEGORY_HEIGHT, QUESTION_HEIGHT, MARGIN, BOARD_WIDTH, SCORE_SECTION_HEIGHT

    # Calcular márgenes
    MARGIN = max(SIZE_CONFIG["min_margin"], int(HEIGHT * SIZE_CONFIG["margin_factor"]))
    BOARD_WIDTH = WIDTH - 2 * MARGIN

    # Calcular espacio disponible para el tablero
    available_height = (
        HEIGHT - SIZE_CONFIG["board_top_margin"] - SIZE_CONFIG["board_bottom_margin"]
    )

    # Calcular altura de categorías
    CATEGORY_HEIGHT = max(
        SIZE_CONFIG["min_category_height"],
        int(available_height * SIZE_CONFIG["category_height_factor"]),
    )

    # Calcular altura de preguntas
    remaining_height = available_height - CATEGORY_HEIGHT
    QUESTION_HEIGHT = max(
        SIZE_CONFIG["min_question_height"],
        int(
            remaining_height
            * SIZE_CONFIG["question_height_factor"]
            / len(question_values)
        ),
    )

    # Calcular altura de la sección de puntuaciones
    SCORE_SECTION_HEIGHT = max(
        SIZE_CONFIG["min_score_section_height"],
        int(HEIGHT * SIZE_CONFIG["score_section_height_factor"]),
    )


# Inicializar dimensiones por primera vez
calculate_dimensions()


# Clase para botones mejorada
class Button:
    def __init__(
        self,
        relative_x,
        relative_y,
        relative_width,
        relative_height,
        text,
        color,
        hover_color,
    ):
        self.relative_x = relative_x
        self.relative_y = relative_y
        self.relative_width = relative_width
        self.relative_height = relative_height
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.update_position()

    def update_position(self):
        self.rect.x = int(self.relative_x * WIDTH)
        self.rect.y = int(self.relative_y * HEIGHT)
        self.rect.width = max(
            SIZE_CONFIG["button_min_width"], int(self.relative_width * WIDTH)
        )
        self.rect.height = max(
            SIZE_CONFIG["button_min_height"], int(self.relative_height * HEIGHT)
        )

    def draw(self, surface):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=5)
        pygame.draw.rect(surface, BLACK, self.rect, 2, border_radius=5)

        if button_font:
            text = self.text
            if button_font.size(text)[0] > self.rect.width - 10:
                while (
                    len(text) > 3
                    and button_font.size(text + "...")[0] > self.rect.width - 10
                ):
                    text = text[:-1]
                text = text + "..." if len(text) > 3 else self.text[:3] + "..."

            text_surf = button_font.render(text, True, WHITE)
            text_rect = text_surf.get_rect(center=self.rect.center)
            surface.blit(text_surf, text_rect)

    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)
        return self.is_hovered

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


# Crear botones - CENTRADOS DENTRO DEL MARGEN DE LA VENTANA DE PREGUNTA
show_answer_button = Button(
    0.22, 0.85, 0.15, 0.07, "Mostrar Respuesta", GREEN, (100, 200, 100)
)
assign_points_button = Button(
    0.42, 0.85, 0.15, 0.07, "Asignar Puntos", ORANGE, (255, 180, 0)
)
no_points_button = Button(0.62, 0.85, 0.15, 0.07, "Sin Puntos", GRAY, (100, 100, 100))

# Botones para el modo de asignación de puntos
assign_to_current_button = Button(
    0.22, 0.85, 0.15, 0.07, "Correcto (+)", GREEN, (100, 200, 100)
)
assign_to_other_button = Button(
    0.42, 0.85, 0.15, 0.07, "Otro Equipo", BLUE_LIGHT, (100, 150, 255)
)
cancel_assign_button = Button(0.62, 0.85, 0.15, 0.07, "Cancelar", RED, (200, 100, 100))

menu_button = Button(0.02, 0.02, 0.08, 0.04, "MENÚ", PURPLE, (180, 60, 200))

# Botones del menú
reset_scores_button = Button(
    0.02, 0.08, 0.15, 0.04, "Reiniciar Puntuaciones", ORANGE, (255, 180, 0)
)
reset_game_button = Button(
    0.02, 0.14, 0.15, 0.04, "Reiniciar Juego", RED, (255, 100, 100)
)
next_turn_button = Button(
    0.02, 0.20, 0.15, 0.04, "Siguiente Turno", BLUE_LIGHT, (100, 150, 255)
)
close_menu_button = Button(
    0.02, 0.26, 0.15, 0.04, "Cerrar Menú", (128, 128, 128), (150, 150, 150)
)

# Botones para seleccionar equipo al asignar puntos
team_buttons = []
for i in range(7):
    team_buttons.append(
        Button(
            0.15 + (i % 4) * 0.2,
            0.65 + (i // 4) * 0.08,
            0.15,
            0.06,
            selected_teams[i],
            team_colors[i],
            team_colors[i],
        )
    )


def update_button_positions():
    show_answer_button.update_position()
    assign_points_button.update_position()
    no_points_button.update_position()
    assign_to_current_button.update_position()
    assign_to_other_button.update_position()
    cancel_assign_button.update_position()
    menu_button.update_position()
    reset_scores_button.update_position()
    reset_game_button.update_position()
    next_turn_button.update_position()
    close_menu_button.update_position()

    # Actualizar posiciones de botones de equipos
    for i, button in enumerate(team_buttons):
        button.text = selected_teams[i]  # Actualizar nombre del equipo
        button.color = team_colors[i]
        button.hover_color = team_colors[i]
        button.relative_x = 0.15 + (i % 4) * 0.2
        button.relative_y = 0.65 + (i // 4) * 0.08
        button.update_position()


update_button_positions()


def next_turn():
    global current_turn
    current_turn = (current_turn + 1) % 7


def draw_text(surface, text, font, color, rect, max_lines=10):
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        test_line = current_line + [word]
        test_text = " ".join(test_line)
        test_width = font.size(test_text)[0]

        if test_width <= rect.width - 20:
            current_line.append(word)
        else:
            if current_line:
                lines.append(" ".join(current_line))
            current_line = [word]

    if current_line:
        lines.append(" ".join(current_line))

    lines = lines[:max_lines]

    # Calcular altura total del texto para centrar verticalmente
    total_text_height = len(lines) * (font.get_height() + 5) - 5
    y = rect.top + (rect.height - total_text_height) // 2

    for line in lines:
        text_surf = font.render(line, True, color)
        text_rect = text_surf.get_rect(center=(rect.centerx, y))
        surface.blit(text_surf, text_rect)
        y += font.get_height() + 5  # Espaciado entre líneas


def draw_menu():
    menu_width = int(0.18 * WIDTH)
    menu_height = int(0.32 * HEIGHT)
    menu_x = int(0.01 * WIDTH)
    menu_y = int(0.06 * HEIGHT)

    menu_rect = pygame.Rect(menu_x, menu_y, menu_width, menu_height)
    pygame.draw.rect(screen, (40, 40, 40), menu_rect, border_radius=8)
    pygame.draw.rect(screen, WHITE, menu_rect, 2, border_radius=8)

    if button_font:
        menu_title = button_font.render("OPCIONES", True, WHITE)
        title_rect = menu_title.get_rect(center=(menu_x + menu_width // 2, menu_y + 15))
        screen.blit(menu_title, title_rect)

    reset_scores_button.draw(screen)
    reset_game_button.draw(screen)
    next_turn_button.draw(screen)
    close_menu_button.draw(screen)


def draw_timer(surface, modal_rect):
    if not timer_active and not time_expired:
        return

    # Calcular tiempo transcurrido
    if time_expired:
        remaining_time = 0
        progress = 0
    else:
        elapsed_time = time.time() - question_start_time
        remaining_time = max(0, timer_duration - elapsed_time)
        progress = remaining_time / timer_duration

    # Dibujar el círculo del temporizador
    timer_radius = 30
    timer_x = modal_rect.right - timer_radius - 20
    timer_y = modal_rect.top + timer_radius + 20

    # Fondo del círculo
    pygame.draw.circle(surface, BLUE_MEDIUM, (timer_x, timer_y), timer_radius)

    # Arco de progreso (rojo cuando queda poco tiempo o tiempo expirado)
    if time_expired:
        color = RED
        # Dibujar círculo completo en rojo cuando el tiempo expira
        pygame.draw.circle(surface, RED, (timer_x, timer_y), timer_radius)
    else:
        color = (
            RED if remaining_time <= 3 else GREEN
        )  # Rojo cuando quedan 3 segundos o menos

    if progress > 0 and not time_expired:
        pygame.draw.arc(
            surface,
            color,
            (
                timer_x - timer_radius,
                timer_y - timer_radius,
                timer_radius * 2,
                timer_radius * 2,
            ),
            -3.14159 / 2,
            2 * 3.14159 * progress - 3.14159 / 2,
            5,
        )

    # Texto del tiempo restante
    timer_text = "0s" if time_expired else str(int(remaining_time) + 1) + "s"
    timer_surf = modal_font.render(timer_text, True, WHITE)
    timer_rect = timer_surf.get_rect(center=(timer_x, timer_y))
    surface.blit(timer_surf, timer_rect)


def draw_board():
    calculate_dimensions()

    # Dibujar título
    title_surf = title_font.render("JEOPARDY GAME", True, WHITE)
    title_rect = title_surf.get_rect(center=(WIDTH // 2, 40))
    screen.blit(title_surf, title_rect)

    # Dibujar categorías
    category_width = BOARD_WIDTH // len(categories)
    for i, category in enumerate(categories):
        x = MARGIN + i * category_width
        y = SIZE_CONFIG["board_top_margin"]
        rect = pygame.Rect(x, y, category_width - MARGIN, CATEGORY_HEIGHT)
        pygame.draw.rect(screen, BLUE_DARK, rect, border_radius=5)
        pygame.draw.rect(screen, WHITE, rect, 2, border_radius=5)
        draw_text(
            screen,
            category,
            category_font,
            WHITE,
            rect,
            SIZE_CONFIG["max_category_lines"],
        )

    # Dibujar preguntas
    for i in range(len(categories)):
        for j in range(len(question_values)):
            x = MARGIN + i * category_width
            y = (
                SIZE_CONFIG["board_top_margin"]
                + CATEGORY_HEIGHT
                + MARGIN
                + j * (QUESTION_HEIGHT + MARGIN)
            )
            rect = pygame.Rect(x, y, category_width - MARGIN, QUESTION_HEIGHT)

            question_key = f"{i}-{j}"
            if question_key in used_questions:
                pygame.draw.rect(screen, BLUE_DARK, rect, border_radius=5)
            else:
                pygame.draw.rect(screen, BLUE_MEDIUM, rect, border_radius=5)
                pygame.draw.rect(screen, GOLD, rect, 2, border_radius=5)

                # MODIFICACIÓN: Quitar el signo $ del valor
                value_surf = value_font.render(str(question_values[j]), True, GOLD)
                value_rect = value_surf.get_rect(center=rect.center)
                screen.blit(value_surf, value_rect)

    # Dibujar indicador de turno actual (con más separación)
    turn_text = f"Turno actual: {selected_teams[current_turn]}"
    turn_surf = turn_font.render(turn_text, True, YELLOW)
    turn_rect = turn_surf.get_rect(
        center=(
            WIDTH // 2,
            HEIGHT - SCORE_SECTION_HEIGHT - 60,
        )  # Más separación (60 en lugar de 40)
    )
    screen.blit(turn_surf, turn_rect)

    # Dibujar puntuaciones de los 7 equipos
    score_margin = max(5, int(WIDTH * SIZE_CONFIG["score_margin_factor"]))
    team_score_width = (WIDTH - 40 - 6 * score_margin) // 7

    for i in range(7):
        x = 20 + i * (team_score_width + score_margin)
        y = HEIGHT - SCORE_SECTION_HEIGHT - 20
        rect = pygame.Rect(x, y, team_score_width, SCORE_SECTION_HEIGHT)

        if i == current_turn:
            pygame.draw.rect(screen, YELLOW, rect, border_radius=10)
            pygame.draw.rect(screen, YELLOW, rect, 4, border_radius=10)
            inner_rect = pygame.Rect(
                x + 3, y + 3, team_score_width - 6, SCORE_SECTION_HEIGHT - 6
            )
            pygame.draw.rect(screen, team_colors[i], inner_rect, border_radius=8)
        else:
            pygame.draw.rect(screen, team_colors[i], rect, border_radius=10)
            pygame.draw.rect(screen, WHITE, rect, 2, border_radius=10)

        # MODIFICACIÓN: Mostrar nombre completo del equipo en negrita
        team_name = selected_teams[i]
        
        # Usar la nueva fuente en negrita para los nombres de equipos
        team_surf = team_bold_font.render(team_name, True, WHITE)
        
        # Ajustar el texto si es demasiado ancho para el cuadro
        if team_surf.get_width() > team_score_width - 10:
            # Si el texto es demasiado ancho, reducimos el tamaño de fuente gradualmente
            temp_font_size = team_bold_font.get_height()
            while temp_font_size > 10 and team_surf.get_width() > team_score_width - 10:
                temp_font_size -= 1
                temp_font = pygame.font.SysFont("Arial", temp_font_size, bold=True)
                team_surf = temp_font.render(team_name, True, WHITE)
        
        team_rect = team_surf.get_rect(center=(x + team_score_width // 2, y + 25))
        screen.blit(team_surf, team_rect)

        score_surf = score_font.render(str(team_scores[i]), True, GOLD)
        score_rect = score_surf.get_rect(
            center=(x + team_score_width // 2, y + SCORE_SECTION_HEIGHT - 25)
        )
        screen.blit(score_surf, score_rect)

    menu_button.draw(screen)
    if show_menu:
        draw_menu()


def draw_question():
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 200))
    screen.blit(overlay, (0, 0))

    modal_width = int(WIDTH * SIZE_CONFIG["modal_width_factor"])
    modal_height = int(HEIGHT * SIZE_CONFIG["modal_height_factor"])
    modal_rect = pygame.Rect(
        (WIDTH - modal_width) // 2,
        (HEIGHT - modal_height) // 2,
        modal_width,
        modal_height,
    )

    pygame.draw.rect(screen, BLUE_DARK, modal_rect, border_radius=10)
    pygame.draw.rect(screen, WHITE, modal_rect, 3, border_radius=10)

    # Dibujar temporizador
    draw_timer(screen, modal_rect)

    # MODIFICACIÓN: Quitar el signo $ del valor en la información del turno
    turn_info_text = (
        f"Turno de: {selected_teams[current_turn]} - Valor: {current_question_value}"
    )
    turn_info_surf = modal_font.render(turn_info_text, True, YELLOW)
    turn_info_text_rect = turn_info_surf.get_rect(
        center=(
            modal_rect.centerx,
            modal_rect.top + 50,
        )  # Más separación (50 en lugar de 40)
    )
    screen.blit(turn_info_surf, turn_info_text_rect)

    if current_question and not assigning_points:
        # Calcular espacio vertical disponible después del texto del turno
        available_height = modal_rect.height - 100  # Más espacio para contenido

        # Área para la pregunta - mejor centrado vertical
        question_height = available_height * 0.55  # 40% del espacio disponible
        question_rect = pygame.Rect(
            modal_rect.left + 30,  # Más margen izquierdo
            modal_rect.top + 80,  # Más separación del texto del turno
            modal_rect.width - 60,  # Compensar márgenes aumentados
            question_height,
        )

        # Dibujar fondo para la pregunta (opcional, para mejor visualización)
        pygame.draw.rect(screen, BLUE_MEDIUM, question_rect, border_radius=5)

        draw_text(
            screen,
            current_question["question"],
            modal_font,
            WHITE,
            question_rect,
            SIZE_CONFIG["modal_max_lines"],
        )

        if show_answer:
            # Área para la respuesta - mejor centrado vertical
            answer_height = available_height * 0.4  # 40% del espacio disponible
            answer_rect = pygame.Rect(
                modal_rect.left + 30,  # Más margen izquierdo
                modal_rect.top + 80 + question_height + 20,  # Separación de la pregunta
                modal_rect.width - 60,  # Compensar márgenes aumentados
                answer_height,
            )

            # Dibujar fondo para la respuesta (opcional)
            pygame.draw.rect(screen, (30, 80, 160), answer_rect, border_radius=5)

            draw_text(
                screen,
                f"Respuesta: {current_question['answer']}",
                modal_font,
                GOLD,
                answer_rect,
                SIZE_CONFIG["modal_max_lines"],
            )

    if not assigning_points:
        # Mostrar solo los 3 botones centrados dentro del margen de la ventana
        show_answer_button.draw(screen)
        assign_points_button.draw(screen)
        no_points_button.draw(screen)
    else:
        # Modo de asignación de puntos - Mostrar solo la interfaz de asignación
        instruction_text = "¿Quién respondió correctamente?"
        instruction_surf = modal_font.render(instruction_text, True, WHITE)
        instruction_rect = instruction_surf.get_rect(
            center=(modal_rect.centerx, modal_rect.top + 100)
        )
        screen.blit(instruction_surf, instruction_rect)

        assign_to_current_button.draw(screen)
        assign_to_other_button.draw(screen)
        cancel_assign_button.draw(screen)

        if game_state == "select_team":
            # Mostrar botones de selección de equipo
            for button in team_buttons:
                button.draw(screen)


def assign_points(team_index):
    team_scores[team_index] += current_question_value
    print(
        f"Puntos asignados a {selected_teams[team_index]}: +{current_question_value}"  # MODIFICACIÓN: Quitar $
    )


def no_points():
    print(f"Ningún equipo recibió puntos por esta pregunta ({current_question_value})")  # MODIFICACIÓN: Quitar $


def close_question_modal():
    global game_state, show_answer, assigning_points, timer_active, time_expired
    game_state = "board"
    show_answer = False
    assigning_points = False
    timer_active = False
    time_expired = False
    next_turn()


def handle_board_click(pos):
    global current_question, show_answer, game_state
    global current_category_index, current_value_index, current_question_value
    global question_start_time, timer_active, time_expired

    if game_state != "board":
        return

    category_width = BOARD_WIDTH // len(categories)

    for i in range(len(categories)):
        for j in range(len(question_values)):
            x = MARGIN + i * category_width
            y = (
                SIZE_CONFIG["board_top_margin"]
                + CATEGORY_HEIGHT
                + MARGIN
                + j * (QUESTION_HEIGHT + MARGIN)
            )
            rect = pygame.Rect(x, y, category_width - MARGIN, QUESTION_HEIGHT)

            if rect.collidepoint(pos):
                question_key = f"{i}-{j}"
                if question_key not in used_questions:
                    # VERIFICACIÓN DE SEGURIDAD
                    category_name = categories[i]
                    if category_name not in questions_data:
                        print(f"Error: Categoría '{category_name}' no encontrada")
                        return

                    used_questions[question_key] = True
                    current_category_index = i
                    current_value_index = j
                    current_question_value = question_values[j]
                    current_question = questions_data[category_name][j]
                    show_answer = False
                    game_state = "question"

                    # Iniciar temporizador
                    question_start_time = time.time()
                    timer_active = True
                    time_expired = False

                    print(f"Pregunta seleccionada: {category_name} - {question_values[j]}")  # MODIFICACIÓN: Quitar $
                    return


def main():
    global game_state, show_answer, team_scores, used_questions, current_question, selected_teams, current_turn
    global WIDTH, HEIGHT, screen, show_menu, assigning_points
    global timer_active, question_start_time, time_expired

    clock = pygame.time.Clock()

    print("Equipos seleccionados para esta partida:")
    for i, team in enumerate(selected_teams):
        print(f"Equipo {i+1}: {team}")
    print(f"Comienza el equipo: {selected_teams[current_turn]}\n")

    while True:
        mouse_pos = pygame.mouse.get_pos()

        menu_button.check_hover(mouse_pos)

        if show_menu:
            reset_scores_button.check_hover(mouse_pos)
            reset_game_button.check_hover(mouse_pos)
            next_turn_button.check_hover(mouse_pos)
            close_menu_button.check_hover(mouse_pos)

        if game_state in ["question", "answer", "assign_points", "select_team"]:
            if not assigning_points:
                show_answer_button.check_hover(mouse_pos)
                assign_points_button.check_hover(mouse_pos)
                no_points_button.check_hover(mouse_pos)
            else:
                assign_to_current_button.check_hover(mouse_pos)
                assign_to_other_button.check_hover(mouse_pos)
                cancel_assign_button.check_hover(mouse_pos)
                if game_state == "select_team":
                    for button in team_buttons:
                        button.check_hover(mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.size
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
                initialize_fonts()
                calculate_dimensions()
                update_button_positions()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if menu_button.is_clicked(mouse_pos):
                    show_menu = not show_menu
                elif show_menu:
                    if reset_scores_button.is_clicked(mouse_pos):
                        team_scores = [0] * 7
                        print("Puntuaciones reiniciadas")
                        show_menu = False
                    elif reset_game_button.is_clicked(mouse_pos):
                        team_scores = [0] * 7
                        used_questions = {}
                        current_question = None
                        current_turn = 0
                        selected_teams = random.sample(team_names, 7)
                        print("Juego reiniciado")
                        print("Nuevos equipos seleccionados:")
                        for i, team in enumerate(selected_teams):
                            print(f"Equipo {i+1}: {team}")
                        print(f"Comienza el equipo: {selected_teams[current_turn]}\n")
                        show_menu = False
                    elif next_turn_button.is_clicked(mouse_pos):
                        next_turn()
                        print(f"Turno cambiado a: {selected_teams[current_turn]}")
                        show_menu = False
                    elif close_menu_button.is_clicked(mouse_pos):
                        show_menu = False
                elif game_state == "board":
                    handle_board_click(mouse_pos)
                elif game_state in [
                    "question",
                    "answer",
                    "assign_points",
                    "select_team",
                ]:
                    if not assigning_points:
                        if show_answer_button.is_clicked(mouse_pos):
                            show_answer = True
                            game_state = "answer"
                        elif assign_points_button.is_clicked(mouse_pos):
                            assigning_points = True
                            game_state = "assign_points"
                        elif no_points_button.is_clicked(mouse_pos):
                            no_points()
                            close_question_modal()
                    else:
                        if assign_to_current_button.is_clicked(mouse_pos):
                            assign_points(current_turn)
                            close_question_modal()
                        elif assign_to_other_button.is_clicked(mouse_pos):
                            game_state = "select_team"
                        elif cancel_assign_button.is_clicked(mouse_pos):
                            assigning_points = False
                            game_state = "question"
                        elif game_state == "select_team":
                            for i, button in enumerate(team_buttons):
                                if button.is_clicked(mouse_pos):
                                    assign_points(i)
                                    close_question_modal()
                                    break

        # Verificar temporizador
        if timer_active and not time_expired:
            elapsed_time = time.time() - question_start_time
            if elapsed_time >= timer_duration:
                time_expired = True
                timer_active = False
                print("¡Tiempo agotado!")

        screen.fill(BLUE_DARK)

        if game_state == "board":
            draw_board()
        elif game_state in ["question", "answer", "assign_points", "select_team"]:
            draw_question()

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()