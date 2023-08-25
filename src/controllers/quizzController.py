from models.answer import Answer
from models.quizz import Quizz

def obterQuizz(quantidade = 10, assunto = ''):
    lista_quizz = []

    for _ in range(quantidade):
        answer1 = Answer('Elisabeth', True)
        answer2 = Answer('Martha', False)
        answer3 = Answer('Mary Jane', False)
    
        quizz = Quizz(assunto, [answer1, answer2, answer3])
        lista_quizz.append(quizz)
    
    return lista_quizz