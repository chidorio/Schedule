from flet import *
from Controls.Tabs import *
from Controls.Views import GroupView

def build_main_page(page: Page):
    page.title = "ЯПЭК"

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                View(
                    route="/",
                    controls=[create_tabs(page=page)],
                    bgcolor=colors.WHITE
                )
            )
        elif page.route == "/add_edit_group":
            page.views.append(
                View(
                    route="/add_edit_group",
                    controls=[GroupView.create_view(page=page)],
                    bgcolor=colors.WHITE,
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER
                )

            )
        page.update()

    page.on_route_change = route_change
    page.go(page.route)


if __name__ == '__main__':
    app(target=build_main_page)
