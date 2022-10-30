"""Climate Class."""

import re

import np


# pylint: disable=W1401, C0103, E1101
class Climate:
    """The collection of temperature records loaded from given csv file."""

    def __init__(self, filename):
        """Initialize a Climate instance.

        Stores the temperature records loaded from a given csv file specified by filename.

        Args:
            filename (str): name of the csv file
        """
        self.rawdata = {}

        f = open(filename, 'r')
        header = f.readline().strip().split(',')
        for line in f:
            items = line.strip().split(',')

            date = re.match('(\d\d\d\d)(\d\d)(\d\d)', items[header.index('DATE')])  # noqa: W605
            year = int(date.group(1))
            month = int(date.group(2))
            day = int(date.group(3))

            city = items[header.index('CITY')]
            temperature = float(items[header.index('TEMP')])
            if city not in self.rawdata:
                self.rawdata[city] = {}
            if year not in self.rawdata[city]:
                self.rawdata[city][year] = {}
            if month not in self.rawdata[city][year]:
                self.rawdata[city][year][month] = {}
            self.rawdata[city][year][month][day] = temperature

        f.close()

    def get_yearly_temp(self, city, year):
        """Get the daily temperatures for the given year and city.

        Args:
            city (str): city name
            year (int): the year to get the data for

        Returns:
            numpy 1-d array: daily temperatures for the specified year and city
        """
        temperatures = []
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        for month in range(1, 13):
            for day in range(1, 32):
                if day in self.rawdata[city][year][month]:
                    temperatures.append(self.rawdata[city][year][month][day])
        return np.array(temperatures)

    def get_daily_temp(self, city, month, day, year):
        """Get the daily temperature for the given city and time (year + date).

        Args:
            city (str): city name
            month (int): the month to get the data for (int, where January = 1, December = 12)
            day (int): the day to get the data for (int, where 1st day of month = 1)
            year (int): the year to get the data for

        Returns:
            float: the daily temperature for the specified time (year + date) and city
        """
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        assert month in self.rawdata[city][year], "provided month is not available"
        assert day in self.rawdata[city][year][month], "provided day is not available"
        return self.rawdata[city][year][month][day]
