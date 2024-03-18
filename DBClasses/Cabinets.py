from DB import DB
from flet import *


class Cabinet:
    def __init__(self):
        self.list = []
        for row in DB.view_data(table='Cabinets',
                                request=f'SELECT *'
                                        f' FROM public."Cabinets" AS cab;'):
            self.list.append(list(row))

    def list_datarow(self):
        data = []
        for item in self.list:
            data.append(
                DataRow([DataCell(Text(item[1])), DataCell(Text(item[2])), DataCell(Text(item[3]))]
                        )
            )
        return data

    @classmethod
    def create_column(cls):
        return [DataColumn(Text('Номер')),
                DataColumn(Text('Название')),
                DataColumn(Text('Тип'))]
