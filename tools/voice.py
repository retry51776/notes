import tkinter as tk
from tkinter import ttk, scrolledtext
import sounddevice as sd
import numpy as np
import wave
import whisper
import threading
import pyperclip

class VoiceTypingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Whisper Voice Typing")
        self.root.geometry("800x600")
        
        self.is_recording = False
        self.recording = []
        self.model = whisper.load_model("base")
        self.auto_copy = tk.BooleanVar(value=True)
        #self.root.iconphoto(True, tk.PhotoImage(file="mic1.png"))

        self.setup_ui()
        
    def setup_ui(self):
        # Text Display
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, font=("Helvetica", 14))
        self.text_area.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        # Controls Frame
        controls_frame = ttk.Frame(self.root)
        controls_frame.pack(pady=10)
        
        # Record Button
        self.record_btn = ttk.Button(controls_frame, text="🎤 Start Recording", command=self.toggle_recording)
        self.record_btn.pack(side=tk.LEFT, padx=5)
        
        # Copy Button
        self.copy_btn = ttk.Button(controls_frame, text="📋 Copy", command=self.copy_text)
        self.copy_btn.pack(side=tk.LEFT, padx=5)
        
        # Auto-copy Checkbox
        ttk.Checkbutton(controls_frame, text="Auto Copy", variable=self.auto_copy).pack(side=tk.LEFT, padx=5)
        
        # Status Label
        self.status = ttk.Label(self.root, text="Ready")
        self.status.pack(pady=5)
        
    def toggle_recording(self):
        if not self.is_recording:
            self.start_recording()
        else:
            self.stop_recording()
    
    def start_recording(self):
        self.is_recording = True
        self.recording = []
        self.record_btn.config(text="⏹ Stop Recording")
        self.status.config(text="Recording...")
        
        self.audio_stream = sd.InputStream(
            samplerate=16000,
            channels=1,
            dtype="int16",
            callback=self.audio_callback
        )
        self.audio_stream.start()
    
    def audio_callback(self, indata, frames, time, status):
        if self.is_recording:
            self.recording.append(indata.copy())
    
    def stop_recording(self):
        self.is_recording = False
        self.audio_stream.stop()
        self.record_btn.config(text="🎤 Start Recording")
        self.status.config(text="Processing...")
        
        # Save recording to file
        recording_array = np.concatenate(self.recording, axis=0)
        with wave.open("output.wav", "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(16000)
            wf.writeframes(recording_array.tobytes())
        
        # Start processing in thread
        threading.Thread(target=self.transcribe_audio).start()
    
    def transcribe_audio(self):
        result = self.model.transcribe("output.wav")
        text = result["text"]
        
        self.text_area.insert(tk.END, text + "\n")
        if self.auto_copy.get():
            pyperclip.copy(text)
            self.status.config(text="Text copied to clipboard!")
        else:
            self.status.config(text="Ready")
    
    def copy_text(self):
        text = self.text_area.get("1.0", tk.END)
        pyperclip.copy(text.strip())
        self.status.config(text="Text copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceTypingApp(root)
    root.mainloop()