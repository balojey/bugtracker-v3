import reflex as rx
from ..models import User
from ..enumerations import Role
from typing import Optional


class State(rx.State):
    """The base state for the app"""

    user: Optional[User] = None

    @rx.var
    def is_admin(self):
        """Check if user is admin"""
        return self.user.role == Role.ADMIN

    @rx.var
    def is_project_manager(self):
        """Check if user is project manager"""
        return self.user.role == Role.PROJECT_MANAGER

    @rx.var
    def is_developer(self):
        """Check if user is developer"""
        return self.user.role == Role.DEVELOPER

    @rx.var
    def is_submitter(self):
        """Check if user is submitter"""
        return self.user.role == Role.SUBMITTER

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
