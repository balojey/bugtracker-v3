from models.models import (
    User,
    Project,
    Ticket,
    Attachment,
    Comment,
    TicketHistory,
)
from enumerations import Role, TicketType, Priority, Status, Action
import reflex as rx
from sqlmodel import create_engine, SQLModel, Session


sqlite_file_name = "reflex.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# user = User(first_name="Ademola", last_name="Balogun", email="ade@mola.com", password="ademola")
# project = Project(name="Bug tracker", description="help teams keep track of bugs", creator_id=user.id )
# project_member = ProjectMember(project_id=project.id, user_id=user.id, role=Role.DEVELOPER)
# ticket = Ticket(title="Bug tracker", description="help teams keep track of bugs", submitter_id=project_member.id, project_id=project.id, assigned_developer_id=project_member.id, status=Status.OPEN, priority=Priority.HIGH, ticket_type=TicketType.BUG_ERROR)
# attachment = Attachment(ticket_id=ticket.id, description="This is a file description", file_name="bug_tracker.py", file_path="/home/bug_tracker.py")
# comment = Comment(ticket_id=ticket.id, commenter_id=user.id, content="This is a comment")
# ticket_history = TicketHistory(ticket_id=ticket.id, user_id=user.id, action=Action.TITLE_CHANGE, previous_value="Bug tracker", present_value="Bug tracker app")

# creator_id will be absent
# project = Project(name="Bug tracker", description="help teams keep track of bugs", creator=user)


