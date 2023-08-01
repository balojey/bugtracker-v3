import reflex as rx
from .state import State
from ..schemas.roles import Role
from ..schemas.response_status import ResponseStatus
import httpx




class UserSignUp(rx.Base):
    """The sign up page."""

    first_name: str
    last_name: str
    email: str
    password: str
    role: Role


class SignUpPageState(State):
    """The sign up page state."""

    form_data: dict = {}
    role: Role = Role.DEVELOPER
    success: bool = False

    def handle_submit(self, form_data: dict):
        """Handle the submit event."""
        self.form_data = form_data
        self.form_data["role"] = self.role
        response = httpx.post(f"{self.url}/auth/register", json=self.form_data)
        print("Form data: ", self.form_data)
        print("Response: ", response.json())
        if response.status_code == 201:
            self.message, self.status = (
                "User created successfully",
                ResponseStatus.SUCCESS.value,
            )
            self.success = True
        elif response.status_code == 400:
            self.message, self.status = (
                response.json()["detail"]["reason"]
                if type(response.json()["detail"]) == dict
                else response.json()["detail"],
                ResponseStatus.ERROR.value,
            )
            self.success = False
