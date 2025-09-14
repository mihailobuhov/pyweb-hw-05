from datetime import datetime, timedelta
from constants.errors import DateError

class DateService:
    @staticmethod
    def generate_dates(days: int) -> list:
        if days < 1 or days > 10:
            raise DateError("Number of days must be between 1 and 10")

        today = datetime.today()
        return [(today - timedelta(days=i)).strftime("%d.%m.%Y") for i in range(days)]