def populate():
    # Create users
    print("Creating users...")
    names = [
        "DemoAdmin1",
        "DemoAdmin2",
        "DemoProjectManager1",
        "DemoProjectManager2",
        "DemoProjectManager3",
        "DemoProjectManager4",
        "DemoDeveloper1",
        "DemoDeveloper2",
        "DemoDeveloper3",
        "DemoDeveloper4",
        "DemoDeveloper5",
        "DemoDeveloper6",
        "DemoDeveloper7",
        "DemoDeveloper8",
        "DemoSubmitter1",
        "DemoSubmitter2",
        "DemoSubmitter3",
        "DemoSubmitter4",
        "DemoSubmitter5",
        "DemoSubmitter6",
        "DemoSubmitter7",
        "DemoSubmitter8",
        "DemoSubmitter9",
        "DemoSubmitter10",
    ]
    emails = [
        "demoadmin1@bugtracker.com",
        "demoadmin2@bugtracker.com",
        "demoprojectmanager1@bugtracker.com",
        "demoprojectmanager2@bugtracker.com",
        "demoprojectmanager3@bugtracker.com",
        "demoprojectmanager4@bugtracker.com",
        "demodeveloper1@bugtracker.com",
        "demodeveloper2@bugtracker.com",
        "demodeveloper3@bugtracker.com",
        "demodeveloper4@bugtracker.com",
        "demodeveloper5@bugtracker.com",
        "demodeveloper6@bugtracker.com",
        "demodeveloper7@bugtracker.com",
        "demodeveloper8@bugtracker.com",
        "demosubmitter1@bugtracker.com",
        "demosubmitter2@bugtracker.com",
        "demosubmitter3@bugtracker.com",
        "demosubmitter4@bugtracker.com",
        "demosubmitter5@bugtracker.com",
        "demosubmitter6@bugtracker.com",
        "demosubmitter7@bugtracker.com",
        "demosubmitter8@bugtracker.com",
        "demosubmitter9@bugtracker.com",
        "demosubmitter10@bugtracker.com",
    ]
    passwords = [
        "demoadmin1",
        "demoadmin2",
        "demoprojectmanager1",
        "demoprojectmanager2",
        "demoprojectmanager3",
        "demoprojectmanager4",
        "demodeveloper1",
        "demodeveloper2",
        "demodeveloper3",
        "demodeveloper4",
        "demodeveloper5",
        "demodeveloper6",
        "demodeveloper7",
        "demodeveloper8",
        "demosubmitter1",
        "demosubmitter2",
        "demosubmitter3",
        "demosubmitter4",
        "demosubmitter5",
        "demosubmitter6",
        "demosubmitter7",
        "demosubmitter8",
        "demosubmitter9",
        "demosubmitter10",
    ]
    role = [
        Role.ADMIN,
        Role.ADMIN,
        Role.PROJECT_MANAGER,
        Role.PROJECT_MANAGER,
        Role.PROJECT_MANAGER,
        Role.PROJECT_MANAGER,
        Role.DEVELOPER,
        Role.DEVELOPER,
        Role.DEVELOPER,
        Role.DEVELOPER,
        Role.DEVELOPER,
        Role.DEVELOPER,
        Role.DEVELOPER,
        Role.DEVELOPER,
        Role.SUBMITTER,
        Role.SUBMITTER,
        Role.SUBMITTER,
        Role.SUBMITTER,
        Role.SUBMITTER,
        Role.SUBMITTER,
        Role.SUBMITTER,
        Role.SUBMITTER,
        Role.SUBMITTER,
        Role.SUBMITTER,
    ]
    projects = {
        "project1": {
            "name": "Bug tracker",
            "description": "help teams keep track of bugs",
        },
        "project2": {
            "name": "Trek with me",
            "description": "help people find hiking partners",
        },
        "project3": {
            "name": "Course chat room",
            "description": "help students in a course chat with each other",
        },
        "project4": {
            "name": "School management system",
            "description": "help schools manage their students",
        },
    }

    tickets = {
        "ticket2": {
            "title": "Ticket title 2",
            "description": "Ticket description 2",
            "ticket_type": TicketType.CHANGE_REQUEST,
            "priority": Priority.LOW,
            "status": Status.CLOSED,
        },
        "ticket3": {
            "title": "Ticket title 3",
            "description": "Ticket description 3",
            "ticket_type": TicketType.DOCUMENTATION,
            "priority": Priority.NONE,
            "status": Status.DUPLICATE,
        },
        "ticket4": {
            "title": "Ticket title 4",
            "description": "Ticket description 4",
            "ticket_type": TicketType.BUG_ERROR,
            "priority": Priority.HIGH,
            "status": Status.OPEN,
        },
        "ticket5": {
            "title": "Ticket title 5",
            "description": "Ticket description 5",
            "ticket_type": TicketType.BUG_ERROR,
            "priority": Priority.HIGH,
            "status": Status.OPEN,
        },
        "ticket6": {
            "title": "Ticket title 6",
            "description": "Ticket description 6",
            "ticket_type": TicketType.BUG_ERROR,
            "priority": Priority.HIGH,
            "status": Status.OPEN,
        },
        "ticket7": {
            "title": "Ticket title 7",
            "description": "Ticket description 7",
            "ticket_type": TicketType.BUG_ERROR,
            "priority": Priority.HIGH,
            "status": Status.OPEN,
        },
        "ticket8": {
            "title": "Ticket title 8",
            "description": "Ticket description 8",
            "ticket_type": TicketType.BUG_ERROR,
            "priority": Priority.HIGH,
            "status": Status.OPEN,
        },
        "ticket9": {
            "title": "Ticket title 9",
            "description": "Ticket description 9",
            "ticket_type": TicketType.BUG_ERROR,
            "priority": Priority.HIGH,
            "status": Status.OPEN,
        },
        "ticket10": {
            "title": "Ticket title 10",
            "description": "Ticket description 10",
            "ticket_type": TicketType.BUG_ERROR,
            "priority": Priority.HIGH,
            "status": Status.OPEN,
        },
        "ticket1": {
            "title": "Ticket title 1",
            "description": "Ticket description 1",
            "ticket_type": TicketType.BUG_ERROR,
            "priority": Priority.HIGH,
            "status": Status.OPEN,
        },
    }

    with Session(engine) as session:
        create_db_and_tables()

        # user = session.query(User).where(User.name == "DemoAdmin2").one()
        # user.role = Role.ASSIGNED_ADMIN
        # session.add(user)
        # session.commit()
        # session.refresh(user)

        # Create ticket histories
        # print("Creating ticket histories...")
        # tickets = session.query(Ticket).all()
        # developers = session.query(User).where(User.role == Role.DEVELOPER).all()
        # admin = session.query(User).where(User.role == Role.ADMIN).first()
        # i = 0
        # for ticket in tickets:
        #     previous_value = ticket.assigned_developer_id if ticket.assigned_developer_id else ""
        #     ticket.assigned_developer_id = developers[i % len(developers)].id
        #     present_value = developers[i % len(developers)].id
        #     ticket_history = TicketHistory(
        #         action=Action.ASSIGNED_DEVELOPER_CHANGE,
        #         previous_value=previous_value,
        #         present_value=present_value,
        #         ticket_id=ticket.id,
        #         made_by=admin.id,
        #     )
        #     session.add(ticket_history)
        #     session.add(ticket)
        #     session.commit()
        #     session.refresh(ticket)

        # Create comments
        # print("Creating comments...")
        # tickets = session.query(Ticket).all()
        # users = session.query(User).all()
        # i = 0
        # for user in users:
        #     comment = Comment(
        #         content="This is a comment",
        #         commenter_id=user.id,
        #         ticket_id=tickets[i % len(tickets)].id,
        #     )
        #     session.add(comment)
        #     session.commit()
        #     i += 1

        # Create attachments
        # print("Creating attachments...")
        # tickets = session.query(Ticket).all()
        # for ticket in tickets:
        #     attachment = Attachment(
        #         ticket_id=ticket.id,
        #         description="This is a file description",
        #         file_name="bug_tracker.py",
        #         file_path="/home/bug_tracker.py",
        #     )
        #     session.add(attachment)
        #     session.commit()

        # Create tickets
        # print("Creating tickets...")
        # submitters = session.query(User).where(User.role == Role.SUBMITTER).all()
        # projects = session.query(Project).all()
        # i = 0
        # for ticket in tickets.values():
        #     i += 1
        #     ticket = Ticket(
        #         **ticket,
        #         submitter_id=submitters[i % len(submitters)].id,
        #         project_id=projects[i % len(projects)].id,
        #     )
        #     session.add(ticket)
        #     session.commit()

        # Add members to projects
        # projects = session.query(Project).all()
        # users = session.query(User).where(User.role != Role.ADMIN).all()
        # for project in projects:
        #     print("Project memers:", project.members)
        #     for user in users:
        #         project.members.append(user)
        #     session.add(project)
        #     session.commit()
        #     session.refresh(project)

        # demoadmin1 = session.query(User).where(User.name == "DemoAdmin1").one()

        # # Create projects
        # print("Creating projects...")
        # for project in projects.values():
        #     project = Project(**project, creator_id=demoadmin1.id)
        #     session.add(project)
        #     session.commit()

        # for name, email, password, role in zip(names, emails, passwords, role):
        #     user = User(
        #         name=name,
        #         email=email,
        #         password=password,
        #         role=role,
        #     )
        #     session.add(user)
        #     session.commit()


if __name__ == "__main__":
    populate()
