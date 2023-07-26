import numpy as np
import requests
from mlserver.codecs import NumpyCodec
from mlserver.types import InferenceRequest, RequestInput



# encode the request for the model
inference_request = InferenceRequest(
    inputs=[
        NumpyCodec.encode_input("odds", np.array([i for i in range(1, 10, 2)])),
        NumpyCodec.encode_input("evens", np.array([i for i in range(0, 10, 2)])),
    ]
)

response = requests.post(
    #"http://multiply-2:80/v2/models/model/infer", # Hit model directly
    # "http://model-chainer-00005-private:80/v2/models/model/infer", # Hit inference graph
    "http://localhost:8080/v2/models/model/infer",
    json=inference_request.dict(),
)

print("STATUS: ", response.status_code)
print("RESULT: ", response.text)
