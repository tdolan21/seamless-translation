from transformers import AutoProcessor, SeamlessM4Tv2Model
import torchaudio
import soundfile as sf

# Initialize the processor and model
processor = AutoProcessor.from_pretrained("facebook/seamless-m4t-v2-large")
model = SeamlessM4Tv2Model.from_pretrained("facebook/seamless-m4t-v2-large")

# Text to audio conversion
text_inputs = processor(text="Hello, my dog is cute", src_lang="eng", return_tensors="pt")
audio_array_from_text = model.generate(**text_inputs, tgt_lang="rus")[0].cpu().numpy().squeeze()

# Save the audio generated from text
sf.write('audio_from_text.wav', audio_array_from_text, 16000)  # 16000 is the sampling rate

# Audio to audio conversion
audio, orig_freq = torchaudio.load("https://www2.cs.uic.edu/~i101/SoundFiles/preamble10.wav")
audio = torchaudio.functional.resample(audio, orig_freq=orig_freq, new_freq=16000)  # Resample to 16 kHz
audio_inputs = processor(audios=audio, return_tensors="pt")
audio_array_from_audio = model.generate(**audio_inputs, tgt_lang="rus")[0].cpu().numpy().squeeze()

# Save the audio generated from another audio
sf.write('audio_from_audio.wav', audio_array_from_audio, 16000)  # 16000 is the sampling rate
