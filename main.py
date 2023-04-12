import os
import time
import replicate  # pip install replicate

start = time.time()

os.environ["REPLICATE_API_TOKEN"] = "e703f82f0d7127588a4bd85d57284c3acb192ae5"

output = replicate.run(
    "rmokady/clip_prefix_caption:9a34a6339872a03f45236f114321fb51fc7aa8269d38ae0ce5334969981e4cd8",
    input={"image": open("image.jpeg", "rb")}
)

print(output)
# A photo of a sunset with a single tree in the background.
# time : 1.8036510944366455

end = time.time()
print(f"time : {end - start}")
