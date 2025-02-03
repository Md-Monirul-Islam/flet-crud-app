import flet as ft
from utils.api import create_item

def create_page(page):
    name_input = ft.TextField(label="Name")
    desc_input = ft.TextField(label="Description")
    price_input = ft.TextField(label="Price", keyboard_type=ft.KeyboardType.NUMBER)
    feedback = ft.Text()

    def save_item(e):
        if not name_input.value or not price_input.value:
            feedback.value = "Name and price are required!"
            page.update()
            return

        try:
            data = {
                "name": name_input.value,
                "description": desc_input.value,
                "price": float(price_input.value),
            }
            response = create_item(data)
            if "id" in response:
                feedback.value = "Item created successfully!"
                name_input.value, desc_input.value, price_input.value = "", "", ""
                page.update()
                page.go("/")
            else:
                feedback.value = "Error creating item!"
        except Exception as ex:
            feedback.value = f"Error: {str(ex)}"
        
        page.update()

    save_button = ft.ElevatedButton("Save Item", on_click=save_item)
    back_button = ft.ElevatedButton("Back to List", on_click=lambda e: page.go("/"))

    page.controls.append(ft.Column(controls=[name_input, desc_input, price_input, save_button, feedback, back_button]))
    page.update()
