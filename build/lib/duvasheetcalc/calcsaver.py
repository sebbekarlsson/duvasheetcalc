class CalcSaver(object):

    def save(self, calculations, output):
        
        with open(output, 'w') as savefile:
            for day in calculations['days']:
                savefile.write(
                        'DATE: {}, HOURS: {}, REF {}\n'.format(
                            day['date'],
                            day['hours'],
                            day['ref']
                            ))

            savefile.write('TOTAL HOURS: {}'.format(calculations['hours']))

        return True
