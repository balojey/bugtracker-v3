import reflex as rx
from .state import State
from ..schemas.response_status import ResponseStatus
import httpx


class UserLogin(rx.Base):
    """The login page."""

    email: str
    password: str


class LoginPageState(State):
    """The login page state."""

    form_data: dict = {}
    logged_in: bool = False

    def handle_submit(self, form_data: dict):
        """Handle the submit event."""
        self.form_data = form_data
        print("Login Form data: ", self.form_data)
        response = httpx.post(
            f"{self.url}/auth/jwt/login",
            headers={"Content-type": "application/x-www-form-urlencoded"},
            data=f"grant_type=&username={self.form_data['email']}&password={self.form_data['password']}&scope=&client_id=&client_secret=",
        )
        print("Login Response: ", response.json())
        if response.status_code == 200:
            self.message, self.status = (
                "You have successfully logged in",
                ResponseStatus.SUCCESS.value,
            )
            self.access_token = response.json()["access_token"]
            self.token_type = response.json()["token_type"]
            self.logged_in = True
            return rx.redirect("/dashboard")
        elif response.status_code == 400:
            self.message, self.status = (
                response.json()["detail"],
                ResponseStatus.ERROR.value,
            )
