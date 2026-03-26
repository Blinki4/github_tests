from pydantic import BaseModel


class GetRepositoryOwnerModel(BaseModel):
    login: str
    id: int
    url: str
    type: str

class GetRepositoryModel(BaseModel):
    id: int
    name: str
    full_name: str
    owner: GetRepositoryOwnerModel
    private: bool
    description: str | None