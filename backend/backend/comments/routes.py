from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_users import FastAPIUsers
from beanie.odm.fields import PydanticObjectId
from models import User
from auth.backend import auth_backend
from users.user_manager import get_user_manager
from permissions import check_reporter, check_author_or_admin
from .schemas import CommentOut, CommentUpdate
from .utils import read_comment, edit_comment, remove_comment


router = APIRouter(prefix="/comments", tags=["comments"])
fastapi_users = FastAPIUsers[User, PydanticObjectId](get_user_manager, [auth_backend])
current_active_verified_user = fastapi_users.current_user(active=True, verified=True)


@router.patch(
    "/{comment_id}", response_model=CommentOut, status_code=status.HTTP_200_OK
)
async def update_comment(
    comment_id: str,
    comment: CommentUpdate,
    user: User = Depends(current_active_verified_user),
):
    """A route to update a comment"""
    try:
        db_comment = await read_comment(comment_id)
        if not db_comment:
            raise Exception("Comment not found")
        await check_reporter(user, db_comment.author)
        return await edit_comment(db_comment, comment)
    except Exception as e:
        if str(e) == "You cannot edit this bug":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_comment(
    comment_id: str, user: User = Depends(current_active_verified_user)
):
    """A route to delete a comment"""
    try:
        comment = await read_comment(comment_id)
        if not comment:
            raise Exception("Comment not found")
        await check_author_or_admin(user, comment)
        return await remove_comment(comment)
    except Exception as e:
        if str(e) == "You cannot edit this bug":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
