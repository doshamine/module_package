from application.db.people import get_employees
from application.salary import calculate_salary
import datetime
import matplotlib.pyplot as plt

def date1():
    print(datetime.datetime.strftime(datetime.datetime.now(), "%a, %d %b %Y"))

def date2():
    print(datetime.datetime.strftime(datetime.datetime.now(), "%A, %d %B %Y"))

if __name__ == "__main__":
    calculate_salary()
    get_employees()
    date1()
    date2()
    x = [i for i in range(100)]
    y = [i**2 for i in range(100)]
    fig = plt.plot(x, y, color='blue', linestyle='-', marker='o')
    plt.savefig('figure.pdf', dpi=300, format='pdf')