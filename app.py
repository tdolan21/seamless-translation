import streamlit as st
from transformers import AutoProcessor, SeamlessM4Tv2Model
import torchaudio
import soundfile as sf
import torch
import os

language_map = {
    "Modern Standard Arabic": "arb", "Bengali": "ben", "Catalan": "cat",
    "Czech": "ces", "Mandarin Chinese": "cmn", "Welsh": "cym",
    "Danish": "dan", "German": "deu", "English": "eng",
    "Estonian": "est", "Finnish": "fin", "French": "fra",
    "Hindi": "hin", "Indonesian": "ind", "Italian": "ita",
    "Japanese": "jpn", "Kannada": "kan", "Korean": "kor",
    "Maltese": "mlt", "Dutch": "nld", "Western Persian": "pes",
    "Polish": "pol", "Portuguese": "por", "Romanian": "ron",
    "Russian": "rus", "Slovak": "slk", "Spanish": "spa",
    "Swedish": "swe", "Swahili": "swh", "Tamil": "tam",
    "Telugu": "tel", "Tagalog": "tgl", "Thai": "tha",
    "Turkish": "tur", "Ukrainian": "ukr", "Urdu": "urd",
    "Northern Uzbek": "uzn", "Vietnamese": "vie"
}

# Check if CUDA (GPU support) is available and set the device accordingly
device = "cuda" if torch.cuda.is_available() else "cpu"

# Function to load and cache the model and processor
@st.cache_resource
def load_model_and_processor():
    processor = AutoProcessor.from_pretrained("facebook/seamless-m4t-v2-large")
    model = SeamlessM4Tv2Model.from_pretrained("facebook/seamless-m4t-v2-large")
    model.to(device)
    return processor, model

processor, model = load_model_and_processor()

# Streamlit app layout
st.title("Seamless Translation")

# Sidebar components
st.sidebar.header("Input Settings")
input_text = st.sidebar.text_input("Enter text for conversion:", "Hello, my dog is cute")
selected_language_name = st.sidebar.selectbox("Select Target Language:", list(language_map.keys()))
selected_language_code = language_map[selected_language_name]

# Function to convert text to audio and save
def text_to_audio(text, language):
    text_inputs = processor(text=text, src_lang="eng", return_tensors="pt").to(device)
    audio_array = model.generate(**text_inputs, tgt_lang=language)[0].cpu().numpy().squeeze()
    file_path = 'audio_from_text.wav'
    sf.write(file_path, audio_array, 16000)
    return file_path


# Function to convert audio to audio and save
def audio_to_audio(input_audio_path, language):
    audio, orig_freq = torchaudio.load(input_audio_path)
    audio = torchaudio.functional.resample(audio, orig_freq=orig_freq, new_freq=16000).to(device)
    audio_inputs = processor(audios=audio, return_tensors="pt").to(device)
    audio_array = model.generate(**audio_inputs, tgt_lang=language)[0].cpu().numpy().squeeze()
    file_path = 'audio_from_audio.wav'
    sf.write(file_path, audio_array, 16000)
    return file_path

# UI to trigger text-to-audio conversion
if st.sidebar.button("Convert Text to Audio"):
    with st.spinner("Converting..."):
        audio_path = text_to_audio(input_text, selected_language_code)
        st.audio(audio_path)

# UI to upload audio file and trigger audio-to-audio conversion
uploaded_audio = st.sidebar.file_uploader("Upload audio for conversion:", type=["wav"])
if uploaded_audio is not None and st.button("Convert Uploaded Audio"):
    with st.spinner("Converting..."):
        audio_file_path = f"temp_{uploaded_audio.name}"
        with open(audio_file_path, "wb") as f:
            f.write(uploaded_audio.getvalue())
        converted_audio_path = audio_to_audio(audio_file_path, selected_language_code)
        st.audio(converted_audio_path)
        os.remove(audio_file_path)