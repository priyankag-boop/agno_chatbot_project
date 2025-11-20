# agent/agent.py

import os

class AgnoAgent:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.session_history = []

    def add_message(self, message: str):
        self.session_history.append(message)

    def get_response(self, query: str):
        self.add_message(f"User: {query}")
        response = f"Agent response to: {query}"
        self.add_message(response)
        return response
