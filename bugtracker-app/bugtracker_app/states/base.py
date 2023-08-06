import reflex as rx
from ..models import User
from typing import Optional


class State(rx.State):
    """The base state for the app"""

    user: Optional[User] = None

    def logout(self):
        """Logout user"""
        self.reset()
        return rx.redirect("/")

    def check_login(self):
        """Check if user is logged in"""
        if not self.logged_in:
            return rx.redirect("/login")

    @rx.var
    def logged_in(self):
        """Check if user is logged in"""
        return self.user is not None
