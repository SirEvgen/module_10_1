from threading import Thread
from time import sleep
from datetime import datetime




def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(word_count + 1):
            file.writelines(f'Какое-то слово № {str(i)}\n')
            sleep(0.1)
        file.close()
    return print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = datetime.now()
print(f"работа потоков {time_end - time_start})")

time_start2 = datetime.now()
the_first = Thread(target=write_words(10, 'example5.txt'))
the_second = Thread(target=write_words(30, 'example6.txt'))
the_third = Thread(target=write_words(200, 'example7.txt'))
the_fourth = Thread(target=write_words(100, 'example8.txt'))


the_first.start()
the_second.start()
the_third.start()
the_fourth.start()

the_first.join()
the_second.join()
the_third.join()
the_fourth.join()
time_end2 = datetime.now()
print(f"работа потоков 'к сведению - это так не работает, ну ок, вот вам псевдопоток, МУЛЬТИПОТОК ага' {time_end2 - time_start2})")
