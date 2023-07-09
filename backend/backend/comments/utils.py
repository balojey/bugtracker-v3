from datetime import datetime
from ..models import Comment, Bug, ProjectMember
from .schemas import CommentIn, CommentUpdate


async def read_comment(comment_id: str) -> Comment:
    """A function to read a comment from the database"""
    try:
        comment = await Comment.get(comment_id, fetch_links=True)
        if not comment:
            raise Exception("Comment not found")
        return comment
    except Exception as e:
        raise e


async def write_comment(comment: CommentIn, bug: Bug, author: ProjectMember) -> Comment:
    """A function to write a comment to the database"""
    try:
        comment = Comment(
            **comment.dict(),
            bug=bug,
            author=author,
        )
        await comment.save()
        return await read_comment(comment.id)
    except Exception as e:
        raise e


async def read_comments(bug: Bug) -> list[Comment]:
    """A function to read comments from the database"""
    try:
        cmnts = [
            cmnt for cmnt in await Comment.find().to_list() if cmnt.bug.ref.id == bug.id
        ]
        for cmnt in cmnts:
            await cmnt.fetch_all_links()
        return cmnts

    except Exception as e:
        raise e


async def edit_comment(comment: Comment, comment_update: CommentUpdate) -> Comment:
    """A function to edit a comment"""
    try:
        comment.content = comment_update.content
        comment.updated_at = datetime.utcnow()
        await comment.save()
        return await read_comment(comment.id)
    except Exception as e:
        raise e


async def remove_comment(comment: Comment) -> None:
    """A function to remove a comment"""
    try:
        await comment.delete()
    except Exception as e:
        raise e
