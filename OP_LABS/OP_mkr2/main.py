
class WorkDay:
    def __init__(self, date, hours, project_name):
        self.date = date
        self.hours = hours
        self.project_name = project_name


class Worker:
    DAYS = [WorkDay('14.05', 5, 'game'), WorkDay('15.05', 4, 'game'), WorkDay('16.05', 3, 'app'), WorkDay('17.05', 6, 'app')]

    def __init__(self, pib, posada):
        self.pib = pib
        self.posada = posada

    def total_time_on_project(self, project_name):
        total = 0
        for day in Worker.DAYS:
            if day.project_name == project_name:
                total += day.hours

        return total

    def medium_time_on_period(self):
        summa = 0
        days_number = 0
        for day in Worker.DAYS:
            summa += day.hours
            days_number += 1
        med_time = summa / days_number
        return med_time

    def find_max_hours_day(self):
        maximum = None
        for day in Worker.DAYS:
            if maximum is None or day.hours > maximum:
                maximum = day.hours
        return maximum

print("Assignment completed by Kochev Hennadii, IP-91,\nip9113, variant (13+91)%27+1 = 24")

myWorker = Worker("Vasil", "Manager")
total_time_on_game = myWorker.total_time_on_project('game')
print("Total time on game:", total_time_on_game)
med_time = myWorker.medium_time_on_period()
print("Medium time:", med_time)
max_hours = myWorker.find_max_hours_day()
print("Max hours:", max_hours)

