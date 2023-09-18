def answer_verification (flag, score, lap_counter, answer_counter, array, answer=str):
    if (flag == False):
        answer_counter["value"] = 1
    else:
        if ((answer_counter["value"] < 2) or (array[lap_counter-1] == answer)):
            if (array[lap_counter-1] == answer):
                answer_counter["value"] = 1
                score["value"] += 10
                return("Respuesta Correcta")
            else:
                answer_counter["value"] += 1
                return("Respuesta Incorrecta")
        else:
            answer_counter["value"] = 1
            return("No más opciones")