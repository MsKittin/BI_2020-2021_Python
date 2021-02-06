import numpy as np

'''
Task 5
Сделайте программу, получающую на вход текст, и выдающую этот же текст со следующими изменениями - буквы во всех 
словах кроме первой и последней перемешаны. Для простоты пока будем считать, что пунктуации нет. Пример: 
"По рзеузльаттам илссоевадний одонго анлигсйокго унвиертисета, не иеемт занчнеия, в каокм проякде рсапжоолены 
бкувы в солве. Галовне, чотбы преавя и пслонедяя бквуы блыи на мсете. осатьлыне бкувы мгоут селдовтаь в плоонм 
бсепордяке, все-рвано ткест чтаитсея без побрелм. Пичрионй эгото ялвятеся то, что мы не чиаетм кдаужю бкуву
по отдльенотси, а все солво цлиеком."
'''

given_string = 'Я уехал в провинцию начал рисовать подсолнухи и пить вино чтобы не сойти с ума от влюбленности в тебя' \
         ' но ничего не помогло'

words_list = given_string.split(" ")


def shuffle_chars(word) -> str:
    char_list = [char for char in word]

    shuffled_string = ""

    if (len(char_list) == 1) or (len(char_list) == 2) or (len(char_list) == 3):
        shuffled_string = "".join(char_list)
    else:
        for i in range(1, len(char_list) - 1):
            r = np.random.randint(1, len(char_list) - 2)
            char_list[i], char_list[r] = char_list[r], char_list[i]
            shuffled_string = "".join(char_list)

    return shuffled_string


result_string = []

for i in words_list:
    result_string.append(shuffle_chars(i))

print(*result_string)

'''
Example output:
Я ухаел в пниицровю нчаал росвтиаь пхонолудси и птиь внио чбтоы не сотйи с ума от вюбсотнлнлеи в тбея но ничгео не пмлгооо
'''