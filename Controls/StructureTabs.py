from flet import *


def create_structure_tabs(flag, index_column, page, route_tb):
    table = create_table(flag=flag)

    def filter_dt_rows(e):
        for data_rows in table.rows:
            data_cell = data_rows.cells[index_column]
            text = data_cell.content
            data_rows.visible = (
                True
                if e.control.value.lower() in str(text.value).lower()
                else False
            )
            data_rows.update()

    return Column(
        expand=True,
        scroll=ScrollMode.ADAPTIVE,
        controls=[
            Row(controls=[Container(content=Text(value='Поиск по названию', size=20, color=colors.GREEN_300)),
                          Container(width=380,
                                    bgcolor=colors.GREEN_300,
                                    border_radius=6,
                                    padding=8,
                                    margin=Margin(0, 10, 0, 0),
                                    content=Row(
                                        spacing=10,
                                        vertical_alignment=CrossAxisAlignment.CENTER,
                                        controls=[
                                            Icon(name=icons.SEARCH_ROUNDED, color=colors.WHITE, size=17, opacity=0.85),
                                            TextField(
                                                border_color=colors.TRANSPARENT,
                                                height=20,
                                                text_size=14,
                                                content_padding=0,
                                                cursor_width=1,
                                                color=colors.WHITE,
                                                hint_text="Search",
                                                cursor_color=colors.WHITE,
                                                on_change=filter_dt_rows
                                            )
                                        ]
                                    )),
                          Container(ElevatedButton(text="Добавить",
                                                   on_click=lambda _: page.go(route=route_tb),
                                                   bgcolor=colors.GREEN_300,
                                                   color=colors.GREEN_50),
                                    margin=Margin(0, 10, 0, 0))],
                height=50),
            ResponsiveRow(controls=[ListView(adaptive=True, controls=[table])]),
        ]
    )


def create_table(flag):
    return DataTable(columns=flag[0],
                     vertical_lines=border.BorderSide(2, colors.GREEN_300),
                     horizontal_lines=border.BorderSide(2, colors.GREEN_300),
                     divider_thickness=0,
                     heading_row_height=65,
                     heading_text_style=TextStyle(size=20, color=colors.BLACK, weight=FontWeight.BOLD),
                     data_text_style=TextStyle(size=14, color=colors.BLACK),
                     border=border.only(bottom=BorderSide(2, colors.GREEN_300),
                                        top=BorderSide(2, colors.GREEN_300)),
                     rows=flag[1],
                     )
