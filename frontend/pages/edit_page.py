import flet as ft
from utils.api import update_item, get_items

def edit_page(page):
    item_id = page.session.get("edit_item_id")  # Retrieve the item ID to edit
    if not item_id:
        page.go("/")  # Redirect to list if no item ID is found
        return

    # Get existing item details
    item_data = next((item for item in get_items() if item["id"] == item_id), None)
    if not item_data:
        page.go("/")
        return

    name_input = ft.TextField(label="Name", value=item_data["name"])
    desc_input = ft.TextField(label="Description", value=item_data["description"])
    price_input = ft.TextField(label="Price", value=str(item_data["price"]), keyboard_type=ft.KeyboardType.NUMBER)
    feedback = ft.Text()

    def save_changes(e):
        data = {
            "name": name_input.value,
            "description": desc_input.value,
            "price": float(price_input.value),
        }
        response = update_item(item_id, data)
        if "id" in response:
            feedback.value = "Item updated successfully!"
            page.update()
            page.go("/")  # Redirect to list after saving changes
        else:
            feedback.value = "Error updating item!"
            page.update()

    save_button = ft.ElevatedButton("Save Changes", on_click=save_changes)
    back_button = ft.ElevatedButton("Back to List", on_click=lambda e: page.go("/"))

    page.controls.append(ft.Column(controls=[name_input, desc_input, price_input, save_button, feedback, back_button]))
    page.update()
