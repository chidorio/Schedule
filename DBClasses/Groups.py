from DB import DB
from flet import *


class Group:
    selected_name = ''
    selected_status = ''
    dict_status_group = {
        'П/П': 1,
        'У/П': 2,
        'Сессия': 3,
        'Обычный режим учебы': 4
    }

    def __init__(self):
        self.list = []
        for row in DB.view_data(table='Cabinets',
                                request=f'SELECT g."Id", g."Name", sg."Name" FROM public."Groups" AS g '
                                        f'JOIN public."Status_group" AS sg ON g."Id_Status_group" = sg."Id"'
                                        f'ORDER BY g."Name";'):
            self.list.append(list(row))

    def list_datarow(self):
        data = []
        for item in self.list:
            data.append(
                DataRow([DataCell(Text(item[1])), DataCell(Text(item[2]))]
                        )
            )
        return data

    @classmethod
    def create_column(cls):
        return [DataColumn(Text('Группа')),
                DataColumn(Text('Статус')),
                ]


    @classmethod
    def idstatus_in_text(cls, id):
        return cls.dict_status_group.get(id)

