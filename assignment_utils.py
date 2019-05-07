import holidays


class AssignmentChecks():

    def __init__(self, days):
        self.days = days
        self.errors = ''

    def check_za_holidays(self):
        """Checks that each date in a list of datetime objects is not a South African public holiday.
        Returns a boolean value indicating whether or not any object's date falls on a South African public holiday.
        """
        za_holidays = holidays.ZA()
        for day in self.days:
            if day.date() in za_holidays:
                self.errors += " A date provided fell on a South African holiday."
                return True        
        return False

    def check_weekdays(self):
        """Checks that each day in a list of datetime objects is a week day.
        Returns a boolean value indicating whether or not any object's day is not a week day.
        """
        for day in self.days:
            if day.isoweekday() not in range(0, 6):
                self.errors += " A day value outside of a weekday was provided."
                return False        
        return True

    def check_work_hours(self):
        """Checks that each hour in a list of datetime objects falls within working hours (8AM-5PM).
        Returns a boolean value indicating whether or not any object's hour falls outside work hours.
        Datetime objects with hour values of zero are accommodated.
        """
        for day in self.days:
            if day.hour not in range(8, 18) and day.hour != 0:
                self.errors += " An hour value outside of work hours was provided."
                return False        
        return True

    def has_errors(self):
        if self.errors != '':
            return True
        return False
