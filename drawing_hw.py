import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

''' Задание 1. Нарисуйте line plot по небольшому набору данных'''

iris_df = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/master/pandas/tests/io/data/csv/iris.csv")

plt.plot(iris_df["SepalLength"], 'b--')
plt.xlabel("Id")
plt.ylabel("Sepal Length (cm)")
plt.show()

''' Задание 2. Сделайте программу, принимающую путь к fasta, и выводящую распределение длин последовательностей в ней'''


def calculate_length(lst):
    len_list = []
    for i in lst:
        len_list.append(len(i))
    return len_list


def draw_length_distribution(path):
    with open(path, 'r') as fasta_file:
        temp_fasta = [line.rstrip("\n") for line in fasta_file]

    fasta_list = temp_fasta[1::2]

    fasta_lengths = calculate_length(fasta_list)

    plt.hist(fasta_lengths, bins=np.arange(np.min(fasta_lengths), np.max(fasta_lengths) + 2) - 0.5)
    plt.title("Sequence length distribution")
    plt.xlabel("Sequence Length (bp)")
    plt.ylabel("Frequency")
    plt.xticks(np.arange(np.min(fasta_lengths), np.max(fasta_lengths) + 2, step=15))
    plt.show()


path_to_fasta = "/home/misskittin/Downloads/sample.fa"
draw_length_distribution(path_to_fasta)

'''Задание 3. Нарисуйте свой любимый график '''
# у меня нет любимого графика, пусть будут скрипки :)

plt.figure()
sns.violinplot(x='Name', y="SepalWidth", data=iris_df, inner="quartile")
plt.title("Violin Plot of Sepal Width by Name")
plt.show()

print(iris_df)
