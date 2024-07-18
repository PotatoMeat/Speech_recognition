from pyannote.audio import Pipeline
from pyannote_whisper.utils import diarize_text
from pywhispercpp.model import Model

class separate_voice:
    def __init__(self, CONFIG_PATH='config.yaml', MODEL_PATH='/models', MODEL_NAME='large-v1'):
        # Указываем путь до файла с конфигом, он должен быть в той же директории, как сказано на шаге 3.
        self.pipeline = Pipeline.from_pretrained(CONFIG_PATH)

        # Указываем название модели large-v1 и путь до директории с whisper-моделями из шага 1.
        self.model = Model(MODEL_NAME, MODEL_PATH, n_threads=6)


    def transcribe(self, INPUT_PATH, LANGUAGE='ru'):
        # Указываем путь до аудио-файл, кторый будем расшифровывать в текст. Путь обязательно абсолютный.
        asr_result = self.model.transcribe(INPUT_PATH, language=LANGUAGE)

        # Конвертация результата в формат, который понимает pyannote-whisper.
        result = {'segments': list()}

        for item in asr_result:
            result['segments'].append({
                'start': item.t0 / 100,
                'end': item.t1 / 100,
                'text': item.text
            }
            )

        # Сегментация аудио-файла на реплики спикеров. Путь обязательно абсолютный.
        diarization_result = self.pipeline(INPUT_PATH)

        # Пересечение расшифровки и сегментаци.
        final_result = diarize_text(result, diarization_result)

        ansver=''

        # Вывод результата.
        for seg, spk, sent in final_result:
            line = f'{seg.start:.2f} {seg.end:.2f} {spk} {sent}'
            ansver = ansver + line +'\n'
            #print(line)

        return ansver

