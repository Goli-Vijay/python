import pandas as pd
import matplotlib.pyplot as plt

# data = {'MARKS_A': [94, 71, 75, 95, 77, 88, 95, 87, 64, 93], 'MARKS_B': [65, 81, 99, 86, 91, 93, 63, 88, 73, 84],
#      'MARKS_C': [73, 69, 86, 77, 69, 92, 68, 69, 99, 68]}
# df=pd.DataFrame(data)
# df.to_csv('marks.csv')
# file = pd.read_csv('marks.csv')
# file = file.drop(columns=['Unnamed: 0'])
# #print(file)
# #print(pd.read_csv('marks.csv').drop(columns=['Unnamed: 0']))
# #print(file.describe())
# print(df.iloc[6][2])
file = pd.read_csv('mnist_test.csv')
val = file.values
# print(val.shape)
x = val[:, 1:]
y = val[:, 0]
print(y)


def Img(x, y, i):
    plt.imshow(x[i].reshape(28, 28))
    plt.show()
    plt.title("label" + str(y[i + 1]))


for i in range(5):
    print(Img(x, y, i))
