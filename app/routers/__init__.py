# Import all routers for easy inclusion in main.py
from app.routers import (
    message,
    login,
    personal,
    group,
    label,
    favor,
    download,
    contact
)

# List of all routers to be included in the main application
routers = [
    message.router,
    login.router,
    personal.router,
    group.router,
    label.router,
    favor.router,
    download.router,
    contact.router
]