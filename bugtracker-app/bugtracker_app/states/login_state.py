from .auth import AuthState


class LoginState(AuthState):
    """Login state of the bugtracker app."""

    def login_as_demo_user(self, user: str):
        """Handle login as demo admin 1."""
        # Define demo_users
        demo_users = {
            "demoadmin1": {
                "email": "demoadmin1@bugtracker.com",
                "password": "demoadmin1",
            },
            "demoadmin2": {
                "email": "demoadmin2@bugtracker.com",
                "password": "demoadmin2",
            },
            "demoprojectmanager1": {
                "email": "demoprojectmanager1@bugtracker.com",
                "password": "demoprojectmanager1",
            },
            "demodeveloper1": {
                "email": "demodeveloper1@bugtracker.com",
                "password": "demodeveloper1",
            },
            "demosubmitter1": {
                "email": "demosubmitter1@bugtracker.com",
                "password": "demosubmitter1",
            },
        }
        self.email, self.password = (
            demo_users[user]["email"],
            demo_users[user]["password"],
        )
        return self.login()

    def handle_user_login(self, form_data: dict):
        """Handle user login."""
        self.email, self.password = form_data["email"], form_data["password"]
        return self.login()
