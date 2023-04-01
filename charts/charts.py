import matplotlib.pyplot as pylot


def generate_pie_chart():
    labels = ['A', 'B', 'C', 'D']
    value = [10, 20, 30, 40]
    
    fig, ax = pylot.subplots()
    ax.pie(value, labels=labels, autopct='%1.1f%%')
    pylot.savefig('.pie.png')
    pylot.close()
    