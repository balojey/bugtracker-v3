import reflex as rx
from ..models import User
from .base import State
from pydantic import EmailStr
from ..enumerations import Role
from typing import Optional


class AuthState(State):
    """The authentication state for sugnup and login"""

    name: str = ""
    email: EmailStr = ""
    password: str = ""
    confirm_password: str = ""
    role: Optional[Role]

    def signup(self):
        """Signup user"""
        if self.password != self.confirm_password:
            return rx.window_alert("Passwords do not match")
        with rx.session() as session:
            if session.query(User).filter_by(email=self.email).one():
                return rx.window_alert("User already exists")
            self.user = User(name=self.name, email=self.email, password=self.password)
            session.add(self.user)
            session.expire_on_commit = False
            session.commit()
            return rx.redirect("/dashboard")

    def login(self):
        """Login user"""
        with rx.session() as session:
            user = session.query(User).where(User.email == self.email).one_or_none()
            if user and user.password == self.password:
                self.user = user
                self.name = user.name
                self.role = user.role
                return rx.redirect("/dashboard")
            return rx.window_alert("Invalid credentials")
