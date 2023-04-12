import os
import time
import replicate  # pip install replicate
from gtts import gTTS  # pip install gtts
from playsound import playsound  # pip install playsound, pip3 install PyObjC

start = time.time()

os.environ["REPLICATE_API_TOKEN"] = "e703f82f0d7127588a4bd85d57284c3acb192ae5"

output = replicate.run(
    "rmokady/clip_prefix_caption:9a34a6339872a03f45236f114321fb51fc7aa8269d38ae0ce5334969981e4cd8",
    input={"image": open("image.jpeg", "rb")}
)

audio = 'image_caption.mp3'
language = 'en'

sp = gTTS(
    lang=language,
    text=output,
    slow=False
)
sp.save(audio)
# playsound(audio)  # 이 코드 한 줄로 대충 5초 차이남

end = time.time()
print(f"time : {end - start}")
# time : 7.232642889022827 25줄 포함
# time : 2.1659789085388184 25줄 미포함
