from separate_voices import separate_voice


def write_to_file(input, file_name):
    with open(file_name, 'w') as file:
        file.write(input)

model_version = 'large-v1' #Версия модели, по умолчанию large-v1
with open('model_version.mv', 'r') as file:
    model_version = file.readline()

print(model_version)
SV = separate_voice(MODEL_NAME=model_version)

input = 'inputs/sample.wav'

ansver = SV.transcribe(input)

out_file_path = 'outputs/ansver.txt'

write_to_file(ansver, out_file_path)

