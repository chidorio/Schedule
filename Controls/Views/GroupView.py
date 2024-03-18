from flet import *
from DBClasses.Groups import Group
from DB import DB


def create_view(page):
    return Container(
        Column(
            controls=[
                TextField(label="Название",
                          bgcolor=colors.WHITE,
                          color=colors.GREEN_200,
                          focused_color=colors.GREEN_200,
                          focused_border_color=colors.GREEN_300,
                          border_color=colors.GREEN_200,
                          cursor_color=colors.GREEN_300,
                          label_style=TextStyle(size=15, color=colors.GREEN_200)
                          ),
                Dropdown(
                    options=[
                        dropdown.Option("П/П"),
                        dropdown.Option("У/П"),
                        dropdown.Option("Сессия"),
                        dropdown.Option("Обычный режим учебы"),
                    ],
                    color=colors.GREEN_300,
                    focused_color=colors.GREEN_300,
                    focused_border_color=colors.GREEN_300,
                    border_color=colors.GREEN_200,
                    filled=True,
                    bgcolor=colors.WHITE,
                    focused_bgcolor=colors.WHITE,
                    autofocus=True

                ),
                ElevatedButton(text='Сохранить',
                               color=colors.GREEN_50,
                               bgcolor=colors.GREEN_300,
                               on_click=lambda _: add_group_btn_click(page))
            ]
        ),
        width=200,
    )


def add_group_btn_click(page):
    name = page.views[0].controls[0].content.controls[0].value
    status = Group.idstatus_in_text(page.views[0].controls[0].content.controls[1].value)
    DB.add_edit_data(table="Groups", request=f'INSERT INTO public."Groups" ("Id", "Name", "Id_Status_group") '
                                             f'VALUES ((SELECT COALESCE(MAX("Id"), 0) + 1 FROM public."Groups"),'
                                             f'\'{name}\', {status});')
    page.update()
    page.go("/")