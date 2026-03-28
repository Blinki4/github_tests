from pydantic import BaseModel


class CreateRepositoryResponseOwnerModel(BaseModel):
    login: str
    id: int
    url: str
    type: str

class CreateRepositoryResponseModel(BaseModel):
    id: int
    name: str
    full_name: str
    owner: CreateRepositoryResponseOwnerModel
    private: bool
    description: str | None
    url: str