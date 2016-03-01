def clean_days(days, strict=False):
    new_days = []
    for day in days:
        if day['interval'] is not None:
            new_days.append(day)

        if strict is True:
            if day in new_days:
                if day['hours'] is None:
                    new_days.pop(day)

    return new_days
