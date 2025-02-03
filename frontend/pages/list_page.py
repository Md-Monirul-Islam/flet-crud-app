import flet as ft
from utils.api import get_items, delete_item

def list_page(page):
    list_view = ft.ListView()
    selected_item_id = None  # Store item ID for deletion

    def load_items():
        """Fetch and display items from the backend."""
        items = get_items()
        list_view.controls.clear()

        for item in items:
            item_id = item["id"]
            text = ft.Text(f"{item['name']} - ${item['price']}")

            # Edit Button (Capturing correct item_id)
            edit_button = ft.ElevatedButton("Edit", on_click=lambda e, i=item_id: go_to_edit(i))

            # Delete Button (Now captures item_id correctly)
            delete_button = ft.ElevatedButton("Delete", on_click=lambda e, i=item_id: show_confirm_dialog(i))

            row = ft.Row(controls=[text, edit_button, delete_button])
            list_view.controls.append(row)

        page.update()

    def go_to_create(e):
        """Navigate to the Create Page."""
        page.go("/create")

    def go_to_edit(item_id):
        """Navigate to the Edit Page with the selected item ID."""
        page.session.set("edit_item_id", item_id)
        page.go("/edit")

    # Confirmation Dialog
    confirm_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Confirm Delete"),
        content=ft.Text("Are you sure you want to delete this item?"),
        actions=[
            ft.TextButton("Cancel", on_click=lambda e: close_confirm_dialog()),
            ft.TextButton("Delete", on_click=lambda e: confirm_delete()),  
        ],
    )

    def show_confirm_dialog(item_id):
        """Show delete confirmation dialog and store selected item ID."""
        nonlocal selected_item_id
        selected_item_id = item_id  # Store item ID for deletion
        confirm_dialog.open = True
        page.update()

    def close_confirm_dialog():
        """Close the delete confirmation dialog."""
        confirm_dialog.open = False
        page.update()

    def confirm_delete():
        """Delete the selected item and refresh the list after successful deletion."""
        nonlocal selected_item_id
        if selected_item_id:
            success = delete_item(selected_item_id)  # Call API to delete item
            if success:  # Ensure deletion was successful
                selected_item_id = None  # Reset selected item
                load_items()  # Reload items after deletion
            else:
                print("Error: Failed to delete item from backend.")
        close_confirm_dialog()

    # Attach the dialog to the page
    page.dialog = confirm_dialog  

    # Add buttons and list view
    create_button = ft.ElevatedButton("Create New Item", on_click=go_to_create)
    page.controls.append(ft.Column(controls=[create_button, list_view]))
    
    load_items()  # Automatically load items on page load
    page.update()
