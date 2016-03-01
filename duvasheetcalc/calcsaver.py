class CalcSaver(object):

    def save(self, days, output):
        
        with open(output, 'a') as savefile:
            for day in days:
                savefile.write(
                        'DATE: {}, HOURS: {}, REF {}\n'.format(
                            day['date'],
                            day['hours'],
                            day['ref']
                            ))

        return True
