
import dateutil.parser as date_parser
import unittest

from assignment_utils import AssignmentChecks


class TestAssignment(unittest.TestCase):
    
    def test_day_is_holiday(self):
        """Assert that Family Day returns True."""
        days = [date_parser.parse('2019-04-22 00:00:00')]
        self.assertTrue(AssignmentChecks(days).check_za_holidays())

    def test_day_is_not_holiday(self):
        """Assert that non-holiday returns False."""
        days = [date_parser.parse('2019-05-07 00:00:00')]
        self.assertFalse(AssignmentChecks(days).check_za_holidays())

    def test_day_is_weekday(self):
        """Assert that weekday returns True."""
        days = [date_parser.parse('2019-05-08 00:00:00')]
        self.assertTrue(AssignmentChecks(days).check_weekdays())

    def test_day_is_not_weekday(self):
        """Assert that non-weekday returns False."""
        days = [date_parser.parse('2019-05-05 00:00:00')]
        self.assertFalse(AssignmentChecks(days).check_weekdays())

    def test_hour_before_8am(self):
        """Assert that hour before 8am returns False."""
        days = [date_parser.parse('2019-05-05 04:00:00')]
        self.assertFalse(AssignmentChecks(days).check_work_hours())

    def test_hour_after_5pm(self):
        """Assert that hour after 5pm returns False."""
        days = [date_parser.parse('2019-05-05 18:00:00')]
        self.assertFalse(AssignmentChecks(days).check_work_hours())

    def test_hour_is_zero(self):
        """Assert that hour value of zero returns True."""
        days = [date_parser.parse('2019-05-05 00:00:00')]
        self.assertTrue(AssignmentChecks(days).check_work_hours())

    def test_hour_is_work_hour(self):
        """Assert that valid hour value returns True."""
        days = [date_parser.parse('2019-05-05 14:45:00')]
        self.assertTrue(AssignmentChecks(days).check_work_hours())


if __name__=="__main__":
    unittest.main()
