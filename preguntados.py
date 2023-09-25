import os
import pygame
from constants import *
from functions import *
from datos import lista

#Ruta
route = os.getcwd()

#Listas
questions = []
options_a = []
options_b = []
options_c = []
answers = []

#Variables
start_flag = False
end_flag = False
fail_flag = "Default"
lap_counter = 0
answer_counter = {"value": 1}
score = {"value": 0}

#Subdivisión de la Lista General
for i in range(len(lista)):
    questions.append(lista[i]["pregunta"])
    options_a.append(lista[i]["a"])
    options_b.append(lista[i]["b"])
    options_c.append(lista[i]["c"])
    answers.append(lista[i]["correcta"])

pygame.init()
screen = pygame.display.set_mode([1433, 800])
running = True

#Título, Ícono, Fondo e Imágenes (ACLARACIÓN, SE DEBEN CAMBIAR LAS RUTAS SEGÚN ESTEN EN CADA PC, YA QUE NO LOGRÉ QUE SE ADAPTEN Y CONSERVEN)
pygame.display.set_caption("Preguntados")
icon = pygame.image.load(os.getcwd() + "/Clase 3/Desafío Preguntados/images/logo.png")
pygame.display.set_icon(icon)
background = pygame.image.load(os.getcwd() + "/Clase 3/Desafío Preguntados/images/background.jpg")
answer_logo = pygame.image.load(os.getcwd() + "/Clase 3/Desafío Preguntados/images/interrogation.png")
reset_logo = pygame.image.load(os.getcwd() + "/Clase 3/Desafío Preguntados/images/reset.png")

#Rectángulos
questions_rect = pygame.Rect((50, 45), (200, 100))
restart_rect = pygame.Rect((1183, 50), (200, 100))
score_rect = pygame.Rect((50, 200), (200, 460))
answer_rect = pygame.Rect((1183, 300), (200, 200))
option_a_rect = pygame.Rect((375, 600), (200, 60))
option_b_rect = pygame.Rect((625, 600), (200, 60))
option_c_rect = pygame.Rect((875, 600), (200, 60))
question_text_rect = pygame.Rect((325, 700), (800, 60))
end_game_rect = pygame.Rect((312, 45), (810, 520))
quit_end = pygame.Rect((620, 275), (200, 200))

#Fuentes de Texto
font_titles = pygame.font.SysFont("Arial Narrow", 50)
font_questions = pygame.font.SysFont("Arial Narrow", 35)
font_options = pygame.font.SysFont("Arial Narrow", 25)

#Textos
text_title_question = font_titles.render("Preguntas", True, (White))
text_title_restart = font_titles.render("Reiniciar", True, (White))
text_title_score = font_titles.render("Score", True, (Black))
text_score = font_titles.render(str(score["value"]), True, (Black))
each_question = font_questions.render("Clickee en 'Preguntas' para comenzar...", True, (White))
text_option_a = font_options.render("Opción A", True, (White))
text_option_b = font_options.render("Opción B", True, (White))
text_option_c = font_options.render("Opción C", True, (White))
end_game_text = font_titles.render("¡Juego Terminado!", True, (White))
end_game_text_two = font_titles.render("Score: {0}".format(str(score["value"])), True, (White))

#Música
pygame.mixer.init()
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.load(os.getcwd() + "/Clase 3/Desafío Preguntados/sounds/background.mp3")
pygame.mixer.music.play(-1)
correct_answer = pygame.mixer.Sound(os.getcwd() + "/Clase 3/Desafío Preguntados/sounds/correct_answer.mp3")
correct_answer.set_volume(0.3)
fail = pygame.mixer.Sound(os.getcwd() + "/Clase 3/Desafío Preguntados/sounds/fail.mp3")
fail.set_volume(0.3)
turn_lost = pygame.mixer.Sound(os.getcwd() + "/Clase 3/Desafío Preguntados/sounds/turn_lost.mp3")
turn_lost.set_volume(0.3)
reset = pygame.mixer.Sound(os.getcwd() + "/Clase 3/Desafío Preguntados/sounds/reset.mp3")
reset.set_volume(0.3)
start = pygame.mixer.Sound(os.getcwd() + "/Clase 3/Desafío Preguntados/sounds/start.mp3")
start.set_volume(0.3)

