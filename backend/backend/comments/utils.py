from ..models import Comment


async def write_comment(comment: dict) -> dict:
    """A function to write a comment to the database"""
    