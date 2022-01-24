import os
import zipfile

import pandas as pd

class SML2010Data:
    PATH = os.sep.join(['.', 'data', 'SML2010'])
    FILE = 'NEW-DATA.zip'
    ARCH = os.sep.join([PATH, FILE])
    COLNAMES = ['Date', 'Time', 
                'Temperature_dining_room', 'Temperature_room', 'Weather_temperature', 
                'CO2_dining_room', 'CO2_room', 
                'Humidity_dining_room', 'Humidity_room', 
                'Lighting_dining_room', 'Lighting_room',
                'Rain', 'Sun_dusk', 'Wind', 
                'Sun_light_west', 'Sun_light_east', 'Sun_light_south',
                'Sun_irradiance',
                'Enthalpic_motor_1', 'Enthalpic_motor_2', 'Enthalpic_motor_turbo',
                'Outdoor_temperature', 'Outdoor_relative_humidity', 'Day_of_week'
                ]


    @staticmethod
    def new_data_1():
        with zipfile.ZipFile(SML2010Data.ARCH, mode='r') as myzip:
            with myzip.open('NEW-DATA-1.T15.txt') as fp:
                data = pd.read_table(fp, header=None, skiprows=1, sep=' ', 
                                     names=SML2010Data.COLNAMES)

        return data


    @staticmethod
    def new_data_2():
        with zipfile.ZipFile(SML2010Data.ARCH, mode='r') as myzip:
            with myzip.open('NEW-DATA-2.T15.txt') as fp:
                data = pd.read_table(fp, header=None, skiprows=1, sep=' ', 
                                     names=SML2010Data.COLNAMES)

        return data


    @staticmethod
    def get_data():
        df1 = SML2010Data.new_data_1()
        df2 = SML2010Data.new_data_2()

        data = pd.concat([df1, df2])

        return data
