import numpy as np
from mlserver import MLModel
from mlserver.codecs import StringCodec, NumpyCodec
from mlserver.types import InferenceRequest, InferenceResponse


class TestModel(MLModel):
    async def load(self) -> bool:
        pass

    async def predict(self, payload: InferenceRequest) -> InferenceResponse:
        
        odds = None
        evens = None
        for input in payload.inputs:
            if input.name == "odds":
                odds = NumpyCodec.decode_input(input)
            if input.name == "evens":
                evens = NumpyCodec.decode_input(input)

        if odds is None:
            raise ValueError("Missing input 'odds'")
        
        if evens is None:
            raise ValueError("Missing input 'evens'")
        
        def func(x):
            return x * 2
        
        
        return InferenceResponse(
            id=payload.id,
            model_name=self.name,
            model_version=self.version,
            outputs=[
                NumpyCodec.encode_output(
                    name="odds", payload=np.array([func(i) for i in odds])
                ),
                NumpyCodec.encode_output(
                    name="evens", payload=np.array([func(i) for i in evens])
                ),
            ],
        )