#Funciones Específicas para Pygame
def reset_advance_score (function_flag):
    global each_question
    global text_option_a
    global text_option_b
    global text_option_c
    global score
    global text_score
    global lap_counter
    global start_flag
    global fail_flag
    global text_score
    global answer_counter
    global answer_logo
    #Implica resetear
    if (function_flag == "Resetear"):
        each_question = font_questions.render("Clickee en 'Preguntas' para comenzar...", True, (White))
        text_option_a = font_options.render("Opción A", True, (White))
        text_option_b = font_options.render("Opción B", True, (White))
        text_option_c = font_options.render("Opción C", True, (White))
        score = {"value": 0}
        text_score = font_titles.render(str(score["value"]), True, (Black))
        lap_counter = 0
        start_flag = False
        fail_flag = "Default"
        answer_logo = pygame.image.load(os.getcwd() + "/Clase 3/Desafío Preguntados/images/interrogation.png")
    #Implica avanzar sin contabilizar puntos
    elif (function_flag == "Avanzar"):
        each_question = font_questions.render(str(questions[lap_counter]), True, (White))
        text_option_a = font_options.render(str(options_a[lap_counter]), True, (White))
        text_option_b = font_options.render(str(options_b[lap_counter]), True, (White))
        text_option_c = font_options.render(str(options_c[lap_counter]), True, (White))
        lap_counter += 1
        start_flag = True
        fail_flag = "Default"
        answer_counter["value"] = 1
        answer_logo = pygame.image.load(os.getcwd() + "/Clase 3/Desafío Preguntados/images/interrogation.png")
    #Implica avanzar contabilizando puntos
    elif ("Score"):
        text_score = font_titles.render(str(score["value"]), True, (Black))
        each_question = font_questions.render(str(questions[lap_counter]), True, (White))
        text_option_a = font_options.render(str(options_a[lap_counter]), True, (White))
        text_option_b = font_options.render(str(options_b[lap_counter]), True, (White))
        text_option_c = font_options.render(str(options_c[lap_counter]), True, (White))
        lap_counter += 1
        fail_flag = "Default"

def end_game ():
    #Implica terminar el juego
    global end_flag
    global end_game_text_two
    end_game_text_two = font_titles.render("Score: {0}".format(str(score["value"])), True, (White))
    end_flag = True

