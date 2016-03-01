import datetime as dt


class SheetCalculator(object):

    def calculate(self, days):
        new_days = []
        
        for day in days:
            start_time = day['interval'].split('-')[0].replace(' ', '') + ':00'
            end_time = day['interval'].split('-')[1].replace(' ', '') + ':00'

            structure = '%H:%M:%S'
            start_dt = dt.datetime.strptime(start_time, structure)
            end_dt = dt.datetime.strptime(end_time, structure)
            diff = (end_dt - start_dt) 
            diff = (diff.seconds/60) / 60

            day['hours'] = diff

            new_days.append(day)

        return new_days
