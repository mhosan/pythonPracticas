import matplotlib.pyplot as plt

def pie_chart():
    labels = ['A', 'B', 'C']
    values = [123,45,66]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.show()
    plt.savefig('pie.png')
    plt.close()

if __name__== '__main__':
    pie_chart()
