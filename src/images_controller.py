from fastapi import APIRouter, File, UploadFile
from fastapi.responses import StreamingResponse
from .drive.drive import Drive

router:APIRouter = APIRouter(
        prefix="/images",
        tags=["images"]
)

@router.post("/upload")
def upload_img(file: UploadFile = File(...)):
    name = file.filename
    f = file.file
    res =Drive.folder.put(name=name,data=f)

    return res


@router.get("/download/{name}")
def download_img(name: str):
    res = Drive.folder.get(name)
    ext:str = name.split(".")[1]

    return StreamingResponse(res.iter_chunks(), media_type=f"image/{ext}")
