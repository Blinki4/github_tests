from pydantic import BaseModel


class CreateRepositoryOwnerModel(BaseModel):
    login: str
    id: int
    url: str
    type: str

class CreateRepositoryModel(BaseModel):
    id: int
    name: str
    full_name: str
    owner: CreateRepositoryOwnerModel
    private: bool
    description: str | None
    url: str