import flet as ft
from pages.list_page import list_page
from pages.create_page import create_page
from pages.edit_page import edit_page

def main(page: ft.Page):
    page.title = "CRUD App"
    page.dialog = None  # Ensure dialog is attached to the page
    
    # Function to handle route changes
    def route_change(e):
        page.controls.clear()
        if page.route == "/create":
            create_page(page)
        elif page.route == "/edit":
            edit_page(page)
        else:
            list_page(page)  # Ensure list_page has delete confirmation dialog attached
        page.update()

    page.on_route_change = route_change
    page.go("/")  # Load List Page by default

ft.app(target=main)
