import datetime as dt
from duvasheetcalc.utils import clean_days


class SheetCalculator(object):

    def calculate_diff(self, start, end):
        structure = '%H:%M:%S'
        start_dt = dt.datetime.strptime(start, structure)
        end_dt = dt.datetime.strptime(end, structure)
        diff = (end_dt - start_dt) 
        diff = (diff.seconds/60) / 60

        return diff


    def calculate(self, days):
        new_days = []
        total_hours = 0


        for i, day in enumerate(days):
            diff = 0
            pre_day = days[max(0, i-1)]
            next_day = days[min(len(days)-1, i+1)]
            
            if pre_day['date'] == day['date'] and i is not 0:
                continue

            start_time = day['interval'].split('-')[0].replace(' ', '') + ':00'
            end_time = day['interval'].split('-')[1].replace(' ', '') + ':00'
            diff = self.calculate_diff(start_time, end_time)

            if next_day['date'] == day['date'] and i is not len(days)-1:
                start_time = next_day['interval'].split('-')[0].replace(' ', '') + ':00'
                end_time = next_day['interval'].split('-')[1].replace(' ', '') + ':00'
                diff += self.calculate_diff(start_time, end_time)


            day['hours'] = (diff-4)
	    
            #if diff-4 > 0:
            total_hours += (diff-4)

            new_days.append(day)
            
        return {'days': clean_days(new_days, True), 'hours': total_hours}
