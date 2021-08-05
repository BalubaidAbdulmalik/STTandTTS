
url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/75486aaf-c5a5-47ee-9fa5-33f886f2f5e0'
apikey = 'aUOhDjnkgMv6qkVheMzXVNoF1HmmxYZG1bsHEGfLtRjl'



from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator




authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)




with open('output.txt', 'r') as text_file:
    text = text_file.readlines()





text = [line.replace('\n', '') for line in text]
text = ''.join(str(line) for line in text)





with open('./output.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept = 'audio/mp3', voice = 'en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)







