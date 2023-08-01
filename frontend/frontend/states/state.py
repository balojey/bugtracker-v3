import reflex as rx
from ..schemas.user_me import Me
from dotenv import load_dotenv
from os import getenv
import httpx
from ..schemas.response_status import ResponseStatus


load_dotenv("../../.env")


class State(rx.State):
    """The app state."""

    url: str = getenv("REFLEX_API_ENDPOINT")
    access_token: str = ""
    token_type: str = ""
    message, status = "", ""
    me: dict = {}

    def get_user(self):
        """The user's data."""
        # if len(self.headers["Authorization"]) < 10:
        #     return rx.redirect("/login")
        response = httpx.get(
            f"{self.url}/users/me", follow_redirects=True, headers=self.headers
        )
        print(
            "==========================Me response============================: ",
            response.json(),
        )
        # if response.status_code == 401:
        #     return rx.redirect("/login")
        self.me = response.json()
        print(
            f"=====================================================\n\n\n{self.me}\n\n\n======================="
        )

    @rx.var
    def headers(self) -> dict:
        """The headers."""
        return {
            "Authorization": f"{self.token_type} {self.access_token}",
            "Content-Type": "application/json",
        }

    def logout(self):
        """Logout a user"""

        print(1)
        self.reset()
        return rx.redirect("/")

    def check_login(self):
        """Check if a user is logged in."""
        if self.access_token == "":
            return rx.redirect("/login")

    def check_response(self, response_json: dict, status_code: int):
        """Check response."""
        if status_code == 401:
            self.message, self.status = (
                "Please Log in to continue",
                ResponseStatus.ERROR.value,
            )
            return rx.redirect("/login")
        elif status_code == 200:
            return response_json
        elif status_code == 400:
            self.message, self.status = (
                response_json["detail"],
                ResponseStatus.ERROR.value,
            )
            return rx.redirect("/login")
        elif status_code == 201:
            self.message, self.status = (
                "Created successfully",
                ResponseStatus.SUCCESS.value,
            )
            return rx.redirect("/dashboard")
        else:
            self.message, self.status = (
                response_json["detail"],
                ResponseStatus.ERROR.value,
            )
