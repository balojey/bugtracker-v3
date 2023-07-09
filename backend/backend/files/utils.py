from ..models import File, Bug
from .schemas import FileIn


async def save_attachment(file: FileIn, bug: Bug) -> File:
    """Save a file"""
    file = await File(**file.dict(), bug=bug).insert()
    return await read_attachment(file.id)


async def read_attachments(bug: Bug) -> list[File]:
    """Read all attachments for a bug"""
    fls = [
        file for file in await File.find_all().to_list() if file.bug.ref.id == bug.id
    ]
    return fls


async def read_attachment(file_id: str) -> File:
    """Read a file"""
    try:
        file = await File.get(file_id, fetch_links=True)
        if not file:
            raise Exception("File not found")
        return file
    except Exception as e:
        raise e
    

async def remove_attachment(file: File) -> None:
    """Remove a file"""
    try:
        await file.delete()
    except Exception as e:
        raise e
