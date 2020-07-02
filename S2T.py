#import library
from ibm_watson import SpeechToTextV1 
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
# store your API url and APIKEY 
SPEECH_TO_TEXT_URL="https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/56537a43-d299-429b-a013-9ee67036ed0f"
SPEECH_TO_TEXT_IAM_APIKEY="W-g24360jzJ74y9fqpCYGzPPgBMWyNy0gT4CAPpl8IWh"
# create API object by authenticating your url and key	
authenticator = IAMAuthenticator(SPEECH_TO_TEXT_IAM_APIKEY)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(SPEECH_TO_TEXT_URL)
s2t
# open your .mp3 audio file
with open(r"C:\Users\GAURAV\Downloads\PolynomialRegressionandPipelines.mp3", mode="rb")  as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3'
			     
#store the response in result			     
response.result
from pandas.io.json import json_normalize
json_normalize(response.result['results'],"alternatives")
response
# read your result and store in recognized_text 
recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
type(recognized_text)
print(recognized_text)
