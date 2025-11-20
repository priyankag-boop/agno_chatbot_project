# ui/app.py
from nicegui import ui
import requests
import threading

# Container for chat messages
chat_container = ui.column().style('gap: 5px; max-height: 400px; overflow-y: auto; border: 1px solid #ccc; padding: 5px;')

def fetch_stream():
    def _stream():
        try:
            response = requests.get("http://127.0.0.1:8000/stream", stream=True)
            for chunk in response.iter_content(chunk_size=5):
                text = chunk.decode()
                # Dynamically add label inside chat container
                with chat_container:
                    ui.label(text)
        except Exception as e:
            with chat_container:
                ui.label(f"Error: {e}")
    threading.Thread(target=_stream).start()  # run in background

# Header + button
with ui.row().style('align-items: center; gap: 10px; margin-bottom: 10px;'):
    ui.label("Agno Chatbot Streaming Demo").style('font-weight: bold;')
    ui.button("Get Stream", on_click=fetch_stream)

ui.run(title="Agno Chatbot UI", port=8080)
