import re
import os
from unicodedata import category
from google.cloud import texttospeech_v1
from google.cloud import translate_v2
from google.cloud import language_v1
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "vaibhav-gcp-2022-7be4e251ac90.json"

def process_message(message, response_array, response):
    # Splits the message and the punctuation into an array
    list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())

    # Scores the amount of words in the message
    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1

    # Returns the response and the score of the response
    # print(score, response)
    return [score, response]

def get_response(message):
    # Add your custom responses here
    response_list = [
        process_message(message, ['hello', 'hi', 'hey'], 'Hey there! Im a telegram bot and I can serve you by typing valid commands and use me whenever you need and I will be happy to reply you back in best possible way'),
        process_message(message, ['bye', 'goodbye'], 'Goodbye! , Remember that whatever you are doing , whatever you are going through in your life everything will be fine and you will succeed one or the other day'),
        process_message(message, ['how', 'are', 'you'], 'I am doing fine thanks , hope you are doing great too I am lucky to have you as my master!'),
        process_message(message, ['your', 'name'], 'My name is gcp bot, nice to meet you!, short for robot and also called an internet bot is a computer program that operates as an agent for a user or other program or to simulate a human activity'),
        process_message(message, ['help', 'me'], 'I will do my best to assist you! , Humans are social creatures. We suffer when we are isolated and thrive when we are part of a community. When we extend a helping hand to members of our community when it costs us something, it is known as altruism'),
        process_message(message, ['enjoy', 'happy'], 'have a great time, Scientific evidence suggests that being happy may have major benefits for your health. For starters, being happy promotes a healthy lifestyle. It may also help combat stress, boost your immune system,'),
        process_message(message, ['eat', 'healthy'], 'Stay fit , Physical activity or exercise can improve your health and reduce the risk of developing several diseases like type 2 diabetes, cancer and cardiovascular disease.'),
        process_message(message, ['clothes', 'beautiful'], 'That is great Clothing can insulate against cold or hot conditions, and it can provide a hygienic barrier, keeping infectious and toxic materials away from the body')
       # process_message(message, ['predict'],takeinp())
        # Add more responses here
    ]
    

    # Checks all of the response scores and returns the best matching response
    response_scores = []
    for response in response_list:
        response_scores.append(response[0])

    # Get the max value for the best response and store it into a variable
    winning_response = max(response_scores)
    matching_response = response_list[response_scores.index(winning_response)]

    # Return the matching response to the user
    if winning_response == 0:
        bot_response = 'I didn\'t understand what you wrote.Come again , write valid comments only or else google it '
    else:
        bot_response = matching_response[1]

    print('Bot response:', bot_response)
    translate_client = translate_v2.Client()
    target = 'kn'
    output = translate_client.translate(
        bot_response,
	    target_language=target)
    print(output) 
    client = texttospeech_v1.TextToSpeechClient()
    synthesis_input = texttospeech_v1.SynthesisInput(text=output["translatedText"])
    voice = texttospeech_v1.VoiceSelectionParams(
        language_code="kn-in", 
        ssml_gender=texttospeech_v1.SsmlVoiceGender.MALE
    )
    audio_config = texttospeech_v1.AudioConfig(
        audio_encoding=texttospeech_v1.AudioEncoding.MP3
    )
    response = client.synthesize_speech(
        input=synthesis_input, 
        voice=voice, 
        audio_config=audio_config
    )
    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
    return bot_response

