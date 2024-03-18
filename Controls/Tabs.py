from flet import *
from Controls.StructureTabs import *
from DBClasses.Cabinets import Cabinet
from DBClasses.Groups import Group


def create_tabs(page):
    cab = Cabinet()
    cab_structure = create_structure_tabs(flag=[Cabinet.create_column(), cab.list_datarow()],
                                          index_column=0,
                                          page=page,
                                          route_tb="/add_edit_cab")
    group = Group()
    group_structure = create_structure_tabs(flag=[Group.create_column(), group.list_datarow()],
                                            index_column=0,
                                            page=page,
                                            route_tb="/add_edit_group")

    return Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            Tab(
                text="Группы",
                content=group_structure
            ),
            Tab(
                text="Кабинеты",
                content=cab_structure
            ),
            Tab(
                text="Замены",
            ),
            Tab(
                text="Расписание",
                # icon=icons.SETTINGS,
                content=Text("This is Tab 3"),
            ),
            Tab(
                text="Преподаватели",
                # icon=icons.SETTINGS,
                content=Text("This is Tab 3"),
            ),
            Tab(
                text="Экзамены",
                # icon=icons.SETTINGS,
                content=Text("This is Tab 3"),
            ),
        ],
        unselected_label_color=colors.GREEN_300,
        overlay_color=colors.GREEN_50,
        label_color=colors.GREEN_300,
        indicator_color=colors.GREEN_300,
        divider_color=colors.GREEN_300,
        expand=1,
    )
