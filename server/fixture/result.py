from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


SYNTHETIC_SAMPLES = (2, 4, 6)


class MeanResult(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True, allow_inf_nan=False)

    version: int = Field(ge=1, le=1)
    method: Literal["synthetic-mean-v1"]
    count: int = Field(gt=0)
    mean: float

    def check_fixture_values(self) -> None:
        if self.count != len(SYNTHETIC_SAMPLES) or abs(self.mean - 4) > 0.000001:
            raise ValueError("R result is incompatible with the fixture input")
