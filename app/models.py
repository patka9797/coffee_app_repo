from pydantic import BaseModel


class Coffee(BaseModel):
    id: str = None
    beverage_method: str
    origin: str
    steps: list[str]
    body: str
    portions: int
    tags: list[str]


    def __str__(self):
        return f"""/
        {self.beverage_method.capitalize()}

        Origin: {self.origin}
        Steps: {self.steps}
        Body: {self.body}
        Portions: {self.portions}
        Tags: {self.tags}"""
