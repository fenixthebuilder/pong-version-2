import winsound

def chime():
    winsound.PlaySound("pad_bounce.wav", winsound.SND_ASYNC)