while running:
    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONDOWN):
            position_click = list(event.pos)
            #Juego Terminado
            if (end_flag == True):
                if ((position_click[0] > 620 and position_click[0] < 820) and (position_click[1] > 275 and position_click[1] < 475)):
                    end_flag = False
                    reset_advance_score("Resetear")
            else:
                #Tanda de Preguntas
                if ((position_click[0] > 50 and position_click[0] < 250) and (position_click[1] > 45 and position_click[1] < 145)):
                    if lap_counter >= len(lista):
                        end_game()
                    else:
                        start.play()
                        reset_advance_score("Avanzar")
                #Reinicio
                if ((position_click[0] > 1183 and position_click[0] < 1385) and (position_click[1] > 50 and position_click[1] < 150)):
                    reset.play()
                    reset_advance_score("Resetear")
                #Respuesta A
                if ((position_click[0] > 375 and position_click[0] < 575) and (position_click[1] > 600 and position_click[1] < 660)):
                    result = answer_verification(start_flag, score, lap_counter, answer_counter, answers, "a")
                    if (result == "Respuesta Correcta" or result == "No más opciones"):
                        if lap_counter >= len(lista):
                            end_game()
                        else:
                            if (result == "Respuesta Correcta"):
                                correct_answer.play()
                                reset_advance_score("Score")
                                answer_logo = pygame.image.load(os.getcwd() + "/Clase 3/Desafío Preguntados/images/check.png")
                            else:
                                turn_lost.play()
                                reset_advance_score("Score")
                    else:
                        fail.play()
                        fail_flag = "Fail_A"
                        answer_logo = pygame.image.load(os.getcwd() + "/Clase 3/Desafío Preguntados/images/error.png")
                #Respuesta B
                if ((position_click[0] > 625 and position_click[0] < 825) and (position_click[1] > 600 and position_click[1] < 660)):
                    result = answer_verification(start_flag, score, lap_counter, answer_counter, answers, "b")
                    if (result == "Respuesta Correcta" or result == "No más opciones"):
                        if lap_counter >= len(lista):
                            end_game()
                        else:
                            if (result == "Respuesta Correcta"):
                                correct_answer.play()
                                reset_advance_score("Score")
                                answer_logo = pygame.image.load(os.getcwd() + "/Clase 3/Desafío Preguntados/images/check.png")
                            else:
                                turn_lost.play()
                                reset_advance_score("Score")
                    else:
                        fail.play()
                        fail_flag = "Fail_B"
                        answer_logo = pygame.image.load(os.getcwd() + "/Clase 3/Desafío Preguntados/images/error.png")
                #Respuesta C
                if ((position_click[0] > 875 and position_click[0] < 1075) and (position_click[1] > 600 and position_click[1] < 660)):
                    result = answer_verification(start_flag, score, lap_counter, answer_counter, answers, "c")
                    if (result == "Respuesta Correcta" or result == "No más opciones"):
                        if lap_counter >= len(lista):
                            end_game()
                        else:
                            if (result == "Respuesta Correcta"):
                                correct_answer.play()
                                reset_advance_score("Score")
                                answer_logo = pygame.image.load(os.getcwd() + "/Clase 3/Desafío Preguntados/images/check.png")
                            else:
                                turn_lost.play()
                                reset_advance_score("Score")
                    else:
                        fail.play()
                        fail_flag = "Fail_C"
                        answer_logo = pygame.image.load(os.getcwd() + "/Clase 3/Desafío Preguntados/images/error.png")
        #Quitar el Juego
        if (event.type == pygame.QUIT):
            running = False

    #Renderizaciones
    screen.blit(background, (0,0))
    if (end_flag == True):
        pygame.draw.rect(screen, (Black), end_game_rect, 0, 15)
        pygame.draw.rect(screen, (White), quit_end, 0, 15)
        screen.blit(end_game_text, (560, 130))
        screen.blit(end_game_text_two, (650, 180))
        screen.blit(reset_logo, (645, 288))
    else:
        pygame.draw.rect(screen, (Green), questions_rect, 0, 15)
        pygame.draw.rect(screen, (Red), restart_rect, 0, 15)
        pygame.draw.rect(screen, (Orange), score_rect, 0, 15)
        pygame.draw.rect(screen, (Yellow), answer_rect, 0, 15)
        pygame.draw.rect(screen, (Black), question_text_rect, 0, 15)
        if (fail_flag == "Fail_A"):
            pygame.draw.rect(screen, (Blue_fail), option_a_rect, 0, 15)
            pygame.draw.rect(screen, (Purple), option_b_rect, 0, 15)
            pygame.draw.rect(screen, (Pink), option_c_rect, 0, 15)
        elif (fail_flag == "Fail_B"):
            pygame.draw.rect(screen, (Blue), option_a_rect, 0, 15)
            pygame.draw.rect(screen, (Purple_fail), option_b_rect, 0, 15)
            pygame.draw.rect(screen, (Pink), option_c_rect, 0, 15)
        elif (fail_flag == "Fail_C"):
            pygame.draw.rect(screen, (Blue), option_a_rect, 0, 15)
            pygame.draw.rect(screen, (Purple), option_b_rect, 0, 15)
            pygame.draw.rect(screen, (Pink_fail), option_c_rect, 0, 15)
        elif (fail_flag == "Default"):
            pygame.draw.rect(screen, (Blue), option_a_rect, 0, 15)
            pygame.draw.rect(screen, (Purple), option_b_rect, 0, 15)
            pygame.draw.rect(screen, (Pink), option_c_rect, 0, 15)
        screen.blit(text_title_question, (65,80))
        screen.blit(text_title_restart, (1205,85))
        screen.blit(text_title_score, (102,230))
        screen.blit(text_score, (105,430))
        screen.blit(each_question, (350,718))
        screen.blit(text_option_a, (400,622))
        screen.blit(text_option_b, (650,622))
        screen.blit(text_option_c, (900,622))
        screen.blit(answer_logo, (1210, 325))
    pygame.display.flip()
