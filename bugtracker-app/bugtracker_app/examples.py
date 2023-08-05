from models.models import (
    User,
    Project,
    Ticket,
    ProjectMember,
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
    user1 = User(
        first_name="testuser1",
        last_name="testuser1",
        email="testuser1@gmail.com",
        password="testuser1",
    )
    user2 = User(
        first_name="testuser2",
        last_name="testuser2",
        email="testuser2@gmail.com",
        password="testuser2",
    )
    user3 = User(
        first_name="testuser3",
        last_name="testuser3",
        email="testuser3@gmail.com",
        password="testuser3",
    )
    user4 = User(
        first_name="testuser4",
        last_name="testuser4",
        email="testuser4@gmail.com",
        password="testuser4",
    )
    print(user1, user2, user3, user4, sep="\n\n")
    print("Users created successfully!")

    # Create projects
    print("Creating projects...")
    project1 = Project(
        name="project1",
        description="project1 description",
        creator_id=user1.id,
    )
    project2 = Project(
        name="project2",
        description="project2 description",
        creator_id=user2.id,
    )
    project3 = Project(
        name="project3",
        description="project3 description",
        creator_id=user3.id,
    )
    project4 = Project(
        name="project4",
        description="project4 description",
        creator_id=user4.id,
    )
    print(project1, project2, project3, project4, sep="\n\n")
    print("Projects created successfully!")

    # Create project members
    print("Creating project members...")
    project_member1 = ProjectMember(
        project_id=project1.id,
        assignee_id=user1.id,
        role=Role.ADMIN,
    )
    project_member2 = ProjectMember(
        project_id=project1.id,
        assignee_id=user2.id,
        role=Role.DEVELOPER,
        assigner_id=project_member1.id,
    )
    project_member3 = ProjectMember(
        project_id=project1.id,
        assignee_id=user3.id,
        role=Role.PROJECT_MANAGER,
        assigner_id=project_member1.id,
    )
    project_member4 = ProjectMember(
        project_id=project1.id,
        assignee_id=user4.id,
        role=Role.SUBMITTER,
        assigner_id=project_member1.id,
    )

    project_member5 = ProjectMember(
        project_id=project2.id,
        assignee_id=user2.id,
        role=Role.ADMIN,
    )
    project_member6 = ProjectMember(
        project_id=project2.id,
        assignee_id=user1.id,
        role=Role.DEVELOPER,
        assigner_id=project_member5.id,
    )
    project_member7 = ProjectMember(
        project_id=project2.id,
        assignee_id=user3.id,
        role=Role.PROJECT_MANAGER,
        assigner_id=project_member5.id,
    )
    project_member8 = ProjectMember(
        project_id=project2.id,
        assignee_id=user4.id,
        role=Role.SUBMITTER,
        assigner_id=project_member5.id,
    )

    project_member9 = ProjectMember(
        project_id=project3.id,
        assignee_id=user3.id,
        role=Role.ADMIN,
    )
    project_member10 = ProjectMember(
        project_id=project3.id,
        assignee_id=user1.id,
        role=Role.DEVELOPER,
        assigner_id=project_member9.id,
    )
    project_member11 = ProjectMember(
        project_id=project3.id,
        assignee_id=user2.id,
        role=Role.PROJECT_MANAGER,
        assigner_id=project_member9.id,
    )
    project_member12 = ProjectMember(
        project_id=project3.id,
        assignee_id=user4.id,
        role=Role.SUBMITTER,
        assigner_id=project_member9.id,
    )

    project_member13 = ProjectMember(
        project_id=project4.id,
        assignee_id=user4.id,
        role=Role.ADMIN,
    )
    project_member14 = ProjectMember(
        project_id=project4.id,
        assignee_id=user1.id,
        role=Role.DEVELOPER,
        assigner_id=project_member13.id,
    )
    project_member15 = ProjectMember(
        project_id=project4.id,
        assignee_id=user2.id,
        role=Role.PROJECT_MANAGER,
        assigner_id=project_member13.id,
    )
    project_member16 = ProjectMember(
        project_id=project4.id,
        assignee_id=user3.id,
        role=Role.SUBMITTER,
        assigner_id=project_member13.id,
    )
    print(
        project_member1,
        project_member2,
        project_member3,
        project_member4,
        project_member5,
        project_member6,
        project_member7,
        project_member8,
        project_member9,
        project_member10,
        project_member11,
        project_member12,
        project_member13,
        project_member14,
        project_member15,
        project_member16,
        sep="\n\n",
    )
    print("Project members created successfully!")

    # Create tickets
    print("Creating tickets...")
    ticket1 = Ticket(
        title="ticket1",
        description="ticket1 description",
        submitter_id=project_member1.id,
        project_id=project1.id,
        assigned_developer_id=project_member2.id,
        status=Status.OPEN,
        priority=Priority.NONE,
        ticket_type=TicketType.BUG_ERROR,
    )
    ticket2 = Ticket(
        title="ticket2",
        description="ticket2 description",
        submitter_id=project_member2.id,
        project_id=project1.id,
        assigned_developer_id=project_member2.id,
        status=Status.IN_PROGRESS,
        priority=Priority.LOW,
        ticket_type=TicketType.FEATURE_REQUEST,
    )
    ticket3 = Ticket(
        title="ticket3",
        description="ticket3 description",
        submitter_id=project_member3.id,
        project_id=project1.id,
        assigned_developer_id=project_member2.id,
        status=Status.PENDING,
        priority=Priority.MEDIUM,
        ticket_type=TicketType.TASK,
    )
    ticket4 = Ticket(
        title="ticket4",
        description="ticket4 description",
        submitter_id=project_member4.id,
        project_id=project1.id,
        assigned_developer_id=project_member2.id,
        status=Status.RESOLVED,
        priority=Priority.HIGH,
        ticket_type=TicketType.INCIDENT,
    )
    ticket5 = Ticket(
        title="ticket5",
        description="ticket5 description",
        submitter_id=project_member5.id,
        project_id=project2.id,
        assigned_developer_id=project_member6.id,
        status=Status.CLOSED,
        priority=Priority.NONE,
        ticket_type=TicketType.CHANGE_REQUEST,
    )
    ticket6 = Ticket(
        title="ticket6",
        description="ticket6 description",
        submitter_id=project_member6.id,
        project_id=project2.id,
        assigned_developer_id=project_member6.id,
        status=Status.REOPENED,
        priority=Priority.LOW,
        ticket_type=TicketType.SUPPORT_HELPDESK,
    )
    ticket7 = Ticket(
        title="ticket7",
        description="ticket7 description",
        submitter_id=project_member7.id,
        project_id=project2.id,
        assigned_developer_id=project_member6.id,
        status=Status.DUPLICATE,
        priority=Priority.MEDIUM,
        ticket_type=TicketType.DOCUMENTATION,
    )
    ticket8 = Ticket(
        title="ticket8",
        description="ticket8 description",
        submitter_id=project_member8.id,
        project_id=project2.id,
        assigned_developer_id=project_member6.id,
        status=Status.OPEN,
        priority=Priority.HIGH,
        ticket_type=TicketType.SECURITY,
    )
    ticket9 = Ticket(
        title="ticket9",
        description="ticket9 description",
        submitter_id=project_member9.id,
        project_id=project3.id,
        assigned_developer_id=project_member10.id,
        status=Status.IN_PROGRESS,
        priority=Priority.NONE,
        ticket_type=TicketType.FEEDBACK,
    )
    ticket10 = Ticket(
        title="ticket10",
        description="ticket10 description",
        submitter_id=project_member10.id,
        project_id=project3.id,
        assigned_developer_id=project_member10.id,
        status=Status.PENDING,
        priority=Priority.LOW,
        ticket_type=TicketType.OTHER,
    )
    ticket11 = Ticket(
        title="ticket11",
        description="ticket11 description",
        submitter_id=project_member11.id,
        project_id=project3.id,
        assigned_developer_id=project_member10.id,
        status=Status.RESOLVED,
        priority=Priority.MEDIUM,
        ticket_type=TicketType.BUG_ERROR,
    )
    ticket12 = Ticket(
        title="ticket12",
        description="ticket12 description",
        submitter_id=project_member12.id,
        project_id=project3.id,
        assigned_developer_id=project_member10.id,
        status=Status.CLOSED,
        priority=Priority.HIGH,
        ticket_type=TicketType.FEATURE_REQUEST,
    )
    ticket13 = Ticket(
        title="ticket13",
        description="ticket13 description",
        submitter_id=project_member13.id,
        project_id=project4.id,
        assigned_developer_id=project_member14.id,
        status=Status.REOPENED,
        priority=Priority.NONE,
        ticket_type=TicketType.TASK,
    )
    ticket14 = Ticket(
        title="ticket14",
        description="ticket14 description",
        submitter_id=project_member14.id,
        project_id=project4.id,
        assigned_developer_id=project_member14.id,
        status=Status.DUPLICATE,
        priority=Priority.LOW,
        ticket_type=TicketType.INCIDENT,
    )
    ticket15 = Ticket(
        title="ticket15",
        description="ticket15 description",
        submitter_id=project_member15.id,
        project_id=project4.id,
        assigned_developer_id=project_member14.id,
        status=Status.OPEN,
        priority=Priority.MEDIUM,
        ticket_type=TicketType.CHANGE_REQUEST,
    )
    ticket16 = Ticket(
        title="ticket16",
        description="ticket16 description",
        submitter_id=project_member16.id,
        project_id=project4.id,
        assigned_developer_id=project_member14.id,
        status=Status.IN_PROGRESS,
        priority=Priority.HIGH,
        ticket_type=TicketType.SUPPORT_HELPDESK,
    )
    print(
        ticket1,
        ticket2,
        ticket3,
        ticket4,
        ticket5,
        ticket6,
        ticket7,
        ticket8,
        ticket9,
        ticket10,
        ticket11,
        ticket12,
        ticket13,
        ticket14,
        ticket15,
        ticket16,
        sep="\n\n",
    )
    print("Tickets created successfully!")

    # Create attachments
    print("Creating attachments...")
    attachment1 = Attachment(
        ticket_id=ticket1.id,
        description="attachment1 description",
        file_name="attachment1.py",
        file_path="/home/attachment1.py",
    )
    attachment2 = Attachment(
        ticket_id=ticket2.id,
        description="attachment2 description",
        file_name="attachment2.py",
        file_path="/home/attachment2.py",
    )
    attachment3 = Attachment(
        ticket_id=ticket3.id,
        description="attachment3 description",
        file_name="attachment3.py",
        file_path="/home/attachment3.py",
    )
    attachment4 = Attachment(
        ticket_id=ticket4.id,
        description="attachment4 description",
        file_name="attachment4.py",
        file_path="/home/attachment4.py",
    )
    attachment5 = Attachment(
        ticket_id=ticket5.id,
        description="attachment5 description",
        file_name="attachment5.py",
        file_path="/home/attachment5.py",
    )
    attachment6 = Attachment(
        ticket_id=ticket6.id,
        description="attachment6 description",
        file_name="attachment6.py",
        file_path="/home/attachment6.py",
    )
    attachment7 = Attachment(
        ticket_id=ticket7.id,
        description="attachment7 description",
        file_name="attachment7.py",
        file_path="/home/attachment7.py",
    )
    attachment8 = Attachment(
        ticket_id=ticket8.id,
        description="attachment8 description",
        file_name="attachment8.py",
        file_path="/home/attachment8.py",
    )
    attachment9 = Attachment(
        ticket_id=ticket9.id,
        description="attachment9 description",
        file_name="attachment9.py",
        file_path="/home/attachment9.py",
    )
    attachment10 = Attachment(
        ticket_id=ticket10.id,
        description="attachment10 description",
        file_name="attachment10.py",
        file_path="/home/attachment10.py",
    )
    attachment11 = Attachment(
        ticket_id=ticket11.id,
        description="attachment11 description",
        file_name="attachment11.py",
        file_path="/home/attachment11.py",
    )
    attachment12 = Attachment(
        ticket_id=ticket12.id,
        description="attachment12 description",
        file_name="attachment12.py",
        file_path="/home/attachment12.py",
    )
    attachment13 = Attachment(
        ticket_id=ticket13.id,
        description="attachment13 description",
        file_name="attachment13.py",
        file_path="/home/attachment13.py",
    )
    attachment14 = Attachment(
        ticket_id=ticket14.id,
        description="attachment14 description",
        file_name="attachment14.py",
        file_path="/home/attachment14.py",
    )
    attachment15 = Attachment(
        ticket_id=ticket15.id,
        description="attachment15 description",
        file_name="attachment15.py",
        file_path="/home/attachment15.py",
    )
    attachment16 = Attachment(
        ticket_id=ticket16.id,
        description="attachment16 description",
        file_name="attachment16.py",
        file_path="/home/attachment16.py",
    )
    attachment17 = Attachment(
        ticket_id=ticket1.id,
        description="attachment17 description",
        file_name="attachment17.py",
        file_path="/home/attachment17.py",
    )
    attachment18 = Attachment(
        ticket_id=ticket2.id,
        description="attachment18 description",
        file_name="attachment18.py",
        file_path="/home/attachment18.py",
    )
    attachment19 = Attachment(
        ticket_id=ticket3.id,
        description="attachment19 description",
        file_name="attachment19.py",
        file_path="/home/attachment19.py",
    )
    attachment20 = Attachment(
        ticket_id=ticket4.id,
        description="attachment20 description",
        file_name="attachment20.py",
        file_path="/home/attachment20.py",
    )
    attachment21 = Attachment(
        ticket_id=ticket5.id,
        description="attachment21 description",
        file_name="attachment21.py",
        file_path="/home/attachment21.py",
    )
    attachment22 = Attachment(
        ticket_id=ticket6.id,
        description="attachment22 description",
        file_name="attachment22.py",
        file_path="/home/attachment22.py",
    )
    attachment23 = Attachment(
        ticket_id=ticket7.id,
        description="attachment23 description",
        file_name="attachment23.py",
        file_path="/home/attachment23.py",
    )
    attachment24 = Attachment(
        ticket_id=ticket8.id,
        description="attachment24 description",
        file_name="attachment24.py",
        file_path="/home/attachment24.py",
    )
    attachment25 = Attachment(
        ticket_id=ticket9.id,
        description="attachment25 description",
        file_name="attachment25.py",
        file_path="/home/attachment25.py",
    )
    attachment26 = Attachment(
        ticket_id=ticket10.id,
        description="attachment26 description",
        file_name="attachment26.py",
        file_path="/home/attachment26.py",
    )
    attachment27 = Attachment(
        ticket_id=ticket11.id,
        description="attachment27 description",
        file_name="attachment27.py",
        file_path="/home/attachment27.py",
    )
    attachment28 = Attachment(
        ticket_id=ticket12.id,
        description="attachment28 description",
        file_name="attachment28.py",
        file_path="/home/attachment28.py",
    )
    attachment29 = Attachment(
        ticket_id=ticket13.id,
        description="attachment29 description",
        file_name="attachment29.py",
        file_path="/home/attachment29.py",
    )
    attachment30 = Attachment(
        ticket_id=ticket14.id,
        description="attachment30 description",
        file_name="attachment30.py",
        file_path="/home/attachment30.py",
    )
    attachment31 = Attachment(
        ticket_id=ticket15.id,
        description="attachment31 description",
        file_name="attachment31.py",
        file_path="/home/attachment31.py",
    )
    attachment32 = Attachment(
        ticket_id=ticket16.id,
        description="attachment32 description",
        file_name="attachment32.py",
        file_path="/home/attachment32.py",
    )
    print(
        attachment1,
        attachment2,
        attachment3,
        attachment4,
        attachment5,
        attachment6,
        attachment7,
        attachment8,
        attachment9,
        attachment10,
        attachment11,
        attachment12,
        attachment13,
        attachment14,
        attachment15,
        attachment16,
        attachment17,
        attachment18,
        attachment19,
        attachment20,
        attachment21,
        attachment22,
        attachment23,
        attachment24,
        attachment25,
        attachment26,
        attachment27,
        attachment28,
        attachment29,
        attachment30,
        attachment31,
        attachment32,
        sep="\n\n",
    )
    print("Attachments created successfully!")

    # Create comments
    print("Creating comments...")
    comment1 = Comment(
        content="comment1 content",
        ticket_id=ticket1.id,
        commenter_id=project_member1.id,
    )
    comment2 = Comment(
        content="comment2 content",
        commenter_id=project_member2.id,
        ticket_id=ticket2.id,
    )
    comment3 = Comment(
        content="comment3 content",
        commenter_id=project_member3.id,
        ticket_id=ticket3.id,
    )
    comment4 = Comment(
        content="comment4 content",
        commenter_id=project_member4.id,
        ticket_id=ticket4.id,
    )
    comment5 = Comment(
        content="comment5 content",
        commenter_id=project_member5.id,
        ticket_id=ticket5.id,
    )
    comment6 = Comment(
        content="comment6 content",
        commenter_id=project_member6.id,
        ticket_id=ticket6.id,
    )
    comment7 = Comment(
        content="comment7 content",
        commenter_id=project_member7.id,
        ticket_id=ticket7.id,
    )
    comment8 = Comment(
        content="comment8 content",
        commenter_id=project_member8.id,
        ticket_id=ticket8.id,
    )
    comment9 = Comment(
        content="comment9 content",
        commenter_id=project_member9.id,
        ticket_id=ticket9.id,
    )
    comment10 = Comment(
        content="comment10 content",
        commenter_id=project_member10.id,
        ticket_id=ticket10.id,
    )
    comment11 = Comment(
        content="comment11 content",
        commenter_id=project_member11.id,
        ticket_id=ticket11.id,
    )
    comment12 = Comment(
        content="comment12 content",
        commenter_id=project_member12.id,
        ticket_id=ticket12.id,
    )
    comment13 = Comment(
        content="comment13 content",
        commenter_id=project_member13.id,
        ticket_id=ticket13.id,
    )
    comment14 = Comment(
        content="comment14 content",
        commenter_id=project_member14.id,
        ticket_id=ticket14.id,
    )
    comment15 = Comment(
        content="comment15 content",
        commenter_id=project_member15.id,
        ticket_id=ticket15.id,
    )
    comment16 = Comment(
        content="comment16 content",
        commenter_id=project_member16.id,
        ticket_id=ticket16.id,
    )
    comment17 = Comment(
        content="comment17 content",
        commenter_id=project_member1.id,
        ticket_id=ticket1.id,
    )
    comment19 = Comment(
        content="comment19 content",
        commenter_id=project_member2.id,
        ticket_id=ticket2.id,
    )
    comment20 = Comment(
        content="comment20 content",
        commenter_id=project_member3.id,
        ticket_id=ticket3.id,
    )
    comment21 = Comment(
        content="comment21 content",
        commenter_id=project_member4.id,
        ticket_id=ticket4.id,
    )
    comment22 = Comment(
        content="comment22 content",
        commenter_id=project_member5.id,
        ticket_id=ticket5.id,
    )
    comment23 = Comment(
        content="comment23 content",
        commenter_id=project_member6.id,
        ticket_id=ticket6.id,
    )
    comment24 = Comment(
        content="comment24 content",
        commenter_id=project_member7.id,
        ticket_id=ticket7.id,
    )
    comment25 = Comment(
        content="comment25 content",
        commenter_id=project_member8.id,
        ticket_id=ticket8.id,
    )
    comment26 = Comment(
        content="comment26 content",
        commenter_id=project_member9.id,
        ticket_id=ticket9.id,
    )
    comment27 = Comment(
        content="comment27 content",
        commenter_id=project_member10.id,
        ticket_id=ticket10.id,
    )
    comment28 = Comment(
        content="comment28 content",
        commenter_id=project_member11.id,
        ticket_id=ticket11.id,
    )
    comment29 = Comment(
        content="comment29 content",
        commenter_id=project_member12.id,
        ticket_id=ticket12.id,
    )
    comment30 = Comment(
        content="comment30 content",
        commenter_id=project_member13.id,
        ticket_id=ticket13.id,
    )
    comment31 = Comment(
        content="comment31 content",
        commenter_id=project_member14.id,
        ticket_id=ticket14.id,
    )
    comment32 = Comment(
        content="comment32 content",
        commenter_id=project_member15.id,
        ticket_id=ticket15.id,
    )
    comment18 = Comment(
        content="comment18 content",
        commenter_id=project_member16.id,
        ticket_id=ticket16.id,
    )
    print(
        comment1,
        comment2,
        comment3,
        comment4,
        comment5,
        comment6,
        comment7,
        comment8,
        comment9,
        comment10,
        comment11,
        comment12,
        comment13,
        comment14,
        comment15,
        comment16,
        comment17,
        comment18,
        comment19,
        comment20,
        comment21,
        comment22,
        comment23,
        comment24,
        comment25,
        comment26,
        comment27,
        comment28,
        comment29,
        comment30,
        comment31,
        comment32,
        sep="\n\n",
    )
    print("Comments created successfully!")

    # Create ticket histories
    print("Creating ticket histories...")
    previous_value = ticket1.title
    ticket1.title = "ticket1 title changed"
    ticket_history1 = TicketHistory(
        ticket_id=ticket1.id,
        previous_value=previous_value,
        present_value=ticket1.title,
        action=Action.TITLE_CHANGE,
    )

    previous_value = ticket2.description
    ticket2.description = "ticket2 description changed"
    ticket_history2 = TicketHistory(
        ticket_id=ticket2.id,
        previous_value=previous_value,
        present_value=ticket2.description,
        action=Action.DESCRIPTION_CHANGE,
    )

    project_member4.role = Role.DEVELOPER
    previous_value = ticket3.assigned_developer_id
    ticket3.assigned_developer_id = project_member4.id
    ticket_history3 = TicketHistory(
        ticket_id=ticket3.id,
        previous_value=previous_value,
        present_value=ticket3.assigned_developer_id,
        action=Action.ASSIGNED_DEVELOPER_CHANGE,
    )

    previous_value = ticket4.status
    ticket4.status = Status.REOPENED
    ticket_history4 = TicketHistory(
        ticket_id=ticket4.id,
        previous_value=previous_value,
        present_value=ticket4.status,
        action=Action.STATUS_CHANGE,
    )

    previous_value = ticket5.priority
    ticket5.priority = Priority.HIGH
    ticket_history5 = TicketHistory(
        ticket_id=ticket5.id,
        previous_value=previous_value,
        present_value=ticket5.priority,
        action=Action.PRIORITY_CHANGE,
    )

    previous_value = ticket6.ticket_type
    ticket6.ticket_type = TicketType.DOCUMENTATION
    ticket_history6 = TicketHistory(
        ticket_id=ticket6.id,
        previous_value=previous_value,
        present_value=ticket6.ticket_type,
        action=Action.TICKET_TYPE_CHANGE,
    )

    previous_value = ticket7.title
    ticket7.title = "ticket7 title changed"
    ticket_history7 = TicketHistory(
        ticket_id=ticket7.id,
        previous_value=previous_value,
        present_value=ticket7.title,
        action=Action.TITLE_CHANGE,
    )

    previous_value = ticket8.description
    ticket8.description = "ticket8 description changed"
    ticket_history8 = TicketHistory(
        ticket_id=ticket8.id,
        previous_value=previous_value,
        present_value=ticket8.description,
        action=Action.DESCRIPTION_CHANGE,
    )

    project_member12.role = Role.DEVELOPER
    previous_value = ticket9.assigned_developer_id
    ticket9.assigned_developer_id = project_member12.id
    ticket_history9 = TicketHistory(
        ticket_id=ticket9.id,
        previous_value=previous_value,
        present_value=ticket9.assigned_developer_id,
        action=Action.ASSIGNED_DEVELOPER_CHANGE,
    )

    previous_value = ticket10.status
    ticket10.status = Status.RESOLVED
    ticket_history10 = TicketHistory(
        ticket_id=ticket10.id,
        previous_value=previous_value,
        present_value=ticket10.status,
        action=Action.STATUS_CHANGE,
    )

    previous_value = ticket11.priority
    ticket11.priority = Priority.LOW
    ticket_history11 = TicketHistory(
        ticket_id=ticket11.id,
        previous_value=previous_value,
        present_value=ticket11.priority,
        action=Action.PRIORITY_CHANGE,
    )

    previous_value = ticket12.ticket_type
    ticket12.ticket_type = TicketType.CHANGE_REQUEST
    ticket_history12 = TicketHistory(
        ticket_id=ticket12.id,
        previous_value=previous_value,
        present_value=ticket12.ticket_type,
        action=Action.TICKET_TYPE_CHANGE,
    )

    previous_value = ticket13.title
    ticket13.title = "ticket13 title changed"
    ticket_history13 = TicketHistory(
        ticket_id=ticket13.id,
        previous_value=previous_value,
        present_value=ticket13.title,
        action=Action.TITLE_CHANGE,
    )

    previous_value = ticket14.description
    ticket14.description = "ticket14 description changed"
    ticket_history14 = TicketHistory(
        ticket_id=ticket14.id,
        previous_value=previous_value,
        present_value=ticket14.description,
        action=Action.DESCRIPTION_CHANGE,
    )

    project_member16.role = Role.DEVELOPER
    previous_value = ticket15.assigned_developer_id
    ticket15.assigned_developer_id = project_member16.id
    ticket_history15 = TicketHistory(
        ticket_id=ticket15.id,
        previous_value=previous_value,
        present_value=ticket15.assigned_developer_id,
        action=Action.ASSIGNED_DEVELOPER_CHANGE,
    )

    previous_value = ticket16.status
    ticket16.status = Status.CLOSED
    ticket_history16 = TicketHistory(
        ticket_id=ticket16.id,
        previous_value=previous_value,
        present_value=ticket16.status,
        action=Action.STATUS_CHANGE,
    )

    previous_value = ticket3.assigned_developer_id
    ticket3.assigned_developer_id = project_member2.id
    ticket_history17 = TicketHistory(
        ticket_id=ticket3.id,
        previous_value=previous_value,
        present_value=ticket3.assigned_developer_id,
        action=Action.ASSIGNED_DEVELOPER_CHANGE,
    )

    previous_value = ticket9.assigned_developer_id
    ticket9.assigned_developer_id = project_member10.id
    ticket_history18 = TicketHistory(
        ticket_id=ticket9.id,
        previous_value=previous_value,
        present_value=ticket9.assigned_developer_id,
        action=Action.ASSIGNED_DEVELOPER_CHANGE,
    )

    previous_value = ticket15.assigned_developer_id
    ticket15.assigned_developer_id = project_member14.id
    ticket_history19 = TicketHistory(
        ticket_id=ticket15.id,
        previous_value=previous_value,
        present_value=ticket15.assigned_developer_id,
        action=Action.ASSIGNED_DEVELOPER_CHANGE,
    )
    print(
        ticket_history1,
        ticket_history2,
        ticket_history3,
        ticket_history4,
        ticket_history5,
        ticket_history6,
        ticket_history7,
        ticket_history8,
        ticket_history9,
        ticket_history10,
        ticket_history11,
        ticket_history12,
        ticket_history13,
        ticket_history14,
        ticket_history15,
        ticket_history16,
        ticket_history17,
        ticket_history18,
        ticket_history19,
        sep="\n\n",
    )
    print("Ticket histories created successfully!")

    # add all to db
    create_db_and_tables()
    with Session(engine) as session:
        all_objects = [
            user1,
            user2,
            user3,
            user4,
            project1,
            project2,
            project3,
            project4,
            project_member1,
            project_member2,
            project_member3,
            project_member4,
            project_member5,
            project_member6,
            project_member7,
            project_member8,
            project_member9,
            project_member10,
            project_member11,
            project_member12,
            project_member13,
            project_member14,
            project_member15,
            project_member16,
            ticket1,
            ticket2,
            ticket3,
            ticket4,
            ticket5,
            ticket6,
            ticket7,
            ticket8,
            ticket9,
            ticket10,
            ticket11,
            ticket12,
            ticket13,
            ticket14,
            ticket15,
            ticket16,
            attachment1,
            attachment2,
            attachment3,
            attachment4,
            attachment5,
            attachment6,
            attachment7,
            attachment8,
            attachment9,
            attachment10,
            attachment11,
            attachment12,
            attachment13,
            attachment14,
            attachment15,
            attachment16,
            attachment17,
            attachment18,
            attachment19,
            attachment20,
            attachment21,
            attachment22,
            attachment23,
            attachment24,
            attachment25,
            attachment26,
            attachment27,
            attachment28,
            attachment29,
            attachment30,
            attachment31,
            attachment32,
            comment1,
            comment2,
            comment3,
            comment4,
            comment5,
            comment6,
            comment7,
            comment8,
            comment9,
            comment10,
            comment11,
            comment12,
            comment13,
            comment14,
            comment15,
            comment16,
            comment17,
            comment18,
            comment19,
            comment20,
            comment21,
            comment22,
            comment23,
            comment24,
            comment25,
            comment26,
            comment27,
            comment28,
            comment29,
            comment30,
            comment31,
            comment32,
            ticket_history1,
            ticket_history2,
            ticket_history3,
            ticket_history4,
            ticket_history5,
            ticket_history6,
            ticket_history7,
            ticket_history8,
            ticket_history9,
            ticket_history10,
            ticket_history11,
            ticket_history12,
            ticket_history13,
            ticket_history14,
            ticket_history15,
            ticket_history16,
            ticket_history17,
            ticket_history18,
            ticket_history19,
        ]
        for obj in all_objects:
            session.add(obj)
            session.commit()
        print("Done!")


if __name__ == "__main__":
    populate()
